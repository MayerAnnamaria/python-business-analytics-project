# Project Budget & Delivery Performance Analytics

**Python · Google Colab · pandas · Excel · Data Cleaning · PMO / Business Analytics**

A reusable, end-to-end portfolio project that transforms realistic **synthetic IT and operations project data** into decisions about budget control and project delivery. Designed for a PMO analyst, business analyst, data analyst, or IT project coordinators.

> **Data disclosure:** All included Excel workbooks are simulated for demonstration; no real employer records or proven cost savings are represented. Reports are reproducible with a fixed reference date (`2026-01-31`).

## Business questions

| Theme | Business question | Output |
|---|---|---|
| Budget variance | Which projects and departments are over budget? | Project and cost-category variance |
| Cost optimization | Where should finance investigate unexpected spending? | Cost-category drill-down and action register |
| Delivery performance | Which completed projects missed their deadlines? | On-time percentage, delay days |
| Operational improvement | Which open projects are overdue and which milestones slip? | Project and milestone monitoring |
| Management decisions | What specific next action and KPI should be assigned? | Evidence-based action register |

## Repository structure

```text
project-budget-performance-analytics/
├── README.md
├── requirements.txt
├── run_analysis.py
├── data/
│   ├── sample/                    # 4 shareable synthetic Excel files
│   │   ├── projects.xlsx
│   │   ├── budget_plan.xlsx
│   │   ├── actual_costs.xlsx
│   │   └── milestones.xlsx
│   └── processed/                 # Generated, gitignored
├── notebooks/
│   ├── 00_colab_setup.ipynb
│   ├── 01_import_merge_excel.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_budget_optimization.ipynb
│   ├── 04_project_performance.ipynb
│   └── 05_business_recommendations.ipynb
├── src/business_analytics/
│   ├── io.py
│   ├── cleaning.py
│   ├── budget.py
│   ├── delivery.py
│   ├── recommendations.py
│   └── pipeline.py
├── tests/test_analytics.py
├── docs/data_dictionary.md
├── docs/business_case.md
└── outputs/                     # Generated reports, gitignored
```

## Quick start in Google Colab

1. Upload this entire project to a GitHub repository, for example `project-budget-performance-analytics`.
2. Open **[Google Colab](https://colab.research.google.com/)**, choose **GitHub**, paste the repository URL, then open `notebooks/00_colab_setup.ipynb`.
3. Run the setup notebook's cells. The first cell clones your repo into `/content` and installs dependencies. To work with your own Excel workbooks, you may mount Google Drive and set `INPUT_DIR` to the folder containing the **four required filenames**.
4. Open notebooks `01` through `05` in order. Each has a standalone initialization cell, so individual notebooks can run in fresh Colab sessions after setup.
5. Review CSV reports saved in `outputs/` and update the notebook's source path when switching to your own files.

**Alternative (without GitHub):** Upload the unzipped project folder to Colab `/content` and update `PROJECT_DIR` accordingly in the setup cell.

### Example code for connecting Google Drive

```python
from google.colab import drive
drive.mount('/content/drive')
INPUT_DIR = '/content/drive/MyDrive/project-budget-performance-analytics/input'
```

The input folder must contain `projects.xlsx`, `budget_plan.xlsx`, `actual_costs.xlsx`, and `milestones.xlsx` with the fields listed in [Data Dictionary](docs/data_dictionary.md). For your first run, use the included `data/sample/` files.

## Running locally

```bash
python -m pip install -r requirements.txt
python run_analysis.py --input-dir data/sample --output-dir outputs --as-of 2026-01-31
python -m pytest -q
```

## Notebook workflow

| Notebook | Focus | Skills shown |
|---|---|---|
| `00_colab_setup` | Environment, GitHub clone, optional Drive mount | Colab setup |
| `01_import_merge_excel` | Excel inputs, grain-aware merging, schema inspection | pandas merges, validation |
| `02_data_cleaning` | Missing data, duplicates, date conversions, key validation | Data quality, reproducible cleaning |
| `03_budget_optimization` | Project variance, percent difference, cost category drivers | KPIs, aggregation, charts |
| `04_project_performance` | Late deliveries, open overdue projects, milestone monitoring | Time metrics, charts |
| `05_business_recommendations` | Findings, investigation priorities, measurable improvements | Business recommendations |

## Outputs and KPI definitions

- `budget_by_project.csv`: planned vs actual, variance and variance %. Positive means overspend.
- `budget_by_department.csv`: department-level budget overview.
- `budget_by_category.csv`: detailed cost drivers without duplicated planned amounts.
- `project_delivery.csv`: completed-project delays and open-project overdue status.
- `milestone_delivery.csv`: planned vs actual milestone outcomes.
- `action_register.csv`: rule-based priorities and follow-up measures.
- `quality_before.csv`, `quality_after.csv`: quality audit tables.
- `delivery_kpis.csv`: top-level project metrics.

A cost overrun is **not** a confirmed cause or recoverable saving. Review timing, accruals, scope and procurement decisions before drawing conclusions. See [Business Case](docs/business_case.md).

## Data cleaning decisions

- Remove **exact** duplicated rows, trim text, standardize column and identifier casing.
- Parse dates and numeric costs; fail visibly on invalid amounts, missing identifiers, or ambiguous natural keys.
- Do **not** fill missing actual completion dates: they are expected for unfinished projects.
- Investigate nulls rather than blindly applying mean or forward-fill imputation to financial values.

## Reuse with your own workbooks

Keep the same file names and required column names, or adjust `src/business_analytics/io.py` and `cleaning.py` to map your organization's data. Preserve the **grain** (one row per project, one per budget category, one per transaction, one per milestone) to avoid double counting. Confirm a consistent currency, reporting period and budget version.

## Skills demonstrated

**Python · pandas · Excel ETL · Data validation · Financial variance analysis · Schedule analytics · PMO KPIs · Reporting · Root-cause investigation framing · Automated testing**

## Limitations

- All metrics represent illustrative synthetic data; they do not measure real organizational impact.
- Transaction costs are treated as available expenditure, not full earned-value accounting.
- Open project delays depend on the reporting cutoff; this sample uses 2026-01-31.
- Recommendations signal priorities for review; they do not prove why a variance occurred.


