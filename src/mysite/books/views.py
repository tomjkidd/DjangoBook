from models import Publisher
from django.shortcuts import render_to_response
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponse

def display_publisher(request):
    """This function retrieves the Apress object created in the tutorial, giving access to it for display"""
    p1 = Publisher.objects.get(name__contains='Apress')
    return render_to_response("books_display_publisher.html",{"p1":p1})
    
def display_publisher_by_id(request, id):
    try:
        p1 = Publisher.objects.get(id=id)
    except ObjectDoesNotExist:
        raise Http404()
    
    return render_to_response("books_display_publisher.html",{"p1":p1})

def search_form(request):
    return render_to_response('books_search_form.html')

def search(request):
    if 'q' in request.GET:
        message = "You searched for: %r" %request.GET['q']
    else:
        message = "You submitted an empty form."
    return HttpResponse(message)