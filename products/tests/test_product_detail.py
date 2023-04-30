from django.test import TestCase
from django.urls import reverse

from products.models import Products


class ProductDetailTestCase(TestCase):
    '''
      Verify the correct functionality of ProductDetail user cases
      following the next testcases:
        * product_detail path render product_detail template
        * if product not exist render product_detail template but
        with error message
    '''

    def setUp(self) -> None:
        self.productSuject = Products(None, 'test_product')
        self.productSuject.save()

    def test_get(self):
        '''
          Check if request product_detail route response with
          product_detail template and status_code 200
        '''
        url = reverse('product_detail', args=[self.productSuject.id])
        response = self.client.get(
            url
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product_detail.html')

        self.assertContains(response, self.productSuject.name)

    def test_product_not_exist_render_product_not_found_template(self):
        url = reverse('product_detail', args=[999999])
        response = self.client.get(
            url
        )

        self.assertEqual(response.status_code, 204)
        self.assertTemplateUsed(response, 'product_not_found.html')

        self.assertContains(response, 'The product is no longer available')
