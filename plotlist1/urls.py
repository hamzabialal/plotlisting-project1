"""plotlist1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from pages import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeTemplate.as_view(), name='homepage'),
    path('category/', views.CategoryTemplate.as_view(), name='category'),
    path('contact/', views.ContactTemplate.as_view(), name='contact'),
    path('listing/', views.ListingTemplate.as_view(), name='listing'),
    path('signup/', views.SignupTemplate.as_view(), name='signup'),
    path('login/', views.LoginTemplate.as_view(), name='login'),
    path('mylistings/', views.MyListings.as_view(), name='mylisting'),
    path('Search/', views.SearchView.as_view(), name= 'Search'),
    path('appartements/', views.AppartementsTemplate.as_view(), name='appartements'),
    path('foodandlife/', views.FoodAndLife.as_view(), name= 'foodandlife'),
    path('car/', views.CarTemplate.as_view(), name= 'car'),
    path('shopping/', views.ShoppingTemplate.as_view(), name= 'shopping'),
    path('travelling/', views.TravellingTemplate.as_view(), name= 'travelling'),
    path('foodandlifelisting/', views.FoodsAndLife.as_view(), name='foodandlifelisting'),
    path('carlisting/', views.CarListing.as_view(), name='carlisting'),
    path('travellinglisting/', views.TravellingListing.as_view(), name='travellinglisting'),
    path('appartementslisting/', views.AppartementsListing.as_view(), name='appartementslisting'),
    path('shoppinglisting/', views.ShoppingListing.as_view(), name='shoppinglisting'),
    path('privacypolicy', views.PrivacyPolicy.as_view(), name='privacypolicy'),
    path('termsandconditions', views.TermsAndConditions.as_view(), name='termsandconditions'),
    path('changepass/', views.ChangePass.as_view(), name='Changepassword'),
    path('logout/', views.Logout.as_view(), name='logout'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
