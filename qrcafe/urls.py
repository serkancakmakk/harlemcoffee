from . import views
from qrcafe.views import index
from django.contrib import admin
from django.urls import include, path
from django.conf import settings

from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name='index'),
    path('anasayfa/', views.index, name='index'),
    path('company/', views.create_company, name='company'),
    path('category/', views.create_category, name='category'),
    path('product/', views.add_product, name='product'),
    path('kategori/<slug:slug>/', views.kategori, name='kategori'),
    path('menu/', views.all_menu, name='menu'),
    path('menü/', views.tüm_menü, name='menü'),
    path('iletisim/', views.iletisim, name='iletisim'),
    path('admin_mesajlari/', views.admin_messages, name='admin_mesajlari'),
    path('mesaji_kapat/<int:id>', views.message_close, name='mesaji_kapat'),
    path('add_gallery/', views.add_gallery, name='add_gallery'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('hakkimizda/',views.hakkimizda,name="hakkimizda"),
    path('harlemadminlogin/', views.user_login, name='harlemadminlogin'),
    path('set_language/<str:lang_code>', views.set_language, name='set_language'),
    path('verify_code',views.verify_code,name="verify_code"),
    ################################################################################ request.session lang code == en
    path('homepage/', views.homepage, name='homepage'),
    path('about_us/', views.about_us, name='about_us'),
    path('category/<slug:slug>/', views.category, name='category'),
    # Add other URL patterns as needed
    path('urun_listele', views.list_product, name='urun_listele'),
    path('urun_duzenle/<int:id>', views.edit_product, name='urun_duzenle'),
    path('kategori_listele', views.list_category, name='kategori_listele'),
    path('kategori_duzenle/<int:id>', views.edit_category, name='kategori_duzenle'),
    path('test/', views.test, name='test'),
    path('delete_gallery_images',views.delete_gallery_images,name='delete_gallery_images'),
    path('delete_message/<int:id>', views.delete_message, name='delete_message'),
    path('logout/', views.logout, name='logout'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
