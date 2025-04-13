import pytest

from tests.accounts.factories import UserFactory


@pytest.fixture()
def auth_client(client):
    """An already authenticated client."""
    user = UserFactory()
    client.force_login(user)
    return client
