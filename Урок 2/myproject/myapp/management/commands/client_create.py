from django.core.management.base import BaseCommand
from myapp.models import Client, Product, Order

# CRUD functions


class Command(BaseCommand):
    help = "Get user by id."

    def add_arguments(self, parser):
        parser.add_argument('name', type=str,
                            help='User name', required=True)
        parser.add_argument('email', type=str,
                            help='User Email', required=True)
        parser.add_argument('phone', type=str,
                            help='User Phone', required=True)

    def handle(self, *args, **kwargs):
        client = Client.objects.create(
            name=kwargs['name'],
            email=kwargs['email'],
            phone=kwargs['phone'])
        client.save()
        self.stdout.write(f'{client}')
