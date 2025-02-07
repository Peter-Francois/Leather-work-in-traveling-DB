from django.urls import path
from . import views

app_name = 'boutique'

urlpatterns = [
    path('', views.index, name="index"),
    path('tous-les-produits/macrames/', views.macrames, name="macrames"),
    path('tous-les-produits/maroquinerie/', views.maroquinerie, name="maroquinerie"),
    path('creation-sur-mesure/', views.creation_sur_mesure, name="creation-sur-mesure"),
    path('tous-les-produits/autres-produits/', views.autres_produits, name="autres-produits"),
    path('contact/', views.contact, name="contact"),
    path('tous-les-produits/', views.tous_les_produits, name="tous-les-produits"),
    path('panier/', views.panier, name="panier"),
    path('a-propos/', views.a_propos, name="a-propos"),
]