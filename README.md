# Docker_data_engineering

Historic College Cost Analysis using docker image and container

Overview

This project analyzes the cost of college education in the U.S. using open-source data from the College Scorecard. It demonstrates data engineering skills, including data ingestion, transformation, and analysis using PySpark.

Objectives

Analyze the increase in college costs over the years.

Identify the most expensive states for college education.

Learn and apply key data engineering skills such as working with dirty data, writing modular and testable code, and leveraging Docker for reproducibility.

Technologies Used

PySpark: For data processing and transformations.

Docker: For containerizing the project.

Python: Primary programming language.

Apache Spark: Distributed data processing engine.

pyspark.sql: Used for data manipulation and queries.

Unit Testing: Implemented using pytest.

Dataset

The dataset used is from the U.S. College Scorecard, consisting of multiple CSV files containing information about colleges, student demographics, and costs. The files include a data.yaml file with metadata, and the year is extracted from filenames using regex.

Project Structure

.
├── app/
│   ├── main.py  # Main PySpark script
│   ├── utils.py  # Helper functions
│   ├── tests/  # Unit tests
│   ├── Dockerfile  # Docker setup
│   ├── README.md  # Project documentation
│   ├── requirements.txt  # Python dependencies
│   ├── data/  # Raw CSV data files

Implementation

1. Data Processing Steps

Read Data: Load CSV files into a PySpark DataFrame.

Extract Metadata: Add a column with the source filename.

Select Relevant Columns: Filter necessary columns (NPT4_PUB, STABBR).

Handle Missing Data: Remove rows where NPT4_PUB is null.

Extract Year: Use regex to extract the year from filenames.

Compute Metrics:

Average college cost over years.

Top 10 most expensive states for college in 2019.

2. Running the Project with Docker

Build the Docker Image:

docker build --tag=college-cost-analysis .

Run the Container:

docker run --rm college-cost-analysis

3. Running Tests

To ensure the correctness of data processing, unit tests are implemented. Run tests using:

pytest tests/

