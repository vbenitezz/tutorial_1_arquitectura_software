from django.urls import path
from .views import HomePageView, AboutPageView, ProductIndexView, ProductShowView, ProductCreateView, ContactPageView, ProductCreatedView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('products/', ProductIndexView.as_view(), name='index'),
    path('products/create', ProductCreateView.as_view(), name='form'),
    path('products/<str:id>', ProductShowView.as_view(), name='show'),

    # Activity 1
    path('contact/', ContactPageView.as_view(), name='contact'),
    # Activity 8
    path('product_created/', ProductCreatedView.as_view(), name='product_created'),
]