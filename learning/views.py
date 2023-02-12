from django.shortcuts import render

from .models import Topic, Entry

# Create your views here.
def index(request):
    topics = Topic.objects.all()
    context = {'topics': topics}
    return render(request, 'learning/index.html', context)

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'entries': entries, 'topic': topic}
    return render(request, 'learning/entries.html', context)

def entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    entry_next = entry.id + 1
    entry_last = entry.id - 1
    id_last = Entry.objects.last().id
    id_first = Entry.objects.first().id
    context = {'entry': entry, 'entry_next': entry_next, 'entry_last': entry_last, 'id_last': id_last, 'id_first': id_first}
    return render(request, 'learning/entry.html', context)