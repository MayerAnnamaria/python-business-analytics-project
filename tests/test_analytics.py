import pandas as pd
import pytest
from src.business_analytics.budget import budget_analysis
from src.business_analytics.cleaning import clean_sources
from src.business_analytics.delivery import project_analysis
from src.business_analytics.recommendations import action_register
from src.business_analytics.io import read_sources


def sources():
    return {
        'projects':pd.DataFrame({'project_id':['P1','P2'],'project_name':['Alpha','Beta'],'department':['IT','Ops'],'project_manager':['A','B'],'status':['Completed','In Progress'],'start_date':['2025-01-01','2025-01-01'],'planned_end_date':['2025-05-01','2025-05-01'],'actual_end_date':['2025-05-04',None]}),
        'budget_plan':pd.DataFrame({'project_id':['P1','P1','P2'],'cost_category':['Labor','Software','Labor'],'planned_budget':[100,100,100]}),
        'actual_costs':pd.DataFrame({'transaction_id':['T1','T2','T3'],'project_id':['P1','P1','P2'],'cost_category':['Labor','Labor','Labor'],'transaction_date':['2025-03-01']*3,'actual_cost':[70,60,80]}),
        'milestones':pd.DataFrame({'milestone_id':['M1','M2'],'project_id':['P1','P2'],'milestone_name':['Test','Test'],'planned_date':['2025-03-01','2025-03-01'],'actual_date':['2025-03-03',None],'status':['Completed','Open']})
    }


def test_budget_avoids_many_to_many_joins():
    cat, prj=budget_analysis(clean_sources(sources()))
    assert prj.loc[prj.project_id=='P1','planned_budget'].iloc[0]==200
    assert prj.loc[prj.project_id=='P1','actual_cost'].iloc[0]==130


def test_variance_sign():
    _, prj=budget_analysis(clean_sources(sources()))
    assert prj.set_index('project_id').loc['P1','variance']==-70


def test_completed_ontime_denominator():
    proj, milestones, metrics=project_analysis(clean_sources(sources()),'2025-06-01')
    assert metrics['completed_projects']==1
    assert metrics['on_time_completed_pct']==0.0
    assert metrics['open_overdue_projects']==1


def test_duplicate_transaction_id_rejected():
    s=sources();s['actual_costs'].loc[1,'transaction_id']='T1'
    with pytest.raises(ValueError): clean_sources(s)


def test_unknown_project_rejected():
    s=sources();s['milestones'].loc[0,'project_id']='INVALID'
    with pytest.raises(ValueError): clean_sources(s)


def test_action_register_flags_open_overdue():
    s=clean_sources(sources());_,b=budget_analysis(s);d,_,_=project_analysis(s,'2025-06-01')
    a=action_register(b,d)
    assert (a.project_id=='P2').any()
