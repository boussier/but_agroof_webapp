from django.urls import include, path

urlpatterns = [
    path('trees/', TreeDetailView.as_view(), name='tree_detail_view'), 
]
