from django import forms

from .models import Signature

class SignatureForm(forms.ModelForm):

    class Meta:
        model = Signature
        fields = ('name', 'ip_proto', 'ip_src', 'ip_dst','ip_sport', 'ip_dport', 'raw')