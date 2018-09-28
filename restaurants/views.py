from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import City, Restaurant, Eating, Eating_details, Comment_restaurant
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from tourer.models import Tourer
from datetime import datetime
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import generic
from book.models import Book_Tour,Place_tour

# Create your views here.


def index(request):
    restaurant = Restaurant.objects.select_related('location').order_by('-id')
    idempresa = ''
    if 'account' in request.session:
        idempresa = request.session['account']
    else:
        idempresa = None

    page = request.GET.get('page', 1)

    paginator = Paginator(restaurant, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    context = {
        'idempresa': idempresa,
        'place': users
    }
    return render(request, 'home/restaurants/restaurant.html', context)



def eating(request, id):
    restaurant = Restaurant.objects.get(pk=id)
    restaurant.review = restaurant.review + 1
    restaurant.save()
    # account
    idempresa = ''
    if 'account' in request.session:
        idempresa = request.session['account']
    else:
        idempresa = None

    tourer = Tourer.objects.filter(email=idempresa)
    eatings = Eating.objects.filter(restaurant=id)
    sum_commnet = Comment_restaurant.objects.filter(restaurant=id).count()
    comment = Comment_restaurant.objects.filter(
        restaurant=id).order_by('-date')
    # context
    context = {
        'idempresa': idempresa,
        'tourer': tourer,
        'eatings': eatings,
        'sum_commnet': sum_commnet,
        'comment': comment,
        'restaurant':restaurant,
        'id_res':id,
    }
    return render(request, 'home/restaurants/restaurant_details.html', context)

def create_comment_eating(request,id):
    restaurant_details = Restaurant.objects.get(pk=id)
    # email = request.GET['email']
    commnet_items = request.GET['comment_items']
    idempresa= ''
    if 'account' in request.session:
        idempresa = request.session['account']
    else:
        idempresa=None

    
    if idempresa == None:
        return redirect('login')
    else:
        try:
            account_details = Tourer.objects.get(email=idempresa)
            comment_place = Comment_restaurant(restaurant=restaurant_details,commnet=commnet_items,date=datetime.now(),account=account_details)
            comment_place.save()
            return redirect('eating',id=id)
        except Exception as e:
            print(e)
            return redirect('eating',id=id)

def eating_details(request, id, id_restaurant):
    # account
    idempresa = ''
    if 'account' in request.session:
        idempresa = request.session['account']
    else:
        idempresa = None

    eating_items = Eating_details.objects.filter(eating=id_restaurant)
    # context
    context = {
        'idempresa': idempresa,
        'eating_items':eating_items,
    }
    return render(request, 'home/restaurants/food_details.html',context)

# city
class IndexView_Restaurants_City(generic.ListView):
    template_name = "dashboard/restaurants/city/table.html"
    context_object_name = 'city'
    paginate_by = 12
    def get_queryset(self):
        return City.objects.all()

    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(IndexView_Restaurants_City, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(IndexView_Restaurants_City, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class CreateRestaurants_City(CreateView):
    template_name = 'dashboard/restaurants/city/form.html'
    model = City
    fields = '__all__'
    #urls name
    def form_valid(self, form):
        # Instead of return this HttpResponseRedirect, return an 
        #  new rendered page
        return super(CreatePlace_City, self).form_valid(form)

    
    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(CreateRestaurants_City, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(CreateRestaurants_City, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class UpdateRestaurants_City(UpdateView):
    template_name = 'dashboard/restaurants/city/form.html'
    model = City
    fields = '__all__'
    #urls name
    def form_valid(self, form):
        # Instead of return this HttpResponseRedirect, return an 
        #  new rendered page
        return super(UpdateRestaurants_City, self).form_valid(form)

    
    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(UpdateRestaurants_City, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(UpdateRestaurants_City, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class RestaurantsDelete_City(DeleteView):
    model = City
    success_url = reverse_lazy('IndexView_Restaurants_City')

# restaurants
class IndexView_Restaurants(generic.ListView):
    template_name = "dashboard/restaurants/restaurants/table.html"
    context_object_name = 'context'
    paginate_by = 12
    def get_queryset(self):
        return Restaurant.objects.all().order_by("-id")

    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(IndexView_Restaurants, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(IndexView_Restaurants, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class CreateRestaurant(CreateView):
    template_name = 'dashboard/restaurants/restaurants/form.html'
    model = Restaurant
    fields = '__all__'
    #urls name
    def form_valid(self, form):
        # Instead of return this HttpResponseRedirect, return an 
        #  new rendered page
        return super(CreateRestaurant, self).form_valid(form)

    
    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(CreateRestaurant, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(CreateRestaurant, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class UpdateRestaurant(UpdateView):
    template_name = 'dashboard/restaurants/restaurants/form.html'
    model = Restaurant
    fields = '__all__'
    #urls name
    def form_valid(self, form):
        # Instead of return this HttpResponseRedirect, return an 
        #  new rendered page
        return super(UpdateRestaurant, self).form_valid(form)

    
    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(UpdateRestaurant, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(UpdateRestaurant, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class RestaurantDelete(DeleteView):
    model = Restaurant
    success_url = reverse_lazy('IndexView_Restaurants')

# eating
class IndexView_Eating(generic.ListView):
    template_name = "dashboard/restaurants/eating/table.html"
    context_object_name = 'context'
    paginate_by = 12
    def get_queryset(self):
        return Eating.objects.all().order_by("-id")

    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(IndexView_Eating, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(IndexView_Eating, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class CreateEating(CreateView):
    template_name = 'dashboard/restaurants/eating/form.html'
    model = Eating
    fields = '__all__'
    #urls name
    def form_valid(self, form):
        # Instead of return this HttpResponseRedirect, return an 
        #  new rendered page
        return super(CreateEating, self).form_valid(form)

    
    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(CreateEating, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(CreateEating, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class UpdateEating(UpdateView):
    template_name = 'dashboard/restaurants/eating/form.html'
    model = Eating
    fields = '__all__'
    #urls name
    def form_valid(self, form):
        # Instead of return this HttpResponseRedirect, return an 
        #  new rendered page
        return super(UpdateEating, self).form_valid(form)

    
    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(UpdateEating, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(UpdateEating, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class EatingDelete(DeleteView):
    model = Eating
    success_url = reverse_lazy('IndexView_Eating')
    
# eating_details
class IndexView_Eating_details(generic.ListView):
    template_name = "dashboard/restaurants/eating_details/table.html"
    context_object_name = 'context'
    paginate_by = 12
    def get_queryset(self):
        return Eating_details.objects.all().order_by("-id")

    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(IndexView_Eating_details, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(IndexView_Eating_details, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class CreateEating_details(CreateView):
    template_name = 'dashboard/restaurants/eating_details/form.html'
    model = Eating_details
    fields = '__all__'
    #urls name
    def form_valid(self, form):
        # Instead of return this HttpResponseRedirect, return an 
        #  new rendered page
        return super(CreateEating_details, self).form_valid(form)

    
    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(CreateEating_details, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(CreateEating_details, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class UpdateEating_details(UpdateView):
    template_name = 'dashboard/restaurants/eating_details/form.html'
    model = Eating_details
    fields = '__all__'
    #urls name
    def form_valid(self, form):
        # Instead of return this HttpResponseRedirect, return an 
        #  new rendered page
        return super(UpdateEating_details, self).form_valid(form)

    
    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(UpdateEating_details, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(UpdateEating_details, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class Eating_detailsDelete(DeleteView):
    model = Eating
    success_url = reverse_lazy('IndexView_Eating_details')