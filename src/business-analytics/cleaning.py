"""Type-safe cleaning, validation, and data-quality reporting."""
import pandas as pd

DATE_COLUMNS = {
    'projects': ['start_date', 'planned_end_date', 'actual_end_date'],
    'budget_plan': [],
    'actual_costs': ['transaction_date'],
    'milestones': ['planned_date', 'actual_date'],
}
NUMERIC_COLUMNS = {'budget_plan': ['planned_budget'], 'actual_costs': ['actual_costs']}
KEYS = {'projects': 'project_id', 'budget_plan': None, 'actual_costs': 'transaction_id', 'milestones': 'milestone_id'}


def quality_report(tables):
    """Describe missing values and duplicate records; no values are silently imputed."""
    rows = []
    for name, df in tables.items():
        for col in df.columns:
            rows.append({
                'dataset': name, 'column': col, 'rows': len(df),
                'missing_count': int(df[col].isna().sum()),
                'missing_pct': round(100 * df[col].isna().mean(), 2) if len(df) else 0,
                'exact_duplicate_rows': int(df.duplicated().sum()),
            })
    return pd.DataFrame(rows)


def clean_sources(tables):
    """Normalize strings and types; reject ambiguous keys and invalid financial data."""
    cleaned = {}
    for name, source in tables.items():
        df = source.copy()
        df.columns = df.columns.astype(str).str.strip().str.lower().str.replace(' ', '_')
        for col in df.select_dtypes(include=['object', 'string']).columns:
            df[col] = df[col].astype('string').str.strip().replace('', pd.NA)
        df = df.drop_duplicates().reset_index(drop=True)
        for col in DATE_COLUMNS[name]:
            df[col] = pd.to_datetime(df[col], errors='coerce')
        for col in (['planned_budget'] if name == 'budget_plan' else ['actual_cost'] if name == 'actual_costs' else []):
            df[col] = pd.to_numeric(df[col], errors='coerce')
            if df[col].isna().any() or (df[col] < 0).any():
                raise ValueError(f'{name}.{col}: missing, nonnumeric, or negative amounts; review source data')
        df['project_id'] = df['project_id'].astype('string').str.strip().str.upper()
        if df['project_id'].isna().any():
            raise ValueError(f'{name}: missing project_id')
        key = KEYS[name]
        if key and (df[key].isna().any() or df[key].duplicated().any()):
            raise ValueError(f'{name}: {key} must be unique and nonmissing')
        if name == 'budget_plan':
            if df[['project_id', 'cost_category']].isna().any().any() or df.duplicated(['project_id', 'cost_category']).any():
                raise ValueError('budget_plan: one row required per (project_id, cost_category)')
        if name in ['budget_plan', 'actual_costs']:
            df['cost_category'] = df['cost_category'].astype('string').str.strip().str.title()
        cleaned[name] = df
    master = set(cleaned['projects']['project_id'])
    for name in ['budget_plan','actual_costs','milestones']:
        unknown = set(cleaned[name]['project_id']) - master
        if unknown:
            raise ValueError(f'{name}: project_id not present in projects: {sorted(unknown)}')
    if (cleaned['projects']['planned_end_date'] < cleaned['projects']['start_date']).any():
        raise ValueError('projects: planned_end_date cannot precede start_date')
    return cleaned
