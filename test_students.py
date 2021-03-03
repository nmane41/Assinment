import pytest
import students
from unittest.mock import Mock

students = students.Student()
mock = Mock()


@pytest.fixture()
def records():
    id = 111
    name = "Uttam"
    lastname = "Pawar"
    standard = 6
    records = [id, name, lastname, standard]
    return records


def test_insert_record(records):
    assert students.insert_table_values(records[0], records[1], records[2], records[3]) == records[1]


def test_update_record():
    assert students.update_record(111, 6) == 1


def test_delete_record():
    assert students.delete_record(111) == 1
