from django.urls import path
from journal import views

urlpatterns = [
    path('', views.index, name='index'),
    path('students/', views.students, name='students'),
    path('students/<int:student_id>', views.student, name='student'),
    path('marks/<str:squad_code>/<int:subject_id>', views.marks_squad, name='marks_squad'),
    path('attendance/', views.attendance, name='attendance'),
    path('attendance/<int:attendance_id>', views.edit_attendance, name='attendance_edit'),
    # path("<int:user_id>", views.borrower_page, name="borrower_page")
]
