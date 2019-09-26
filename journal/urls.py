from django.urls import path

import journal.views.index
import journal.views.marks_base
import journal.views.marks_squad
import journal.views.student
import journal.views.students
from journal import views


urlpatterns = [
    path('', journal.views.index.index, name='index'),
    path('students/', journal.views.students.students, name='students'),
    path('students/<int:student_id>', journal.views.student.student, name='student'),
    path('marks/', journal.views.marks_base.marks_base, name='marks'),
    path('marks/<str:squad_code>/<int:subject_id>', journal.views.marks_squad.marks_squad, name='marks_squad'),
    # path("<int:user_id>", views.borrower_page, name="borrower_page")
]
