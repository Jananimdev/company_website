
from django.urls import path
from . import views
from .views import contact_view



urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.post, name='post'),
    path('form/', views.form, name='form'),
    path('sampletemplate/', views.sampletemplate, name='sampletemplate'),
    path('sampletemplate/about/', views.about, name='about'),
    path('sampletemplate/index.html', views.index_html, name='index_html'),
    path('sampletemplate/about.html', views.about_html, name='about_html'),
    path('sampletemplate/services.html', views.services, name='services'),
    path('sampletemplate/blog.html', views.blog, name='blog'),
    path('sampletemplate/testimonial.html', views.test, name='test'),
    
    path('sampletemplate/contact.html', views.contact, name='contact'),
    path('sampletemplate/success.html', views.success_view, name='success'),
    path('send-email/', views.send_email_to_admin, name='send_email_to_admin'),

   
]
