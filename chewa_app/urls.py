from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('profile', views.profile, name='profile'),
    path('language', views.language, name='language'),
    path('lesson', views.lesson, name='lesson'),
    path('ksl', views.KSL_page, name='ksl'),
    path('luo', views.luo_page, name='luo'),
    path('luo-begin', views.luo_beginning, name='luo-begin'),

    path('luo-begin-test/', views.luo_test1, name='luo-begin-test'),

    path('kikuyu', views.kikuyu_page, name='kikuyu'),
    path('ki-begin', views.kikuyu_beginning, name='ki-begin'),
    path('ki-begin-test', views.kikuyu_test1, name='ki-begin-test'),
    path('kiswahili', views.swahili_page, name='swahili'),
    path('swa-begin', views.swahili_beginning, name='swa-begin'),
    path('swa-begin-test', views.swahili_test1, name='swa-begin-test'),
    path('search', views.luo_test1, name='luo_test1'),
    path('api/lessons', views.LessonList.as_view()),
    path('api-token-auth/', obtain_auth_token),
    path('api/lesson/lesson-id/<int:pk>/',views.LessonDescription.as_view()),
    path('settings/', views.settings, name='settings'),
    path('settings/password/', views.password, name='password'),
    path('signup/', views.sign_up, name='sign_up'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
