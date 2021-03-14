from django.contrib.auth.models import User
from django.test import TestCase


class LoginTest(TestCase):

    def setUp(self) -> None:
        self.user=User.objects.create(
            username='Ali',
            password='123',
            email='123@gmail.com'
        )

    def test_login_user(self):
        response=self.client.post('/account/login/',{'username':self.user.username,'password':self.user.password},follow=True)
        self.assertEquals(response.status_code,200)
        print(self.user.username)

