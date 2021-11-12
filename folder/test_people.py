import requests
from assertpy.assertpy import assert_that
from json import dumps


BASE_URI = 'https://rahulshettyacademy.com/maps/api/place'


def test_read_all_has_kent():
    response = requests.get(BASE_URI)
    places = response
    print(places)

    assert_that(response.status_code).is_equal_to(200)
    # first_name = [people['fname']for people in people]
    # assert_that(first_name).contains('Kent')