"""Run end-to-end reporting from prepared Excel source files."""
from pathlib import Path
import pandas as pd
from .io import read_sources
from .cleaning import clean_sources, quality_report
from .budget import budget_analysis
from .delivery import project_analysis
from .recommendations import action_register


def run_pipeline(input_dir, output_dir, as_of='2026-01-31'):
    """Write audit-friendly CSV reports and return a results dictionary.

    as_of is an explicit reporting cutoff for reproducible sample comparisons.
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    raw = read_sources(input_dir)
    before = quality_report(raw)
    clean = clean_sources(raw)
    after = quality_report(clean)
    category, budget_projects = budget_analysis(clean)
    delivery_projects, milestones, kpis = project_analysis(clean, as_of=as_of)
    actions = action_register(budget_projects, delivery_projects)
    budget_by_department = budget_projects.groupby('department', as_index=False)[['planned_budget', 'actual_cost', 'variance']].sum()
    budget_by_department['variance_pct'] = (100 * budget_by_department['variance'] / budget_by_department['planned_budget'].replace(0, float('nan'))).round(1)
    results = {
        'quality_before': before, 'quality_after': after,
        'budget_by_category': category, 'budget_by_project': budget_projects,
        'budget_by_department': budget_by_department,
        'project_delivery': delivery_projects, 'milestone_delivery': milestones,
        'action_register': actions,
    }
    for name, df in results.items():
        df.to_csv(output_dir / f'{name}.csv', index=False)
    pd.DataFrame([kpis]).to_csv(output_dir / 'delivery_kpis.csv', index=False)
    return {**results, 'delivery_kpis':kpis}
