from django.contrib import admin

# Register your models here.
from .models import Item, Pkmn, Tag, Party

# admin.site.register(Item)
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    ordering = ("name",)
    pass

@admin.register(Pkmn)
class PkmnAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    ordering = ("name",)
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    ordering = ("name",)
    pass

@admin.register(Party)
class PartyAdmin(admin.ModelAdmin):
    list_filter = ["partycheck"]
    autocomplete_fields = ("pkmn1","item1","tag1","pkmn2","item2","tag2","pkmn3","item3","tag3","pkmn4","item4","tag4","pkmn5","item5","tag5","pkmn6","item6","tag6")
    pass

