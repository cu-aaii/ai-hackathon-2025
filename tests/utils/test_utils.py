from src.utils.databricks import is_running_on_databricks


def test_is_running_on_databricks():
    assert not is_running_on_databricks()
