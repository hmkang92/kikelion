from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.shortcuts import redirect
from django.views.generic import RedirectView

def root(request):
	return redirect('board:post_list')

urlpatterns = [
    
    #url(r'^$', root, name='root'),
    url(r'^$', lambda r: redirect('board:post_list'), name='root'),
    #url(r'^$', RedirectView.as_view(pattern_name='board:post_list')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^board/', include('board.urls', namespace='board')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

if settings.DEBUG:
	import debug_toolbar
	urlpatterns += [
		url(r'^__debug__/', include(debug_toolbar.urls)),
	]