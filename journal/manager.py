from journal.models import Mark, Student
from api.models import namedtuple_wrapper
from datetime import datetime as dt

tMark = namedtuple_wrapper(
    "tMark",
    [
        "id",
        "x_key",
        "y_key",
        "val",
        "date",
    ]
)

tKey = namedtuple_wrapper(
    "tKey",
    [
        "id",
        "display",
        "sort",
    ]
)



# date X student, fixed subject ID
def by_subject(marks_list: [Mark]) -> [tMark]:
    ls = []

    for m in marks_list:
        mr = tMark(
            id=m.id,
            x_key=student_to_key(m.student),
            y_key=date_to_key(m.date),
            val=m.val,
            date=m.date,
        )
        ls.append(mr)
    return ls



def make_cells(x_keys: [tKey], y_keys: [tKey], marks: [tMark]):
    pass



def date_to_key(d):
    date = dt.date(d)
    return tKey(
        id=123,
        display=date.isoformat(),
        sort=date,
    )



def student_to_key(s: Student) -> tKey:
    return tKey(
        id=s.id,
        display=student_short_name(s),
        sort=student_short_name(s),
    )



def students_to_keys(ls: [Student]) -> [tKey]:
    return sorted(map(student_to_key, ls), key=lambda x: x.sort)



def student_short_name(s: Student) -> str:
    return f'{s.last_name} {__get0(s.first_name)}. {__get0(s.middle_name)}'



def __get0(s: str) -> str:
    if len(s) > 0:
        return s[0]
    return ''
