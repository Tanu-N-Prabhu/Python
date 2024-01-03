import pytest
from calculator import Calculator


@pytest.fixture(scope='session', autouse=True)
def session_scope_fixture():
    print('session_scope_fixture')


@pytest.fixture(scope='module', autouse=True)
def module_scope_fixture():
    print('module_scope_fixture')


@pytest.fixture(scope='class', autouse=True)
def class_scope_fixture():
    print('class_scope_fixture')


@pytest.fixture
def calculator():
    return Calculator()


def test_initial_value(calculator):
    assert calculator.total == 0


# testing Calculator class method
# @pytest.mark.skip(reason='not implemented yet')
def test_add_one():
    calculator.set(1)
    calculator.add()
    assert calculator.total == 1


def test_increament_integet_3():
    assert calculator.increment(3) == 4
