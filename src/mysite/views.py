'''
Created on Feb 7, 2012

@author: tkidd
'''
from django.http import HttpResponse, Http404
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
import datetime

def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    """This function returns the current time"""
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body><html>" % now
    return HttpResponse(html)

def current_datetime_render_to_response(request):
    """This function performs the same function as current_datetime, but using render_to_response"""
    now = datetime.datetime.now()
    return render_to_response("current_datetime.html",{"now":now})

def hours_ahead(request,offset):
    """This function returns the time offset hours from now. It embeds html to return a response"""
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

def hours_ahead_context(request,offset):
    """This function shows how to use hours_ahead with a Template and Context"""
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    t = Template("<html><body>In {{ offset }} hour(s), it will be {{ dt }}.</body></html>")
    html = t.render(Context({"offset":offset,"dt":dt}))
    return HttpResponse(html)

def hours_ahead_get_template(request, offset):
    """This function shows how to use hours_ahead with get_template"""
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    t = get_template("hours_ahead_get_template.html")
    html = t.render(Context({"offset":offset,"dt":dt}))
    return HttpResponse(html)

def hours_ahead_render_to_response(request, offset):
    """This function shows how to use hours_ahead with render_to_response"""
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render_to_response("hours_ahead_get_template.html",{"offset":offset,"dt":dt})

def display_meta(request):
    """This function displays the META data about an HTTP request"""
    values = request.META.items()
    values.sort()
    html = []
    for k,v in values:
        html.append("<tr><td>%s</td><td>%s</td></tr>" % (k,v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def display_meta_render_to_response(request):
    """This function is the same as display_meta, but uses a template for the html"""
    values = request.META.items()
    values.sort()
    return render_to_response("display_meta.html",{"values":values,
                                                   "path":request.path,
                                                   "host":request.get_host(),
                                                   "fullpath":request.get_full_path(),
                                                   "secure":request.is_secure()
                                                   })