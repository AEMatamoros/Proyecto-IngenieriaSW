from django.forms import ModelForm
from .models import Ad

# Create the form class.
class AdForm(ModelForm):
    class Meta:
        model = Ad
        fields = ['ad_name', 'ad_description', 'price', 'ad_images', 'id_ad_kind','id_category','id_location', 'id_user','id_unit', 'id_store']