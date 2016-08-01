from django.test import TestCase
from .models import Post
# Create your tests here.

class PostTests(TestCase):
    """
    Here we will define tests
    that we will run against our post model
    """

    def test_str(self):
        test_title = Post(title='My latest blog post')
        self.assertEquals(str(test_title),'My latest blog post')