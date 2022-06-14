from django.test import TestCase

from equation.models import Comments
from services import quadratic_equation


class TestComment(TestCase):

    @classmethod
    def setUpTestData(cls):
        Comments.objects.create(username='TestUser', comment_text='TestCommentText')

    def test_username_length(self):
        comment = Comments.objects.get(id=1)
        max_length = comment._meta.get_field('comment_text').max_length
        self.assertEqual(max_length, 300)


