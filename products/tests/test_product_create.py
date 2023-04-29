from django.test import TestCase
from django.urls import reverse


class ProductCreateTestCase(TestCase):
    def setUp(self):
        self.url = reverse('product_create')

    def test_product_create_with_get_method_return_view(self):
        '''
            Verify if request product_create route return product_create view
        '''
        response = self.client.get(self.url)

        self.assertTemplateUsed(response, 'product_create.html')
