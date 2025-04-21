from django.shortcuts import redirect, render
from markdown2 import Markdown
from . import util
import random

markdowner = Markdown()

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def add_entry(request):
    if request.method =="POST":
        title = request.POST['title']
        content = request.POST['content']
        if util.get_entry(title):
            # Handle the case where the entry altready exists
            return render(request, "encyclopedia/error.html", {
                "message": "Entry already exists"
            })
        else:
            util.save_entry(title, content)
            return redirect("entry", title=title)
        return render(request, "encyclopedia/add_entry.html")
    
def search(request):
    query = request.GET.get("q")
    if query:
        entry = util.get_entry(query)
        if entry:
            return redirect("entry", title=query)
        else:
            # Checks for lower and upper case
            entries = [e for e in util.list_entries() if query.lower() in e.lower()]
            return render(request, "encyclopedia/search_results.html", {
                "entries": entries,
                "query": query
            })
    return redirect("index")

def entry(request, title):
    entry = util.get_entry(title)
    if entry:
        html_content = markdowner.convert(entry)
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": entry
        })
    else:
        return render(request, "encyclopedia/error.html", {
            "message": "Entry not found"
        })
        
def save_entry(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        if util.get_entry(title) is not None:
            return render(request, "encyclopedia/add_entry.html", {
                "error": "An entry with this title already exists."
            })
        util.save_entry(title, content)
        return redirect("index")
    else:
        return render(request, "encyclopedia/add_entry.html")
        
def random_page(request):
    entries = util.list_entries()
    random_entry = random.choice(entries)
    return redirect("entry", title=random_entry)
    
def edit_entry(request,title ):
    content = util.get_entry(title)
    if content is None:
        return render(request, "encyclopedia/edit_entry.html", {
            "title": title,
            "error": "Entry not found."
        })
    return render (request, "encyclopedia/edit_entry.html", {
        "title": title,
        "content": content
    })
    
def save_edit(request, title):
    if request.method == "POST":
        content = request.POST['content']
        util.save_entry(title, content)
        return redirect("entry", title=title)
    