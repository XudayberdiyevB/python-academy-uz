from django.test import TestCase
from .models import CardModel


class HomeTest(TestCase):

    def setUp(self) -> None:
        self.card=CardModel.objects.create(
            title='salom',
            text='salom',
        )

    def test_home_page(self):
        response=self.client.get('/')
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'home/index.html')


