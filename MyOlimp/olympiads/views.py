from django.shortcuts import render
from django.db.models import Q
from django.views import generic
from .models import Olympiad
from django.views.generic.edit import CreateView, UpdateView
from .forms import OlympiadSearchForm


class OlympiadListView(generic.ListView):
    model = Olympiad


class OlympiadDetailView(generic.DetailView):
    model = Olympiad


class OlympiadCreateView(CreateView):
    model = Olympiad
    fields = ['name',
              'subject',
              'olympiad_level',
              'olympiad_extramural_start',
              'olympiad_extramural_end',
              'olympiad_intramural_start',
              'olympiad_intramural_end',
              'olympiad_file']
    template_name_suffix = '_create_form'


class OlympiadEditView(UpdateView):
    model = Olympiad
    fields = ['name',
              'subject',
              'olympiad_level',
              'olympiad_extramural_start',
              'olympiad_extramural_end',
              'olympiad_intramural_start',
              'olympiad_intramural_end',
              'olympiad_file',
              'winner',
              'participants']
    template_name_suffix = '_update_form'


class SearchResultsView(generic.ListView):
    model = Olympiad
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Olympiad.objects.filter(
            Q(name__icontains=query) | Q(olympiad_level__icontains=query)
        )
        return object_list
