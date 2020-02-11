from django.test import TestCase
from django.urls import reverse, resolve
from ..views import signup
from ..forms import SignUpForm
from pprint import pprint
from django.contrib.auth.models import User


class SignUpTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_signup_url_resolves_signup_view(self):
        view = resolve('/signup')
        self.assertEqual(view.func, signup)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, SignUpForm)


class SuccessfulSignupTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        data = {
            'username': 'join',
            'email': 'john@doe.com',
            'password1': 'abcdef123456',
            'password2': 'abcdef123456',
        }
        self.response = self.client.post(url, data)
        self.home_url = reverse('home')

    def test_redirection(self):
        """
        A valid form submission should redirect user home
        """
        self.assertRedirects(self.response, self.home_url)

    def test_user_creation(self):
        self.assertTrue(User.objects.exists())

    def test_user_authentication(self):
        response = self.client.get(self.home_url)
        user = response.context.get('user')
        self.assertTrue(user.is_authenticated)


class InvalidSignUp(TestCase):
    def setUp(self):
        self.url = reverse('signup')
        self.response = self.client.post(self.url, {})

    def test_signup_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_not_create_user(self):
        self.assertFalse(User.objects.exists())

    def test_passwords_dont_match_error(self):
        data = {
            'username': 'kalen',
            'password1': 'asdf',
            'password2': 'fffff',
        }
        response = self.client.post(self.url, data)
        self.assertContains(response, "The two password fields didn’t match")
