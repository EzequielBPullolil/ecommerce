from django.http import Http404
from django.shortcuts import render


def handle_not_found(func):
    '''
        Handle the case of not found product 
        to render product_not_found template
    '''
    def wrapper(request, *args, **kwargs):
        try:
            return func(request, *args, **kwargs)
        except Http404:
            return render(request, 'product_not_found.html')
    return wrapper
