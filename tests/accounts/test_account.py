from http import HTTPStatus

import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse


@pytest.mark.django_db
def test_sign_up_post(client):
    """The repsonse to a POST request redirects to the homepage and creates a new user."""
    data = {"email": "anon@acme.com", "password1": "5QCcj$r*qWn7eY"}
    response = client.post(reverse("account_signup"), data)
    assert response.status_code == HTTPStatus.FOUND
    assert get_user_model().objects.get(email="anon@acme.com")
