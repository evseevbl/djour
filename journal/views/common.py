from journal.models import Mark


def get_average_mark(subject, student_id, absent_zero=False):
    print("avg for", subject.short)
    if absent_zero:
        marks = Mark.objects.filter(student_id=student_id, lesson__subject=subject)
    else:
        marks = Mark.objects.filter(student_id=student_id, lesson__subject=subject, val__gt=0)
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
    print(f'avg student={student_id}, avg={avg}, subj={subject.short}, zeroed={absent_zero}')
    return avg