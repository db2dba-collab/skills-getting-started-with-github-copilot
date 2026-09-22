from fastapi.testclient import TestClient

from src.app import app, activities


client = TestClient(app)


def test_student_cannot_sign_up_twice_for_same_activity():
    activity_name = "Chess Club"
    email = "newstudent@mergington.edu"

    original_participants = activities[activity_name]["participants"][:]

    try:
        activities[activity_name]["participants"] = [email]

        response = client.post(
            f"/activities/{activity_name}/signup?email={email}"
        )

        assert response.status_code == 409
        assert response.json()["detail"] == "Student already signed up for this activity"
    finally:
        activities[activity_name]["participants"] = original_participants
