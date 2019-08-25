from django.urls import path
from journal import views


urlpatterns = [
    path('', views.index, name='index'),
    path('students/', views.students, name='students')
    # path("<int:user_id>", views.borrower_page, name="borrower_page")
]
