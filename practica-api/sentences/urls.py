from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from sentences import views

urlpatterns = [
    path('', views.sentence_generator),
    path('english/<word>/', views.english, name='sentences'),
    path('espanol/<palabra>/', views.espanol, name='sentences'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
