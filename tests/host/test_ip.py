import pytest
from pydantic import ValidationError

from src.host import Host

invalid_ip_tests = [
    {
        'ip': 'asd',
        'port': '22',
        'username': 'aaa',
        'password': 'bbb'
    },
    {
        'ip': '256.0.0.1',
        'port': '22',
        'username': 'aaa',
        'password': 'bbb'
    },
    {
        'ip': '',
        'port': '22',
        'username': 'aaa',
        'password': 'bbb'
    },
    {
        'ip': '0.0.0.1:22',
        'port': '22',
        'username': 'aaa',
        'password': 'bbb'
    },
    {
        'ip': 55,
        'port': '22',
        'username': 'aaa',
        'password': 'bbb'
    },
    {
        'port': '22',
        'username': 'aaa',
        'password': 'bbb'
    },
    {
        'ip': '010.0.0.1',
        'port': '22',
        'username': 'aaa',
        'password': 'bbb'
    },
    {
        'ip': 'fe80:2030:31:24',
        'port': '22',
        'username': 'aaa',
        'password': 'bbb'
    }
]


@pytest.mark.parametrize("profile", invalid_ip_tests)
def test_invalid_ip(profile):
    with pytest.raises(ValidationError):
        Host.model_validate(profile)


correct_ip_tests = [
    {
        'ip': '0.0.0.0',
        'port': '22',
        'username': 'aaa',
        'password': 'bbb'
    },
    {
        'ip': '255.255.255.255',
        'port': '22',
        'username': 'aaa',
        'password': 'bbb'
    },
    {
        'ip': '2001:0db8:85a3:0000:0000:8a2e:0370:7334',
        'port': '22',
        'username': 'aaa',
        'password': 'bbb'
    }
]


@pytest.mark.parametrize("profile", correct_ip_tests)
def test_correct_ip(profile):
    Host.model_validate(profile)
