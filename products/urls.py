from django.urls import path
from . import views

urlpatterns = [
    path('proteine/',views.ProtAction , name="product"),
     path('proteine/<int:pk>/',views.ProtDetailAction , name="productDetails"),
     path('vetements/homme',views.VetHAction , name="vetementH"),
     path('vetements/femme',views.VetFAction , name="vetementF"),
     path('vetements/<int:pk>/',views.VetDetailAction , name="vetementDetails"),
     path('materiels/body_building',views.MatBAction , name="materielB"),
     path('materiels/fitness',views.MatFAction , name="materielF"),
     path('materiels/<int:pk>/',views.MatDetailAction , name="materielsDetails"),
]