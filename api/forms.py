from django import forms

class LessonForm(forms.Form):
    name = forms.CharField(label='Название', max_length=100)
    date = forms.CharField(label='Дата', max_length=100)
    subject_id = forms.IntegerField(label='Дисциплина')
    squad_code = forms.CharField(label='Взвод', max_length=100)
