from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class consoles(models.Model):
    name = models.CharField( max_length=50)
    
    def __str__(self):
        return self.name

class Tournament(models.Model):
    tournament_pic = models.ImageField(upload_to='quest_pics/',blank=True)
    name = models.CharField(max_length=50)
    details = models.CharField( max_length=100)
    owner = models.CharField( max_length=50, default=None)
    # location
    slots_available = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    cash_prize = models.IntegerField(default=0)
    ranking =models.IntegerField(default=0)
    consoles = models.ManyToManyField(consoles)  
    ticket_prize = models.IntegerField(default=0)


    def save_tournament(self):
        self.save()

    def delete_tournament(self):
        self.delete()

    @classmethod
    def fetch_all_tournaments(cls):
        all_quest = Tournament.objects.all()
        return all_quest

    @classmethod
    def search_tournament_by_title(cls,search_term):
        tournament = cls.objects.filter(title__icontains=search_term)
        return tournament

    @classmethod
    def get_single_tournament(cls, project):
        tournament = cls.objects.get(id=project)
        return tournament
    
    def __str__(self):
        return self.name

class Profile(models.Model):
    profile_picture = models.ImageField(upload_to='prof_pics/',blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    contact_info = models.CharField(max_length=200,blank=True)
    games_played =models.CharField( max_length=50)
    consoles = models.ManyToManyField(consoles)  
    contact_info = models.CharField(max_length=13,blank=True)
    all_Tournaments = models.ForeignKey('Tournament',on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_bio(self,bio):
        self.bio = bio
        self.save()

