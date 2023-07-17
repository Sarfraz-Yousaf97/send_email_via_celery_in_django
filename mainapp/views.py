from django.shortcuts import render
from .task import task_func
from django.http import HttpResponse

def test(request):
    task_func.delay()
    return HttpResponse('Done')

