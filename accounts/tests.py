from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django_dynamic_fixture import G
from unittest import skip

# Create your tests here.

class SignupViewTestCase(TestCase):

    def setUp(self) -> None:

        self.valid_data = {
            'username': 'testuser',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        }
        self.bad_data = {
            'username': 'testuser',
            'password1': 'testpassword123',
            'password2': 'otherpassword',
        }
        self.valid_login = {
            'username': 'testuser',
            'password': 'testpassword123'
        }


    def test_signup_successful(self):
        response = self.client.post(reverse('signup'), self.valid_data)
        self.assertRedirects(response, reverse('index'))
        self.assertTrue(User.objects.filter(username='testuser').exists())
        self.assertEqual(response.status_code, 302)

    def test_signup_invalid(self):
        response = self.client.post(reverse('signup'), self.bad_data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.filter(username='testuser').exists())

    #@skip("Not yet")
    def test_login_successful(self):
        response = self.client.post(reverse('login'), self.valid_login)
        self.assertEqual(response.status_code, 200)
