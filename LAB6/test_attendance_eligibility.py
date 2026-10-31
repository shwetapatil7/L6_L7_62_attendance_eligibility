import pytest
from attendance_eligibility import attendance_percent, exam_eligibility, attendance_warning


# Original test cases
def test_plain_percent():
    assert attendance_percent(30, 40, 0) == 75


def test_eligible():
    assert exam_eligibility(80, False, True) == "eligible"


# Attendance percentage tests
def test_invalid_total():
    with pytest.raises(ValueError):
        attendance_percent(10, 0, 0)


def test_negative_attendance():
    with pytest.raises(ValueError):
        attendance_percent(-5, 40, 0)


def test_attendance_greater_than_total():
    with pytest.raises(ValueError):
        attendance_percent(45, 40, 0)


def test_medical_leave_above_five():
    assert attendance_percent(20, 40, 6) == 62


def test_medical_leave_within_limit():
    assert attendance_percent(20, 40, 5) == 62


def test_credited_attendance_exceeds_total():
    assert attendance_percent(38, 40, 5) == 100


# Exam eligibility tests
def test_fees_pending():
    assert exam_eligibility(90, False, False) == "fees pending"


def test_eligible_by_attendance():
    assert exam_eligibility(75, False, True) == "eligible"


def test_eligible_with_condonation():
    assert exam_eligibility(65, True, True) == "eligible"


def test_condonation_required():
    assert exam_eligibility(65, False, True) == "condonation required"


def test_detained():
    assert exam_eligibility(60, False, True) == "detained"


# Attendance warning tests
def test_no_warning():
    assert attendance_warning(85, 2) is None


def test_critical_warning():
    assert attendance_warning(70, 5) == "critical"


def test_final_notice():
    assert attendance_warning(70, 4) == "final notice"


def test_reminder():
    assert attendance_warning(80, 3) == "reminder"