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
    date = models.DateField(blank=True, null=True)
    squad = models.ForeignKey('journal.Squad', models.DO_NOTHING, blank=False, null=True)
    students = models.ManyToManyField('journal.StudentAttendance')



    class Meta:
        managed = True
        db_table = 'attendance'



class StudentAttendance(models.Model):
    student = models.ForeignKey('journal.Student', models.DO_NOTHING)
    value = models.IntegerField(null=True)
    pass



class Duty(models.Model):
    student = models.ForeignKey('journal.Student', models.DO_NOTHING)
    type = models.ForeignKey('journal.DutyType', models.DO_NOTHING, db_column='type')
    date = models.DateField()
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
    student = models.ForeignKey('journal.Student', models.DO_NOTHING)
    event = models.ForeignKey('journal.Event', models.DO_NOTHING, blank=True, null=True)



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
    subject = models.ForeignKey('journal.Subject', models.DO_NOTHING, db_column='subject')
    date = models.DateField()
    name = models.CharField(max_length=100, blank=True, null=True)



    class Meta:
        managed = True
        db_table = 'exams'



class FinalMark(models.Model):
    student = models.ForeignKey('journal.Student', models.DO_NOTHING, blank=True, null=True)
    val = models.IntegerField(blank=True, null=True)
    final = models.ForeignKey('journal.Final', models.DO_NOTHING, blank=True, null=True)



    class Meta:
        managed = True
        db_table = 'final_marks'



class Final(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True)
    subject = models.ForeignKey('journal.Subject', models.DO_NOTHING, blank=True, null=True)
    squad = models.ForeignKey('journal.Squad', models.DO_NOTHING, blank=True, null=True)
    date = models.DateField(blank=True, null=True)



    class Meta:
        managed = True
        db_table = 'finals'



class Mark(models.Model):
    student = models.ForeignKey('journal.Student', models.DO_NOTHING, blank=True, null=True)
    teacher = models.ForeignKey('journal.Teacher', models.DO_NOTHING, blank=True, null=True)
    # subject = models.ForeignKey('journal.Subject', models.DO_NOTHING, blank=True, null=True)
    val = models.IntegerField(blank=True, null=True)
    lesson = models.ForeignKey('journal.Lesson', models.DO_NOTHING, blank=True, null=True)



    class Meta:
        managed = True
        db_table = 'marks'



class Penalty(models.Model):
    type = models.ForeignKey('journal.PenaltyType', models.DO_NOTHING, db_column='type')
    comment = models.CharField(max_length=256, blank=True, null=True)
    student = models.ForeignKey('journal.Student', models.DO_NOTHING)
    teacher = models.ForeignKey('journal.Teacher', models.DO_NOTHING, blank=True, null=True)
    date = models.DateField()



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



    def __str__(self):
        return f'{self.code}'



class Student(models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    squad = models.ForeignKey(Squad, models.DO_NOTHING, blank=True, null=True)


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
    short = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)



    class Meta:
        managed = True
        db_table = 'subjects'
        verbose_name = 'Дисциплина'
        verbose_name_plural = 'Дисциплины'



class Teacher(models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    rank = models.CharField(max_length=50, blank=True, null=True)



    class Meta:
        managed = True
        db_table = 'teachers'



class Curriculum(models.Model):
    squad = models.ForeignKey(Squad, models.DO_NOTHING, blank=True, null=True)
    subject = models.ForeignKey(Subject, models.DO_NOTHING, blank=True, null=True)



    class Meta:
        managed = True
        db_table = 'curriculum'



class Lesson(models.Model):
    squad = models.ForeignKey(Squad, models.DO_NOTHING, blank=True, null=True)
    subject = models.ForeignKey(Subject, models.DO_NOTHING, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=False)



    class Meta:
        managed = True
        db_table = 'lessons'



class PersonalInfo(models.Model):
    student = models.ForeignKey(Student, models.DO_NOTHING, blank=False, null=False)

    passport_code = models.CharField(max_length=4, blank=True, null=False)
    passport_number = models.CharField(max_length=6, blank=True, null=False)
    passport_issued = models.CharField(max_length=6, blank=True, null=False)

    address = models.CharField(max_length=512, blank=True, null=False)

    birth_date = models.DateField(blank=True, null=True)

    characteristic = models.TextField(blank=True, null=False)



    class Meta:
        managed = True
        db_table = 'student_info'
