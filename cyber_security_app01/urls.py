from django.urls import path
from cyber_security_app01 import views

urlpatterns = [
    path('', views.Homepage, name="homepage"),
    path('contact/', views.Contact_view, name="contact"),
    path('our_team/', views.Our_tem, name="our_team"),
    path('Services/', views.Our_Services, name="Services"),
    path('service_single_page/<int:id>/', views.service_single_page, name="service_single_page"),
    path('Latest_News/', views.Latest_News, name="Latest_News"),
    path('Latest_News_details/<int:id>/', views.Latest_News_details, name="Latest_News_details"),
    path('Latest_News_category/<int:id>/',views.Latest_News_category,name='Latest_News_category'),
    path('search/',views.search,name="search"),


]
