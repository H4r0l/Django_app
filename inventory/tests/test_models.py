from django.test import TestCase
from django.urls import reverse
from freezegun import freeze_time
from django_dynamic_fixture import G, F
from inventory.models import Product, Comment

class GetProductViewTest(TestCase):
    def setUp(self):
        # Create a test product and a related comment
        self.product = G(Product, name='Test product', brand=F(name='Test brand'), price=10.5)
        self.comment = G(Comment, product=self.product, text='Msg for test', created_date='2013-04-09')

    def test_view_url_accessible_by_name(self):
        # Check if the URL is accessible by its name
        response = self.client.get(reverse('get_product', args=[self.product.id]))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        # Check if the correct template is being used
        response = self.client.get(reverse('get_product', args=[self.product.id]))
        self.assertTemplateUsed(response, 'products/show_product.html')

    def test_view_displays_product_details(self):
        # Check if the view displays product details correctly
        response = self.client.get(reverse('get_product', args=[self.product.id]))
        self.assertContains(response, 'Test product')
        self.assertContains(response, '10.5')

    @freeze_time('2013-04-09')
    def test_view_displays_comments(self):
        # Check if the view displays comments with the correct date
        response = self.client.get(reverse('get_product', args=[self.product.id]))
        self.assertEqual(self.comment.created_date, '2013-04-09')
        self.assertContains(response, 'Msg for test')
