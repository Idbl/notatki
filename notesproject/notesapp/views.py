from django.shortcuts import render, redirect

from .forms import NoteForm
from .models import Note


# Create your views here.

def notesTable(request):
    notes = Note.objects.all()
    return render(request, "notes-table.html", {'notes': notes})


def notesCreate(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('notes-table')
            except:
                pass
    else:
        form = NoteForm()
    return render(request, 'notes-create.html', {'form': form})


def notesUpdate(request, id):
    note = Note.objects.get(id=id)
    form = NoteForm(initial={'title': note.title, 'content': note.content, 'creation_date': note.creation_date,
                             'author': note.author})
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        try:
            if form.is_valid():
                form.save()
                model = form.instance
                return redirect('/notes-table')
        except Exception as e:
            pass
    return render(request, 'notes-update.html', {'form': form})


def notesDelete(request, id):
    note = Note.objects.get(id=id)
    try:
        note.delete()
    except:
        pass
    return redirect('/notes-table')