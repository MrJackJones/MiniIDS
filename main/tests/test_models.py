from django.test.testcases import TestCase
from main.models import Signature, Alerts, Data
from django.utils import timezone



class Test_signature_TEST(TestCase):
    def setUp(self):
        Signature.objects.create(name="TEST", raw="Torrent", ip_proto='6', ip_sport='80', ip_dport='80')
        Signature.objects.create(name="TEST2", raw="SOME_TEXT", ip_proto='6', ip_sport='4857', ip_dport='4561')

    def test_signature_TEST(self):
        TEST = Signature.objects.get(name="TEST")
        TEST2 = Signature.objects.get(name="TEST2")
        self.assertEqual(TEST.ip_proto, '6')
        self.assertEqual(TEST2.raw, 'SOME_TEXT')


class Test_alerts_TEST(TestCase):
    def setUp(self):
        Alerts.objects.create(signature_name = 'TEST', raw='Torrent', id_signature='1', action_time=timezone.now())
        Alerts.objects.create(signature_name = 'TEST2', raw='SOME_TEXT', id_signature='2', action_time=timezone.now())

    def test_alerts_TEST(self):
        TEST = Alerts.objects.get(signature_name="TEST")
        TEST2 = Alerts.objects.get(signature_name="TEST2")
        self.assertEqual(TEST.id_signature, '1')
        self.assertEqual(TEST2.raw, 'SOME_TEXT')


class Test_Data_TEST(TestCase):
    def setUp(self):
        Data.objects.create(action_time=timezone.now(), ethernet_dst='10.1.10.3', ethernet_src='10.1.20.43', raw='SOME_TEXT')

    def test_Data_TEST(self):
        TEST = Data.objects.get(ethernet_dst='10.1.10.3')
        self.assertEqual(TEST.ethernet_src, '10.1.20.43')
        self.assertEqual(TEST.raw, 'SOME_TEXT')