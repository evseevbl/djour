from django.urls import path

import api.views.add_lesson
import api.views.add_mark
from api import views


urlpatterns = [
    # path('', views.index, name='index'),
    path('marks/add', api.views.add_mark.add_mark, name='marks_add'),
    path('lessons/add', api.views.add_lesson.add_lesson, name='lessons_add'),
    # path('students/<int:student_id>', views.student, name='student'),

    # path('marks/', views.marks_base, name='marks'),
    # path('marks/<str:squad_code>/<int:subject_id>', views.marks_squad, name='marks_squad'),
    # path("<int:user_id>", views.borrower_page, name="borrower_page")
]
