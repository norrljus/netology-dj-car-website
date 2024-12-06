from django.http import Http404
from django.shortcuts import render
from django.db.models import Q

from main.models import Car, Sale


def cars_list_view(request):
    template_name = 'main/list.html'
    query = request.GET.get("q")
    if query is not None:
        query_list = Car.objects.filter(Q(model__contains=query))
        context = {
            'cars': query_list,
        }
        return render(request, template_name, context)
    else:
        all_cars = Car.objects.all()
        context = {
            'cars': all_cars
        }
        return render(request, template_name, context)



def car_details_view(request, car_id):
    try:
        one_car = Car.objects.get(id=car_id)
        context = {
            'car': one_car,
        }
        template_name = 'main/details.html'
        return render(request, template_name, context)
    except Car.DoesNotExist:
        raise Http404('Car not found')


def sales_by_car(request, car_id):
    try:
        one_car = Car.objects.get(id=car_id)
        sales = Sale.objects.filter(car=car_id)
        context = {
            'car': one_car,
            'sales': sales,
        }
        template_name = 'main/sales.html'
        return render(request, template_name, context)
    except Car.DoesNotExist:
        raise Http404('Car not found')
