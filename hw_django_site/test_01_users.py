from django.contrib.auth.models import User
import pytest


@pytest.mark.django_db
def test_my_user():
    me = User.objects.get(username='x')
    assert me.is_superuser
