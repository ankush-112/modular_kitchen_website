from django.urls import path
from .views import home_page, gallery_page, get_categories, get_projects, submit_inquiry,contact_view,about_page,kitchen_page,product_page,walkin_wardrobe,hinged_wardrobe,sliding_wardrobe

urlpatterns = [
    path('', home_page, name='home'),  # Home page
    path('gallery/', gallery_page, name='gallery'),
    path('about/', about_page, name='about'),
    path('product/',product_page, name='product'),
    path('kitchen/', kitchen_page, name='kitchen'),
     path('contact/', contact_view, name='contact'),# Gallery page
    path('categories/', get_categories, name='categories'),  # API: Get categories
    path('projects/', get_projects, name='projects'),  # API: Get projects
    path('inquiry/', submit_inquiry, name='submit_inquiry'),
    path('walk-in/', walkin_wardrobe, name='walkin_wardrobe'),
    path('hinged-in/', hinged_wardrobe, name='hinged_wardrobe'),
    path('sliding_wardrobe/', sliding_wardrobe, name='sliding_wardrobe'),
    # API: Post Inquiry
]
