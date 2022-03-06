from django.urls import path 
from . import views

urlpatterns = [
    path('translate/', views.translator_view, name = 'translating'),
    path('grammar_check/', views.grammar_corr, name = 'grammar_correction'),
    path('', views.about_view, name = 'about view' )
]