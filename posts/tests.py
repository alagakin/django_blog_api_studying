from django.contrib.auth import get_user_model
from django.test import TestCase


from .models import Post


class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create(
            username='test',
            email='test@gmail.com',
            password='123'
        )

        cls.post = Post.objects.create(
            author=cls.user,
            title='Test title',
            body='Test body'
        )

    def test_post_model(self):
        self.assertEqual(self.post.author.username, 'test')
        self.assertEqual(self.post.author.email, 'test@gmail.com')
        self.assertEqual(self.post.title, 'Test title')
        self.assertEqual(self.post.body, 'Test body')
        self.assertEqual(str(self.post), 'Test title')
