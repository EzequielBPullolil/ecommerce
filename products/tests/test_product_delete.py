from django.test import TestCase
from django.urls import reverse

from products.models import Products


class ProductDeleteTestCase(TestCase):
    '''
      Verify the correct functionality of ProductDelete user case
      following the next testgoodcases:
        * product_delete path render product_delete template
        * if product not exist render product_not_found template
        * verify if product was deleted from db
    '''

    def setUp(self) -> None:
        self.productSuject = Products(None, 'product_to_delete')
        self.productSuject.save()

    def test_product_delete_route_render_product_delete_template(self):
        '''
          Check if request product_delete route with GET method
          render product_delete template
        '''
        url = reverse('product_delete', args=[self.productSuject.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product_delete.html')

    def test_not_found_product_render_template_product_not_found(self):
        url = reverse('product_delete', args=[909])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product_not_found.html')

    def test_succefully_request_delete_product_from_db(self):
        '''
          Verify if succefully request of delete_product user case
          remove product from db
        '''
        url = reverse('product_delete', args=[self.productSuject.id])
        response = self.client.post(url)

        self.assertEqual(response.status_code, 200)
        productDeleted = Products.objects.filter(
            id=self.productSuject.id).exists()
        self.assertFalse(productDeleted)
