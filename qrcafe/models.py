from django.utils import timezone
from io import BytesIO
from django.db import models
from PIL import Image
from django.forms import ValidationError
# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=25)
    address = models.CharField(max_length=255,null=True,blank=True)
    city = models.CharField(max_length=255,null=True,blank=True)
    country = models.CharField(max_length=255,null=True,blank=True)
    location = models.CharField(max_length=255,null=True,blank=True)
    facebook = models.CharField(max_length=255,null=True,blank=True)
    instagram = models.CharField(max_length=255,null=True,blank=True)
    youtube = models.CharField(max_length=255,null=True,blank=True)
    twitter = models.CharField(max_length=255,null=True,blank=True)
    phone = models.CharField(max_length=255,null=True,blank=True)
    mail = models.CharField(max_length=255,null=True,blank=True)
    about_us =models.CharField(max_length=255,null=True,blank=True)
    about_us_en =models.CharField(max_length=255,null=True,blank=True)
    vision = models.CharField(max_length=255,null=True,blank=True)
    vision_en = models.CharField(max_length=255,null=True,blank=True)
    mission = models.CharField(max_length=255,null=True,blank=True)
    mission_en = models.CharField(max_length=255,null=True,blank=True)
    iframe = models.CharField(max_length=255,null=True,blank=True)
    opening_hours = models.CharField(max_length=255,null=True,blank=True,default="Pazartesi - Pazar (09:00 24:00)")
# from django.utils.text import slugify
from django.core.files.base import ContentFile
def validate_image_dimensions(image):
    allowed_dimensions = [(3840, 2160), (5120, 2880), (2560, 1440),(1920,1080)]
    width, height = image.width, image.height
    if (width, height) not in allowed_dimensions:
        raise ValidationError("Resim boyutları geçersiz. Desteklenen boyutlar: 3840x2160, 5120x2880, 2560x1440.")

class Category(models.Model):
    name = models.CharField(max_length=25)
    name_en = models.CharField(max_length=25)
    description = models.CharField(max_length=50, null=True, blank=True)
    description_en = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to='static/image/category_image', validators=[validate_image_dimensions])
    status = models.BooleanField(default=True)
    slug = models.SlugField(unique=True)
    slug_en = models.SlugField(unique=True)
    created_by = models.CharField(max_length=255,null=False,blank=False)
    created_date = models.DateField(auto_now_add=True)  # Sadece gün, ay ve yıl
    created_time = models.TimeField()  # Sadece saat ve dakika


    def __str__(self):
        return str(self.name)
    def save(self, *args, **kwargs):
        if self.image:
            try:
                img = Image.open(self.image)
                desired_size = (3840, 2160)
                img = img.resize(desired_size, Image.ANTIALIAS)
                output = BytesIO()
                img.save(output, format='JPEG')
                self.image.file = ContentFile(output.getvalue())
            except Exception as e:
                # Hata işleme stratejisi
                print("Hata oluştu:", e)

        # Objeyi kaydet
        super(Category, self).save(*args, **kwargs)
class Product(models.Model):
    name = models.CharField(max_length=25)
    image = models.ImageField(upload_to='static/image/product_image')
    category = models.ForeignKey(Category,on_delete=models.DO_NOTHING)
    description = models.CharField(max_length=50)
    description_en = models.CharField(max_length=50)
    ingredients = models.CharField(max_length=255)
    ingredients_en = models.CharField(max_length=255)
    previous_price = models.DecimalField(max_digits=5, decimal_places=2,null=True,blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.BooleanField(default=True)
    priority = models.BooleanField(default=False)
    rating = models.IntegerField(default=5)
    created_by = models.CharField(max_length=255,null=False,blank=False)
    created_date = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    first_name = models.CharField(max_length=50,null=False,blank=False)
    last_name = models.CharField(max_length=50,null=False,blank=False)
    message = models.CharField(max_length=255,null=False,blank=False)
    subject = models.CharField(max_length=255,null=False,blank=False)
    phone = models.CharField(max_length=255,null=False,blank=False)
    email = models.EmailField(max_length=255,null=False,blank=False)
    status = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
class Gallery(models.Model):
    image = models.ImageField(upload_to='static/image/gallery_image')
class Log(models.Model):
    log = models.CharField(max_length=255)
from django.contrib.auth.models import AbstractUser

# class CustomUser(AbstractUser):
#     username = models.CharField(max_length=50)
#     password = models.CharField(max_length=255)
#     email = models.EmailField(max_length=255)

#     # Meta verileri ayarlayabilirsiniz
#     class Meta:
#         verbose_name = 'User'
#         verbose_name_plural = 'Users'