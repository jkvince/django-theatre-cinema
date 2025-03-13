from django.test import TestCase
from django.urls import reverse
from .models import CustomUser

import random

ACCOUNTS_CREATION = 16000

class ProductModelTest(TestCase):
    

    def setUp(self):
        self.user = []
        self.check_data = []
        for x in range(ACCOUNTS_CREATION):
            g_username = 'user' + str(x)
            g_email = 'user' + str(random.randint(0, 2000)) + '@domain.com'
            g_is_superuser = random.choice((True, False))
            g_is_premium = random.choice((True, False))
            g_phone = str(random.randint(0, 999999))
            
            self.check_data.append([g_username, g_email, g_is_superuser, g_is_premium, g_phone])

            self.user.append(
                CustomUser.objects.create(
                    username=g_username,
                    email=g_email,
                    is_superuser=g_is_superuser,
                    is_premium=g_is_premium,
                    phone=g_phone
                )
            )

    def test_user_creation(self):
        for x in range(ACCOUNTS_CREATION):
            self.assertEqual(self.user[x].username, self.check_data[x][0])
            self.assertEqual(self.user[x].email, self.check_data[x][1])
            self.assertEqual(self.user[x].is_superuser, self.check_data[x][2])
            self.assertEqual(self.user[x].is_premium, self.check_data[x][3])
            self.assertEqual(self.user[x].phone, self.check_data[x][4])