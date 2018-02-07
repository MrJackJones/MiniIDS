# -*- encoding: utf-8 -*-
from django.test.testcases import TestCase
from django.urls import reverse
from django.test import Client
from main.models import Signature


class QuestionIndexViewTests(TestCase):

    def setUp(self):
        pass

    def test_no_login(self):

        response = self.client.get(reverse('main:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Необходима авторизация")

    def test_is_login(self):
        response = self.client.post('/login/', {'username': 'test_user', 'password': 'Qwerty123'})
        self.assertEqual(response.status_code, 200)

    def test_all_signature(self):

        response = self.client.get(reverse('main:all_signature'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Синатуры")

    def test_new_signature(self):

        response = self.client.get(reverse('main:signature'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Новая сигнатура")


