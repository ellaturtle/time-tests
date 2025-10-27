import pytest
# Import the times.py file to test its functions.
from times import time_range, compute_overlap_time

# Move the content from the `if __name__ ...` block from `times.py` to a function called `test_given_input` into `test_times.py`
def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00")
    result = compute_overlap_time(large, short)
    expected = [("2010-01-12 10:30:00", "2010-01-12 10:45:00")]
    assert result == expected

def test_no_overlap():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 10:30:00")
    short = time_range("2010-01-12 10:40:00", "2010-01-12 10:50:00")
    result = compute_overlap_time(large, short)
    expected = []
    assert result == expected

def test_several_intervals():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00", 3)
    short = time_range("2010-01-12 10:20:00", "2010-01-12 10:40:00", 2)
    result = compute_overlap_time(large, short)
    expected = [("2010-01-12 10:20:00", "2010-01-12 10:30:00"),
                ("2010-01-12 10:30:00", "2010-01-12 10:40:00")]
    assert result == expected

def test_times_touching():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 10:30:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00")
    result = compute_overlap_time(large, short)
    expected = []
    assert result == expected   

def test_backwards_time_range():
    try:
        result = time_range("2010-01-12 10:30:00", "2010-01-12 10:00:00")
    except ValueError as e:
        result = e

def test_backwards_time_range():
    start_time = "2010-01-12 10:30:00"
    end_time = "2010-01-12 10:00:00"

    with pytest.raises(ValueError, match="end_time must be after start_time"):
        time_range(start_time, end_time)        