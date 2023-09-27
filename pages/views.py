from django.shortcuts import render
from django.views.generic import TemplateView, FormView, ListView
from .forms import Mylisting_form, Contactform, login_form, Signup_form
from .models import  Listings
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect

class CustomLoginRequiredMixin(LoginRequiredMixin):
    login_url = reverse_lazy('login')  # Replace 'login' with the name of your login view

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


# Create your views here.
class HomeTemplate(ListView):
    template_name = 'homepage.html'
    model = Listings
    context_object_name = 'allpost'
class CategoryTemplate(TemplateView):
    template_name = 'category.html'
class ContactTemplate(FormView):
    template_name = 'contact.html'
    form_class = Contactform
    success_url = '/listing/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
class AppartementsTemplate(ListView):
    template_name = 'Appartements.html'
    model = Listings
    context_object_name = 'appartements_listings'
    def get_queryset(self):
        return self.model.objects.filter(listing_type='Appartements')
class CarTemplate(ListView):
    template_name = 'car.html'
    model = Listings
    context_object_name = 'car_listings'
    def get_queryset(self):
        return self.model.objects.filter(listing_type='Car')
class ListingTemplate(ListView):
    template_name = 'listing.html'
    model = Listings
    context_object_name = 'appartements_listings'

    def get_queryset(self):
        return self.model.objects.filter(listing_type='Appartements')
class FoodAndLife(ListView):
    template_name = 'foodandlife.html'
    model = Listings
    context_object_name = 'food_and_life_listings'
    def get_queryset(self):
        return self.model.objects.filter(listing_type='Food and Life')
class ShoppingTemplate(ListView):
    template_name = 'Shopping.html'
    model  = Listings
    context_object_name = 'shopping_listings'
    def get_queryset(self):
        return self.model.objects.filter(listing_type='Shopping')
class TravellingTemplate(ListView):
    template_name = 'travelling.html'
    model = Listings
    context_object_name = 'travelling_listings'
    def get_queryset(self):
        return self.model.objects.filter(listing_type='Travelling')



class SignupTemplate(FormView):
    template_name = 'sihnup.html'
    form_class = Signup_form
    success_url = '/listing/'

    def form_valid(self, form):
        user = form.save()
        group = Group.objects.get(name='Editor')
        user.groups.add(group)
        messages.add_message(self.request, messages.SUCCESS, "Congrats")
        return super().form_valid(form)



class LoginTemplate(FormView):
    template_name = 'login-1.html'
    form_class = login_form
    success_url = '/contact/'

    def form_valid(self, form):
        uname = form.cleaned_data['username']
        upass = form.cleaned_data['password']
        user = authenticate(username=uname, password=upass)
        if user is not None:
            login(self.request, user)
            messages.add_message(self.request, messages.SUCCESS, "Successfully Logged In!")
            return super().form_valid(form)
        return self.form_invalid(form)
class MyListings(CustomLoginRequiredMixin, FormView):
    template_name = 'addlistings.html'
    form_class = Mylisting_form
    success_url = '/contact/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
class SearchView(ListView):
    template_name = 'search.html'
    model = Listings
    context_object_name = 'allpost'

    def get_queryset(self):
        query = self.request.GET.get('q')
        address = self.request.GET.get('address')
        price_range = self.request.GET.get('price')

        queryset = self.model.objects.all()

        if query:
            queryset = queryset.filter(Q(area__icontains=query))

        if address:
            queryset = queryset.filter(Q(location__icontains=address))

        if price_range:
            if price_range == "1000+":
                queryset = queryset.filter(Q(price__gte=1000))
            else:
                min_price, max_price = price_range.split('-')
                queryset = queryset.filter(Q(price__gte=min_price) & Q(price__lte=max_price))

        return queryset


class FoodsAndLife(ListView):
    template_name = 'foodandlife1.html'
    model = Listings
    context_object_name = 'food_and_life_listings'

    def get_queryset(self):
        return self.model.objects.filter(listing_type='Food and Life')


class CarListing(ListView):
    template_name = 'car1.html'
    model = Listings
    context_object_name = 'car_listings'

    def get_queryset(self):
        return self.model.objects.filter(listing_type='Car')


class TravellingListing(ListView):
    template_name = 'travelling1.html'
    model = Listings
    context_object_name = 'travelling_listings'

    def get_queryset(self):
        return self.model.objects.filter(listing_type='Travelling')


class AppartementsListing(ListView):
    template_name = 'Appartements1.html'
    model = Listings
    context_object_name = 'appartements_listings'

    def get_queryset(self):
        return self.model.objects.filter(listing_type='Appartements')


class ShoppingListing(ListView):
    template_name = 'Shopping1.html'
    model = Listings
    context_object_name = 'shopping_listings'

    def get_queryset(self):
        return self.model.objects.filter(listing_type='Shopping')


class PrivacyPolicy(TemplateView):
    template_name = 'privacyandpolicy.html'

class TermsAndConditions(TemplateView):
    template_name = 'TermsandConditions.html'


class ChangePass(FormView):
    template_name = 'changepasss.html'
    form_class = PasswordChangeForm
    success_url = '/'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class Logout(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')
