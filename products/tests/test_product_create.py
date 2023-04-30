from django.test import TestCase
from django.urls import reverse

from products.models import Products
from products.forms import ProductForm


class ProductCreateTestCase(TestCase):
    def setUp(self):
        self.url = reverse('product_create')
        self.data = {
            'name': 'Test product',
            'description': 'A test product',
            'price': 10.99,
            'quantity': 20,
        }

    def test_get(self):
        '''
            Request products/create route and check if they return the
            product_create template
        '''
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product_create.html')
        self.assertIsInstance(response.context['form'], ProductForm)

    def test_post(self):
        '''
            Request products/create route with POST method and verify 
            the next testcases:
                * Response Status_code 302 
                * Product persist
                * Render product_detail
        '''

        response = self.client.post(self.url, data=self.data)
        self.assertEqual(response.status_code, 302)
        product = Products.objects.first()

        self.assertIsNotNone(product)

        self.assertRedirects(response, reverse(
            'product_detail', args=[product.id]))
