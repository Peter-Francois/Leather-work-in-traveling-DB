from django.urls import path
from . import views
from page_vente.views import rendre_indisponible, rendre_disponible, get_product_details, add_to_cart, cart_detail, vider_panier, remove_from_cart

app_name = 'boutique'

urlpatterns = [
    path('', views.index, name="index"),
    path('tous-les-produits/macrames/', views.macrames, name="macrames"),
    path('tous-les-produits/maroquinerie/', views.maroquinerie, name="maroquinerie"),
    path('creation-sur-mesure/', views.creation_sur_mesure, name="creation-sur-mesure"),
    path('tous-les-produits/hybride/', views.hybride, name="hybride"),
    path('contact/', views.contact, name="contact"),
    path('tous-les-produits/', views.tous_les_produits, name="tous-les-produits"),
    path('panier/', views.panier, name="panier"),
    path('a-propos/', views.a_propos, name="a-propos"),
    path('rendre_indisponible/<int:product_id>/', rendre_indisponible, name='rendre_indisponible'),
    path('rendre_disponible/<int:product_id>/', rendre_disponible, name='rendre_disponible'),
    path('get_product_details/<int:article_id>/', get_product_details, name='get_product_details'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart_detail/', cart_detail, name='cart_detail'),
    path('vider_panier/', vider_panier, name='vider_panier'),
    path('remove_from_cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
]