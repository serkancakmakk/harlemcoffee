import random
import string
from django.shortcuts import get_object_or_404, redirect, render

from .models import Category, Company, Gallery, Message, Product

from .forms import CategoryForm, CompanyForm, GalleryForm, LoginForm, MessageForm, ProductForm

# Create your views here.
def index(request):
    if 'lang_code' not in request.session or request.session['lang_code'] != 'tr':
        request.session['lang_code'] = 'tr'
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {
        'products':products,
        'categories':categories,
    }
    return render(request,'index.html',context)
def create_company(request):
    if not request.user.is_authenticated:
        return redirect('index')
    company = Company.objects.first()
    company_instance, created = Company.objects.get_or_create(pk=1)  # Tek bir kayıt al veya oluştur

    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company_instance)
        if form.is_valid():
            form.save()
            return redirect('success')  # Başarı durumunda yönlendirilecek sayfa
    else:
        
        form = CompanyForm(instance=company_instance)
        context ={
            'form':form,
            'company':company,
        }

    return render(request, 'company.html',context)
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
@login_required
@csrf_protect
def create_category(request):
    categories = Category.objects.all()
    timezone.localtime(timezone.now())
    print(timezone.localtime(timezone.now()))
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.save(commit=False)
            category.created_by = request.user.username
            category.created_time = timezone.localtime(timezone.now()).replace(second=0, microsecond=0)
            # Görsel dosya türü doğrulaması yapın
            image = form.cleaned_data['image']
            if not image.content_type.startswith('image/'):
                form.add_error('image', 'Sadece resim dosyaları kabul edilir.')
                return render(request, 'add_category.html', {'form': form, 'categories': categories})
            category.save()
            return redirect('success')
    else:
        form = CategoryForm()
    
    return render(request, 'add_category.html', {'form': form, 'categories': categories})
def kategori(request, slug):
    # Görünüm kodları buraya eklenecek
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category = category)
    context = {
        'category':category,
        'products':products,
    }
    return render(request, 'category_detail.html',context)
from django.contrib import messages
def add_product(request):
    if not request.user.is_authenticated:
        return redirect('index')
    products = Product.objects.all()
    categories = Category.objects.all()
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            name = form.cleaned_data["name"]
            messages.success(request, f'Yeni ürün eklendi {name}')
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        form = ProductForm()
        print(form.errors)
    print(form.errors)
    context = {
        'form':form,
        'products':products,
        'categories':categories,
        }
    return render(request, 'add_product.html', context)
from itertools import groupby
from operator import itemgetter

def all_menu(request):

    categories = Category.objects.all()
    context = {
            'categories':categories,
        }
    return render(request, 'all_menu.html', context)
def contact(request):

    if request.method == "POST":
        form = MessageForm(request.POST,)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = MessageForm()
        print(form.errors)
    print(form.errors)
    context = {
        'form':form,
        }
    return render(request, 'contact.html', context)
def admin_messages(request):
    if not request.user.is_authenticated:
        return redirect('index')
    messages = Message.objects.filter(status=True).order_by('status')
    closed_messages = Message.objects.filter(status=False).order_by('date_joined')
    context = {
        'closed_messages':closed_messages,
        'messages':messages,
    }
    return render(request,'admin/messages.html',context)
def message_close(request,id):
    if not request.user.is_authenticated:
        return redirect('index')
    message = get_object_or_404(Message,id=id)
    if message.status == False:
        message.status = True
        message.save()
        return redirect(request.META['HTTP_REFERER'])
    if message.status == True:
        message.status = False
        message.save()
    return redirect(request.META['HTTP_REFERER'])
from django.contrib.auth.decorators import login_required

def add_gallery(request):
    if not request.user.is_authenticated:
        return redirect('index')  # Kullanıcı giriş yapmamışsa anasayfaya yönlendir
    form = GalleryForm()
    if request.method == "POST":
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    context = {
        'form': form,
    }
    return render(request, 'admin/add_gallery.html', context)
def gallery(request):
    gallery = Gallery.objects.all()
    context = {
        'gallery':gallery,
    }
    return render(request,'gallery.html',context)
def contact(request):
    return render(request,'contact.html')
def hakkimizda(request):
    if request.session['lang_code'] != 'tr':
        request.session['lang_code'] = 'tr'
    company = Company.objects.first()
    context = {
        'company':company,
    }
    return render(request,'about_us.html',context)
def about_us(request):
    company = Company.objects.first()
    context = {
        'company':company,
    }
    return render(request,'about_us.html',context)
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.utils.crypto import get_random_string

