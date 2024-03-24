from django.core.management.base import BaseCommand
from myapp.models import Client, Product, Order

# CRUD functions


class Command(BaseCommand):
    help = "Delete client"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int,
                            help='User id', required=True)

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        client = Client.objects.get(id=pk)
        client.delete()
