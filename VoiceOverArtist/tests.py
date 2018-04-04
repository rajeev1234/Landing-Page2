from django.test import TestCase,SimpleTestCase
from django.urls import reverse,reverse_lazy
from .models import VoiceOverArtist
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone


#  Test Class for VoiceOverArtist Application

class VoiceOverArtistTest(TestCase):

########################## Model Testing ####   ########################
  

    # VoiceOverArtist object with dummy data 
    def setUp(self):

        # dummy user for login 
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password = 'test'
        )

        self.VoiceOverArtist =  VoiceOverArtist.objects.create(

        # Fields according to defined in Model    
        VoiceOverArtist_Charges_Available = True,
        VoiceOverArtist_Daily_charges = 1234,
        VoiceOverArtist_Description = 'VoiceOverArtist_Description',
        VoiceOverArtist_Language = 'VoiceOverArtist_Language',
        VoiceOverArtist_Voice_Scale = 'VoiceOverArtist_Voice_Scale',
        VoiceOverArtist_Author = self.user,
        )

#-----------------------------------------------------------------------------------------#

    # Check redirection URL
    def test_get_absolute_url(self):
        # Redirection goes to VoiceOverArtist details
        self.assertEquals(self.VoiceOverArtist.get_absolute_url(), '/voiceoverartist/1')

#-----------------------------------------------------------------------------------------#

    # Check Conent of VoiceOverArtist object created by create object query set
    def test_VoiceOverArtist_content(self):
        # Verify for each field  
        self.assertEqual(int(f'{self.VoiceOverArtist.VoiceOverArtist_Daily_charges}'), 1234)
        self.assertEqual(bool(f'{self.VoiceOverArtist.VoiceOverArtist_Charges_Available}'), True)
        self.assertEqual(f'{self.VoiceOverArtist.VoiceOverArtist_Description}', 'VoiceOverArtist_Description')
        self.assertEqual(f'{self.VoiceOverArtist.VoiceOverArtist_Language}', 'VoiceOverArtist_Language')
        self.assertEqual(f'{self.VoiceOverArtist.VoiceOverArtist_Voice_Scale}', 'VoiceOverArtist_Voice_Scale')
        self.assertEqual(f'{self.VoiceOverArtist.VoiceOverArtist_Author}', self.user.username)
#--------------------------------------------------------------------------------------------#

# #############################   Model Test End   ###########################################







# ###############################    Views Test       ########################################

    
    # Test VoiceOverArtist List View
    
    def test_VoiceOverArtistList_view(self):
    # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Get respomse from defined URL namespace
        response = self.client.get(reverse('VoiceOverArtist_list'))
        self.assertEqual(response.status_code, 200)

        # Check Content of List View
        self.assertContains(response,'VoiceOverArtist_Language')
        self.assertContains(response,'VoiceOverArtist_Description')
        self.assertContains(response,'True')
        self.assertContains(response,1234)
        # Check for Correct template used in template/VoiceOverArtists
        self.assertTemplateUsed(response, 'VoiceOverArtist/VoiceOverArtist_list.html')

