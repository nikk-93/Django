from datetime import datetime, timedelta
import logging
from .models import Order_Product
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render

logger = logging.getLogger(__name__)


class ProductView(View):
    def get(self, request, client_id, show_step=7):
        start_date = datetime.now() - timedelta(days=show_step)
        orders = Order_Product.objects.filter(
            order__client__id=client_id,
            order__order_date__date__gte=start_date)
        products = set([order.product for order in orders])
        context = {"products": products, "show_step": show_step}
        return render(request, "myapp/my_template.html", context)


def index(request):
    logger.info('Index page accessed')
    return HttpResponse('Главная')


def about(request):
    logger.info('About page accessed')
    return HttpResponse('О нас')
