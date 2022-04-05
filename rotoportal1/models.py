from email.policy import default
from unicodedata import name
from django.db import models
from django.db.models import Q
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=20, help_text="持ち物名を入力")
    img = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, default="")
    def __str__(self):
        return self.name
    class Meta:
        ordering = ["name"]

class Pkmn(models.Model):
    img = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, default="")
    name = models.CharField(max_length=20, help_text="ポケモン名を入力")
    bigimg = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, default="", null=True, blank=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ["name"]


class Tag(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    class Meta:
        ordering = ["name"]


class Party(models.Model):
    SEASONS = [("","全て"),("8S17","剣盾S17"),("8S16","剣盾S16"),("8S15","剣盾S15")]
    RULES = [("single","シングル"), ("double", "ダブル")]
    GAMES = [("SwSh","剣盾"),("SV","スカバイ")]

    partyid = models.AutoField(primary_key=True)

    username = models.CharField(max_length=20, help_text="著者名を入力", default="")

    twitterid = models.CharField(max_length = 100, null=True, blank=True, help_text='TwitterIDを、"@"を含めた形で入力')
    
    articletitle = models.CharField(max_length=50, help_text="記事のタイトルを入力", default="")

    pkmn1 = models.ForeignKey(Pkmn,on_delete=models.CASCADE, related_name="party_pkmn1", default="")

    item1 = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="party_item1", default="")

    tag1 = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name="party_tag1", default="", null=True, blank=True)

    pkmn2 = models.ForeignKey(Pkmn,on_delete=models.CASCADE, related_name="party_pkmn2", default="")

    item2 = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="party_item2", default="")

    tag2 = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name="party_tag2", default="", null=True, blank=True)

    pkmn3 = models.ForeignKey(Pkmn,on_delete=models.CASCADE, related_name="party_pkmn3", default="")

    item3 = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="party_item3", default="")

    tag3 = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name="party_tag3", default="", null=True, blank=True)

    pkmn4 = models.ForeignKey(Pkmn,on_delete=models.CASCADE, related_name="party_pkmn4", default="")

    item4 = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="party_item4", default="")

    tag4 = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name="party_tag4", default="", null=True, blank=True)

    pkmn5 = models.ForeignKey(Pkmn,on_delete=models.CASCADE, related_name="party_pkmn5", default="")

    item5 = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="party_item5", default="")

    tag5 = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name="party_tag5", default="", null=True, blank=True)

    pkmn6 = models.ForeignKey(Pkmn,on_delete=models.CASCADE, related_name="party_pkmn6", default="")

    item6 = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="party_item6", default="")

    tag6 = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name="party_tag6", default="", null=True, blank=True)

    season = models.IntegerField(default="", null=True,validators=[MinValueValidator(0), MaxValueValidator(100)])

    rank = models.IntegerField(null=True, blank=True)

    rating = models.IntegerField(null=True, blank=True)

    rule = models.CharField(max_length= 10, choices= RULES)

    game = models.CharField(max_length = 10, choices = GAMES)

    url = models.URLField(max_length=1000, default="")
    
    partycheck = models.BooleanField(default=False)

    def __str__(self):
        return self.articletitle
    


