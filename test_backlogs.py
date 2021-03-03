import pytest
from backlogs import Backlog_class
from unittest.mock import Mock

backlog = Backlog_class()
mock = Mock()


@pytest.fixture()
def records():
    bid = 1
    sub = "Maths"
    status = "Active"
    stud_id = 101
    records = [bid, sub, status, stud_id]
    return records


def test_insert_table_values(records):
    assert backlog.insert_table_values(records[0], records[1], records[2], records[3]) == records[1]


def test_update_record():
    assert backlog.update_record(1, "Closed") == 1


def test_delete_record():
    assert backlog.delete_record(1) == 1
