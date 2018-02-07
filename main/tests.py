from django.test.testcases import TestCase
from .models import Signature
# Create your tests here.



class TestUM(TestCase):
    def setUp(self):
        Signature.objects.create(name="TEST", raw="Torrent", ip_proto='6', ip_sport='123', ip_dport='321')
        Signature.objects.create(name="TEST2", raw="SOME_TEXT", ip_proto='6', ip_sport='123', ip_dport='321')

    def tearDown(self):
        pass

    def test_signature_TEST(self):
        TEST = Signature.objects.get(name="TEST")
        TEST2 = Signature.objects.get(name="TEST2")
        self.assertEqual(TEST.ip_proto, '6')
        self.assertEqual(TEST2.raw, 'SOME_TEXT')

    def test_numbers_3_4(self):
        self.assertEqual(3 * 4, 12)

    def test_strings_a_3(self):
        self.assertEqual('a' * 3, 'aaa')


# class SignatureTestCase(TestCase):
#     def setUp(self):
#         Signature.objects.create(name="TEST", raw="Torrent", ip_proto='6', ip_sport='123', ip_dport='321')
#         Signature.objects.create(name="TEST2", raw="SOME_TEXT", ip_proto='6', ip_sport='123', ip_dport='321')
#
#     def test_animals_can_speak(self):
#         lion = Signature.objects.get(name="lion")
#         cat = Signature.objects.get(name="cat")
#         self.assertEqual(lion.speak(), 'The lion says "roar"')
#         self.assertEqual(cat.speak(), 'The cat says "meow"')