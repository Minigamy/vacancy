
from django.contrib import admin
from django.urls import path
from appvacancy import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<int:id>/', views.main_view),
    path('vacancy/<int:idd>/', views.vacancy_view),
]
