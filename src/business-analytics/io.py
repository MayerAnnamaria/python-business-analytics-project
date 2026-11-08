"""Input readers and schema checks for Excel business datasets."""
from pathlib import Path
import pandas as pd

REQUIRED = {
    'projects': {'project_id', 'project_name', 'department', 'project_manager', 'status', 'start_date', 'planned_end_date', 'actual_end_date'},
    'budget_plan': {'project_id', 'cost_category', 'planned_budget'},
    'actual_costs': {'transaction_id', 'project_id', 'cost_category', 'transaction_date', 'actual_cost'},
    'milestones': {'milestone_id', 'project_id', 'milestone_name', 'planned_date', 'actual_date', 'status'},
}
FILES = {key: f'{key}.xlsx' for key in REQUIRED}


def read_sources(folder):
    """Read four Excel source files and validate required column names."""
    folder = Path(folder)
    result = {}
    for name, filename in FILES.items():
        path = folder / filename
        if not path.is_file():
            raise FileNotFoundError(f'Missing {path}. See README for input filenames.')
        frame = pd.read_excel(path, engine='openpyxl')
        frame.columns = frame.columns.astype(str).str.strip().str.lower().str.replace(' ', '_')
        missing = REQUIRED[name] - set(frame.columns)
        if missing:
            raise ValueError(f'{filename} missing required columns: {sorted(missing)}')
        result[name] = frame
    return result
