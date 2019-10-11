from django.urls import path

import api.views as views


urlpatterns = [
    # path('', views.index, name='index'),
    path('marks/add', views.add_mark, name='marks_add'),
    path('lessons/add', views.add_lesson, name='lessons_add'),
    path('attendance/add', views.add_attendance, name='attendance_add'),
    path('attendance/set', views.set_attendance, name='attendance_set'),
    # path('students/<int:student_id>', views.student, name='student'),

    # path('marks/', views.marks_base, name='marks'),
    # path('marks/<str:squad_code>/<int:subject_id>', views.marks_squad, name='marks_squad'),
    # path("<int:user_id>", views.borrower_page, name="borrower_page")
]
