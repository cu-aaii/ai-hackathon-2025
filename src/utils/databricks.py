import os


def is_running_on_databricks() -> bool:
    return os.getenv("DATABRICKS_RUNTIME_VERSION") is not None
