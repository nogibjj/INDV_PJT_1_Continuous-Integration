# IDS-706 Data Engineering Assignment
## Individual Project : Continuous Integration using Gitlab Actions of Python Data Science Project

#### Status(CI/CD) badge
[![Format](https://github.com/nogibjj/INDV_PJT_1_Continuous-Integration/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/INDV_PJT_1_Continuous-Integration/actions/workflows/format.yml)
[![Install](https://github.com/nogibjj/INDV_PJT_1_Continuous-Integration/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/INDV_PJT_1_Continuous-Integration/actions/workflows/install.yml)
[![Lint](https://github.com/nogibjj/INDV_PJT_1_Continuous-Integration/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/INDV_PJT_1_Continuous-Integration/actions/workflows/lint.yml)
[![Test](https://github.com/nogibjj/INDV_PJT_1_Continuous-Integration/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/INDV_PJT_1_Continuous-Integration/actions/workflows/test.yml)
------
### Requirements
The project structure must include the following files:

* ***Jupyter Notebook*** with:
    - Cells that perform descriptive statistics using Polars or Panda.
    - Tested by using nbval plugin for pytest
* ***Makefile*** with the following:
    - Run all tests (must test notebook and script and lib)
    - Formats code with `Python black` Links to an external site.
    - Lints code with `Ruff` Links to an external site.
    - Installs code via: pip install -r requirements.txt
* ***main.py*** to run functions 
* ***test_main.py*** to test script
* ***requirements.txt***
* Gitlab Actions performs all four Makefile commands with badges for each one in the README.md
---------
### Demo video
[Click Here For Demo](https://www.youtube.com/watch?v=6nCP6vfzQdU)
--------------
### Analysis
Dataset : [HR.csv](HR.csv) 
 - The data used in this analysis was provided by IBM and was originally created to study employee turnover.
 - From the available variables, I specifically focused on the "Age" at retirement.
 - Calcuated mean, median, standard Deviation and so on 

Functions :
- `explore data` : Use `describe` to do exploratory data analysis 
- `calculate statistics` : compute the mean(`mean`), median(`median`), standard deviation(`std`) of age
- `plot_age_histogram` : Plot a histrogram to visualize the age distribution of all employees. 
- `plot_attrition_pie_chart` : Create a plot `pie chart` to illustarte the overall attirition. 
- `plot_attrition_by_department` : Create a plot `bar chart` to analyze attrition by departments.

#### Summary Statistics
-----------
![Exploratory data analysis_1](Summary_Stat.png)
![Exploratory data analysis_2](Summary_age.png)

#### Attrition analysis
-----------
![data analysis_2](Attrition_pie.png)
![data analysis_0](Attrition_dpart_summary.png)\
![data analysis_1](Attrition_dprt.png)\