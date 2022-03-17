from .test_setup import TestSetup
from ..models import User

from faker import Faker

class TestViews(TestSetup):

    def test_user_cannot_register_with_no_data(self):
        res = self.client.post(self.register_url)
        self.assertEqual(res.status_code, 400)

    # def test_user_can_register_correctly(self):
    #     res = self.client.post(self.register_url, self.user_data, format ="json")
    #     self.assertEqual(res.data['first_name'], self.user_data['first_name'])
    #     self.assertEqual(res.data['last_name'], self.user_data['last_name'])
    #     self.assertEqual(res.data['email'], self.user_data['email'])
    #     self.assertEqual(res.data['username'], self.user_data['username'])
    #     self.assertEqual(res.status_code, 201)

    def test_user_cannot_login_with_an_unverified_email(self):
        self.client.post(
            self.register_url, self.user_data, format= 'json'
        )
        res = self.client.post(self.login_url, self.user_data, format = 'json')
        self.assertEqual(res.status_code, 400)

    def test_user_can_login_after_verification(self):
        response = self.client.post(
            self.register_url, self.user_data, format= 'json'
        )
        email = response.data['email']
        user = User.objects.get(email=email)
        user.is_verified = True
        user.save()
        res = self.client.post(self.login_url, self.user_data, format = 'json')
        self.assertEqual(res.status_code, 200)

    