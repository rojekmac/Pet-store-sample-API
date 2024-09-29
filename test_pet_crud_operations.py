import pytest
import requests

BASE_URL = "https://petstore.swagger.io/v2"

@pytest.fixture
def new_pet_data():
    return {
        "id": 133713371337,
        "category": {"id": 1, "name": "Doggo"},
        "name": "Loupe's Pet",
        "photoUrls": ["https://loremipsum.com/big-dog-photo.png"],
        "tags": [{"id": 1, "name": "Good boi"}],
        "status": "available"
    }

@pytest.fixture
def add_new_pet(new_pet_data):
    response = requests.post(f"{BASE_URL}/pet", json=new_pet_data)
    return response

# Covering "Create" - checking the correct status code / id / name / status
def test_add_new_pet_status_code(add_new_pet):
    assert add_new_pet.status_code == 200

def test_add_new_pet_id(add_new_pet, new_pet_data):
    pet_data = add_new_pet.json()
    assert pet_data["id"] == new_pet_data["id"]

def test_add_new_pet_name(add_new_pet, new_pet_data):
    pet_data = add_new_pet.json()
    assert pet_data["name"] == new_pet_data["name"]

def test_add_new_pet_status(add_new_pet, new_pet_data):
    pet_data = add_new_pet.json()
    assert pet_data["status"] == new_pet_data["status"]

# Covering "Read"
def test_get_pet_by_id(new_pet_data):
    pet_id = new_pet_data["id"]
    response = requests.get(f"{BASE_URL}/pet/{pet_id}")
    assert response.status_code == 200
    pet_data = response.json()
    assert pet_data["id"] == pet_id
    assert pet_data["name"] == new_pet_data["name"]

# Covering "Update"
def test_update_pet(new_pet_data):
    updated_data = new_pet_data.copy()
    updated_data["name"] = "UpdatedDoggo"
    response = requests.put(f"{BASE_URL}/pet", json=updated_data)
    assert response.status_code == 200
    updated_pet = response.json()
    assert updated_pet["name"] == "UpdatedDoggo"

# Covering "Delete"
def test_delete_pet(add_new_pet, new_pet_data):
    pet_id = new_pet_data["id"]
    response = requests.delete(f"{BASE_URL}/pet/{pet_id}")
    assert response.status_code == 200
    
    # Verify our dog got deleted successfully
    get_response = requests.get(f"{BASE_URL}/pet/{pet_id}")
    assert get_response.status_code == 404

if __name__ == "__main__":
    pytest.main()