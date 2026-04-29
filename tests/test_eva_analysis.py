import pytest
from eva_data_analysis import text_to_duration, calculate_crew_size

def test_text_to_duration_float():
    """
    Test that text_to_duration returns expected ground truth values
    for typical durations with a non-zero minute component
    """
    actual_result = text_to_duration("10:20")
    expected_result = 10.33333333
    assert actual_result == pytest.approx(expected_result)

def test_text_to_duration_integer():
    """
    Test that text_to_duration returns expected ground truth values
    for typical whole hour durations
    """
    actual_result = text_to_duration("10:00")
    expected_result = 10
    assert actual_result == expected_result


def test_calculate_crew_size():
    """
    Test that calculate_crew_size returns expected size of crew entries,
    which is a string of names separated by semicolons
    """

    # Typical value 1
    actual_result = calculate_crew_size("Carlota Segura Garcia; Hugues Gesbert")
    expected_result = 2
    assert actual_result == expected_result

    # Typical value 2
    actual_result = calculate_crew_size("Carlota Segura Garcia; Hugues Gesbert;")
    expected_result = 2
    assert actual_result == expected_result

    # Typical value 2
    actual_result = calculate_crew_size("Carlota Segura Garcia; Hugues Gesbert;;")
    expected_result = 2
    assert actual_result == expected_result

# Edge cases
def test_calculate_crew_size_edge_cases():
    """
    Test that calculate_crew_size returns expected ground truth values
    for edge case where crew is an empty string
    """
    actual_result = calculate_crew_size("")
    assert actual_result is None