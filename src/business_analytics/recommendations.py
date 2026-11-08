"""Explainable, rule-based recommendations for business review; not causal claims."""
import pandas as pd


def action_register(budget_projects, delivery_projects):
    """Flag projects needing investigation and supply testable follow-up KPIs."""
    combined = budget_projects.merge(
        delivery_projects[['project_id','overdue_open','open_days_overdue','is_complete','delay_days','late_milestone_pct']],
        on='project_id', validate='one_to_one'
    )
    actions = []
    for r in combined.itertuples(index=False):
        if r.variance > 0:
            actions.append({
                'project_id': r.project_id, 'department': r.department,
                'priority': 'High' if (pd.notna(r.variance_pct) and r.variance_pct >= 10) else 'Medium',
                'finding': f'Cost overrun: {r.variance:,.0f} ({r.variance_pct:.1f}% vs budget)' if pd.notna(r.variance_pct) else f'Unbudgeted spend: {r.variance:,.0f}',
                'suggested_action': 'Review the largest unfavorable cost categories; validate scope changes and purchase approvals.',
                'follow_up_kpi': 'Budget variance %; unapproved change cost',
                'evidence_type': 'Descriptive flag — cause not established',
            })
        if r.overdue_open:
            actions.append({
                'project_id': r.project_id, 'department': r.department, 'priority': 'High',
                'finding': f'Open project overdue by {int(r.open_days_overdue)} days',
                'suggested_action': 'Review critical-path blockers, dependencies, and owner assignments; agree a revised delivery plan.',
                'follow_up_kpi': 'Overdue project count; forecast finish variance',
                'evidence_type': 'Descriptive flag — cause not established',
            })
        if pd.notna(r.late_milestone_pct) and r.late_milestone_pct > 30:
            actions.append({
                'project_id': r.project_id, 'department': r.department, 'priority': 'Medium',
                'finding': f'{r.late_milestone_pct:.1f}% of completed milestones late',
                'suggested_action': 'Review handoff and review-cycle times; pilot clearer milestone acceptance criteria.',
                'follow_up_kpi': 'Milestone on-time completion rate',
                'evidence_type': 'Descriptive flag — cause not established',
            })
    cols = ['project_id','department','priority','finding','suggested_action','follow_up_kpi','evidence_type']
    if not actions:
        return pd.DataFrame(columns=cols)
    return pd.DataFrame(actions, columns=cols).sort_values(['priority','project_id'], key=lambda x: x.map({'High':0,'Medium':1}).fillna(2) if x.name=='priority' else x).reset_index(drop=True)
