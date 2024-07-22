
from django.urls import path,include
from . import views
from .views import PersonClassview,PersonModelViewset,PersonViewsets,PersonConcreteGenricView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'PersonModelViewsets',PersonModelViewset,basename='personModelviewsets')
# router.register(r'personsViewsets', PersonViewsets, basename='personsViewsets')
urlpatterns = router.urls

urlpatterns = [
    path('',include(router.urls)),
    path('person/',views.Personview),
    path('personclass/',PersonClassview.as_view()),
    path('PersonConcreteGenricView/',PersonConcreteGenricView.as_view())
 
]
