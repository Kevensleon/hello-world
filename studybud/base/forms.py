from django.forms import ModelForm
from .models import Room


class RoomForm(ModelForm):
    class Meta:
        meta = Room
        fields = '__all__'