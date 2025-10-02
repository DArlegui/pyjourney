# test_employee.py
import pytest
from employee import Employee


@pytest.fixture
def individual():
    # adjust names/salary to match your Employee class
    return Employee("Ada", "Lovelace", 50_000)


def test_annual(individual: Employee):
    individual.give_raise(5000)
    assert individual.salary == 55_000


def test_annual2(individual: Employee):
    individual.give_raise(1000)
    assert individual.salary == 51_000
