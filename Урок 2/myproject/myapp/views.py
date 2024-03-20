import logging
from django.http import HttpResponse


logger = logging.getLogger(__name__)

main_page_html = '<!DOCTYPE html> \
<html lang="en"> \
<head>\
    <meta charset="UTF-8">\
    <meta name="viewport" content="width=device-width, initial-scale=1.0">\
    <title>Главная</title>\
</head>\
<body>\
    <div>Текст главной страницы</div>\
</body>\
</html>'

about_page_html = '<!DOCTYPE html> \
<html lang="en"> \
<head>\
    <meta charset="UTF-8">\
    <meta name="viewport" content="width=device-width, initial-scale=1.0">\
    <title>О себе</title>\
</head>\
<body>\
    <div>Текст о себе</div>\
</body>\
</html>'


def index(request):
    logger.info('Index page accessed')
    return HttpResponse(main_page_html)


def about(request):
    logger.info('About page accessed')
    return HttpResponse(about_page_html)
