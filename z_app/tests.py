from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Post

# Create your tests here.
class BlogTests(TestCase):
    def setup(self):
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'niran360@gmail.com',
            password = 'password'
        )

        self.post = Post.objects.create(
            title = 'A good day to code',
            body = 'Everyday is a good day to code if you want',
            author = self.user
        )

def test_string_representation(self):
    post = Post(title = 'A great day')
    self.assertEqual(str(post), post.title)

def test_post_content(self):
    self.assertEqual(f'{self.post.title}', 'A great day indeed')
    self.assertEqual(f'{self.post.author}', 'testuser')
    self.assertEqual(f'{self.post.body}', 'Nice body')

def test_post_list_view(self):
    response = self.client.get(reverse('home'))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, 'Nice body')
    self.assertTemplateUsed(response, 'home.html')

def test_post_detail_view(self):
    response = self.client.get('/post/1/')
    no_response = self.client.get('/post/100000/')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(no_response.status_code, 404)
    self.assertContains(response, 'good title')
    self.assertTemplateUsed(response, 'poast_detail.html')