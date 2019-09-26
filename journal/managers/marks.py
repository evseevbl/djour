from datetime import datetime as dt

from journal.models import Mark, Student
from maintenance.helpers.named_tuple import namedtuple_wrapper

tMark = namedtuple_wrapper(
    "tMark",
    [
        "id",
        "x_key",
        "y_key",
        "val",
    ]
)
tKey = namedtuple_wrapper(
    "tKey",
    [
        "id",
        "display",
        "sort",
        "val",
        "comment",
    ]
)



def by_subject(marks_list: [Mark]) -> [tMark]:
    ls = []

    for m in marks_list:
        mr = tMark(
            id=m.id,
            x_key=student_to_key(m.student),
            y_key=date_to_key(m.date),
            val=m.val,
        )
        ls.append(mr)
    return ls



def make_cells(x_keys: [tKey], y_keys: [tKey], marks: [tMark]):
    # сортируем для отображения
    x_keys.sort(key=lambda k: k.sort)
    y_keys.sort(key=lambda k: k.sort)

    # порядковый номер ключа после сортировки
    xd = {}
    for i in range(len(x_keys)):
        xd[x_keys[i].id] = i
    yd = {}
    for i in range(len(y_keys)):
        yd[y_keys[i].id] = i

    # empty rows
    cells = [['' + ''] * len(x_keys) for _ in range(len(y_keys))]
    for m in marks:
        x = xd[m.x_key]
        y = yd[m.y_key]
        cells[y][x] = m

    # грязный хак: добавляем первый столбец
    for i in range(len(cells)):
        cells[i] = [y_keys[i]] + cells[i]

    return x_keys, cells



def date_to_key(d):
    ff = dt.combine(d, dt.min.time())
    return tKey(
        id=123,
        display=ff,
        sort=ff,
    )



def student_to_key(s: Student) -> tKey:
    return tKey(
        id=s.id,
        display=student_short_name(s),
        sort=student_short_name(s),
        val=s.id,
    )



def students_to_keys(ls: [Student]) -> [tKey]:
    return sorted(map(student_to_key, ls), key=lambda x: x.sort)



def student_short_name(s: Student) -> str:
    return f'{s.last_name} {__get0(s.first_name)}. {__get0(s.middle_name)}'



def __get0(s: str) -> str:
    if len(s) > 0:
        return s[0]
    return ''
