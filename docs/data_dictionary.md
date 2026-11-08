# Data Dictionary

All example data is **synthetic**, modeled after common IT and operations portfolio-management data. Monetary units are **illustrative units** (not a specific currency); amounts should only be compared after confirming consistent currencies.

| Excel workbook | Grain | Key fields | Description |
|---|---|---|---|
| `projects.xlsx` | One project | `project_id` | Department, manager, status, planned and actual dates |
| `budget_plan.xlsx` | One project–cost category | `project_id`, `cost_category` | Approved planning baseline |
| `actual_costs.xlsx` | One transaction | `transaction_id` | Individual project expenses and cost category |
| `milestones.xlsx` | One milestone | `milestone_id` | Planned and actual milestone dates |

## Key assumptions
- A **positive budget variance** means actual spending exceeds budget. Negative means under budget.
- Cost transactions are summed before joining to planned budgets to prevent double counting.
- **On-time rate** only includes completed projects with recorded actual end dates.
- Open overdue projects are calculated relative to a supplied report **as-of date**.
- `actual_cost` is assumed to contain expenses recognized by the reporting cutoff. A real implementation should filter transaction dates and budget baseline versions consistently.
- Under-budget spending does not automatically mean efficiency; delayed scope, incomplete invoices and reduced deliverables may explain the variance.
- Flags and recommended follow-ups are **hypotheses for investigation**, not proof of root causes or measured improvements.
- This example records no sensitive personal customer information.
