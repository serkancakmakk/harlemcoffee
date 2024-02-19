from django import forms

from .models import Category, Company, Gallery, Message, Product

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'address', 'city', 'country', 'location', 'facebook', 'instagram', 'youtube', 'twitter', 'phone', 'mail', 'vision','vision_en','mission_en', 'iframe','opening_hours','about_us','about_us_en','index_text','index_text_en']
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name','description','image','status','name_en','description_en','slug','slug_en']
class CategoryEditForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name','description','image','status','name_en','description_en','slug','slug_en']
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','image','category','description','ingredients','previous_price','price','status','priority','showcase_product']
class ProductEditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'image', 'category', 'description', 'ingredients', 'previous_price', 'price', 'status', 'priority', 'showcase_product']

    def clean_previous_price(self):
        previous_price = self.cleaned_data.get('previous_price')
        try:
            float(previous_price)
        except ValueError:
            raise forms.ValidationError('Geçerli bir sayı girin.')
        return previous_price

    def clean_price(self):
        price = self.cleaned_data.get('price')
        try:
            float(price)
        except ValueError:
            raise forms.ValidationError('Geçerli bir sayı girin.')
        return price
from captcha.fields import ReCaptchaField

class MessageForm(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = Message
        fields=['first_name','last_name','message','subject','phone','email','captcha']

class GalleryForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'accept': 'image/*'}))
    class Meta:
        model = Gallery  # Use 'model' instead of 'models'
        fields = ['image']
class LoginForm(forms.Form):
    username = forms.CharField(label="Kullanıcı Adı")
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Şifre", widget=forms.PasswordInput)
