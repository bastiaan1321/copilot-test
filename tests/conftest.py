import copy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def reset_activities_state():
    original_state = copy.deepcopy(activities)

    yield

    activities.clear()
    activities.update(original_state)


@pytest.fixture
def client(reset_activities_state):
    return TestClient(app)
