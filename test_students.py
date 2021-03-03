import pytest
import students
from unittest.mock import Mock

students = students.Student()
mock = Mock()


@pytest.fixture()
def records():
    id = 110
    name = "Uttam"
    lastname = "Pawar"
    standard = 5
    records = [id, name, lastname, standard]
    return records


def test_insert_employee(records):
    assert students.insert_table_values(records[0], records[1], records[2], records[3]) == records[1]


def test_update_employee():
    assert students.update_record(101, 5) == 1


def test_delete_employee():
    assert students.delete_record(101) == 1
