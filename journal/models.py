# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Attendance(models.Model):
    type = models.IntegerField()
    date = models.DateField(blank=True, null=True)
    student = models.ForeignKey('journal.models.Student', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attendance'


class Duties(models.Model):
    student = models.ForeignKey('journal.models.Student', models.DO_NOTHING)
    type = models.ForeignKey('DutyTypes', models.DO_NOTHING, db_column='type')
    date = models.DateField()
    mark = models.IntegerField(blank=True, null=True)
    comment = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'duties'


class DutyTypes(models.Model):
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'duty_types'


class EventParticipants(models.Model):
    student = models.ForeignKey('journal.models.Student', models.DO_NOTHING)
    event = models.ForeignKey('Events', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event_participants'


class Events(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'events'


class Exam(models.Model):
    subject = models.ForeignKey('journal.models.Subject', models.DO_NOTHING, db_column='subject')
    date = models.DateField()
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exams'


class FinalMark(models.Model):
    student = models.ForeignKey('journal.models.Student', models.DO_NOTHING, blank=True, null=True)
    val = models.IntegerField(blank=True, null=True)
    final = models.ForeignKey('journal.models.Final', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'final_marks'


class Final(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True)
    subject = models.ForeignKey('journal.models.Subject', models.DO_NOTHING, blank=True, null=True)
    squad = models.ForeignKey('journal.models.Squad', models.DO_NOTHING, blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'finals'


class Mark(models.Model):
    student = models.ForeignKey('journal.models.Student', models.DO_NOTHING, blank=True, null=True)
    teacher = models.ForeignKey('journal.models.Teacher', models.DO_NOTHING, blank=True, null=True)
    subject = models.ForeignKey('journal.models.Subject', models.DO_NOTHING, blank=True, null=True)
    val = models.IntegerField(blank=True, null=True)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'marks'


class Penalty(models.Model):
    type = models.ForeignKey('journal.models.PenaltyType', models.DO_NOTHING, db_column='type')
    comment = models.CharField(max_length=256, blank=True, null=True)
    student = models.ForeignKey('journal.models.Student', models.DO_NOTHING)
    teacher = models.ForeignKey('journal.models.Teacher', models.DO_NOTHING, blank=True, null=True)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'penalties'


class PenaltyType(models.Model):
    name = models.CharField(unique=True, max_length=256)
    good = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'penalty_types'


class Squad(models.Model):
    code = models.CharField(unique=True, max_length=4, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'squads'


class Student(models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    squad = models.ForeignKey(Squad, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students'


class Subject(models.Model):
    short = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subjects'


class Teacher(models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    rank = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teachers'
