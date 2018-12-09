from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import generic
from .models import Tour,PlaceTour,BookTour
from tourer.models import Tourer,Account
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Sum,Count
from django.db.models import F
from datetime import datetime
from django.contrib import messages
from .forms import TourForm, PlaceTourForm
from bootstrap_modal_forms.mixins import PassRequestMixin, DeleteAjaxMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView

# Create your views here.
class ListTour(generic.ListView):
    template_name = "dashboard/tour/tour/index.html"
    context_object_name = 'context'
    paginate_by = 12
    def get_queryset(self):
        return Tour.objects.all().order_by("-id")

    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(ListTour, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(ListTour, self).get_context_data(**kwargs)
            tourer = Account.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class AddTour(PassRequestMixin, SuccessMessageMixin,
                     generic.CreateView):
    template_name = 'dashboard/tour/tour/_create.html'
    form_class = TourForm
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('ListTour')
   

class UpdateTour(PassRequestMixin, SuccessMessageMixin,
                     generic.UpdateView):
    model = Tour
    template_name = 'dashboard/tour/tour/_update.html'
    form_class = TourForm
    success_message = 'Success: Book was updated.'
    success_url = reverse_lazy('ListTour')
   

class DeleteTour(DeleteAjaxMixin, generic.DeleteView):
    model = Tour
    template_name = 'dashboard/tour/tour/_delete.html'
    success_message = 'Success: Place was deleted.'
    success_url = reverse_lazy('ListTour')

# Read
class TourReadView(generic.DetailView):
    model = Tour
    template_name = 'dashboard/tour/tour/_read.html'


# List Tour

class ListPlaceTour(generic.ListView):
    template_name = "dashboard/tour/place_tour/index.html"
    context_object_name = 'context'
    paginate_by = 12
    def get_queryset(self):
        return PlaceTour.objects.all().order_by("-id")

    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(ListPlaceTour, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(ListPlaceTour, self).get_context_data(**kwargs)
            tourer = Account.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class AddPlaceTour(PassRequestMixin, SuccessMessageMixin,
                     generic.CreateView):
    template_name = 'dashboard/tour/place_tour/_create.html'
    form_class = PlaceTourForm
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('ListPlaceTour')

class UpdatePlaceTour(PassRequestMixin, SuccessMessageMixin,
                     generic.UpdateView):
    model = PlaceTour
    template_name = 'dashboard/tour/place_tour/_update.html'
    form_class = PlaceTourForm
    success_message = 'Success: Book was updated.'
    success_url = reverse_lazy('ListPlaceTour')

class DeletePlaceTour(DeleteAjaxMixin, generic.DeleteView):
    model = PlaceTour
    template_name = 'dashboard/tour/place_tour/_delete.html'
    success_message = 'Success: Place was deleted.'
    success_url = reverse_lazy('ListPlaceTour')

# Read
class PlaceTourReadView(generic.DetailView):
    model = PlaceTour
    template_name = 'dashboard/tour/place_tour/_read.html'



from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()
# filter
@register.filter
def in_place(tour):
    return PlaceTour.objects.filter(tour=tour).aggregate(Sum('price'))


# list tour
def list_tour(request):
    tour = Tour.objects.annotate(sum_price = Sum(F('person'))).order_by('-id')
    query = "SELECT *,(sum(a.price) * t.person) as sum_price, sum(a.price) as total_price FROM tour_placeTour a inner join tour_tour t on a.tour_id  = t.id group by t.id "
    place = PlaceTour.objects.raw(query)
    query_item_1 = "SELECT *,(sum(a.price) * t.person) as sum_price, sum(a.price) as total_price FROM tour_placeTour a inner join tour_tour t on a.tour_id  = t.id group by t.id order by a.id limit 5"
    place_tour = PlaceTour.objects.raw(query_item_1)
    tour_city = Tour.objects.raw("SELECT  city,id from tour_tour group by city")
    idempresa= ''
    if 'account' in request.session:
        idempresa = request.session['account']
    else:
        idempresa=None
        
    page = request.GET.get('page', 1)

    paginator = Paginator(place, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    context = { 
        'idempresa':idempresa,
        'context':users,
        'tour_city':tour_city,
        'place_tour':place_tour
    }
    return render(request,'home/tour/tour.html',context)

def add_tour(request,id):
    if request.method == "POST":
        tour = Tour.objects.get(pk=id)
        date = request.POST['date']
        person_book = request.POST['person_book']
        phone = request.POST['phone']
        email = request.POST['email']
        idempresa= ''
        if 'account' in request.session:
            idempresa = request.session['account']
        else:
            idempresa=None
        if idempresa == None:
            messages.error(request, 'Please sign in to book.')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            try:
                isBook= BookTour.objects.filter(tour=tour.id)
                if isBook.count() > 0:
                    messages.error(request, 'Tour has been created')
                    return redirect(request.META.get('HTTP_REFERER')) 
                else:
                    account_details = Account.objects.get(email=idempresa)
                    booktour = BookTour(accout=account_details,date_book=datetime.now(),date_start=date,tour=tour,person_book=person_book,phone=phone,email=email)
                    booktour.save()
                    messages.success(request, 'Book to success')
                    return redirect(request.META.get('HTTP_REFERER'))
            except Exception as e:
                messages.error(request, 'Error Page')
                return redirect(request.META.get('HTTP_REFERER'))


def tour_details(request,id):
    tour = Tour.objects.get(id=id)
    placeTour = PlaceTour.objects.filter(tour=tour).order_by('id')
    query = "SELECT *,(sum(a.price) * t.person) as sum_price,sum(a.price) as total_price FROM tour_placeTour a inner join tour_tour t on a.tour_id  = t.id where a.tour_id = "+ str(id) + "  group by t.id "
    sum_place = PlaceTour.objects.raw(query)
    query_item_1 = "SELECT *,(sum(a.price) * t.person) as sum_price, sum(a.price) as total_price FROM tour_placeTour a inner join tour_tour t on a.tour_id  = t.id group by t.id order by a.id limit 5"
    place_tour = PlaceTour.objects.raw(query_item_1)
    tour_city = Tour.objects.raw("SELECT  city,id from tour_tour group by city")
    context = {
        'context':placeTour,
        'tour':tour,
        'sum_place':sum_place,
        'place_tour':place_tour,
        'tour_city':tour_city
    }
    return render(request,'home/tour/tour_details.html',context)

def search_form(request):
    if request.method == "POST": 
        name = request.POST['city']
        if name == "all":
            return redirect('/tour')
        else :
            return redirect('/tour/search/'+name)

def search_tour_place(request,name):
    query = "SELECT *,(sum(a.price) * t.person) as sum_price, sum(a.price) as total_price FROM tour_placeTour a inner join tour_tour t on a.tour_id  = t.id  where city = '" + name + "'" + " group by t.id"
    place = PlaceTour.objects.raw(query)
    city = Tour.objects.values('city').distinct()
    tour_city = Tour.objects.raw("SELECT  city,id from tour_tour group by city")
    query_item_1 = "SELECT *,(sum(a.price) * t.person) as sum_price, sum(a.price) as total_price FROM tour_placeTour a inner join tour_tour t on a.tour_id  = t.id group by t.id order by a.id limit 5"
    place_tour = PlaceTour.objects.raw(query_item_1)
    idempresa= ''
    if 'account' in request.session:
        idempresa = request.session['account']
    else:
        idempresa=None
        
    page = request.GET.get('page', 1)

    paginator = Paginator(place, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    context = { 
        'idempresa':idempresa,
        'context':users,
        'tour_city':tour_city,
        'place_tour':place_tour

    }
    return render(request,'home/tour/tour.html',context)

def query_mutil(city,price,person,date):
    query = ("SELECT *,(sum(a.price) * t.person) as sum_price, sum(a.price) as total_price"
    " FROM tour_placeTour a inner join " 
    " tour_tour t on a.tour_id  = t.id "
    " where t.city LIKE '%" + city + "%'  and t.person LIKE '%" + person + "%' "  
    " group by t.id "
    " having (sum(a.price) * t.person) <= " + price + ""
    )
    if price == "":
        query = ("SELECT *,(sum(a.price) * t.person) as sum_price, sum(a.price) as total_price"
        " FROM tour_placeTour a inner join " 
        " tour_tour t on a.tour_id  = t.id "
        " where t.city LIKE '%" + city + "%'  and t.person LIKE '%" + person + "%' "  
        " AND t.date_tour LIKE '%" + date +"%'"
        " group by t.id "
        " having (sum(a.price) * t.person) <= " + price + ""
        )
    else:
        query = ("SELECT *,(sum(a.price) * t.person) as sum_price, sum(a.price) as total_price"
        " FROM tour_placeTour a inner join " 
        " tour_tour t on a.tour_id  = t.id "
        " where t.city LIKE '%" + city + "%'  and t.person LIKE '%" + person + "%' "  
        " group by t.id "
        )
    return query

def search_tour_place_price(request,city,price,person,date):
    place = PlaceTour.objects.raw(query_mutil(city,price,person,date))
    city = Tour.objects.values('city').distinct()
    tour_city = Tour.objects.raw("SELECT  city,id from tour_tour group by city")
    idempresa= ''
    if 'account' in request.session:
        idempresa = request.session['account']
    else:
        idempresa=None
        
    page = request.GET.get('page', 1)

    paginator = Paginator(place, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    context = { 
        'idempresa':idempresa,
        'context':users,
        'tour_city':tour_city

    }
    return render(request,'home/tour/tour.html',context)