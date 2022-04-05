from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.index, name="homepage"),
    path('howto/', views.howto, name="howto"),
    path('rankgeneral/', views.rankgeneral, name="rankgeneral"),
    path('privacy/', views.privacy, name="privacy"),
    path('results/', views.results, name="results"),
    path('form/', views.form, name="form"),
    path(r'form', views.party_form, name='form'),
    path("results/", views.PartyList.as_view(), name="search")
    ]