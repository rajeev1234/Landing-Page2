# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create VoiceOverArtist Here

class VoiceOverArtistCreateView(LoginRequiredMixin, CreateView):
    model = models.VoiceOverArtist
    template_name = 'VoiceOverArtist/VoiceOverArtist_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = ['VoiceOverArtist_Charges_Available',
              'VoiceOverArtist_Daily_charges',
              'VoiceOverArtist_Description',
              'VoiceOverArtist_Language',
              'VoiceOverArtist_Voice_Scale',
              'VoiceOverArtist_Author',
              ]

    # Set fields from current data or automated data

    def form_valid(self, form):
        form.instance.VoiceOverArtist_Author = self.request.user
        return super().form_valid(form)

# VoiceOverArtist Details Here


class VoiceOverArtistDetailView(LoginRequiredMixin, DetailView):
    model = models.VoiceOverArtist
    context_object_name = 'VoiceOverArtist'
    template_name = 'VoiceOverArtist/VoiceOverArtist_details.html'
    login_url = 'login'

# VoiceOverArtist ListView Here


class VoiceOverArtistListView(ListView):
    model = models.VoiceOverArtist
    template_name = 'VoiceOverArtist/VoiceOverArtist_list.html'
    login_url = 'login'

# VoiceOverArtist Update Here


class VoiceOverArtistUpdateView(LoginRequiredMixin, UpdateView):
    model = models.VoiceOverArtist

    # Decide fields for editing Here

    fields = ['VoiceOverArtist_Charges_Available',
              'VoiceOverArtist_Daily_charges',
              'VoiceOverArtist_Description',
              'VoiceOverArtist_Language',
              'VoiceOverArtist_Voice_Scale',
              'VoiceOverArtist_Author',
              ]
    template_name = 'VoiceOverArtist/VoiceOverArtist_update.html'
    login_url = 'login'

# VoiceOverArtist Delete here


class VoiceOverArtistDeleteView(LoginRequiredMixin, DeleteView):
    model = models.VoiceOverArtist
    template_name = 'VoiceOverArtist/VoiceOverArtist_delete.html'
    success_url = reverse_lazy('VoiceOverArtist_list')
    login_url = 'login'



