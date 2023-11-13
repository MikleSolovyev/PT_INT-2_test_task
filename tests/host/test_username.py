import pytest
from pydantic import ValidationError

from src.host import Host

invalid_username_tests = [
    {
        'ip': '0.0.0.0',
        'port': '22',
        'username': 1,
        'password': 'bbb'
    },
    {
        'ip': '0.0.0.0',
        'port': '22',
        'username': '',
        'password': 'bbb'
    },
    {
        'ip': '0.0.0.0',
        'port': '22',
        'password': 'bbb'
    }
]


@pytest.mark.parametrize("profile", invalid_username_tests)
def test_invalid_username(profile):
    with pytest.raises(ValidationError):
        Host.model_validate(profile)


correct_username_tests = [
    {
        'ip': '0.0.0.0',
        'port': '22',
        'username': 'a',
        'password': 'bbb'
    }
]


@pytest.mark.parametrize("profile", correct_username_tests)
def test_correct_username(profile):
    Host.model_validate(profile)
