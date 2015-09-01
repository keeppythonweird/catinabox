def test_service_works(food_truck_client):
    resp = food_truck_client.get('')
    assert resp.status_code == 200
    assert resp.json() == 'Welcome to the food truck!'
