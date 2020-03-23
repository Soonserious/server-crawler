from django.shortcuts import render

# Create your views here.
from .models import *
from .forms import *

def start_search(request):
    if request.Method == 'get':
        return render(request, template_name="templates/search/searchmain.html",
                      context={'searchForm': SearchForm(), }
                      )
    else:
        searchForm = SearchForm(request.POST)
        if searchForm.is_valid():
            search_engine = searchForm.cleaned_data["search_engine"]
            keyword = searchForm.cleaned_data["keyword"]

