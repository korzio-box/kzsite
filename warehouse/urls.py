"""kzsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from warehouse.views import *


urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('', PGroupListView.as_view(), name='pgroup_list'),
    path('', PTypeListView.as_view(), name='ptype_list'),
    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('ptype_detail/<int:pk>/', PTypeDetailView.as_view(), name='ptype_detail'),
    path('pgroup_detail/<int:pk>/', PGroupDetailView.as_view(), name='pgroup_detail'),
    path('ptype_create/', PTypeCreateView.as_view(), name='ptype_create'),
    path('pgroup_create/', PGroupCreateView.as_view(), name='pgroup_create'),
    path('product_create/', ProductCreateView.as_view(), name='product_create'),
    path('product_edit/<int:pk>/', ProductEditView.as_view(), name='product_edit'),
    path('ptype_edit/<int:pk>/', PTypeEditView.as_view(), name='ptype_edit'),
    path('pgroup_edit/<int:pk>/', PGroupEditView.as_view(), name='pgroup_edit'),


]





