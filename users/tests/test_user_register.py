from django.test import TestCase
from django.urls import reverse

from users.models import Users


class UserRegisterTestCase(TestCase):
    '''
      Test the correct main flow of user_register use case
      using the following testcases:
        * Request user_register route with get method return user_register.html template 
        * Request user_register routh with post method using already registered
        render user_error.html template 
        * Valid post request persist user in db 
    '''

    def setUp(self) -> None:
        self.url = reverse('user_register')
        self.registeredUser = Users(
            None, 'ezequiel', 'ezequiel', 'ezequiel@test.com')
        self.registeredUser.save()

        self.data = {
            'name': 'user_test_name',
            'password': 'a password',
            'email': 'test@email.com'
        }

    def test_request_user_register_with_post_return_user_register_template(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)

    def test_post_request_to_user_register_with_alredy_registerd_email_render_user_error_template(self):
        response = self.client.post(self.url, data={
            'name': 'testname',
            'email': self.registeredUser.email,
            'password': 'a password'
        })

        self.assertEqual(response.status_code, 200)
