import pytest
from pyspark.sql import SparkSession, Row
import main  # Importing your main script

# PySpark Session Fixture
@pytest.fixture(scope="session")
def spark_session():
    """Creates a PySpark session for testing."""
    spark = SparkSession.builder.master("local[2]").appName("test").getOrCreate()
    yield spark
    spark.stop()

# Unit Test 1: Test Data Loading
@pytest.mark.usefixtures("spark_session")
def test_read_college_date(spark_session):
    test_df = main.read_college_date(spark_session)
    assert test_df is not None

# Unit Test 2: Test Adding Source File Column
@pytest.mark.usefixtures("spark_session")
def test_add_source_file(spark_session):
    test_df = main.read_college_date(spark_session)
    test_df = main.add_source_file(test_df)
    assert 'source_file' in test_df.columns

# Unit Test 3: Test Filtering and Selecting Relevant Columns
@pytest.mark.usefixtures("spark_session")
def test_select_and_filter(spark_session):
    test_df = spark_session.createDataFrame(
        [('10000', 'IA', 'test.file'), ('NULL', 'IA', 'test.file')],
        ['NPT4_PUB', 'STABBR', 'source_file']
    )
    test_df = main.select_and_filter(test_df)
    assert test_df.count() == 1  # Only non-NULL rows should remain

# Unit Test 4: Test Extracting Year from Filename
@pytest.mark.usefixtures("spark_session")
def test_pull_year_from_file_name(spark_session):
    test_df = spark_session.createDataFrame(
        [('10000', 'IA', 'MERGED2019_')],
        ['NPT4_PUB', 'STABBR', 'source_file']
    )
    test_df = main.pull_year_from_file_name(test_df)
    assert test_df.select('year').collect() == [Row(year='2019')]  # Expecting 2019 extracted

