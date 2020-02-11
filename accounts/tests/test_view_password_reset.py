from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import PasswordResetForm
from django.test import TestCase
from django.urls import reverse, resolve


class PasswordResetTests(TestCase):
    def setUp(self):
        url = reverse('password_reset')
        self.response = self.client.get(url)

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_view_function(self):
        view = resolve('/reset')
        self.assertEqual(view.func.view_class, auth_views.PasswordResetView)



