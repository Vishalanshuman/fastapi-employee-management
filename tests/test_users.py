import pytest
import csv
from config import schema


def write_to_csv(test_name, status_code, response_data):
    with open('test_results.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([test_name, status_code, response_data])


def test_login(client, test_user):
    res = client.post(
        "/auth/login/",
        json={
            "email": test_user['email'], "password": test_user["password"]
        }
    )
    print(res.json())
    login_creds = schema.Token(**res.json())
    
    # Write results to CSV
    write_to_csv('test_login', res.status_code, res.json())
    
    assert res.status_code == 200
    assert login_creds.token_type == "bearer"


@pytest.mark.parametrize("email, password, status_code", [
    ("invalid_email", "wrognpassword", 422),
    ("example@email.com", "", 401),
    (None, "wrognpassword", 422),
    ("invalid_email", None, 422),
])
def test_invalid_credentials(client, email, password, status_code):
    res = client.post(
        "/auth/login/",
        json={
            "email": email, "password": password
        }
    )
    print(res.json())
    
    # Write results to CSV
    write_to_csv('test_invalid_credentials', res.status_code, res.json())
    
    assert res.status_code == status_code
