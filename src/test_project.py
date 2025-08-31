from main import get_next_3_days_data, get_rain_probabilities, determine_highest_probability, determine_rain_likelihood

import pytest

# test input must be list
def test_input_list():
    assert get_next_3_days_data([0, 1, 2, 3, 4, 5]) == [1, 2, 3]
    assert type(get_next_3_days_data([0, 1, 2, 3, 4, 5])) == list
    with pytest.raises(ValueError):
        get_next_3_days_data({"hi": 1})

# test length of output list
def test_output_length():
    assert len(get_next_3_days_data([0, 1, 2, 3, 4, 5])) == 3

# test comparing day and night probability of rain
def test_compare_day_night_rain():
    assert get_rain_probabilities({"time": 2020-12-31, "dayProbabilityOfRain": 10, "nightProbabilityOfRain": 90}) == {"time": 2020-12-31, "probability_of_rain": 90}
    assert get_rain_probabilities({"time": 2000-12-31, "dayProbabilityOfRain": 85, "nightProbabilityOfRain": 50}) == {"time": 2000-12-31, "probability_of_rain": 85}

# test return the day with highest probability of rain
def test_day_highest_prob_rain():
    assert determine_highest_probability([{"time": "2020-01-01", "probability_of_rain": 90}, {"time": "2020-01-02", "probability_of_rain": 50}]) == {"time": "2020-01-01", "probability_of_rain": 90}

# test for rain likelihood
def test_rain_likelihood():
    assert determine_rain_likelihood({"time": "2020-01-01", "probability_of_rain": 90}) == "It is very likely to rain on 2020-01-01"
    assert determine_rain_likelihood({"time": "2025-01-01", "probability_of_rain": 1}) == "WATER YOUR PLANTS!"
    assert determine_rain_likelihood({"time": "2000-01-01", "probability_of_rain": 65}) == "It is likely to rain on 2000-01-01"
