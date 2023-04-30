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
        url = reverse('product_update', args=[909])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product_not_found.html')

    def test_product_updated_succefully_update_product_in_db(self):
        '''
            Verify if product[productSuject] is updated when
            request product_update route with POST method
        '''
        url = reverse('product_update', args=[self.productSuject.id])
        response = self.client.post(url, data=self.data)

        self.assertEqual(response.status_code, 302)
        updated_product = Products.objects.get(id=self.productSuject.id)
        self.assertEqual(updated_product.name, self.data['name'])

    def test_succefully_request_update_product_redirect_to_product_detail(self):
        '''
            Check if the correctr request to update_product redirect to product_detail
            template
        '''
        name = 'a test new name'
        url = reverse('product_update', args=[self.productSuject.id])
        response = self.client.post(url, data={
            'name': name
        })

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse(
            'product_detail', args=[self.productSuject.id]))
