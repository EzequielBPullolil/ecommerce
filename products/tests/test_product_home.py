from django.test import TestCase
from django.urls import reverse

from products.models import Products


class ProductHomeTestCase(TestCase):
    '''
      Verify the correct functionality of ProductHome user cases
      following the next testcases:
        * product_home path render product_home template
    '''

    def setUp(self) -> None:
        self.url = reverse('product_home')

    def test_product_home_route_render_product_home_template(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product_home.html')
