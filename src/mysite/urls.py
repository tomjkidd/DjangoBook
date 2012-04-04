from django.contrib import admin
admin.autodiscover()

from django.conf.urls.defaults import patterns
from mysite.views import hello,current_datetime,current_datetime_render_to_response,hours_ahead,hours_ahead_context,hours_ahead_get_template,hours_ahead_render_to_response,display_meta,display_meta_render_to_response
from mysite.books.views import display_publisher, display_publisher_by_id, search_form, search
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^hello/$', hello),
    (r'^time/$', current_datetime),
    (r'^timerender/$', current_datetime_render_to_response),
    (r'^time/plus/(\d{1,2})/$', hours_ahead), # The open, '(', and close, ')', indicate a variable
    (r'^timecontext/plus/(\d{1,2})$', hours_ahead_context),
    (r'^timegettemplate/plus/(\d{1,2})$', hours_ahead_get_template),
    (r'^timerender/plus/(\d{1,2})$', hours_ahead_render_to_response),
    (r'^displaymeta/$', display_meta),
    (r'^displaymetarender/$', display_meta_render_to_response),
    (r'^admin/', admin.site.urls),
    
    (r'^books/publisher$', display_publisher),
    (r'^books/publisher/(\d{1,2})$', display_publisher_by_id),
    (r'^books/search-form/$', search_form),
    (r'^books/search/$', search),
    
    
    
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
