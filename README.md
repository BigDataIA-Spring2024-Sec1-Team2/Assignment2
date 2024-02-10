## Big Data Systems and Intelligence Analytics (DAMG 7245)
| Name | Email | NUID |
| ------ | ------ | ----- |
| Ameya Apte | apte.ame@northeastern.edu | 2764540 | 
| Sayali Dalvi | dalvi.sa@northeastern.edu | 2799803 |
| Soeb Hussain | hussain.soe@northeastern.edu | 2747200 | 



# Case_Study_2


# Finance Professional Development Resource Database

## Overview
This project aims to aggregate and make accessible finance professional development materials through a comprehensive data engineering solution. It involves creating datasets from materials listed on the CFA Institute’s website, structuring the data, extracting text from PDF files, and integrating cloud storage solutions.

## Features
- **Data Extraction**: Utilizes web scraping to gather finance-related materials.
- **Data Structuring**: Organizes scraped data into a coherent structure suitable for database integration.
- **Text Extraction**: Implements algorithms to extract text from PDF documents.
- **Cloud Integration**: Utilizes AWS S3 for storage and Snowflake for database management.

## Technologies Used
- Python for scripting and web scraping
- Jupyter Notebook for data analysis and visualization
- Snowflake for data storage and management
- AWS S3 for cloud-based file storage

## Setup and Installation
1. Clone the repository to your local machine.
2. Install the required Python libraries using `pip install -r requirements.txt`.
3. Configure AWS S3 and Snowflake with the provided setup guide.


Naming Conventions: 
* s3 bucketname: CFA-PDFs
* snowflake DB: DAMG_7245_CFA
* snowflake warehouse: DAMG_7245_CFA
* Tables:
    * metadata: CFA_META_R
    * web scraped data: CFA_WEB_DATA_R

