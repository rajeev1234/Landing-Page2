# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create theater_actor Here

class theater_actorCreateView(LoginRequiredMixin, CreateView):
    model = models.theater_actor
    template_name = 'theater_actor/theater_actor_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = ['Body_Type','Daily_Charges','Description','Ethnicity','Favorite_Acting_Style','Financial_Available','Height','Skin_Color','Special_Skills','Theater_Actor_ID','Weight','theater_actor_Message']

    # Set fields from current data or automated data
    #
    def form_valid(self, form):
        form.instance.theater_actor_Author = self.request.user
        return super().form_valid(form)

# theater_actor Details Here


class theater_actorDetailView(LoginRequiredMixin, DetailView):
    model = models.theater_actor
    template_name = 'theater_actor/theater_actor_detail.html'
    login_url = 'login'

# theater_actor ListView Here


class theater_actorListView(ListView):
    model = models.theater_actor
    template_name = 'theater_actor/theater_actor_list.html'
    login_url = 'login'

# theater_actor Update Here


class theater_actorUpdateView(LoginRequiredMixin, UpdateView):
    model = models.theater_actor

    # Decide fields for editing Here

    fields = ['Body_Type','Daily_Charges','Description','Ethnicity','Favorite_Acting_Style','Financial_Available','Height','Skin_Color','Special_Skills','Theater_Actor_ID','Weight','theater_actor_Message']
    template_name = 'theater_actor/theater_actor_update.html'
    login_url = 'login'

# theater_actor Delete here


class theater_actorDeleteView(LoginRequiredMixin, DeleteView):
    model = models.theater_actor
    template_name = 'theater_actor/theater_actor_delete.html'
    success_url = reverse_lazy('theater_actor_list')
    login_url = 'login'



