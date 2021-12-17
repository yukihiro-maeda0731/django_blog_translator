from django.urls.resolvers import URLPattern
from . import views
from django.urls import path

urlpatterns = [
    # translator_viewはviews.pyに記述
    path('', views.translator_view, name='translator_view')
]