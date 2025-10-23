# Import the times.py file to test its functions.
from times import time_range, compute_overlap_time

# Move the content from the `if __name__ ...` block from `times.py` to a function called `test_given_input` into `test_times.py`
def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00")
    result = compute_overlap_time(large, short)
    expected = [("2010-01-12 10:30:00", "2010-01-12 10:45:00")]
    assert result == expected
    

