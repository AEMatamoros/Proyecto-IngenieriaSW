from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Ad
from account.models import Account
from images.models import Image
from django.views.generic.edit import CreateView
from django.urls import reverse, reverse_lazy
from .forms import AdForm
from django.http import  HttpResponseRedirect

class ShowAdsListView(ListView):

    model= Ad
    template_name="ad_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["ads_data"]= Ad.objects.prefetch_related()
        
        return context
#id_user ,id_store ,id_location,id_ad_kind,id_category,id_unit,ad_name,ad_description,price,date_created

class AdCreate(CreateView):
    model = Ad
    fields = ['ad_name', 'ad_description', 'price', 'ad_images']

    def post(self, request, *args, **kwargs):
        form = AdForm(request.POST)
        if form.is_valid():
            ad = form.save()
            ad.save()
            user_ad.user = request.user
            user_ad.ad = store
            user_ad.save()
            return HttpResponseRedirect(reverse_lazy('my_products')+'?added')
        return HttpResponseRedirect(reverse_lazy('my_products')+'?error')
    
    def get_success_url(self):
        return reverse_lazy('my_products')+'?added'