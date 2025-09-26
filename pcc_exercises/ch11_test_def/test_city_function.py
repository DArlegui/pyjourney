from city_function import get_formatted_location, get_formatted_location_default


# def test_missing_paramter():  # Fail
#     formatted_location = get_formatted_location("sacramento", "california")
#     assert formatted_location == "Sacramento California 5000000"


# def test_filled_parameter():  # Pass
#     formatted_location = get_formatted_location("sacramento", "california", 5_000_000)
#     assert formatted_location == "Sacramento California 5000000"


def test_get_formatted_location_default():  # Pass
    formatted_location = get_formatted_location_default("santiago", "chile")
    assert formatted_location == "Santiago Chile 3500000"
