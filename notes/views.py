from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Context, loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from notes.forms import SignUpForm
from notes.models import Notes
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm(request.POST)
    return render(request, 'signup.html', {'form': form})

@login_required
def home(request):
    recent_notes = Notes.objects.filter(user_name = request.user.get_username()).order_by('-id')[:4]
    print(recent_notes)
    for note in recent_notes:
        print(note.title)
        print(note.text)
    return render(request, 'home.html', {"recent_notes":recent_notes,"title":"first"})

@login_required
def new_note(request):
    return render(request, 'new_note.html', {})

@login_required
def create_note(request):
    if request.method == 'POST':
        data = {}
        data.update({'user_name' : request.user})
        data.update({'title' : request.POST.get('title')})
        data.update({'text' : request.POST.get('text')})
        note = Notes()
        note.set_params(data)
        note.save()
        return redirect('/')
    else:
        return HttpResponse({'error':'invalid request'})

@login_required
def manage_all_notes(request):
    all_notes = Notes.objects.filter(user_name = request.user.get_username()).order_by("-id")
    print(all_notes)
    for note in all_notes:
        print(note.id)
    return render(request, 'manage_all_notes.html', {"all_notes":all_notes})

@login_required
def delete(request, id):
    note_to_be_deleted = Notes.objects.get(id=id)
    note_to_be_deleted.delete()
    return redirect('manage_all_notes')

@login_required
def update(request, id):
    if request.method == "POST":
        note_to_be_updated = Notes.objects.get(id = id)
        note_to_be_updated.text = request.POST.get("updated_text")
        note_to_be_updated.save()
        return redirect('manage_all_notes')
    else:
        return HttpResponse({'error':'invalid request'})

def about(request):
    return render(request, 'about_us.html', {})