from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView

from .models import Anleitung, Anleitungsschritt, Komponente

# Create your views here.


def start(request):
    return render(request, 'Startbildschirm.html')

def add(request):
    return render(request, 'Add_page.html')

def anleitungsschritt(request):
    return render(request, 'AnleitungSchritte.html')

def anleitung_gespeichert_und_hochgeladen(request):
    return render(request, 'Anleitung_gespeichert_und_hochgeladen.html')

def entwurf_gespeichert(request):
    return render(request, 'Entwurf_gespeichert.html')

#Anleitung durchgehen

# anleitung = Anleitung.objects.all()
# anleitungstitel = anleitung[0]
# schrittinhalte = Anleitungsschritt.objects.all()

# class MyView(View):
#     def get(self, request):
#         return HttpResponse('Anleitung_durchgehen.html')


class AnleitungDetailView(DetailView):

    def get_object(self):
        # Retrieve the Anleitung object using pk1
        anleitung = get_object_or_404(Anleitung, pk=self.kwargs['pk1'])

        # Retrieve the Anleitungsschritt object using pk2
        anleitungsschritt = get_object_or_404(Anleitungsschritt, pk=self.kwargs['pk2'])

        # Attach the Anleitungsschritt object to the Anleitung object
        anleitung.anleitungsschritt = anleitungsschritt

        # Retrieve the corresponding Komponente object
        komponenten = Komponente.objects.filter(anleitungsschritt=anleitungsschritt).first()

        return anleitung
    
    model = Anleitung
    template_name = 'Anleitung_durchgehen.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        anleitung = self.kwargs['pk1']
        anleitungsschritt = self.kwargs['pk2']

        context['anleitungsbezeichnungen'] = self.object.anleitungsbezeichnungen.filter(pk = self.kwargs['pk2']).values('schrittbenennung', 'beschreibung')
        context['anleitungsschritt'] = anleitungsschritt

        komponente = Komponente.objects.filter(anleitungsschritt__anleitung = anleitung)
        context['komponente'] = komponente

        next_komponente = Komponente.objects.filter(anleitungsschritt__anleitung = anleitung, pk__gt = komponente.first().pk).first()
        context['next_komponente'] = next_komponente        
        
        return context

# def anleitung_durchgehen(request):

#     schritt1 = schrittinhalte[0].schrittbenennung
#     schritt1beschreibung = schrittinhalte[0].beschreibung
#     komp0 = Komponenten.objects.get(pk=2)
#     komp1 = Komponenten.objects.get(pk=3)

#     return render(request, 'Anleitung_durchgehen.html',
#     {'anleitungstitel': anleitungstitel,
#     'schritt1': schritt1,
#     'schritt1beschreibung': schritt1beschreibung,
#     'komp0': komp0,
#     'komp1': komp1})

# def anleitung_durchgehen2(request):

#     schritt2 = schrittinhalte[1].schrittbenennung
#     schritt2beschreibung = schrittinhalte[1].beschreibung
#     komp0 = Komponenten.objects.get(pk=4)
#     komp1 = Komponenten.objects.get(pk=5)
    
#     return render(request, 'Anleitung_durchgehen2.html',
#     {'anleitungstitel': anleitungstitel,
#     'schritt2': schritt2,
#     'schritt2beschreibung': schritt2beschreibung,
#     'komp0': komp0,
#     'komp1': komp1})
    
# def anleitung_durchgehen3(request):

#     schritt3 = schrittinhalte[2].schrittbenennung
#     schritt3beschreibung = schrittinhalte[2].beschreibung
#     komp0 = Komponenten.objects.get(pk = 6)
#     komp1 = Komponenten.objects.get(pk=7)
#     komp2 = Komponenten.objects.get(pk=8)

#     return render(request, 'Anleitung_durchgehen3.html',
#     {'anleitungstitel': anleitungstitel,
#     'schritt3': schritt3,
#     'schritt3beschreibung': schritt3beschreibung,
#     'komp0': komp0,
#     'komp1': komp1,
#     'komp2': komp2})

# def anleitung_durchgehen4(request):

#     schritt4 = schrittinhalte[3].schrittbenennung
#     schritt4beschreibung = schrittinhalte[4].beschreibung
#     komp0 = Komponenten.objects.get(pk =9)
#     komp1 = Komponenten.objects.get(pk = 10)

#     return render(request, 'Anleitung_durchgehen4.html',
#     {'anleitungstitel': anleitungstitel,
#     'schritt4': schritt4,
#     'schritt4beschreibung': schritt4beschreibung,
#     'komp0': komp0,
#     'komp1': komp1})

# def anleitung_durchgehen5(request):

#     schritt5 = schrittinhalte[4].schrittbenennung
#     schritt5beschreibung = schrittinhalte[4].beschreibung
#     komp0 =Komponenten.objects.get(pk = 11)

#     return render(request, 'Anleitung_durchgehen5.html',
#     {'anleitungstitel': anleitungstitel,
#     'schritt5': schritt5,
#     'schritt5beschreibung': schritt5beschreibung,
#     'komp0': komp0})

# def anleitung_durchgehen6(request):

#     schritt6 = schrittinhalte[5].schrittbenennung
#     schritt6beschreibung = schrittinhalte[5].beschreibung
#     komp0 = Komponenten.objects.get(pk = 12)
#     komp1 = Komponenten.objects.get(pk = 13)

#     return render(request, 'Anleitung_durchgehen6.html',
#     {'anleitungstitel': anleitungstitel,
#     'schritt6': schritt6,
#     'schritt6beschreibung': schritt6beschreibung,
#     'komp0': komp0,
#     'komp1': komp1})

# def anleitung_beendet(request):
#     return render(request, 'Anleitung_beendet.html')


# Profil

def profil(request):
    return render(request, 'Mein_Profil.html')

def meine_anleitungen(request):
    return render(request, 'Meine_Anleitungen.html')