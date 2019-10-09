# from catinabox.catgenerator import get_name
# from catinabox.catgenerator import get_birthday
from catinabox import catgenerator


def test_get_name(mocker):
    mock_get = mocker.patch('requests.get', autospec=True)
    mock_get.return_value.json.return_value = (['tim'],)
    assert catgenerator.get_name() == ['tim']


def test_get_birthday(mocker):
    mock_time = mocker.patch('time.time', autospec=True)
    mock_time.side_effect = (catgenerator.SECONDS_IN_YEAR * 35,)
    mock_bday = mocker.patch('random.randint')
    mock_bday.return_value = catgenerator.SECONDS_IN_YEAR * 2
    assert catgenerator.get_birthday() == "1972-01-01 00:00:00"
    mock_bday.assert_called_with(catgenerator.SECONDS_IN_YEAR * 5,
                                 catgenerator.SECONDS_IN_YEAR * 35)


def test_cat_generator(mocker):
    mock_name = mocker.patch('catgenerator.get_name')
    mock_name.side_effect = ["David", "Moe"]
    mock_bday = mocker.patch(catgenerator, 'get_birthday')
    mock_bday.return_value = 'birthday'
    catgen = catgenerator.cat_generator()
    assert next(catgen) == {"name": "David",
                            "birthday": "birthday"}
    assert next(catgen) == {"name": "Moe",
                            "birthday": "birthday"}
