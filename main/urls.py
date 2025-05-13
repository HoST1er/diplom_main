from django.urls import path
from . import views
from .views import RegisterView

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile_view'),
    path('home', views.home, name='home'),
    path('start', views.start_page, name='start_page'),
    path("upload/", views.parse_excel_files, name="parse_excel_files"),
    path("upload_competencies/", views.parse_competencies, name="parse_competencies"),
    path("upload_excel/", views.upload_excel, name="upload_excel"),
    path('excel-popup/', views.excel_popup, name='excel_popup'),
    path('excel-popup1/', views.excel_popup1, name='excel_popup1'),
    path('get_suggestions/', views.get_suggestions, name='get_suggestions'),
    path('save_user_data/', views.save_user_data, name='save_user_data'),
    path('save_user_data1/', views.save_user_data1, name='save_user_data1'),
    path('save_user_data2/', views.save_user_data2, name='save_user_data2'),
    path('save_user_data3/', views.save_user_data3, name='save_user_data3'),
    path('save_user_data4/', views.save_user_data4, name='save_user_data4'),
    path('save_user_data5/', views.save_user_data5, name='save_user_data5'),
    path('save_user_data6/', views.save_user_data6, name='save_user_data6'),
    path('save_user_data7/', views.save_user_data7, name='save_user_data7'),
    path('save_user_data8/', views.save_user_data8, name='save_user_data8'),
    path('competencies/', views.competencies, name='competencies'),
    path('content_of_discipline/', views.content_of_discipline, name='content_of_discipline'),
    path('curriculum/', views.curriculum, name='curriculum'),
    path('content_of_seminars/', views.content_of_seminars, name='content_of_seminars'),
    path('list_of_questions/', views.list_of_questions, name='list_of_questions'),
    path('questions_to_work/', views.questions_to_work, name='questions_to_work'),
    path('example_tasks/', views.example_tasks, name='example_tasks'),
    path('example_quest_to_test/', views.example_quest_to_test, name='example_quest_to_test'),
    path('export-word/', views.export_to_word, name='export_to_word')

]