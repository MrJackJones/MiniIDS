from django.test import TestCase
from main.forms import SignatureForm

class MyTests(TestCase):
    def test_forms(self):
        form_data = {'name': 'SOME_TEXT', 'ip_proto': '6', 'ip_src': '10.1.1.10', 'ip_dst': '10.1.1.12','ip_sport': '80', 'ip_dport': '80', 'raw': 'TEXT'}
        form = SignatureForm(data=form_data)
        self.assertTrue(form.is_valid())