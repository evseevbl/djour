from django.urls import path

import api.views as views


urlpatterns = [
    path('marks/add', views.add_mark, name='marks_add'),
    path('lessons/add', views.add_lesson, name='lessons_add'),
    path('attendance/add', views.add_attendance, name='attendance_add'),
    path('attendance/set', views.set_attendance, name='attendance_set'),

    # path("<int:user_id>", views.borrower_page, name="borrower_page")
]
