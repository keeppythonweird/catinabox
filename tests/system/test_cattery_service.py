import json


class TestGetCats(object):
    def test__empty_cattery(self, cattery_client):
        # Returns no cats
        result = cattery_client.get('cats')
        assert result.json() == []
        assert result.status_code == 200

        # Removing cat gives you an error
        result = cattery_client.delete('cats',
                                       data=json.dumps({"name": "Theodora"}))
        assert result.status_code == 404

        # Feeding cat gives you an error

    def test__adding_a_cat(self, cattery_client):
        # Add the cat
        result = cattery_client.post('cats',
                                     data=json.dumps({"name": "Theodora"}))
        assert result.status_code == 201

        # Get the cat that was just added
        result = cattery_client.get('cats')
        assert result.json() == [{"name": "Theodora", "food_eaten": []}]
        assert result.status_code == 200

    def test__removing_a_cat(self, cattery_client):
        # Add a cat
        cattery_client.post('cats', data=json.dumps({"name": "Theodora"}))

        # Remove the cat
        result = cattery_client.delete('cats',
                                       data=json.dumps({"name": "Theodora"}))
        assert result.status_code == 204

        # Make sure the cat is gone
        result = cattery_client.get('cats')
        assert result.json() == []

    def test__feeding_cats(self, cattery_client):
        # Add two cats
        cattery_client.post('cats', data=json.dumps({"name": "Theodora"}))
        cattery_client.post('cats', data=json.dumps({"name": "Bronson"}))

        # Put food in the pantry
        result = cattery_client.patch('pantry',
                                      data=json.dumps([("burger", 1),
                                                       ("cheezburger", 4)]))
        assert result.status_code == 204

        # Feed the cats
        result = cattery_client.post('cats/dishes')
        assert result.status_code == 204

        # Verify the cats were fed
        result = cattery_client.get('cats')
        assert result.status_code == 200
        assert result.json() == [
            {"name": "Theodora", "food_eaten": ["burger"]},
            {"name": "Bronson",
             "food_eaten": ["cheezburger"]}]

        # Verify the pantry has food left
        result = cattery_client.get('pantry')
        assert result.status_code == 200
        assert result.json() == ["cheezburger",
                                 "cheezburger",
                                 "cheezburger"]
