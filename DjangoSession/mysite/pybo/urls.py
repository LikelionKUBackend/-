from django.urls import path

from . import views

#하나의 프로젝트 내에 여러 개의 앱이 추가될 수 있으므로, app_name으로 이름공간을 지정
app_name = 'pybo'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:question_id>/', views.detail, name= 'detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/form', views.question_form, name = 'question_form'),
    path('question/create', views.question_create, name = 'question_create'),
    path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'),
    path('question/star/<int:question_id>/', views.question_stars, name='question_stars'),
    path('apitest', views.QuestionListAPI),
    path('api/question/create', views.create_question_by_api),
]