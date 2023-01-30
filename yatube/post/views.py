from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')


def groups_list(request):
    return HttpResponse('Список групп')


def group_posts(request, slug):
    return HttpResponse(f'Посты группы {slug}')

# Create your views here.
