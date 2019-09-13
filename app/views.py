from django.shortcuts import render, redirect
from rest_framework.views import APIView
from .models import *
from .serializer import TournamentSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.

def landing(request):
    quest = Tournament.fetch_all_tournaments()
    return render(request, "app/landing.html", {'quest': quest})

@login_required(login_url='/accounts/login/')
def index(request):
    quest = Tournament.fetch_all_tournaments()
    return render(request, "app/index.html",{'quest': quest})

# @login_required(login_url='/accounts/login/')
def leaderboard(request):
    return render(request, "app/leaderboard.html")

def new_tournament(request):
    current_user = request.user
    if request.method == 'POST':
        form = TournamentForm(request.POST,request.FILES)
        if form.is_valid():
            tournament = form.save(commit=False)
            tournament.user = current_user
            tournament.save()
        return redirect('index')
    else:
        form = TournamentForm()
    return render(request,"app/new_tournament.html",{"form":form})
# @login_required(login_url='/accounts/login/')
def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.prof_user = current_user
            profile.profile_Id = request.user.id
            profile.save()
        return redirect('profile')
    else:
        form = ProfileForm()
    return render(request, 'profile/new_profile.html', {"form": form})

# @login_required(login_url='/accounts/login/')
def profile_edit(request):
    current_user = request.user
    if request.method == 'POST':
        logged_user = Profile.objects.get(prof_user=request.user)
        form = ProfileForm(request.POST, request.FILES, instance=logged_user)
        if form.is_valid():
            form.save()
        return redirect('profile')
    else:
        form = ProfileForm()
    return render(request,'profile/edit_profile.html',{'form':form})

# @login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    quests = Tournament.objects.filter(user = current_user)

    try:   
        prof = Profile.objects.get(prof_user=current_user)
    except ObjectDoesNotExist:
        return redirect('new_profile')

    return render(request,'profile/profile.html',{'profile':prof})

class TournamentList(APIView):
     def get(self, request, format=None):
        all_quest = Tournament.objects.all()
        serializers = TournamentSerializer(all_quest, many=True)
        return Response(serializers.data)
    
     def post(self, request, format=None):
        serializers = TournamentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class TournamentDescription(APIView):
    def get_quest(self,pk):
        try:
            return Tournament.objects.get(pk=pk)
        except Tournament.DoesNotExist:
            return Http404
    
    def get(self, request, pk, format=None):
        quest = self.get_quest(pk)
        serializers = TournamentSerializer(quest)
        return Response(serializers.data)