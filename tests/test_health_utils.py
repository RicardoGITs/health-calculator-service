import pytest
from health_utils import calculate_bmi, calculate_bmr
from app import app

def test_calculate_bmi():
    assert round(calculate_bmi(1.75, 70), 2) == 22.86

def test_calculate_bmi_zero_height():
    with pytest.raises(ValueError):
        calculate_bmi(0, 70)

def test_calculate_bmr_male():
    # corrected expected value to 1695.67
    assert round(calculate_bmr(175, 70, 30, 'male'), 2) == pytest.approx(1695.67, rel=1e-2)

def test_calculate_bmr_female():
    # corrected expected value to 1389.84
    assert round(calculate_bmr(160, 60, 25, 'female'), 2) == pytest.approx(1389.84, rel=1e-2)

@pytest.fixture
def client():
    return app.test_client()

def test_bmi_endpoint(client):
    response = client.post('/bmi', json={'height': 1.75, 'weight': 70})
    assert response.status_code == 200
    assert 'bmi' in response.json

def test_bmr_endpoint(client):
    response = client.post('/bmr', json={'height': 175, 'weight': 70, 'age': 30, 'gender': 'male'})
    assert response.status_code == 200
    assert 'bmr' in response.json
