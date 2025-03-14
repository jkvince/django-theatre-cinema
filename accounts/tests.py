from django.test import TestCase
from django.urls import reverse
from .models import CustomUser

import random

class ProductModelTest(TestCase):
    ACCOUNTS_CREATION = 16000

    def setUp(self):
        RANDOM_RANGE = 10000
        
        self.user = []
        self.data = []
        for x in range(self.ACCOUNTS_CREATION):
            generated = [
                'user' + str(x),
                'user' + str(random.randint(0, RANDOM_RANGE)) + '@domain.com',
                random.choice([True, False]),
                random.choice([True, False]),
                str(random.randint(0, 9999999))
            ]
            
            self.data.append(generated)
            
            self.user.append(
                CustomUser.objects.create(
                    username=generated[0],
                    email=generated[1],
                    is_superuser=generated[2],
                    is_premium=generated[3],
                    phone=generated[4]
                )
            )

    def test_user_creation(self):
        for x in range(self.ACCOUNTS_CREATION):
            self.assertEqual(self.user[x].username, self.data[x][0])
            self.assertEqual(self.user[x].email, self.data[x][1])
            self.assertEqual(self.user[x].is_superuser, self.data[x][2])
            self.assertEqual(self.user[x].is_premium, self.data[x][3])
            self.assertEqual(self.user[x].phone, self.data[x][4])


