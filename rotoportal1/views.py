from pdb import post_mortem
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Item, Pkmn, Tag, Party
from .forms import PartyForm
from django.db.models import Q
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

#今のシーズン
seasonnow=27
gamenow="SwSh"

def index(request):
    data = Party.objects.filter(partycheck=True,rank__gte=4,rank__lte=10, game=gamenow, season=seasonnow)
    data= data.order_by('rank')
    topdata = Party.objects.filter(partycheck=True,rank__lte=3, game=gamenow, season=seasonnow)
    topdata= topdata.order_by('rank')
    params = {"toppartydata" : topdata, "partydata":data}
    return render(request, 'home.html', params)

def form(request):
    return render(request, 'form.html')

def howto(request):
    return render(request, 'howto.html')

def privacy(request):
    return render(request, 'privacy.html')

def results(request):
    data = Party.objects.filter(partycheck=True)
    data=data.order_by("-partyid")
    pkmnq = request.GET.get("pkmnq")
    itemq = request.GET.get("itemq")
    tagq = request.GET.get("tagq")
    ruleq = request.GET.get("ruleq")
    gameq = request.GET.get("gameq")
    seasonstartq = request.GET.get("seasonstartq")
    seasonendq = request.GET.get("seasonendq")
    rankq = request.GET.get("rankq")
    if pkmnq and itemq and tagq:
        data = data.filter(
        Q(pkmn1__name__iexact=pkmnq, item1__name__iexact=itemq, tag1__name_iexact=tagq) |
        Q(pkmn2__name__iexact=pkmnq, item2__name__iexact=itemq, tag2__name_iexact=tagq) |
        Q(pkmn3__name__iexact=pkmnq, item3__name__iexact=itemq, tag3__name_iexact=tagq) |
        Q(pkmn4__name__iexact=pkmnq, item4__name__iexact=itemq, tag4__name_iexact=tagq) |
        Q(pkmn5__name__iexact=pkmnq, item5__name__iexact=itemq, tag5__name_iexact=tagq) |
        Q(pkmn6__name__iexact=pkmnq, item6__name__iexact=itemq, tag6__name_iexact=tagq)  )

    elif pkmnq and itemq:
        data = data.filter(
        Q(pkmn1__name__iexact=pkmnq, item1__name__iexact=itemq,) |
        Q(pkmn2__name__iexact=pkmnq, item2__name__iexact=itemq,) |
        Q(pkmn3__name__iexact=pkmnq, item3__name__iexact=itemq,) |
        Q(pkmn4__name__iexact=pkmnq, item4__name__iexact=itemq,) |
        Q(pkmn5__name__iexact=pkmnq, item5__name__iexact=itemq,) |
        Q(pkmn6__name__iexact=pkmnq, item6__name__iexact=itemq,)  )

    elif pkmnq and tagq:
        data = data.filter(
        Q(pkmn1__name__iexact=pkmnq, tag1__name_iexact=tagq) |
        Q(pkmn2__name__iexact=pkmnq, tag2__name_iexact=tagq) |
        Q(pkmn3__name__iexact=pkmnq, tag3__name_iexact=tagq) |
        Q(pkmn4__name__iexact=pkmnq, tag4__name_iexact=tagq) |
        Q(pkmn5__name__iexact=pkmnq, tag5__name_iexact=tagq) |
        Q(pkmn6__name__iexact=pkmnq, tag6__name_iexact=tagq)  )

    elif itemq and tagq:
        data = data.filter(
        Q(item1__name__iexact=itemq, tag1__name_iexact=tagq) |
        Q(item2__name__iexact=itemq, tag2__name_iexact=tagq) |
        Q(item3__name__iexact=itemq, tag3__name_iexact=tagq) |
        Q(item4__name__iexact=itemq, tag4__name_iexact=tagq) |
        Q(item5__name__iexact=itemq, tag5__name_iexact=tagq) |
        Q(item6__name__iexact=itemq, tag6__name_iexact=tagq)  )

    elif pkmnq:
        data = data.filter(
        Q(pkmn1__name__iexact=pkmnq) |
        Q(pkmn2__name__iexact=pkmnq) |
        Q(pkmn3__name__iexact=pkmnq) |
        Q(pkmn4__name__iexact=pkmnq) |
        Q(pkmn5__name__iexact=pkmnq) |
        Q(pkmn6__name__iexact=pkmnq)  )
        
    elif itemq:
        data = data.filter(
        Q(item1__name__iexact=itemq) |
        Q(item2__name__iexact=itemq) |
        Q(item3__name__iexact=itemq) |
        Q(item4__name__iexact=itemq) |
        Q(item5__name__iexact=itemq) |
        Q(item6__name__iexact=itemq)  )

    elif tagq:
        data = data.filter(
        Q(tag1__name__iexact=tagq) |
        Q(tag2__name__iexact=tagq) |
        Q(tag3__name__iexact=tagq) |
        Q(tag4__name__iexact=tagq) |
        Q(tag5__name__iexact=tagq) |
        Q(tag6__name__iexact=tagq)  )

    if ruleq:
        data = data.filter(rule=ruleq)
    
    if gameq:
        data = data.filter(game=gameq)

    if seasonstartq and seasonendq:
        data = data.filter(season__range=(seasonstartq, seasonendq))
    
    elif seasonstartq:
        data = data.filter(season__range=(seasonstartq, 10000))

    elif seasonendq:
        data = data.filter(season__range=(800, seasonendq))

    if rankq == "1000":
        data = data.filter(rank__lte=1000)

    if rankq == "100":
        data = data.filter(rank__lte=100)
    

    params = {"partydata" : data,}
    
    return render(request, "results.html", params)

def rankgeneral(request):
   
    seasonq = request.GET.get("seasonselect")
    gameq = request.GET.get("gameq")
    if seasonq and gameq:
        data = Party.objects.filter(partycheck=True, rank__lte=100)
        data = data.order_by("rank")
        data = data.filter(game=gameq, season=seasonq)
    else:
        data = Party.objects.filter(rank=1)
        data = data.order_by("-season")
    params = {"partydata" : data,}
    return render(request, 'rankgeneral.html', params)

# パーティ登録フォーム
def party_form(request):
    if request.method == "POST":
        form =PartyForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PartyForm()
    return render(request, "form.html",{"form":form})

class PartyList(ListView):
    model = Party
    pagenate_by = 10



