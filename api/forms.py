from django import forms


class LessonForm(forms.Form):
    name = forms.CharField(label='Название', max_length=100)
    date = forms.CharField(label='Дата', max_length=100)
    subject_id = forms.IntegerField(label='Дисциплина')
    squad_code = forms.CharField(label='Взвод', max_length=100)


class PenaltyForm(forms.Form):
    student_id = forms.IntegerField(label="Студент")
    comment = forms.CharField(label='Комментарий', max_length=100)
    attendance_id = forms.IntegerField(label='День посещения')
    penalty_type = forms.CharField(label="Статус")


class NewAttendanceForm(forms.Form):
    squad_code = forms.CharField(label="Взвод", max_length=4)
    date = forms.DateField(label='Дата')


class SetAttendanceStatusForm(forms.Form):
    student_id = forms.IntegerField(label="Студент")
    attendance_id = forms.IntegerField(label="Записка")
    attendance_type = forms.IntegerField(label="Статус")
