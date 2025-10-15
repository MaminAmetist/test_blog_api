from django.contrib.auth.models import User
from django.test import TestCase


class FirstCase(TestCase):
    def setUp(self):
        User.objects.create_user(username='testuser1',
                                 password='12345')

    def test_login(self):
        login = self.client.login(username='testuser1', password='12345')
        self.assertTrue(login)
