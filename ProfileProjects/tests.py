from django.test import TestCase,SimpleTestCase
from django.urls import reverse,reverse_lazy
from .models import ProfileProjects
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.forms.models import model_to_dict


#  Test Class for ProfileProjects Application

class ProfileProjectsTest(TestCase):

########################## Model Testing ############################
  

    # ProfileProjects object with dummy data 
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password = 'test'
        )

        self.ProfileProjects =  ProfileProjects.objects.create(

        # Fields according to defined in Model    
        ProfileProjects_Category='ProfileProjects_Category',
        ProfileProjects_Director='ProfileProjects_Director',
        ProfileProjects_Production_House='ProfileProjects_Production_House',
        ProfileProjects_Title ='ProfileProjects_Title',
        ProfileProjects_Author = self.user,
        )

#-----------------------------------------------------------------------------------------#

    # Check redirection URL
    def test_get_absolute_url(self):
        # Redirection goes to ProfileProjects details
        self.assertEquals(self.ProfileProjects.get_absolute_url(), '/profileprojects/1')

#-----------------------------------------------------------------------------------------#

    # Check Conent of ProfileProjects object created by create object query set
    def test_ProfileProjects_content(self):
        # Verify for each field  
        self.assertEqual(f'{self.ProfileProjects.ProfileProjects_Category}', 'ProfileProjects_Category')
        self.assertEqual(f'{self.ProfileProjects.ProfileProjects_Director}', 'ProfileProjects_Director')
        self.assertEqual(f'{self.ProfileProjects.ProfileProjects_Production_House}', 'ProfileProjects_Production_House')
        self.assertEqual(f'{self.ProfileProjects.ProfileProjects_Title}', 'ProfileProjects_Title')
#--------------------------------------------------------------------------------------------#

# #############################   Model Test End   ###########################################







# ###############################    Views Test       ########################################

    
    # Test ProfileProjects List View
    
    def test_ProfileProjectsList_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Get respomse from defined URL namespace
        response = self.client.get(reverse('ProfileProjects_list'))
        self.assertEqual(response.status_code, 200)

        # Check Content of List View
        self.assertContains(response,self.user.username)
        self.assertContains(response,'ProfileProjects_Title')

        # Check for Correct template used in template/ProfileProjectss
        self.assertTemplateUsed(response, 'ProfileProjects/ProfileProjects_list.html')

#--------------------------------------------------------------------------------------------#
    

    # Test ProfileProjects Detail View

    def test_ProfileProjectsDetail_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        ProfileProjects_pk = ProfileProjects.objects.get(ProfileProjects_Title='ProfileProjects_Title').pk
        
        # Get response
        response = self.client.get(reverse_lazy('ProfileProjects_details',kwargs={'pk':ProfileProjects_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('ProfileProjects_details',kwargs={'pk':10000}))

        # 202 for valid and 404 for invalid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

        # check for content of Detail Page


        # Check for Correct template used in template/ProfileProjectss
        self.assertTemplateUsed(response, 'ProfileProjects/ProfileProjects_details.html')

#-------------------------------------------------------------------------------------------#    


    # Test ProfileProjects Create View
    
    def test_ProfileProjectsCreate_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test') 

        # Generate response after creating an view using Http post method
        '''
        If we send json file in post request to ProfileProjects_new.html then it gets 
        302 in response code, so instead checking the response of form we can check the
        response of ultimate page where data goes when form button is submitted i.e. on
        details page. If details page gives correct response content after submitting the
        form then it will return 200.
        So we have added follow = True here which sends the JSON data through form to 
        details page.
        So two modification here :
        1. Follow = True
        2. Template used will be of .._details.html page not .._new.html

        '''
        response = self.client.post('/profileprojects/new/', {
        'ProfileProjects_Category':'ProfileProjects_Category',
        'ProfileProjects_Director':'ProfileProjects_Director',
        'ProfileProjects_Production_House':'ProfileProjects_Production_House',
        'ProfileProjects_Title' : 'ProfileProjects_Title',
        'ProfileProjects_Author' : self.user
        },follow = True)
        
        # Check for successful response
        self.assertEqual(response.status_code, 200)

        # Check response values
        self.assertContains(response, 'ProfileProjects_Category')
        self.assertContains(response, 'ProfileProjects_Director')
        self.assertContains(response, 'ProfileProjects_Production_House')
        self.assertContains(response, 'ProfileProjects_Title')

        # Check for correct template used in template/ProfileProjectss
        self.assertTemplateUsed(response, 'ProfileProjects/ProfileProjects_details.html')

#---------------------------------------------------------------------------------------#


    # Test ProfileProjects Update view 

    def test_ProfileProjectsupdate_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        ProfileProjects_pk = ProfileProjects.objects.get(ProfileProjects_Title='ProfileProjects_Title').pk
        
        # Get response using pk on details view
        response = self.client.get(reverse_lazy('ProfileProjects_details',kwargs={'pk':ProfileProjects_pk}), {
        'ProfileProjects_Category':'ProfileProjects_Category',
        'ProfileProjects_Director':'ProfileProjects_Director',
        'ProfileProjects_Production_House':'ProfileProjects_Production_House',
        'ProfileProjects_Title' : 'ProfileProjects_Title',
        'ProfileProjects_Author' : self.user
        })
        # Check for successful response
        self.assertEqual(response.status_code, 200)

        # Check for correct templates
        self.assertTemplateUsed(response,'ProfileProjects/ProfileProjects_details.html')


#--------------------------------------------------------------------------------------------#


# Test Delete View of ProfileProjects views

    def test_ProfileProjectsdelete_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        ProfileProjects_pk = ProfileProjects.objects.get(ProfileProjects_Title='ProfileProjects_Title').pk
        
        # Get response to delete 

        response = self.client.get(reverse_lazy('ProfileProjects_delete',kwargs={'pk':ProfileProjects_pk}))
        self.assertContains(response, 'Are you sure you want to delete') # THIS PART WORKS

        # Check deleted value , returns false i.e.302
        post_response = self.client.post(reverse_lazy('ProfileProjects_delete',kwargs={'pk':ProfileProjects_pk}))
        
        # self.assertRedirects(post_response, reverse_lazy('ProfileProjects_delete',kwargs={'pk':ProfileProjects_pk}), status_code=302)


        self.assertEqual(response.status_code, 200)

        # check for Correct Template Used
        self.assertTemplateUsed(response, 'ProfileProjects/ProfileProjects_delete.html')




# ################################     View Testing End   #################################################



# ################################     Testing the URLs       ##############################################

class PagesTests(SimpleTestCase):

    # Check URL for list/ Home
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

# #-----------------------------------------------------------------------------------------------------#

#     # URL for new
#     def test_new_page_status_code(self):
#         # Login the user defined in SetUp
#         # self.client.login(username='testuser', password='test')
        
#         # Get response
#         response = self.client.get('/ProfileProjectss/1/')

#         self.assertEqual(response.status_code, 200)


#------------------------------------------------------------------------------------------------------#
    
        
#     # def test_update_page_status_code(self):
#     #     # url = reverse('ProfileProjectsListView')
#     #     response = self.client.get('/ProfileProjectss/1/')
#     #     self.assertEqual(response.status_code, 200)

#-------------------------------------------------------------------------------------------------------#

#     # def test_detail_page_status_code(self):
#     #     response = self.client.get('/{1}/')
#     #     self.assertEqual(response.status_code, 200)

#-------------------------------------------------------------------------------------------------------#

#     # def test_delete_page_status_code(self):
#     #     response = self.client.get('/{1}/delete/')
#     #     self.assertEqual(response.status_code, 200)