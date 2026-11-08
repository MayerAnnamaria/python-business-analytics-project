# Business Case | IT & Operations Portfolio Review

## Decision-makers
PMO lead, IT delivery manager, finance business partner, and department owners.

## Business questions
1. **Budget** — Which projects or departments are exceeding approved budgets?
2. **Variance** — How far are actual costs above or below approved budget baselines?
3. **Cost control** — Which cost categories deserve investigation before the next steering meeting?
4. **Schedule** — What share of completed projects finished on time?
5. **Delivery risk** — Which open projects are overdue at the reporting cutoff?
6. **Process improvement** — Do repeated late milestones suggest handoffs or scope controls to investigate?

## Analytical method
1. Import four Excel sources at different grains.
2. Profile missing values and duplicates; standardize fields and validate join keys.
3. Aggregate actual transaction costs to project and category **before** joining budgets.
4. Compare costs against budgets; compute schedule and milestone variances.
5. Create an explainable action register with follow-up KPIs.

## Interpreting findings responsibly
- Large positive budget variance: examine invoices, change requests, vendor costs and timing; **do not claim savings without a follow-up measurement**.
- Overdue open projects: review the critical path and workload distribution; **do not assume the cause from status data alone**.
- Unfavorable milestone adherence: run a process review before choosing a remedy.

## Suggested business experiment
Pilot weekly cost and milestone reviews for a subset of projects. Compare budget variance, overdue count, and on-time milestones against a comparable pre-pilot period. Document changes in scope and portfolio mix.
