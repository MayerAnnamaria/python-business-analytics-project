"""Project delivery, milestone slippage and schedule KPIs."""
import pandas as pd


def project_analysis(tables, as_of=None):
    """Review completed projects separately from unfinished projects."""
    as_of = pd.Timestamp(as_of).normalize() if as_of is not None else pd.Timestamp.today().normalize()
    projects = tables['projects'].copy()
    projects['is_complete'] = projects['status'].str.lower().eq('completed') & projects['actual_end_date'].notna()
    projects['delay_days'] = (projects['actual_end_date'] - projects['planned_end_date']).dt.days.where(projects['is_complete'])
    projects['on_time'] = projects['is_complete'] & projects['delay_days'].le(0)
    projects['overdue_open'] = (~projects['is_complete']) & projects['planned_end_date'].lt(as_of)
    projects['open_days_overdue'] = (as_of - projects['planned_end_date']).dt.days.clip(lower=0).where(projects['overdue_open'], 0)
    milestones = tables['milestones'].copy()
    milestones['is_complete'] = milestones['status'].str.lower().eq('completed') & milestones['actual_date'].notna()
    milestones['milestone_delay_days'] = (milestones['actual_date'] - milestones['planned_date']).dt.days.where(milestones['is_complete'])
    milestones['late_milestone'] = milestones['is_complete'] & milestones['milestone_delay_days'].gt(0)
    summary = milestones.groupby('project_id', as_index=False).agg(
        total_milestones=('milestone_id','nunique'),
        completed_milestones=('is_complete','sum'),
        late_milestones=('late_milestone','sum'),
    )
    summary['late_milestone_pct'] = (100 * summary['late_milestones'] / summary['completed_milestones'].replace(0, float('nan'))).round(1)
    report = projects.merge(summary, on='project_id', how='left', validate='one_to_one')
    # On-time rate denominator is completed projects only, not all projects.
    completed = report.loc[report['is_complete']]
    metrics = {
        'projects': len(report),
        'completed_projects': len(completed),
        'on_time_completed_pct': round(100 * completed['on_time'].mean(), 1) if len(completed) else None,
        'open_overdue_projects': int(report['overdue_open'].sum()),
        'avg_completed_delay_days': round(float(completed['delay_days'].mean()), 1) if len(completed) else None,
    }
    return report, milestones, metrics
