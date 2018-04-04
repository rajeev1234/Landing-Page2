from django.test import TestCase,SimpleTestCase
from django.urls import reverse,reverse_lazy
from .models import PortfolioElement
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone


#  Test Class for PortfolioElement Application

class PortfolioElementTest(TestCase):

########################## Model Testing ############################


    # PortfolioElement object with dummy data
    def setUp(self):

        # dummy user for login
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password = 'test'
        )

        self.PortfolioElement =  PortfolioElement.objects.create(

        # Fields according to defined in Model
        PortfolioElement_Category = 'PortfolioElement_Category',
        PortfolioElement_Director='PortfolioElement_Director',
        PortfolioElement_Production_House='PortfolioElement_Production_House',
        PortfolioElement_Title='PortfolioElement_Title',
        # PortfolioElement_Creator = 'PortfolioElement_Creator',
        # PortfolioElement_Image = 'PortfolioElement_Image',
        PortfolioElement_Author = self.user,      # Defined above in get_user_model
        PortfolioElement_Created_Date = timezone.now(),
        )

#-----------------------------------------------------------------------------------------#

    # Check redirection URL
    def test_get_absolute_url(self):
        # Redirection goes to PortfolioElement details
        self.assertEquals(self.PortfolioElement.get_absolute_url(), '/portfolio_element/1')

#-----------------------------------------------------------------------------------------#

    # Check Conent of PortfolioElement object created by create object query set
    def test_PortfolioElement_content(self):
        # Verify for each field
        self.assertEqual(f'{self.PortfolioElement.PortfolioElement_Category}', 'PortfolioElement_Category')
        self.assertEqual(f'{self.PortfolioElement.PortfolioElement_Director}', 'PortfolioElement_Director')
        self.assertEqual(f'{self.PortfolioElement.PortfolioElement_Production_House}', 'PortfolioElement_Production_House')
        self.assertEqual(f'{self.PortfolioElement.PortfolioElement_Title}', 'PortfolioElement_Title')
        # self.assertEqual(f'{self.PortfolioElement.PortfolioElement_Creator}', 'PortfolioElement_Creator')
        # self.assertEqual(f'{self.PortfolioElement.PortfolioElement_Image}', 'PortfolioElement_Image')
        self.assertEqual(f'{self.PortfolioElement.PortfolioElement_Author}', self.user.username)   # Defined in SetUp


#--------------------------------------------------------------------------------------------#

# #############################   Model Test End   ########################################### #


# ###############################    Views Test       ########################################


    # Test PortfolioElement List View

    def test_PortfolioElementList_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Get response from defined URL namespace
        response = self.client.get(reverse('portfolio_element_list'))
        self.assertEqual(response.status_code, 200)

        # Check Content of List View
        self.assertContains(response, self.user.username)
        # Check for Correct template used in template/PortfolioElement
        self.assertTemplateUsed(response, 'portfolio_element/portfolio_element_list.html')

#--------------------------------------------------------------------------------------------#

    # Test PortfolioElement Detail View

    def test_PortfolioElementDetail_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        PortfolioElement_pk = PortfolioElement.objects.get(PortfolioElement_Title = 'PortfolioElement_Title').pk

        # Get response
        response = self.client.get(reverse_lazy('portfolio_element_details',kwargs={'pk':PortfolioElement_pk}))

        # Check for any invalid value
        no_response = self.client.get(reverse_lazy('portfolio_element_details',kwargs={'pk':10000}))
        # print(response.content)
        # 202 for valid and 404 for invalid
        # self.assertEqual(response.status_code, 200)
        # self.assertEqual(no_response.status_code, 404)

        # check for content of Detail Page
        self.assertContains(response, 'PortfolioElement_Title')

        # Check for Correct template used in template/PortfolioElement
        self.assertTemplateUsed(response, 'portfolio_element/portfolio_element_detail.html')

