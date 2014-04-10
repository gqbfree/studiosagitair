from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext
from django.views.generic import ListView, DetailView
from sito.models import *
from django.http import HttpResponseRedirect


# Create your views here.
'''
class HomeView(ListView):
    queryset = Prova.objects.all()
    context_object_name = 'provas'
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        #context['galleria_list'] = Immagini.objects.filter(prova__in = Prova.objects.filter(id = context['prova'].id))
        return context
'''

'''
def index(request):
    return HttpResponse("benvenuti in Sagitair studio")
'''

class IndexView(ListView):
    queryset = Post.objects.all().order_by('id')[1:]
    context_object_name = 'post_list'
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        language = "it"
        session_language = "it"
        if 'lang' in self.request.COOKIES:
            language = self.request.COOKIES['lang']
        if 'lang' in self.request.session:
            session_language = self.request.session['lang']

        context['language'] = language 
        context['session_language'] = session_language
        #context['post_active'] = Post.objects.all().order_by('id')[:1]
        #context['images_list'] = Immagini.objects.filter(id__in = Post.objects.filter(id = context['post'].id))
        return context


def StudioView(request):
   #return render_to_response('studio.html')
    language = "it"
    session_language = "it"
    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']
    if 'lang' in request.session:
        session_language = request.session['lang']
    context = {'language' : language, 
               'session_language' : session_language}

    return render(request, 'studio.html', context)
   #return render_to_response('studio.html', context_instance=RequestContext(request))

def InteriorView(request):
    language = "it"
    session_language = "it"
    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']
    if 'lang' in request.session:
        session_language = request.session['lang']

    categoria_list = Post.objects.filter(categoria__in = '4').order_by('-pub_date')
    context = {'language' : language, 
               'session_language' : session_language,
               'categoria_list': categoria_list}
    return render(request, 'interior.html', context)

def ArchitectureView(request):
    language = "it"
    session_language = "it"
    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']
    if 'lang' in request.session:
        session_language = request.session['lang']

    categoria_list = Post.objects.filter(categoria__in = '1').order_by('-pub_date')[:12]
    context = {'language' : language, 
               'session_language' : session_language,
               'categoria_list': categoria_list}
    #context = {'categoria_list': categoria_list}
    return render(request, 'architettura.html', context)

def RenderView(request):
   #return render_to_response('studio.html')
   return render_to_response('costruzione.html', context_instance=RequestContext(request))


class DettaglioView(DetailView):
    queryset = Post.objects.all()
    #context_object_name = 'post'
    template_name = 'dettaglio.html'

    def get_context_data(self, **kwargs):
        context = super(DettaglioView, self).get_context_data(**kwargs)
        context['categoria_list'] = Post.objects.filter(categoria__in = context['post'].categoria.all()).order_by('-id')
        context['video_list'] = context['post'].video.all().order_by('-id')[:1]
        context['images_left'] = context['post'].galleria.all().order_by('-id')[:3]
        context['images_right'] = context['post'].galleria.all().order_by('-id')[3:][:3]
        context['images_center'] = context['post'].galleria.all()[:1]

        language = "it"
        session_language = "it"
        if 'lang' in self.request.COOKIES:
            language = self.request.COOKIES['lang']
        if 'lang' in self.request.session:
            session_language = self.request.session['lang']

        context['language'] = language 
        context['session_language'] = session_language
        return context

def DesignView(request):
    categoria_list = Post.objects.filter(categoria__in = '5').order_by('id')
    context = {'categoria_list': categoria_list}
    return render(request, 'design.html', context)

def ContattiView(request):
   #return render_to_response('studio.html')
   return render_to_response('contatti.html', context_instance=RequestContext(request))

def RenderingView(request):
    language = "it"
    session_language = "it"
    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']
    if 'lang' in request.session:
        session_language = request.session['lang']
    render_list = Post.objects.exclude(categoria__in = '5').order_by('-id')
    context = {'language' : language, 
               'session_language' : session_language,
               'render_list': render_list}
    return render(request, 'rendering.html', context)

def AnimazioneView(request):
    video_list = Post.objects.exclude(categoria__in = '5').order_by('id')
    language = "it"
    session_language = "it"
    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']
    if 'lang' in request.session:
        session_language = request.session['lang']
    context = {'language' : language, 
               'session_language' : session_language,
               'video_list': video_list}
    return render(request, 'animazione.html', context)



'''
# someone clicks the link to change to English
def switch_to_English_link(request):
    request.session['lang'] = 'en'
  '''



def ProvaView(request):
   #return render_to_response('studio.html')

    language = "it"
    session_language = "it"
    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']
    if 'lang' in request.session:
        session_language = request.session['lang']
    context = {'language' : language, 
               'session_language' : session_language}

    return render(request, 'prova.html', context)


'''
def ProvaView(request):
    if settings.LANGUAGE_CODE == 'it':
        return HttpResponse("You prefer to read Italian.")
    else:
        return HttpResponse("You prefer to read another language.")

'''

def language(request, language='it'):
    response = HttpResponse("setting language to %s" % language)
    response.set_cookie('lang', language)
    request.session['lang'] = language
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    #return response



