import random
import string
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Category, Company, Gallery, Message, Product 
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import CategoryEditForm, CategoryForm, CompanyForm, GalleryForm, LoginForm, MessageForm, ProductEditForm, ProductForm
from django.contrib import messages
from django.http import HttpResponse
from itertools import groupby
from operator import itemgetter
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
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
def index(request):
    if 'lang_code' not in request.session or request.session['lang_code'] != 'tr':
        request.session['lang_code'] = 'tr'
    company = Company.objects.first()
    products = Product.objects.filter(showcase_product=True)
    categories = Category.objects.all()
    context = {
        'company':company,
        'products': products,
        'categories': categories,
    }
    return render(request, 'index.html', context)

def kategori(request, slug):
    # Görünüm kodları buraya eklenecek
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category = category)
    context = {
        'category':category,
        'products':products,
    }
    return render(request, 'category_detail.html',context)
def tüm_menü(request):
    if 'lang_code' not in request.session or request.session['lang_code'] != 'tr':
        request.session['lang_code'] = 'tr'
    categories = Category.objects.all()
    company = Company.objects.first()
    context = {
        'company':company,
            'categories':categories,
        }
    return render(request, 'all_menu.html', context)
def iletisim(request):
    company = Company.objects.first()
    if 'lang_code' not in request.session or request.session['lang_code'] != 'tr':
        request.session['lang_code'] = 'tr'
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = MessageForm()
    context = {
        'form': form,
        'company':company,
        }
    return render(request, 'contact.html', context)
def hakkimizda(request):
    if request.session['lang_code'] != 'tr':
        request.session['lang_code'] = 'tr'
    company = Company.objects.first()
    context = {
        'company':company,
    }
    return render(request,'about_us.html',context)
def all_menu(request):
    if 'lang_code' not in request.session or request.session['lang_code'] != 'en':
        request.session['lang_code'] = 'en'
    categories = Category.objects.all()
    company = Company.objects.first()
    context = {
        'company':company,
        'categories':categories,
        }
    return render(request, 'all_menu.html', context)



from django.contrib.auth.decorators import login_required


import os
from django.conf import settings

def gallery(request):
    company = Company.objects.first()
    gallery = Gallery.objects.all()
    context = {
        'company':company,
        'gallery':gallery,
    }
    return render(request,'gallery.html',context)

def about_us(request):
    if request.session['lang_code'] != 'en':
        request.session['lang_code'] = 'en'
    company = Company.objects.first()
    context = {
        'company':company,
    }
    return render(request,'about_us.html',context)



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
    company = Company.objects.first()
    products = Product.objects.filter(showcase_product=True)
    categories = Category.objects.all()
    context = {
        'company':company,
        'products': products,
        'categories': categories,
    }
    return render(request, 'index.html', context)

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
def contact(request):
    company = Company.objects.first()
    if 'lang_code' not in request.session or request.session['lang_code'] != 'en':
        request.session['lang_code'] = 'en'
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = MessageForm()
    context = {
        'form': form,
        'company':company,
        }
    return render(request, 'contact.html', context)
def test(request):
    return render(request,'test.html')





#####################################
#                                   #
#           OLUŞTURMA İŞLEMLERİ     #
#                                   #
######################################
def create_company(request):
    if not request.user.is_authenticated:
        return redirect('index')
    company = Company.objects.first()
    company_instance, created = Company.objects.get_or_create(pk=1)  # Tek bir kayıt al veya oluştur

    context = {
        'company':company,
    }  # Define context variable
    
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company_instance)
        print(form.errors)
        if form.is_valid():
            print(form.errors)
            form.save()
            return redirect('company')  # Başarı durumunda yönlendirilecek sayfa
    else:
        form = CompanyForm(instance=company_instance)
        print(form.errors)
        context ={
            'form': form,
            'company':company,
        }

    return render(request, 'company.html', context)
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
                return render(request, 'add_html/add_category.html', {'form': form, 'categories': categories})
            category.save()
            return redirect('category')
    else:
        form = CategoryForm()
    
    return render(request, 'add_html/add_category.html', {'form': form, 'categories': categories})
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
    return render(request, 'add_html/add_product.html', context)
