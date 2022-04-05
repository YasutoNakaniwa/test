from django import forms
from .models import Party, Pkmn
from django.contrib import admin
from django.contrib.admin.widgets import AutocompleteSelect

class PartyForm(forms.ModelForm):
    class Meta:
        model = Party
        fields = ("username","twitterid","articletitle","pkmn1","item1","tag1","pkmn2","item2","tag2","pkmn3","item3","tag3","pkmn4","item4","tag4","pkmn5","item5","tag5","pkmn6","item6","tag6","rank","season","rating","rule","game","url")
        labels ={"username":"ハンドルネーム",
        "twitterid":"@付きTwitterID",
        "articletitle":"記事タイトル",
        "pkmn1":"ポケモン1",
        "item1":"ポケモン1の持ち物",
        "tag1":"わざタグ1",
        "pkmn2":"ポケモン2",
        "item2":"ポケモン2の持ち物",
        "tag2":"わざタグ2",
        "pkmn3":"ポケモン3",
        "item3":"ポケモン3の持ち物",
        "tag3":"わざタグ3",
        "pkmn4":"ポケモン4",
        "item4":"ポケモン4の持ち物",
        "tag4":"わざタグ4",
        "pkmn5":"ポケモン5",
        "item5":"ポケモン5の持ち物",
        "tag5":"わざタグ5",
        "pkmn6":"ポケモン6",
        "item6":"ポケモン6の持ち物",
        "tag6":"わざタグ6",
        "rank":"順位",
        "season":"シーズン",
        "rating":"レート",
        "rule":"ルール",
        "game":"ゲーム",
        "url":"記事URL"}

class SearchForm(forms.Form):
    pksearch = forms.CharField(max_length=10)

    itemsearch = forms.CharField(max_length=20)

    tagsearch = forms.CharField(max_length=20)

