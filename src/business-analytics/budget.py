"""Budget variance and cost concentration. Positive variance = over budget."""
import pandas as pd


def budget_analysis(tables):
    """Return detailed category and project reports; avoid fact-to-fact join duplication."""
    planned = tables['budget_plan'].groupby(['project_id','cost_category'], as_index=False, dropna=False)['planned_budget'].sum()
    actual = tables['actual_costs'].groupby(['project_id','cost_category'], as_index=False, dropna=False)['actual_cost'].sum()
    category = planned.merge(actual, on=['project_id','cost_category'], how='outer', validate='one_to_one')
    category[['planned_budget','actual_cost']] = category[['planned_budget','actual_cost']].fillna(0)
    category['variance'] = category['actual_cost'] - category['planned_budget']
    category['variance_pct'] = (100 * category['variance'] / category['planned_budget'].replace(0, float('nan'))).round(1)
    category['budget_status'] = category['variance'].map(lambda x: 'Over budget' if x > 0 else 'On/under budget')
    by_project = category.groupby('project_id', as_index=False)[['planned_budget','actual_cost','variance']].sum()
    by_project['variance_pct'] = (100 * by_project['variance'] / by_project['planned_budget'].replace(0, float('nan'))).round(1)
    by_project = by_project.merge(tables['projects'][['project_id','project_name','department','status']], on='project_id', validate='one_to_one')
    by_project['budget_status'] = by_project['variance'].map(lambda x: 'Over budget' if x > 0 else 'On/under budget')
    return category.sort_values(['variance','project_id'], ascending=[False,True]), by_project.sort_values('variance', ascending=False)