def add_gallery(request):
    if not request.user.is_authenticated:
        return redirect('index')  # Redirect to the homepage if the user is not authenticated

    if request.method == "POST":
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Seçilenler Başarıyla Yüklendi')
            return redirect('add_gallery')
    else:
        form = GalleryForm()

    images = Gallery.objects.all()
    context = {
        'images': images,
        'form': form,
    }
    return render(request, 'add_html/add_gallery.html', context)
#####################################
#                                   #
#           LİSTELEME İŞLEMLERİ     #
#                                   #
######################################
def list_product(request):
    if not request.user.is_authenticated:
        return redirect('index')
    products = Product.objects.all()
    categories = Category.objects.all()
    
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'list_html/list_product.html', context)
def list_category(request):
    if not request.user.is_authenticated:
        return redirect('index')
    categories = Category.objects.all()
    form = CategoryEditForm()
    context = {
        'form': form,
        'categories': categories,
    }
    return render(request, 'list_html/list_category.html', context)
#####################################
#                                   #
#           SİLME İŞLEMLERİ         #
#                                   #
######################################
def delete_gallery_images(request):
    if not request.user.is_authenticated:
        return redirect('index')
    if request.method == "POST":
        images_to_delete_ids = request.POST.getlist('images_to_delete')
        for image_id in images_to_delete_ids:
            image = get_object_or_404(Gallery, id=image_id)
            # dosya konumundan sil
            image_path = os.path.join(settings.MEDIA_ROOT, str(image.image))
            os.remove(image_path)
            # veritabanından sil
            image.delete()
        messages.success(request,'Seçilenler başarıyla silindi')
        return redirect('add_gallery')  # galeriye yönlendir
    else:
        messages.error(request, "Bilinmeyen bir hata oluştu.Lütfen Tekrar Deneyiniz")
        return redirect('add_gallery')  # galeriye yönlendir
    

#####################################
#                                   #
#           DÜZENLEME İŞLEMLERİ     #
#                                   #
######################################
def edit_product(request, id):
    if not request.user.is_authenticated:
        return redirect('index')
    product = get_object_or_404(Product, id=id)
    categories = Category.objects.all()
    if request.method == 'POST':
        form = ProductEditForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('urun_listele'))  
    else:
        form = ProductEditForm(instance=product)
    
    context = {
        'form': form,
        'categories': categories,
        'product_category_name': product.category.name  # Kategori adını context'e ekleyin
    }

    if not form.is_valid():
        context['form_errors'] = form.errors
        return render(request, 'list_html/list_product.html', context)

    return render(request, 'list_html/list_product.html', context)
def edit_category(request, id):
    if not request.user.is_authenticated:
        return redirect('index')
    category = get_object_or_404(Category, id=id)
    categories = Category.objects.all()

    if request.method == 'POST':
        form = CategoryEditForm(request.POST, instance=category)
        if form.is_valid():
            print(category.created_date)   
            form.save()
            return HttpResponseRedirect(reverse('kategori_listele'))  
    else:
        form = CategoryEditForm(instance=category)
    
    context = {
        'form': form,
        'categories': categories,
    }

    if not form.is_valid():
        # Form hatalarını print ile konsola yazdır
        print(form.errors)
        return render(request, 'list_html/list_product.html', context)

    return render(request, 'list_html/list_product.html', context)


#####################################
#                                   #
#           YÖNETİCİ ALANI          #
#                                   #
######################################
def delete_message(request, id):
    if not request.user.is_authenticated:
        return redirect('index')
    message = get_object_or_404(Message, id=id)
    
    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Check if the user has permission to delete the message
            # Delete the message
            message.is_delete=True
            message.save()
            messages.success(request,'Belirtilen Mesaj Silindi')
            return redirect('admin_mesajlari')
    else:
        return redirect('index')
def admin_messages(request):
    if not request.user.is_authenticated:
        return redirect('index')
    messages = Message.objects.filter(is_delete=False).order_by('status')
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
#####################################
#                                   #
#           SİSTEME GİRİŞ İÇİN      #
#           VERİFİCATİON ALANI      #
#                                   #
######################################
verification_codes = {} # Kullanıcı e-posta adresine göre doğrulama kodlarını saklayacak sözlük

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
#####################################
#                                   #
#           SİSTEME GİRİŞ ALANI     #
#                                   #
######################################    
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if username == 'serkan' and password =='serkan':
                user = authenticate(request, username=username, password=password)
                
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
def user_logout(request):
    logout(request)
    return redirect('index')  # Çıkış yaptıktan sonra indexe yönlendir