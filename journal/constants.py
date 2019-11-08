from journal.models import StudentAttendanceType


ATTENDANCE_TYPE_PRESENT = StudentAttendanceType(
    value="present",
    name="_Присутствует",
)

ATTENDANCE_TYPE_TRUANT = StudentAttendanceType(
    value="truant",
    name="_Неув. причина",
)

ATTENDANCE_TYPE_ABSENT = StudentAttendanceType(
    value="absent",
    name="_Ув. причина",
)

ATTENDANCE_TYPE_DUTY = StudentAttendanceType(
    value="duty",
    name="_В наряде",
)

ATT_TYPES = [
    ATTENDANCE_TYPE_PRESENT,
    ATTENDANCE_TYPE_ABSENT,
    ATTENDANCE_TYPE_TRUANT,
    ATTENDANCE_TYPE_DUTY,
]


def name_by_value(value):
    for t in ATT_TYPES:
        if t.value == value:
            return t.name
    return None
