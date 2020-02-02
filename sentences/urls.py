from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from sentences import views

urlpatterns = [
    path('', views.sentence_maker),
    path('english/<word>/', views.english, name='english'),
    path('espanol/<palabra>/', views.espanol, name='español'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
