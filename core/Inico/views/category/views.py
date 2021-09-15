from django.contrib.auth.decorators import login_required
from django.http import JsonResponse,HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView,CreateView
from django.shortcuts import render,redirect
from django.utils.decorators import method_decorator

from core.Inico.forms import CategoryForm
from core.Inico.models import Empleados,Cargos

def categoriry_list(request):
    data={
        'title': 'Personas dirijidas',
        'Empleados':Empleados.objects.all()
    }
    return render(request, 'category/list.html', data)

class Category_ListView(ListView):
    model = Empleados
    template_name = 'Inicio.html'

#loging metodo y decorador
    #@method_decorator(login_required)
#decorador para la protección de la pagina
    #@method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        #Metodo get de recargo de pagina y redirecion al cargar
        #if request.method =='GET':
            #return redirect('erp:category_list')
        return super().dispatch(request,*args,**kwargs)

    #def post(self, request, *args, **kwargs):
     #   data={'name': 'Alex'}
      #  return JsonResponse(data)

#Buscar en la tabla dependiendo de la inicial de la persona
    #def get_queryset(self):
        #return Empleados.objects.filter(name__startswith='A')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']= 'Personas dirijidas'
        context['create_url'] = reverse_lazy('add_programdores')
        return context

class CategoryCreateView(CreateView):
    model = Empleados
    form_class = CategoryForm
    template_name = 'category/create.html'
    success_url = reverse_lazy('inicio')

#Metodo post
    #def post(self, request, *args, **kwargs):
     #   print(request.POST)
      #  form=CategoryForm(request.POST)
       # if form.is_valid():
        #    form.save()
         #   return HttpResponseRedirect(self.success_url)
        #self.object=None
        #context= self.get_context_data(**kwargs)
        #context['form']=form
        #return render(request,self.template_name,context)



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']= 'Añadir personas'
        return context