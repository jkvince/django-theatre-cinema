from django.test import TestCase
from django.urls import reverse
from .models import CustomUser

ACCOUNTS_CREATION = 16000

class ProductModelTest(TestCase):
    def setUp(self):
        self.user = []
        for x in range(ACCOUNTS_CREATION):
            self.user.append(
                CustomUser.objects.create(
                    username='user' + str(x),
                    email='user'+ str(x) +'@domain.com',
                    is_superuser=False,
                    is_premium=True,
                    phone=str(x)
                )
            )

    def test_user_creation(self):
        for x in range(ACCOUNTS_CREATION):
            self.assertEqual(self.user[x].username, 'user' + str(x))
            self.assertEqual(self.user[x].is_superuser, False)
            self.assertEqual(self.user[x].is_premium, True)
            self.assertEqual(self.user[x].email, 'user' + str(x) + '@domain.com')