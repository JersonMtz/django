from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from Apps.Registration.models import Profile
from django.shortcuts import get_object_or_404
# Create your views here.

class ProfilesListView(ListView):
    model = Profile
    paginate_by = 6
    template_name = 'Profiles/profile_list.html'

class ProfilesDetailView(DetailView):
    model = Profile
    template_name = 'Profiles/profile_detail.html'

    def get_object(self):
        return get_object_or_404(Profile, user__username=self.kwargs['username'])