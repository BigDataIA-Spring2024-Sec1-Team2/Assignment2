## Big Data Systems and Intelligence Analytics (DAMG 7245)

| Name         | Email                        | NUID    |
| ------------ | ---------------------------- | ------- |
| Ameya Apte   | apte.ame@northeastern.edu    | 2764540 |
| Sayali Dalvi | dalvi.sa@northeastern.edu    | 2799803 |
| Soeb Hussain | hussain.soe@northeastern.edu | 2747200 |

# Case_Study_2

# Finance Professional Development Resource Database

Big Data Systems and Intelligence Analytics (DAMG 7245) - Case_Study_2

## Overview

This project aims to aggregate and make accessible finance professional development materials through a comprehensive data engineering solution. It involves creating datasets from materials listed on the CFA Institute’s website, structuring the data, extracting text from PDF files, and integrating cloud storage solutions.

## Live application Links

[![codelabs](https://img.shields.io/badge/codelabs-4285F4?style=for-the-badge&logo=codelabs&logoColor=white)]()

## Problem Statement

## Features

- **Data Extraction**: Utilizes web scraping to gather finance-related materials.
- **Data Structuring**: Organizes scraped data into a coherent structure suitable for database integration.
- **Text Extraction**: Implements algorithms to extract text from PDF documents.
- **Cloud Integration**: Utilizes AWS S3 for storage and Snowflake for database management.

## Project Goals

_Include tasks from the assignment_

## Technologies Used

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)
[![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)](https://www.python.org/)

- Python for scripting and web scraping
- Jupyter Notebook for data analysis and visualization
- Snowflake for data storage and management
- AWS S3 for cloud-based file storage

## Data Sources

_Include all the sources of data being used in the assignment_

## Pre requisites

_Define any prerequisites of softwares/knowledge base for the project_

## Project Structure

```
.
├── README.md
├── sqlalchemy
│   ├── 1_mysql.py
│   ├── 2_mysql.py
│   ├── 3_mysql.py
│   ├── 4_snowflake_sqlalchemy.py
│   ├── 5_snowflake.py
│   ├── 6_snowflake.py
│   ├── 7_snowflake.py
│   └── requirements.txt
├── streamlit
│   ├── Dockerfile
│   ├── README.md
│   ├── main.py
│   └── requirements.txt
└── streamlit-multipage
    ├── README.md
    ├── example.env
    ├── main.py
    ├── pages
    │   ├── 1_uber_nyc.py
    │   ├── 2_Plotting_Demo.py
    │   ├── 3_nexrad_station.py
    │   └── 4_test.py
    ├── requirements.txt
    └── streamlit_colab.ipynb
```

_You can generate the project tree using following tools_
_[Project Tree Generator](https://woochanleee.github.io/project-tree-generator)_
_[Generate from terminal](https://www.geeksforgeeks.org/tree-command-unixlinux/)_

## How to run Application locally

## Setup and Installation

1. Clone the repository to your local machine.
2. Install the required Python libraries using `pip install -r requirements.txt`.
3. Configure AWS S3 and Snowflake with the provided setup guide.

Naming Conventions:

- s3 bucketname: CFA-PDFs
- snowflake DB: DAMG_7245_CFA
- snowflake warehouse: DAMG_7245_CFA
- Tables:
  - metadata: CFA_META_R
  - web scraped data: CFA_WEB_DATA_R

Execution Step for code/CSV2Snowflake.ipynb

- create a folder in parent directory with name 'config'
- add .env file in it containing following variables
  - SNOWFLAKE_USER=''
  - SNOWFLAKE_PASSWORD=''
  - SNOWFLAKE_DATABASE='DAMG_7245_CFA_DB'
  - SNOWFLAKE_WAREHOUSE='DAMG_7245_WH_XS'
  - SNOWFLAKE_ACCOUNT_IDENTIFIER=''
  - GROBID_URL='http://localhost:8070/api/processFulltextDocument'
  - PDF_DIR_PATH='../data'
  - OUTPUT_DIR_PATH='../sample_output/'
  - DIR_CFA_WEB = '../sample_output/'
  - CSV_CFA_WEB = 'FinanceHub.csv'
  - TXT_CFA_LINKS = '224_links.txt'

## References

_All the external references must be listed down._

## Learning Outcomes

_List the learning outcomes from the assignment/project_

## Team Information and Contribution

| Name         | Contribution % | Contributions |
| ------------ | -------------- | ------------- |
| Soeb Hussain | 30%            |               |
| Sayali Dalvi | 40%            |               |
| Ameya Apte   | 30%            |               |

Naming Conventions:

- s3 bucketname: CFA-PDFs
- snowflake DB: DAMG_7245_CFA
- snowflake warehouse: DAMG_7245_CFA
- Tables:
  - metadata: CFA_META_R
  - web scraped data: CFA_WEB_DATA_R

Execution Step for code/CSV2Snowflake.ipynb

- create a folder in parent directory with name 'config'
- add .env file in it containing following variables
  - SNOWFLAKE_USER=''
  - SNOWFLAKE_PASSWORD=''
  - SNOWFLAKE_DATABASE='DAMG_7245_CFA_DB'
  - SNOWFLAKE_WAREHOUSE='DAMG_7245_WH_XS'
  - SNOWFLAKE_ACCOUNT_IDENTIFIER=''
  - s3_bucket_name = ''
  - s3_pypdf = ''
  - s3_grobid = ''
  - access_key = ''
  - secret_key = ''
