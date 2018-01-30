from django.conf.urls import url
from .views import Post_list,  Update_signature, Create_signature, Delete_signature, Alert
from django.contrib.auth import views as auth_views

app_name = 'main'

urlpatterns = [
    # Главная страница
    url(r'^$', Alert.as_view(), name='index'),
    # Страница авторизации
    url(r'^login/$', auth_views.login, {'template_name': 'main/login.html'}, name='login'),
    # Страница выхода
    url(r'^logout/$', auth_views.logout, name='logout'),
    # Страница со списокм всех сигнатур
    url(r'^signature/$', Post_list.as_view(), name='all_signature'),
    # Страница добавления сгинатуры
    url(r'^signature/new/$', Create_signature.as_view(), name='signature'),
    # Страница редактирования сигнатуры
    url(r'^signature/update/(?P<pk>[0-9]+)/$',  Update_signature.as_view(), name='update'),
    # Страница удаления сигнатуры
    url(r'^signature/delete/(?P<pk>[0-9]+)/$',  Delete_signature.as_view(), name='delete'),
]