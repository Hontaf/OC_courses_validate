"""merchex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/',views.hello),
    path('about-us/',views.about,name="about"),
    path('listings/',views.listings),
    path('contact-us/',views.contact,name='contact'),
    path('bands/',views.band_list,name='band-list'),
    #chaue chemin se termine par un slash / c'est une convention django
    path('bands/<int:id>/', views.band_detail, name='band-detail'), # ajouter ce motif sous notre autre motif de groupes
    path('listing/',views.listing_list,name='listing-list'),
    path('listing/<int:id>/',views.listing_detail,name='listing-detail'),
    path('listing/confemail/',views.email_sent,name="email_sent"),
    path('bands/add/',views.bands_create , name = 'bands_create'),
    path('listing/add/',views.listings_create,name= 'listing_create'),
    path('bands/<int:id>/change/',views.bands_change,name = 'band-change'),
    path('listing/<int:id>/change/',views.listings_change,name='listing-change'),
    path('bands/<int:id>/delete/',views.band_delete,name='band-delete'),
    path('listing/<int:id>/delete/',views.listing_delete,name='listing-delete')
    
]
