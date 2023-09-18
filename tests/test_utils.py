from project import utils


def test_get_date_formatting():
    assert utils.get_date_formatting(["2019-08-26T10:50:58.294041"]) == "26.08.2019"

