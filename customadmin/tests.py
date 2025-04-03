from django.test import TestCase
from accounts.models import CustomUser
from django.urls import reverse
import json

from venues.models import Seat
import customadmin.urls

class RoomEditorViewTest(TestCase):
    def setUp(self):
        grid_info = [
            {   
                "number": "hey",
                "premium": False,
                "accessible": True,
                "location_row": 7,
                "location_column": 11
            }
        ]
        
        data = {
            "data": json.dumps(grid_info)
        }

        print(data)
        self.client.login(username="supervin",password="passwordAdmin123")
        response = self.client.post(reverse('admin-room'), data)


    def testmodels(self):
        print(Seat.objects.all())
        self.assertEqual(2, 2)