#-------------------------------------------------------------------------------------------#


    # Test EducationInfo Create View

    def test_PortfolioElementCreate_view(self):
        # Login the user defined in SetUp
        self.client.login(username='testuser', password='test')

        # Generate response after creating an view using Http post method
        response = self.client.post('/portfolio_element/new/', {
        'PortfolioElement_Category' : 'PortfolioElement_Category',
        'PortfolioElement_Director':'PortfolioElement_Director',
        'PortfolioElement_Production_House':'PortfolioElement_Production_House',
        'PortfolioElement_Title':'PortfolioElement_Title',
        # 'PortfolioElement_Creator' : 'PortfolioElement_Creator',
        # 'PortfolioElement_Image' : 'PortfolioElement_Image',
        'PortfolioElement_Author' : self.user,      # Defined above in get_user_model
        'PortfolioElement_Created_Date' : timezone.now(),
        }, follow = True)

        # print(response.content)
        # Check for successful response
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, False)
        self.assertContains(response, 'PortfolioElement_Category')
        self.assertContains(response, 'PortfolioElement_Director')
        self.assertContains(response, 'PortfolioElement_Production_House')
        self.assertContains(response, 'PortfolioElement_Title')
        # self.assertContains(response, 'PortfolioElement_Creator')
        # self.assertContains(response, 'PortfolioElement_Image')
        self.assertContains(response, self.user.username)      # Same as defined in SetUp


        # Check for correct template used in template/EducationInfos
        self.assertTemplateUsed(response, 'portfolio_element/portfolio_element_detail.html')

#---------------------------------------------------------------------------------------#


    # Test EducationInfo Update view

    def test_PortfolioElementupdate_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        PortfolioElement_pk = PortfolioElement.objects.get(PortfolioElement_Title='PortfolioElement_Title').pk

        # Get response using pk on details view
        response = self.client.get(reverse_lazy('portfolio_element_details',kwargs={'pk':PortfolioElement_pk}), {
        'PortfolioElement_Category' : 'PortfolioElement_Category',
        'PortfolioElement_Director':'PortfolioElement_Director',
        'PortfolioElement_Production_House':'PortfolioElement_Production_House',
        'PortfolioElement_Title':'PortfolioElement_Title',
        # 'PortfolioElement_Creator' : 'PortfolioElement_Creator',
        # 'PortfolioElement_Image' : 'PortfolioElement_Image',
        'PortfolioElement_Author' : self.user,      # Defined above in get_user_model
        'PortfolioElement_Created_Date' : timezone.now(),
        },follow = True)
        # Check for successful response
        self.assertEqual(response.status_code, 200)

        # Check for correct templates
        self.assertTemplateUsed(response,'portfolio_element/portfolio_element_detail.html')


#--------------------------------------------------------------------------------------------#


# Test Delete View of EducationInfo views

    def test_PortfolioElementdelete_view(self):
        # Login the user
        self.client.login(username='testuser', password='test')

        # Find primary key of table
        PortfolioElement_pk = PortfolioElement.objects.get(PortfolioElement_Title='PortfolioElement_Title').pk

        # Get response to delete

        response = self.client.get(reverse_lazy('portfolio_element_delete',kwargs={'pk':PortfolioElement_pk}))
        self.assertContains(response, 'Are you sure you want to delete') # THIS PART WORKS

        # Check deleted value , returns false i.e.302
        post_response = self.client.post(reverse_lazy('portfolio_element_delete',kwargs={'pk':PortfolioElement_pk}))

        # self.assertRedirects(post_response, reverse_lazy('EducationInfo_delete',kwargs={'pk':EducationInfo_pk}), status_code=302)


        self.assertEqual(response.status_code, 200)

        # check for Correct Template Used
        self.assertTemplateUsed(response, 'portfolio_element/portfolio_element_delete.html')




# ################################     View Testing End   #################################################


# ################################     Testing the URLs       ##############################################

class PagesTests(SimpleTestCase):

    # Check URL for list/ Home
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

# #-----------------------------------------------------------------------------------------------------#
