from django import forms

from .models import Memories

# class MemoryForm(forms.Form):
#     memory_name = forms.CharField(label='Memory name', max_length=100)
#     memory_description = forms.TextInput()

class MemoryForm(forms.ModelForm):
    class Meta:
        model = Memories
        fields = ['name_memorie', 'description_memorie', 'place']