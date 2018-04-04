from django.db import models

from django.conf import settings

from django.urls import reverse

# Create your theater_actors here.


class theater_actor(models.Model):
    Body_Type = models.CharField(max_length=200)
    # Comments = models.ForeignKey(List_Of_Comments, on_delete=models.CASCADE)
    Daily_Charges = models.IntegerField(default=0)
    Description = models.CharField(max_length=200)
    Ethnicity = models.CharField(max_length=200)
    Favorite_Acting_Style = models.CharField(max_length=200)
    Financial_Available = models.BooleanField(default=False)
    Height = models.IntegerField(default=0)
    # Language = models.ForeignKey(List_Of_Texts, on_delete=models.CASCADE)
    # Portfolio = models.ForeignKey(List_Of_Portfolio_Elements, on_delete=models.CASCADE)
    # Ratings = models.ForeignKey(List_of_Ratings, on_delete=models.CASCADE)
    Skin_Color = models.CharField(max_length=200)
    Special_Skills = models.CharField(max_length=200)
    Theater_Actor_ID = models.IntegerField(default=0)
    # Video = models.ForeignKey(List_Of_Files, on_delete=models.CASCADE)
    Weight = models.IntegerField(default=0)

    theater_actor_Message = models.CharField(max_length=280)
    theater_actor_Author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Created_Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.theater_actor_Message

    def get_absolute_url(self):
        return reverse('theater_actor_details', args=[str(self.id)])


# Create theater_actors Comments here.


class Comment(models.Model):

    theater_actor_Comment = models.CharField(max_length=150, null=False)
    # Comment_theater_actor = models.ForeignKey(theater_actor, null=False, on_delete=models.CASCADE)
    theater_actor_Comment_Author = models.ForeignKey(theater_actor, on_delete=models.CASCADE)

    # theater_actor_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.theater_actor_Comment

    def get_absolute_url(self):
        return reverse('theater_actor_list')
