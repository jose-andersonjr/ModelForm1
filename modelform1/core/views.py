from django.shortcuts import render
from django.http import HttpResponse

from modelform1.core.forms import ClienteForm

# Create your views here.
def formulario_modelform(request):
    template_name = "formularios/formulario_modelform.html"
    if request.method == "GET": 
        form = ClienteForm()
        context = {
            'form': form
        }
    else: 
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save() #.save() vai retornar um objeto da classe Cliente
            form = ClienteForm()
        context = {
            'form': form
        }
    return render(request, template_name, context=context)