from django.db import models

from django.conf import settings

from django.urls import reverse

# Create your ProfileProjects here.


class ProfileProjects(models.Model):
    ProfileProjects_Category=models.CharField(max_length=200)
    ProfileProjects_Director=models.CharField(max_length=200)
    ProfileProjects_Production_House = models.CharField(max_length=200)
    ProfileProjects_Title = models.CharField(max_length=200)
    ProfileProjects_Author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='ProfileProjects', on_delete=models.CASCADE)
    ProfileProjects_Created_Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('ProfileProjects_details', args=[str(self.id)])


# Create ProfileProjects Comments here.


# Comment 
class Comment(models.Model):

    ProfileProjects_Comment = models.CharField(max_length=150, null=False)
    Comment_ProfileProjects = models.ForeignKey(ProfileProjects,related_name='ProfileProjects_Comment', null=False, on_delete=models.CASCADE)
    ProfileProjects_Comment_Author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'ProfileProjects_Commentss', on_delete=models.CASCADE)
    ProfileProjects_Comment_Created_On = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ProfileProjects_Comment

    def get_absolute_url(self):
        return reverse('ProfileProjects_list')
