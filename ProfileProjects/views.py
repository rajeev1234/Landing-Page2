# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create ProfileProjects Here

class ProfileProjectsCreateView(LoginRequiredMixin, CreateView):
    model = models.ProfileProjects
    template_name = 'ProfileProjects/ProfileProjects_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = ['ProfileProjects_Category',
    'ProfileProjects_Director',
    'ProfileProjects_Production_House',
    'ProfileProjects_Title']

    # Set fields from current data or automated data
    #
    def form_valid(self, form):
        form.instance.ProfileProjects_Author = self.request.user
        return super().form_valid(form)

# ProfileProjects Details Here


class ProfileProjectsDetailView(LoginRequiredMixin, DetailView):
    model = models.ProfileProjects
    context_object_name = 'ProfileProjects'
    template_name = 'ProfileProjects/ProfileProjects_details.html'
    login_url = 'login'

# ProfileProjects ListView Here


class ProfileProjectsListView(ListView):
    model = models.ProfileProjects
    template_name = 'ProfileProjects/ProfileProjects_list.html'
    login_url = 'login'

# ProfileProjects Update Here


class ProfileProjectsUpdateView(LoginRequiredMixin, UpdateView):
    model = models.ProfileProjects

    # Decide fields for editing Here

    fields = ['ProfileProjects_Category',
                    'ProfileProjects_Director',
                    'ProfileProjects_Production_House',
                    'ProfileProjects_Title']
                    
    template_name = 'ProfileProjects/ProfileProjects_update.html'
    login_url = 'login'

# ProfileProjects Delete here


class ProfileProjectsDeleteView(LoginRequiredMixin, DeleteView):
    model = models.ProfileProjects
    template_name = 'ProfileProjects/ProfileProjects_delete.html'
    success_url = reverse_lazy('ProfileProjects_list')
    login_url = 'login'



