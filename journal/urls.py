from django.urls import path
from journal import views


urlpatterns = [
    path('', views.index, name='index'),
    path('students/', views.students, name='students'),
    path('students/<int:student_id>', views.student, name='student'),
    path('marks/', views.marks_base, name='marks'),
    path('marks/<str:squad_code>/', views.marks_squad, name='marks_squad'),
    # path("<int:user_id>", views.borrower_page, name="borrower_page")
]
