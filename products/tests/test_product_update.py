from django.test import TestCase
from django.urls import reverse

from products.models import Products


class ProductUpdateTestCase(TestCase):
    '''
      Verify the correct functionality of ProductUpdate user cases
      following the next testcases:
        * product_update path render product_update template
        * if product not exist render product_not_found template but
        with error message
        * verify if product was updated in the db
    '''

    def setUp(self) -> None:
        self.productSuject = Products(None, 'test_product')
        self.productSuject.save()
        self.data = {
            'name': 'a new name'
        }

    def test_product_update_route_render_product_update_template(self):
        url = reverse('product_update', args=[self.productSuject.id])
        response = self.client.get(url, data=self.data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product_update.html')

    def test_not_found_product_render_template_product_not_found(self):
        url = reverse('product_update', args=[2002020320])
        response = self.client.get(url, data=self.data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product_not_found.html')
