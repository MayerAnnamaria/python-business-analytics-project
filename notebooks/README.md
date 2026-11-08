
# Python Business Analytics Project

Welcome to the **Python Business Analytics Project** repository! This project demonstrates an end-to-end business analytics workflow, from importing and cleaning Excel datasets to analyzing financial and operational performance and developing actionable management recommendations.

Designed as a portfolio project, it demonstrates practical skills in **Python, data analysis, financial reporting, project performance monitoring, and business decision support**.

The project uses synthetic IT and operational project data to evaluate budget performance, identify delivery risks, and recommend improvements to business efficiency.

**New here? Start with `00_colab_setup.ipynb` in the `notebooks` folder.** It guides you through setting up the project in Google Colab and connecting to GitHub.

---

## 📁 Repository Structure

```text
python-business-analytics-project/
│
├── data/                            # Four Excel source datasets
│   ├── projects.xlsx                # Project details and ownership
│   ├── budget_plan.xlsx             # Planned project costs
│   ├── actual_costs.xlsx            # Actual project expenditure
│   └── milestones.xlsx              # Project milestone records
│
├── notebooks/                            # Business analysis workflow
│   ├── 00_colab_setup.ipynb              # Configure Colab and GitHub
│   ├── 01_import_merge_excel.ipynb       # Import and integrate Excel data
│   ├── 02_data_cleaning.ipynb            # Clean and validate datasets
│   ├── 03_budget_optimization.ipynb      # Analyze budgets and cost drivers
│   ├── 04_project_performance.ipynb      # Analyze delivery and delays
│   └── 05_business_recommendations.ipynb # Management actions
│
├── src/business_analytics/         # Reusable Python analysis modules
├── outputs/                        # Generated CSV reports and PDF brief
├── docs/                           # Business case and data dictionary
├── tests/                          # Automated analysis tests
├── requirements.txt                # Python dependencies
└── README.md                       # Project documentation
```

---

## 📖 Project Overview

The analysis follows six stages:

1. **Environment Setup:** Configure Google Colab, GitHub integration, and Python dependencies.
2. **Data Integration:** Import Excel datasets, examine their structure, and combine related information.
3. **Data Preparation:** Clean, standardize, and validate data to ensure reliable analysis.
4. **Budget Optimization:** Analyze planned versus actual spending, identify cost drivers, and evaluate departmental budget performance.
5. **Project Performance:** Evaluate on-time delivery, overdue projects, milestone delays, and schedule risks.
6. **Management Recommendations:** Translate analytical findings into prioritized corrective actions and measurable performance improvements.

---

## 🎯 Business Objectives

The project addresses three key business challenges:

### Financial Performance & Cost Optimization

Identify projects and departments exceeding their budgets, investigate unfavorable cost variances, and highlight opportunities for better financial control.

### Project Delivery & Process Improvement

Measure project delivery performance, identify scheduling risks, and recommend improvements to project planning, coordination, and milestone management.

### Management Decision Support

Provide evidence-based recommendations to help PMO and Finance teams prioritize operational risks, allocate resources efficiently, and monitor business performance.

---

## 📊 Analytics & Reporting

The project generates management-ready outputs, including:

- **Budget Analysis:** Project, departmental, and cost-category variance reports.
- **Delivery Performance:** Project completion KPIs, overdue project analysis, and milestone tracking.
- **Management Action Register:** Prioritized findings, suggested corrective actions, and follow-up KPIs.
- **Executive Report:** A concise PDF summarizing key business findings and recommended management decisions.

**[View Generated Reports](outputs/)** | **[View Management Decision Brief](outputs/management_decision_brief.pdf)**

---

## 🛠️ Technologies & Tools

- **Python & pandas:** Data manipulation, validation, and analysis.
- **Matplotlib:** Business data visualization.
- **Excel & openpyxl:** Source data processing.
- **Google Colab:** Cloud-based Python development and execution.
- **Git & GitHub:** Version control and project documentation.
- **ReportLab:** Automated PDF management reporting.

---

## 🌟 About Me

Hi, I'm **Annamaria Mayer**. My background combines IT project coordination, software testing, documentation, and data analysis in international environments. I hold a Master's degree in Sociology, which has provided me with a strong foundation in research methodology, statistics, and analytical thinking.

I am developing my expertise in **Python, SQL, business analytics, and IT project management**, with a focus on transforming data into meaningful insights and practical business solutions.

---

**Data Disclaimer:** This project uses synthetic datasets for educational and portfolio purposes. Financial findings and management recommendations demonstrate analytical capabilities and do not represent actual company performance or realized business improvements.

