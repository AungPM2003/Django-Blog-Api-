from django.contrib.auth import get_user_model
from django.test import TestCase
from posts.models import Post
# Create your tests here.
class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create(
            username='apm',
            email='test@gmail.com',
            password='1234567'
        )

        cls.post = Post.objects.create(
            author=cls.user,
            title = "hello",
            body='Hello world'
           )

    def test_post_model(self):
        self.assertEqual(self.post.author.username,'apm')
        self.assertEqual(self.post.title,'hello')
        self.assertEqual(self.post.body,'Hello world')
        self.assertEqual(str(self.post),'hello')