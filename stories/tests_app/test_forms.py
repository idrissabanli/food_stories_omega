from django.test import TestCase
from stories.forms import ContactForm


class TestContactForm(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.valid_data = {
            'name': 'Idris',
            'email': 'idris.sabanli@gmail.com',
            'subject': 1,
            'message': 'lksndflkdsn'
        }
        cls.invalid_data = {
            'name': """
            Lorem Ipsum is simply dummy text of the printing and typesetting 
            industry. Lorem Ipsum has been the industry's standard dummy text 
            ever since the 1500s, when an unknown printer took a galley of type 
            and scrambled it to make a type specimen book. It has survived not only 
            five centuries, but also the leap into electronic typesetting, remaining 
            essentially unchanged. It was popularised in the 1960s with the release of 
            """,
            'email': 'idris',
            'subject': 'lsdnfdlsnf',
            'message': 'lksndflkdsn'
        }
        cls.valid_form = ContactForm(data=cls.valid_data)
        cls.in_valid_form = ContactForm(data=cls.invalid_data)


    def test_form_with_valid_data(self):
        self.assertTrue(self.valid_form.is_valid())

    def test_form_with_invalid_data(self):
        self.assertFalse(self.in_valid_form.is_valid())

    def test_error_email_field(self):
        self.assertIn('email', self.in_valid_form.errors)

    def test_error_subject_field(self):
        self.assertIn('subject', self.in_valid_form.errors)
    
    def test_error_messages(self):
        self.assertIn('Ensure this value has at most 50 characters (it has 483).', self.in_valid_form.errors['name'])

    @classmethod
    def tearDownClass(cls):
        ...