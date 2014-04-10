from django.conf.urls import patterns, include, url
from django.conf import settings
from sito import views
from sito.views import *

from django.conf.urls.i18n import i18n_patterns


urlpatterns = patterns('sito.views',
   # url(r'^i18n/', include('django.conf.urls.i18n')),
   #url(r'^$', HomeView.as_view()),
    url(r'^$', IndexView.as_view()),
    url(r'^interior/$', InteriorView),
    url(r'^architettura/$', ArchitectureView),
    url(r'^(?P<pk>\d+)/$', DettaglioView.as_view()),
    #url(r'^(?P<post_id>\d+)/$', DetailView),
    url(r'^studio/', StudioView),
    url(r'^prova/', ProvaView),
    url(r'^design/$', DesignView),
    #url(r'^design/(?P<pk>\d+)/$', DesignPaginaView.as_view()),
    #url(r'^industrial/', RenderView),
    url(r'^render/', RenderingView),
    url(r'^animazione/', AnimazioneView),
    url(r'^contatti/', ContattiView),
    #url(r'^language/(?P<language>[a-zA-Z\-]+[a-zA-Z]+)/$','views.language'),
    url(r'^language/(?P<language>[a-z\-]+)/$', language),
    #url(r'^i18n/', include('django.conf.urls.i18n')),



    #url(r'^/', include(admin.site.urls)),
)

'''
urlpatterns += i18n_patterns('',
    url(r'^(?P<pk>\d+)/$', DettaglioView.as_view()),
)
'''