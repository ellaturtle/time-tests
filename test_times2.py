import pytest
import yaml
from times import time_range, compute_overlap_time

with open('fixtures.yaml', 'r') as file:
    fixture = yaml.safe_load(file) # Load test fixtures from a YAML file
    print(fixture)      

@pytest.mark.parametrize("test_name", fixture) #fixture is a list of dictionaries
def test_compute_overlap_time(test_name): #test_name is each dictionary in the list
    properties = list(test_name.values())[0] # Get the properties dictionary
    first_range = time_range(*properties['time_range1']) # Unpack the time_range1 list
    second_range = time_range(*properties['time_range2']) # Unpack the time_range2 list
    expected_overlap = [(start, stop) for start, stop in properties['expected']]
    assert compute_overlap_time(first_range, second_range) == expected_overlap

def test_backwards_time_range():
    expected_error_message = "end_time must be after start_time"
    with pytest.raises(ValueError, match=expected_error_message):
        time_range("2010-01-12 10:30:00", "2010-01-12 10:00:00") 