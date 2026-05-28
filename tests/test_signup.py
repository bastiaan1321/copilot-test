from urllib.parse import quote

from src.app import activities


def test_signup_registers_participant(client):
    # Arrange
    activity_name = "Chess Club"
    email = "new.student@mergington.edu"
    activity_path = quote(activity_name, safe="")

    # Act
    response = client.post(f"/activities/{activity_path}/signup", params={"email": email})

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Signed up {email} for {activity_name}"

    activities_response = client.get("/activities")
    participants = activities_response.json()[activity_name]["participants"]
    assert email in participants


def test_unregister_removes_participant(client):
    # Arrange
    activity_name = "Programming Class"
    email = "remove.student@mergington.edu"
    activity_path = quote(activity_name, safe="")
    activities[activity_name]["participants"].append(email)

    # Act
    response = client.delete(f"/activities/{activity_path}/signup", params={"email": email})

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Unregistered {email} from {activity_name}"

    activities_response = client.get("/activities")
    participants = activities_response.json()[activity_name]["participants"]
    assert email not in participants
