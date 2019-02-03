from django.test import TestCase
from django.urls import reverse
import json


# Create your tests here.
class Test_calc_sum(TestCase):
    """Test the calc_sum api"""

    def test_calc_sum(self):
        url = reverse("total")
        numbers_to_add = list(range(10000001))
        result = {"total": sum(numbers_to_add)}
        data = {'list': json.dumps(numbers_to_add),
                }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), result)
