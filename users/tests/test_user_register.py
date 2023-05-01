
from django.test import TestCase
from django.urls import reverse
from users.models import Users

from django.contrib.auth.hashers import check_password


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

    def test_valid_post_request_redirect_to_user_login_route(self):
        '''
            A valid register_user post request redirect to the user_login route 
        '''
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, 302)

        self.assertRedirects(
            response, reverse('user_login')
        )

    def test_user_is_persisted(self):
        '''
            After valid_post verify if user is persisted in db and
            have the password hashed
        '''
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, 302)

        persisted_user = Users.objects.get(email=self.data['email'])

        self.assertNotEqual(persisted_user.password, self.data['password'])

        self.assertTrue(
            check_password(self.data['password'], persisted_user.password)
        )
