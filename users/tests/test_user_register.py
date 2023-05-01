from django.test import TestCase
from django.urls import reverse


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

    def test_request_user_register_with_post_return_user_register_template(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
