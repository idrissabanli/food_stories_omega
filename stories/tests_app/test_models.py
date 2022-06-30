from django.test import TestCase
from stories.models import Contact


class TestContact(TestCase):

    def setUp(self):
        self.data1 = {
            "name": "Idris",
            "email": "idris@gmail.com",
            "subject": 1,
            "message": 'message',
        }
        self.data2 = {
            "name": "Idris2",
            "email": "idris2@gmail.com",
            "subject": 2,
            "message": 'message',
        }
        self.contact1 = Contact.objects.create(**self.data1)
        self.contact2 = Contact.objects.create(**self.data2)

    def test_model_data(self):
        self.assertEqual(self.data1['name'], self.contact1.name)
        self.assertEqual(self.data1['email'], self.contact1.email)

    def test_str_method(self):
        self.assertEqual(str(self.contact1), self.data1['name'])
    

    def tearDown(self):
        del self.contact1
        del self.contact2
