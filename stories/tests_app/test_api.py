from django.test import TestCase
from django.urls import reverse_lazy
from stories.models import Category, User
from django.conf import settings


class TestStoriesAPIView(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.url = reverse_lazy('api_stories')
        cls.cat = Category.objects.create(title='Cat 1', image='cat_image.png')
        cls.user = User.objects.create_user(username='idris', email='idris.sabanli@gmail.com', password='i4383930')
        # cls.valid_data = {
        #     'title': 'STORY #1',
        #     'category': cls.cat.id,
        #     'author': cls.user.id,
        #     'image': ('1_1Y7ahYk.png', open(f'{settings.MEDIA_ROOT}/story_images/1_1Y7ahYk.png', 'rb')),
        #     'cover_image': ('1_1Y7ahYk.png', open(f'{settings.MEDIA_ROOT}/story_images/1_1Y7ahYk.png', 'rb')),
        #     'content': 'sklfnsdklfndkl'
        # }
        # image.close()
        

    def test_api_url(self):
        expected_url = '/api/stories/'
        self.assertEqual(self.url, expected_url)
    
    def test_api_post_request_status_code(self):
        valid_data = {
            'title': 'STORY #1',
            'category': self.cat.id,
            'author': self.user.id,
            'image': ('1_1Y7ahYk.png', open(f'{settings.MEDIA_ROOT}/story_images/1_1Y7ahYk.png', 'rb')),
            'cover_image': ('1_1Y7ahYk.png', open(f'{settings.MEDIA_ROOT}/story_images/1_1Y7ahYk.png', 'rb')),
            'content': 'sklfnsdklfndkl'
        }
        res = self.client.post(self.url, data=valid_data)
        self.assertEqual(res.status_code, 201)

    def test_api_post_request_valid_data_response(self):
        valid_data = {
            'title': 'STORY #1',
            'category': self.cat.id,
            'author': self.user.id,
            'image': ('1_1Y7ahYk.png', open(f'{settings.MEDIA_ROOT}/story_images/1_1Y7ahYk.png', 'rb')),
            'cover_image': ('1_1Y7ahYk.png', open(f'{settings.MEDIA_ROOT}/story_images/1_1Y7ahYk.png', 'rb')),
            'content': 'sklfnsdklfndkl'
        }
        res = self.client.post(self.url, data=valid_data)
        result = res.json()
        self.assertEqual(result['title'], valid_data['title'])

    def test_api_post_request_invalid_data_response(self):
        in_valid_data = {
            # 'title': 'STORY #1',
            'category': self.cat.id,
            'author': self.user.id,
            'image': ('1_1Y7ahYk.png', open(f'{settings.MEDIA_ROOT}/story_images/1_1Y7ahYk.png', 'rb')),
            'cover_image': ('1_1Y7ahYk.png', open(f'{settings.MEDIA_ROOT}/story_images/1_1Y7ahYk.png', 'rb')),
            'content': 'sklfnsdklfndkl'
        }
        res = self.client.post(self.url, data=in_valid_data)
        result = res.json()
        self.assertIn('This field is required.', result['title'])

    def test_api_get_request_response(self):
        res = self.client.get(self.url)
        self.assertIsInstance(res.json(), list)

    def test_api_get_request_status_code(self):
        res = self.client.get(self.url)
        self.assertEqual(res.status_code, 200)

    def test_api_get_request_response(self):
        res = self.client.get(self.url)
        self.assertIsInstance(res.json(), list)

    @classmethod
    def tearDownClass(cls):
        ...



# class A:
#     ...


# a = A()

# isinstance(a, A)