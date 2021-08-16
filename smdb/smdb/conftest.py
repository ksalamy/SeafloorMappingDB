import pytest

from smdb.models import MissionType, Person, PlatformType
from smdb.users.models import User

from smdb.users.tests.factories import UserFactory

from smdb.tests.factories import MissionTypeFactory, PersonFactory, PlatformTypeFactory

##from smdb.tests.factories import MissionFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> User:
    return UserFactory()


@pytest.fixture
def missiontype() -> MissionType:
    return MissionTypeFactory()


@pytest.fixture
def person() -> Person:
    return PersonFactory()


@pytest.fixture
def platformtype() -> PlatformType:
    return PlatformTypeFactory()


""" Waiting for serialization
@pytest.fixture
def mission() -> Mission:
    return MissionFactory()
"""
