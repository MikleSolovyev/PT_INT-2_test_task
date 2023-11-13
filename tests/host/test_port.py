import pytest
from pydantic import ValidationError

from src.host import Host

invalid_port_tests = [
    {
        'ip': '0.0.0.0',
        'port': '',
        'username': 'aaa',
        'password': 'bbb'
    },
    {
        'ip': '0.0.0.0',
        'port': 'a',
        'username': 'aaa',
        'password': 'bbb'
    },
    {
        'ip': '0.0.0.0',
        'port': '1a',
        'username': 'aaa',
        'password': 'bbb'
    },
    {
        'ip': '0.0.0.0',
        'port': '0',
        'username': 'aaa',
        'password': 'bbb'
    },
    {
        'ip': '0.0.0.0',
        'port': '65536',
        'username': 'aaa',
        'password': 'bbb'
    },
    {
        'ip': '0.0.0.0',
        'port': -1,
        'username': 'aaa',
        'password': 'bbb'
    },
    {
        'ip': '0.0.0.0',
        'username': 'aaa',
        'password': 'bbb'
    }
]


@pytest.mark.parametrize("profile", invalid_port_tests)
def test_invalid_port(profile):
    with pytest.raises(ValidationError):
        Host.model_validate(profile)


correct_port_tests = [
    {
        'ip': '0.0.0.0',
        'port': '1',
        'username': 'aaa',
        'password': 'bbb'
    },
    {
        'ip': '0.0.0.0',
        'port': '65535',
        'username': 'aaa',
        'password': 'bbb'
    },
    {
        'ip': '0.0.0.0',
        'port': 22,
        'username': 'aaa',
        'password': 'bbb'
    },
    {
        'ip': '0.0.0.0',
        'port': '022',
        'username': 'aaa',
        'password': 'bbb'
    }
]


@pytest.mark.parametrize("profile", correct_port_tests)
def test_correct_port(profile):
    Host.model_validate(profile)
