"""
tree_api URL Configuration
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from .views import TreeDetailView, TreeListView

urlpatterns = [    
    path('', TreeListView.as_view(), name='trees'),
    path('<int:pk>', TreeDetailView.as_view(), name='tree-detail')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
