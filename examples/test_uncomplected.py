from uncomplected import cats


def test__cat_feed():
    cat = cats.Cat("Whiskers")
    cat.feed("tuna")
    assert cat.last_ate == "tuna"


def test__get_cat_name(mocker):
    mocker.patch('random.choice', return_value="Snookums")
    cat_name = cats.get_cat_name()
    assert cat_name == "Snookums"


def test__get_food(mocker):
    mocker.patch('random.choice', return_value="carrot")
    food = cats.get_food()
    assert food == "carrot"


def test__setup_cats__many_cats(mocker):
    mocker.patch.object(cats, "get_cat_name", side_effect=["Jess", "Larry",
                                                           "Sue"])
    mocker.patch.object(cats, "get_food", side_effect=["berries", "milk",
                                                       "soda"])
    result_cats = cats.setup_cats(3)
    assert result_cats == [
        cats.Cat("Jess", "berries"),
        cats.Cat("Larry", "milk"),
        cats.Cat("Sue", "soda")
    ]


def test__setup_cats__one_cat(mocker):
    mocker.patch.object(cats, "get_cat_name", return_value="Aslan")
    mocker.patch.object(cats, "get_food", return_value="lamb")

    result_cats = cats.setup_cats(1)
    assert result_cats == [cats.Cat("Aslan", "lamb")]


def test__setup_cats__no_cats():
    result_cats = cats.setup_cats(0)
    assert result_cats == []
