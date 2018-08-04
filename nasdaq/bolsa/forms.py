from .models import Bovespa, TICKER
from django.forms import ModelForm




class bovespaFORM(ModelForm):
     class Meta:
         model = TICKER
         fields = '__all__'
