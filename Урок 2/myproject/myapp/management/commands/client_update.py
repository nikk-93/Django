from django.core.management.base import BaseCommand
from myapp.models import Client, Product, Order

# CRUD functions


class Command(BaseCommand):
    help = "Update client"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int,
                            help='User id', required=True)
        parser.add_argument('name', type=str,
                            help='User name', required=False)
        parser.add_argument('email', type=str,
                            help='User Email', required=False)
        parser.add_argument('phone', type=str,
                            help='User Phone', required=False)
        parser.add_argument('address', type=str,
                            help='User address', required=False)

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        name = kwargs['name']
        email = kwargs['email']
        phone = kwargs['phone']
        address = kwargs['address']

        client = Client.objects.get(id=pk)

        if name:
            client.name = name
        if email:
            client.email = email
        if phone:
            client.phone = phone
        if address:
            client.address = address

        client.save()

        self.stdout.write(f'{client}')
