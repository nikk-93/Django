from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from myapp.models import Client, Order_Product, Product, Order


class Command(BaseCommand):
    help = "Update client"

    def handle(self, *args, **kwargs):
        product_pc = Product.objects.create(name='PC', price=1001)
        product_pc.save()

        product_car = Product.objects.create(
            name='Car', price=100002)
        product_car.save()

        product_flat = Product.objects.create(
            name='Flat', price=10000003)
        product_flat.save()

        client1 = Client.objects.create(
            name='Ivan',
            email='ivan@gmail.com',
            phone='+79998887766')
        client1.save()

        now = datetime.now()
        delta = timedelta(weeks=1)
        delta = timedelta(days=30)
        delta = timedelta(days=365)
        now -= delta

        order1 = Order.objects.create(
            client=client1)

        order2 = Order.objects.create(
            client=client1)

        order3 = Order.objects.create(
            client=client1)

        op11 = Order_Product.objects.create(
            order=order1, product=product_pc, quantity=1)
        op12 = Order_Product.objects.create(
            order=order1, product=product_car, quantity=1)
        op2 = Order_Product.objects.create(
            order=order2, product=product_car, quantity=1)
        op3 = Order_Product.objects.create(
            order=order3, product=product_flat, quantity=1)

        op11.save()
        op12.save()
        op2.save()
        op3.save()

        client1 = Client.objects.create(
            name='Pavel',
            email='pavel@gmail.com',
            phone='+76667778899')
        client1.save()

        order1 = Order.objects.create(
            client=client1)

        order2 = Order.objects.create(
            client=client1)

        order3 = Order.objects.create(
            client=client1)

        op11 = Order_Product.objects.create(
            order=order1, product=product_car, quantity=1)
        op2 = Order_Product.objects.create(
            order=order2, product=product_flat, quantity=1)
        op3 = Order_Product.objects.create(
            order=order3, product=product_car, quantity=1)

        op11.save()
        op2.save()
        op3.save()

        self.stdout.write(f'{client1}')
