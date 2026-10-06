from django.test import Client, TestCase

# Create your tests here. 
class MyApp2TestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)