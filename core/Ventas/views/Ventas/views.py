from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.shortcuts import render
from datetime import datetime
# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from core.Ventas.models import Ventas


class VentaListview(TemplateView):
    template_name = 'Ventas/ventas.html'
    model = Ventas
    sucess_url = reverse_lazy('Ventas')

    def graph_sales_year_month(self):
        data=[]
        try:
            year= datetime.now().year
            for m in range (1,8):
                total= Ventas.objects.filter(date_joined__year=year,date_joined__week_day=m).aggregate(r=Coalesce(Sum('total'), 0)).get('r')
                data.append(float(total))
        except:
            pass
            return data

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Ventas_url'] = reverse_lazy('Ventas')
        context['graph_sales_year_month'] = []
        return context
