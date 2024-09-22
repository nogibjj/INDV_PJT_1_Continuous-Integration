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
    - Formats code with Python black Links to an external site.
    - Lints code with Ruff Links to an external site.
    - Installs code via: pip install -r requirements.txt
* ***test_script.py*** to test script
* ***test_lib.py*** to test library
* ***requirements.txt***
* Gitlab Actions performs all four Makefile commands with badges for each one in the README.md
---------
### Demo video
[Click Here For Demo](xxxxx)
--------------
### Analysis
Dataset : [HR.csv](HR.csv) 
 - The data used in this analysis was provided by IBM and was originally created to study employee turnover.
 - From the available variables, I specifically focused on the "Age" at retirement.
 - Calcuated mean, median, standard Deviation and so on 

Functions :
- EDA(Exploratory data analysis) : Use `describe` to check the structure and summary statistics of the dataset and compute the mean(`mean`), median(`mediadn`), standard deviation(`std`) of the data set
- Employee Age Distribution : Plot a histrogram to visualize the age distribution of all employees.
- Employee attrition rate : Create a plot `pie chart` to illustarte the overall attirition rate and a `bar chart` to analyze attrition by departments.

#### Summary Statistics
-----------
![Exploratory data analysis_1](Summary_Stat.png)
![Exploratory data analysis_2](Summary_age.png)

#### Attrition analysis
-----------
![data analysis_0](Attrition_dpart_summary.png)\
![data analysis_1](Attrition_dprt.png)\
![data analysis_2](Attrition_pie.png)
