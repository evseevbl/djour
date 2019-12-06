from journal.models import Mark


def avg_mark_student(subject, student_id, absent_zero=False):
    if absent_zero:
        marks = Mark.objects.filter(student_id=student_id, lesson__subject=subject)
    else:
        marks = Mark.objects.filter(student_id=student_id, lesson__subject=subject, val__gt=0)
    return _avg_mark(marks)


def avg_marks_group(students, subj):
    return _avg_mark(
        Mark.objects.filter(lesson__subject=subj, student_id__in=_to_ids(students), val__gt=0)
    )


def _to_ids(students):
    return [s.id for s in students]


def _avg_mark(marks: [Mark]):
    avg, cnt = 0, 0
    # todo разобраться с Avg и Case/When
    for m in marks:
        m: Mark = m
        if m.val < 0:
            m.val = 0
        avg += m.val
        cnt += 1
    if cnt > 0:
        avg /= cnt
    else:
        avg = None
    return avg