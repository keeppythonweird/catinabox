from complected import cats


def test__setup_cats__many_cats(mocker):
    random_choice = mocker.patch('random.choice')

    random_choice.side_effect = [
        # Mock the cat names
        "Frazzle", "Dazzle", "Razzle",
        # Mock the foods the cats will be fed
        "cheese", "cucumber", "papaya"
    ]

    result_cats = cats.setup_cats(3)

    assert result_cats[0] == {"name": "Frazzle",
                              "last_ate": "cheese"}

    assert result_cats[1] == {"name": "Dazzle",
                              "last_ate": "cucumber"}

    assert result_cats[2] == {"name": "Razzle",
                              "last_ate": "papaya"}


def test__setup_cat__one_cat(mocker):
    random_choice = mocker.patch('random.choice')

    random_choice.side_effect = [
        # Mock the cat names
        "Frazzle",
        # Mock the foods the cats will be fed
        "cheese"
    ]

    result_cats = cats.setup_cats(1)

    assert result_cats == [{"name": "Frazzle",
                            "last_ate": "cheese"}]


def test__setup_cat__no_cats(mocker):
    result_cats = cats.setup_cats(0)
    assert result_cats == []
