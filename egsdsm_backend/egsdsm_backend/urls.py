"""egsdsm_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from server import views as v_server
from communication import views as v_communication
from statistics import views as v_statistics

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/$', v_server.AuthView.as_view()),
    url(r'^auth/check$', v_server.AmIAuthorized.as_view()),
    url(r'^chat/get/$', v_communication.ChatMessagesView.as_view()),
    url(r'^chat/send/$', v_communication.SendChatMessage.as_view()),
    url(r'^restart/$', v_server.RestartView.as_view()),
    url(r'^heartbeat/$', v_statistics.HeartBeatView.as_view()),
    url(r'^corelog/$', v_server.CoreLogView.as_view()),
    url(r'^terminal/get/$', v_server.TerminalGetView.as_view()),
    url(r'^terminal/send/$', v_server.TerminalSendView.as_view()),
    url(r'^players/get/$', v_communication.PlayerInfo.as_view())

]