# Kullanıcı e-posta adresine göre doğrulama kodlarını saklayacak sözlük

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Kullanıcı adı ve şifreyi kullanarak doğrulama yap
            user = authenticate(request, username=username, password=password)
            
            # Eğer kullanıcı adı ve şifre doğruysa ve e-posta adresi kayıtlıysa devam et
            if user is not None and User.objects.filter(email=email).exists():
                # Doğrulama kodu gönderme işlemi
                verification_code = generate_verification_code(email)  # Doğrulama kodunu oluştur
                send_verification_code(email, verification_code)  # Kullanıcıya doğrulama kodunu gönder

                return render(request, 'admin/verification.html', {'email': email})  # Doğrulama sayfasına e-posta bilgisini gönder
            else:
                error_message = 'Hatalı e-posta veya şifre.'
                return render(request, 'admin/admin_login.html', {'form': form, 'error': error_message})
    else:
        form = LoginForm()
    return render(request, 'admin/admin_login.html', {'form': form})
verification_codes = {}  # Kullanıcı e-posta adresine göre doğrulama kodlarını saklayacak sözlük

from datetime import datetime, timedelta

verification_codes = {}

def generate_verification_code(length=6):
    # Doğrulama kodunu oluştururken kullanılacak karakterler
    characters = string.ascii_letters + string.digits
    
    # Rasgele doğrulama kodunu oluşturur
    verification_code = ''.join(random.choices(characters, k=6))
    print(verification_code)

    return verification_code

def send_verification_code(email, verification_code):
    # E-posta adresinin kayıtlı olup olmadığını kontrol et
    if User.objects.filter(email=email).exists():
        # E-posta adresi kayıtlıysa doğrulama kodunu gönder
        verification_codes[email] = verification_code

        subject = 'Doğrulama Kodu'
        html_content = render_to_string('verification_email.html', {'verification_code': verification_code})
        text_content = strip_tags(html_content)  # HTML içeriğini düz metne dönüştür

        email_message = EmailMultiAlternatives(subject, text_content, 'sender@example.com', [email])
        email_message.attach_alternative(html_content, "text/html")
        email_message.send()
    else:
        # E-posta adresi kayıtlı değilse işlem yapma
        print(f"The email address {email} is not registered, verification code could not be sent.")

def verify_code(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        code = request.POST.get('verification_code')
        try:
            user = User.objects.get(email=email)
            # Doğrulama kodunu kontrol et
            if verification_codes.get(email) == code:
                del verification_codes[email]  # Kullanılan doğrulama kodunu sil
                # Kullanıcıyı yetkilendirme
                login(request, user)
                user.is_active = True
                
                user.save()
                request.session['lang_code'] ='tr'
                return redirect('company')  # Kullanıcı yetkilendirildikten sonra yönlendirme
            else:
                return render(request, 'admin/verification.html', {'error': 'Hatalı doğrulama kodu.'})
        except User.DoesNotExist:
            return redirect('harlemadminlogin')
    else:
        return redirect('admin_login')  # POST isteği dışında bu sayfaya erişmeyi engellemek için yönlendirme

def user_logout(request):
    logout(request)
    # Çıkış yaptıktan sonra yönlendirme yapabilirsiniz
    return redirect('anasayfa')  # Çıkış yaptıktan sonra yönlendirilecek sayfanın adını verin
def set_language(request,lang_code):
    if lang_code == 'tr':
        request.session['lang_code'] ='tr'
        print(request.session['lang_code'])
        return redirect('index')
    if lang_code =='en':
        request.session['lang_code'] ='tr'
        print(request.session['lang_code'])
        return redirect('homepage')

######################################################## REQUEST SESSİON == EN ############################################################## 
def homepage(request):
    if 'lang_code' not in request.session or request.session['lang_code'] != 'en':
        request.session['lang_code'] = 'en'
    categories = Category.objects.all()
    context = {
        'categories':categories,
    }
    return render(request,'index.html',context)

def about_us(request):
    if 'lang_code' not in request.session or request.session['lang_code'] != 'en':
        request.session['lang_code'] = 'en'

    company = Company.objects.first()  # Company modelinden bir şirket nesnesi al
    context = {
        'company': company,
    }
    
    return render(request, 'about_us.html', context)
def category(request,slug):
    if 'lang_code' not in request.session or request.session['lang_code'] != 'en':
        request.session['lang_code'] = 'en'
    category = get_object_or_404(Category, slug_en=slug)
    products = Product.objects.filter(category = category)
    context = {
        'category':category,
        'products':products,
    }
    return render(request, 'category_detail.html',context)