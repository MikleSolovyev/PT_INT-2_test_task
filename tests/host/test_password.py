import pytest
from pydantic import ValidationError

from src.host import Host

invalid_password_tests = [
    {
        'ip': '0.0.0.0',
        'port': '22',
        'username': 'a'
    },
    {
        'ip': '0.0.0.0',
        'port': '22',
        'username': 'a',
        'passwords': None
    }
]


@pytest.mark.parametrize("profile", invalid_password_tests)
def test_invalid_password(profile):
    with pytest.raises(ValidationError):
        Host.model_validate(profile)


correct_password_tests = [
    {
        'ip': '0.0.0.0',
        'port': '22',
        'username': 'a',
        'password': ''
    }
]


@pytest.mark.parametrize("profile", correct_password_tests)
def test_correct_password(profile):
    Host.model_validate(profile)
