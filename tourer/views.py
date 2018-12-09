from django.shortcuts import render,HttpResponse,get_object_or_404, redirect,HttpResponseRedirect
from .models import Tourer, Account
from django.views.generic.edit import CreateView
from passlib.hash import sha256_crypt
from django.core.files.storage import FileSystemStorage
from datetime import datetime
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import generic
from django.contrib import messages
from .forms import AccountForm
from bootstrap_modal_forms.mixins import PassRequestMixin, DeleteAjaxMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView
# from .forms import Tourer_form
# Create your views here.
def login(request):
    next_page = request.GET['next']
    context = {
        'next':next_page
    }
    return render(request,'login/login.html',context)

def logout(request):  
    try:
        request.session.pop('account')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
    except Exception as e:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
        

def login_form(request):
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        login = 0
        email_login = ''
        password_email = ''
        error = ''
        try:
            email_login = Account.objects.get(email=email)
            login = 1
        except Exception as e:
            login = 0

        if login == 1:
            if sha256_crypt.verify(password,email_login.password) == True:
                try:
                    request.session['account'] = email_login.email
                    return redirect(request.POST['next'])
                except Exception as e:         
                    return redirect('home')
            else:
                error = 'Sai Mật Khẩu'
                messages.error(request, 'Password wrong.')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
        else:
            messages.error(request, 'Account Wrong.')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

class Register(CreateView):
    template_name = 'login/register.html'
    model = Tourer
    fields = '__all__'

    
    #urls name
    def form_valid(self, form):
        # Instead of return this HttpResponseRedirect, return an 
        #  new rendered page
       
        return  super(Register, self).form_valid(form)
        # return logout(self.request)

def register_main(request):
    return render(request,'login/register.html')

def form_signup(request):
    email = request.POST['email']
    name = request.POST['name']
    password  = request.POST['password']
    if request.method == 'POST' :
        try:
            tourer = Account.objects.filter(email=email)
            if tourer.count() < 1:
                tourer = Account.objects.create(email=email,name=name,password=sha256_crypt.encrypt(password),question='Null',author='account')
                messages.success(request, 'Singnup successs.' + email)
                return render(request,'login/login.html')
            else:
                messages.error(request, 'Email already exists .' + email)
                return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
        except Exception as e:
            messages.error(request, 'Email already exists.' + email)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
    else:
        context = {
             'message' : 'message'
        }
        return render(request,'login/register.html',context)

def error(request):
    return render(request,'error/error.html')

# Create your views here.
class ListAccount(generic.ListView):
    template_name = "dashboard/account/index.html"
    context_object_name = 'context'
    paginate_by = 12
    def get_queryset(self):
        return Account.objects.all().order_by("-id")

    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(ListAccount, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(ListAccount, self).get_context_data(**kwargs)
            tourer = Account.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class AddAccount(PassRequestMixin, SuccessMessageMixin,
                     generic.CreateView):
    template_name = 'dashboard/account/_create.html'
    form_class = AccountForm
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('ListAccount')
   

class UpdateAccount(PassRequestMixin, SuccessMessageMixin,
                     generic.UpdateView):
    model = Account
    template_name = 'dashboard/account/_update.html'
    form_class = AccountForm
    success_message = 'Success: Book was updated.'
    success_url = reverse_lazy('ListAccount')
   

class DeleteAccount(DeleteAjaxMixin, generic.DeleteView):
    model = Account
    template_name = 'dashboard/account/_delete.html'
    success_message = 'Success: Place was deleted.'
    success_url = reverse_lazy('ListAccount')

# # Read
class AccountReadView(generic.DetailView):
    model = Account
    template_name = 'dashboard/account/_read.html'
