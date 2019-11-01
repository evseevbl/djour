# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



# from journal.managers.marks import student_short_name


class Attendance(models.Model):
    date = models.DateField('Дата', blank=True, null=True)
    squad = models.ForeignKey('journal.Squad', models.CASCADE, blank=False, null=True)
    students = models.ManyToManyField('journal.StudentAttendance')


    @property
    def absent(self):
        return len(self.students.filter(type__value__iregex='(absent|truant)'))



    class Meta:
        managed = True
        db_table = 'attendance'



class StudentAttendance(models.Model):
    student = models.ForeignKey('journal.Student', models.CASCADE)
    type = models.ForeignKey('journal.StudentAttendanceType', models.CASCADE, blank=False, null=True)



    class Meta:
        managed = True



class StudentAttendanceType(models.Model):
    value = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)



    class Meta:
        managed = True
        db_table = 'attendance_types'



class Duty(models.Model):
    student = models.ForeignKey('journal.Student', models.CASCADE)
    type = models.ForeignKey('journal.DutyType', models.CASCADE, db_column='type')
    date = models.DateField('Дата')
    mark = models.IntegerField(blank=True, null=True)
    comment = models.CharField(max_length=100, blank=True, null=True)



    class Meta:
        managed = True
        db_table = 'duties'



class DutyType(models.Model):
    name = models.CharField(unique=True, max_length=100)



    class Meta:
        managed = True
        db_table = 'duty_types'



class EventParticipant(models.Model):
    student = models.ForeignKey('journal.Student', models.CASCADE)
    event = models.ForeignKey('journal.Event', models.CASCADE, blank=True, null=True)



    class Meta:
        managed = True
        db_table = 'event_participants'



class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()



    class Meta:
        managed = True
        db_table = 'events'



class Exam(models.Model):
    subject = models.ForeignKey('journal.Subject', models.CASCADE, db_column='subject')
    date = models.DateField('Дата')
    name = models.CharField('Название', max_length=100, blank=True, null=True)



    class Meta:
        managed = True
        db_table = 'exams'



class FinalMark(models.Model):
    student = models.ForeignKey('journal.Student', models.CASCADE, blank=True, null=True)
    val = models.IntegerField('Оценка', blank=True, null=True)
    final = models.ForeignKey('journal.Final', models.CASCADE, blank=True, null=True)



    class Meta:
        managed = True
        db_table = 'final_marks'



class Final(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True)
    subject = models.ForeignKey('journal.Subject', models.CASCADE, blank=True, null=True)
    squad = models.ForeignKey('journal.Squad', models.CASCADE, blank=True, null=True)
    date = models.DateField('Дата', blank=True, null=True)



    class Meta:
        managed = True
        db_table = 'finals'



class Mark(models.Model):
    student = models.ForeignKey('journal.Student', models.CASCADE, blank=True, null=True)
    teacher = models.ForeignKey('journal.Teacher', models.CASCADE, blank=True, null=True)
    # subject = models.ForeignKey('journal.Subject', models.CASCADE, blank=True, null=True)
    val = models.IntegerField(blank=True, null=True)
    lesson = models.ForeignKey('journal.Lesson', models.CASCADE, blank=True, null=True)



    class Meta:
        managed = True
        db_table = 'marks'



class Penalty(models.Model):
    type = models.ForeignKey('journal.PenaltyType', models.CASCADE, db_column='type')
    comment = models.CharField('Комментарий', max_length=256, blank=True, null=True)
    student = models.ForeignKey('journal.Student', models.CASCADE)
    teacher = models.ForeignKey('journal.Teacher', models.CASCADE, blank=True, null=True)
    date = models.DateField('Дата')



    class Meta:
        managed = True
        db_table = 'penalties'



class PenaltyType(models.Model):
    name = models.CharField(unique=True, max_length=256)
    good = models.BooleanField()



    class Meta:
        managed = True
        db_table = 'penalty_types'



class Squad(models.Model):
    code = models.CharField(unique=True, max_length=4, blank=True, null=True)



    class Meta:
        managed = True
        db_table = 'squads'
        verbose_name = 'Взвод'
        verbose_name_plural = 'Взвода'



    def __str__(self):
        return f'{self.code}'



class Student(models.Model):
    last_name = models.CharField('Фамилия', max_length=50, blank=True, null=True)
    first_name = models.CharField('Имя', max_length=50, blank=True, null=True)
    middle_name = models.CharField('Отчество', max_length=50, blank=True, null=True)
    squad = models.ForeignKey(Squad, models.CASCADE, blank=True, null=True)


    def __str__(self):
        return f'({self.squad.code}) {self.last_name} {self.first_name} {self.middle_name} [{self.id}]'


    @property
    def short(self) -> str:
        def __get0(s: str) -> str:
            if len(s) > 0:
                return s[0]
            return '?'


        return f'{self.last_name} {__get0(self.first_name)}. {__get0(self.middle_name)}.'



    class Meta:
        managed = True
        db_table = 'students'
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'



class Subject(models.Model):
    short = models.CharField('Сокращённое название', max_length=10, blank=True, null=True)
    name = models.CharField('Полное название', max_length=255, blank=True, null=True)


    def __str__(self):
        return f'({self.short}) [{self.id}]'



    class Meta:
        managed = True
        db_table = 'subjects'
        verbose_name = 'Дисциплина'
        verbose_name_plural = 'Дисциплины'



class Teacher(models.Model):
    last_name = models.CharField('Фамилия', max_length=50, blank=True, null=True)
    first_name = models.CharField('Имя', max_length=50, blank=True, null=True)
    middle_name = models.CharField('Отчество', max_length=50, blank=True, null=True)
    rank = models.CharField('звание', max_length=50, blank=True, null=True)



    class Meta:
        managed = True
        db_table = 'teachers'



class Curriculum(models.Model):
    squad = models.ForeignKey(Squad, models.CASCADE, blank=True, null=True)
    subject = models.ForeignKey(Subject, models.CASCADE, blank=True, null=True)


    def __str__(self):
        return f'({self.squad.code}) {self.subject.short} [{self.id}]'



    class Meta:
        managed = True
        db_table = 'curriculum'

        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписание'



class Lesson(models.Model):
    squad = models.ForeignKey(Squad, models.CASCADE, blank=True, null=True)
    subject = models.ForeignKey(Subject, models.CASCADE, blank=True, null=True)
    # date = models.DateField(blank=True, null=True)
    name = models.CharField('Название', max_length=100, blank=True, null=False)
    attendance = models.ForeignKey(Attendance, models.CASCADE, blank=True, null=True)



    class Meta:
        managed = True
        db_table = 'lessons'
        verbose_name = 'Занятие'
        verbose_name_plural = 'Занятия'



class PersonalInfo(models.Model):
    student = models.ForeignKey(Student, models.CASCADE, blank=False, null=False)

    passport_code = models.CharField(max_length=4, blank=True, null=False)
    passport_number = models.CharField(max_length=6, blank=True, null=False)
    passport_issued = models.CharField(max_length=6, blank=True, null=False)

    address = models.CharField(max_length=512, blank=True, null=False)

    birth_date = models.DateField(blank=True, null=True)

    characteristic = models.TextField(blank=True, null=False)



    class Meta:
        managed = True
        db_table = 'student_info'
