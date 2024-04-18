from django.shortcuts import render

from ice_cream.models import IceCream


def index(request):
    template_name = 'homepage/index.html'
    ice_cream_list = IceCream.objects.values(
        'id', 'title', 'description'
        # Верни только те объекты, у которых в поле is_on_main указано True:
        ).filter(is_on_main=True)
    # Cписок словарей: <QuerySet [{'id': 1, 'title': 'Золотое мороженое'}, ...]>
    context = {
        'ice_cream_list': ice_cream_list,
    }
    return render(request, template_name, context)
