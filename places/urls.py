from django.urls import path, re_path,include
from . import views
import django.views.defaults
from django.conf.urls import handler404, handler500, url

urlpatterns = [
    # home place
    path('places/',include([
        path('',views.index,name='places'),
        path('<int:id>/',views.places_details,name='places_details'),
        path('create_comment_place/<int:id>/',views.create_comment_place,name='create_comment_place'),
        path('create_place_tour/<int:id>/',views.create_place_tour,name='create_place_tour'),
        path('search/<str:name>/',views.search_place,name='search_place'),
        path('search_places/',views.search_form,name='searchform'),
        
    ])),
    # dashboard
    path('dashboard/places/',include([
        # places
        path('',views.ListPlace.as_view(),name='ListPlace'),
        path('email/',views.AddEmail.as_view(),name='AddEmail'),
        path('create/',views.AddPlace.as_view(),name='AddPlace'),
        path('<int:pk>/',views.UpdatePlace.as_view(),name='UpdatePlace'),
        path('<int:pk>/delete/',views.DeletePlace.as_view(),name='DeletePlace'),
        # places details
        path('details/',include([
            path('',views.ListPlaceDetails.as_view(),name='ListPlaceDetails'),
            path('create/',views.AddPlaceDetails.as_view(),name='AddPlaceDetails'),
            path('<int:pk>/',views.UpdatePlaceDetails.as_view(),name='UpdatePlaceDetails'),
            path('<int:pk>/delete/',views.DeletePlaceDetails.as_view(),name='DeletePlaceDetails'),
        ])),
    ])),
]