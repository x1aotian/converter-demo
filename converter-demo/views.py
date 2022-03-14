from django.http import HttpResponse
from django.shortcuts import render
from src.coverter import converter

def form(request):
    return render(request, 'main.html')

def result(request):
    context = {}

    if request.method == 'POST':
        source = request.POST.get('source')
        target = request.POST.get('target')
        api_key = request.POST.get('api_key')
        base_id = request.POST.get('base_id')
        table_name = request.POST.get('table_name')
        file_path = request.POST.get('file_path')
        converter(source, target, file_path, api_key, base_id, table_name)

        context['res'] = 'Convert successfully from %s to %s!' % (source, target)
        return render(request, 'result.html', context)
    
    return render(request, 'main.html', context)