#--------------------------------------------------------------------------------------------#
    

    # Test VoiceOverArtist Detail View

    def test_VoiceOverArtistDetail_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        VoiceOverArtist_pk = VoiceOverArtist.objects.get(VoiceOverArtist_Language='VoiceOverArtist_Language').pk
        
        # Get response
        response = self.client.get(reverse_lazy('VoiceOverArtist_details',kwargs={'pk':VoiceOverArtist_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('VoiceOverArtist_details',kwargs={'pk':10000}))

        # 202 for valid and 404 for invalid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

        # check for content of Detail Page
        self.assertContains(response,self.user.username)

        # Check for Correct template used in template/VoiceOverArtists
        self.assertTemplateUsed(response, 'VoiceOverArtist/VoiceOverArtist_details.html')

#-------------------------------------------------------------------------------------------#    


    # Test VoiceOverArtist Create View
    
    def test_VoiceOverArtistCreate_view(self):
        # Login the user defined in SetUps
        self.client.login(username='testuser', password='test') 

        # Generate response after creating an view using Http post method
        response = self.client.post('/voiceoverartist/new/', {
        'VoiceOverArtist_Charges_Available' : True,
        'VoiceOverArtist_Daily_charges' : 1234,
        'VoiceOverArtist_Description' : 'VoiceOverArtist_Description',
        'VoiceOverArtist_Language' : 'VoiceOverArtist_Language',
        'VoiceOverArtist_Voice_Scale' : 'VoiceOverArtist_Voice_Scale',
        'VoiceOverArtist_Author' : self.user,
        })

        # print(response.content)
        # Check for successful response
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'VoiceOverArtist_Description')
        self.assertContains(response, 'VoiceOverArtist_Language')
        self.assertContains(response, 'VoiceOverArtist_Voice_Scale')
        self.assertContains(response, self.user.username)
        self.assertContains(response, 'checked')
        self.assertContains(response, 1234)


        # Check for correct template used in template/VoiceOverArtists
        self.assertTemplateUsed(response, 'VoiceOverArtist/VoiceOverArtist_new.html')

#---------------------------------------------------------------------------------------#


    # Test VoiceOverArtist Update view 

    def test_VoiceOverArtistupdate_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')
        
        # Find primary key of table
        VoiceOverArtist_pk = VoiceOverArtist.objects.get(VoiceOverArtist_Language='VoiceOverArtist_Language').pk
        
        # Get response using pk on details view
        response = self.client.get(reverse_lazy('VoiceOverArtist_details',kwargs={'pk':VoiceOverArtist_pk}), {
        'VoiceOverArtist_Charges_Available' : True,
        'VoiceOverArtist_Daily_charges' : 1234,
        'VoiceOverArtist_Description' : 'VoiceOverArtist_Description',
        'VoiceOverArtist_Language' : 'VoiceOverArtist_Language',
        'VoiceOverArtist_Voice_Scale' : 'VoiceOverArtist_Voice_Scale',
        'VoiceOverArtist_Author' : self.user,
        })
        # Check for successful response
        self.assertEqual(response.status_code, 200)

        # Check for correct templates
        self.assertTemplateUsed(response,'VoiceOverArtist/VoiceOverArtist_details.html')


#--------------------------------------------------------------------------------------------#


# Test Delete View of VoiceOverArtist views

    def test_VoiceOverArtistdelete_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        #Find primary key of table
        VoiceOverArtist_pk = VoiceOverArtist.objects.get(VoiceOverArtist_Daily_charges=1234).pk
        
        # Get response to delete 

        response = self.client.get(reverse_lazy('VoiceOverArtist_delete',kwargs={'pk':VoiceOverArtist_pk}))
        # self.assertContains(response, 'Are you sure you want to delete') # THIS PART WORKS

        # Check deleted value , returns false i.e.302
        post_response = self.client.post(reverse_lazy('VoiceOverArtist_delete',kwargs={'pk':VoiceOverArtist_pk}))
        
        # self.assertRedirects(post_response, reverse_lazy('VoiceOverArtist_delete',kwargs={'pk':VoiceOverArtist_pk}), status_code=302)


        self.assertEqual(response.status_code, 200)

        # check for Correct Template Used
        self.assertTemplateUsed(response, 'VoiceOverArtist/VoiceOverArtist_delete.html')




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
#         response = self.client.get('/VoiceOverArtists/1/')

#         self.assertEqual(response.status_code, 200)


#------------------------------------------------------------------------------------------------------#
    
        
#     # def test_update_page_status_code(self):
#     #     # url = reverse('VoiceOverArtistListView')
#     #     response = self.client.get('/VoiceOverArtists/1/')
#     #     self.assertEqual(response.status_code, 200)

#-------------------------------------------------------------------------------------------------------#

#     # def test_detail_page_status_code(self):
#     #     response = self.client.get('/{1}/')
#     #     self.assertEqual(response.status_code, 200)

#-------------------------------------------------------------------------------------------------------#

#     # def test_delete_page_status_code(self):
#     #     response = self.client.get('/{1}/delete/')
#     #     self.assertEqual(response.status_code, 200)