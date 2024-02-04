from django import forms

from .models import Category, Company, Gallery, Message, Product


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'address', 'city', 'country', 'location', 'facebook', 'instagram', 'youtube', 'twitter', 'phone', 'mail', 'vision', 'mission', 'iframe']
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name','description','image','status','name_en','description_en','slug','slug_en']
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','image','category','description','ingredients','previous_price','price','status','priority']
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields=['first_name','last_name','message','subject','phone','email']

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery  # Use 'model' instead of 'models'
        fields = ['image']
class LoginForm(forms.Form):
    username = forms.CharField(label="Kullanıcı Adı")
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Şifre", widget=forms.PasswordInput)
      