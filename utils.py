import os


def get_spark_session():
    """Return a SparkSession.

    In production this can encapsulate common cluster configuration.
    In this repo we keep it minimal and consistent with existing notebooks.
    """

    from pyspark.sql import SparkSession

    return (
        SparkSession.builder.appName(os.environ.get("SPARK_APP_NAME", "TalendJob"))
        .config("spark.jars", os.environ.get("ORACLE_JDBC_JAR", "/usr/local/lib/ojdbc8.jar"))
        .config(
            "spark.driver.extraClassPath",
            os.environ.get("ORACLE_JDBC_JAR", "/usr/local/lib/ojdbc8.jar"),
        )
        .getOrCreate()
    )


def get_main_db_config() -> dict:
    return {
        "url": os.environ.get("MAIN_DB_URL"),
        "user": os.environ.get("MAIN_USER"),
        "password": os.environ.get("MAIN_PASSWORD"),
        "schema": os.environ.get("MAIN_SCHEMA"),
    }

def get_staging_db_config() -> dict:
    return {
        "url": os.environ.get("STG_DB_URL"),
        "user": os.environ.get("STG_USER"),
        "password": os.environ.get("STG_PASSWORD"),
        "schema": os.environ.get("STG_SCHEMA"),
    }


def get_apps_db_config() -> dict:
    """Apps/BOORG database connection config."""
    return {
        "url": os.environ.get("APPS_DB_URL"),
        "user": os.environ.get("APPS_USER"),
        "password": os.environ.get("APPS_PASSWORD"),
        "schema": os.environ.get("APPS_SCHEMA"),
    }
