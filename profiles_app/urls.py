# from django.urls import path
from profiles_app import views
from rest_framework.routers import DefaultRouter
from django.urls import path, re_path, include
#from .views import ViewsToBeImported

router = DefaultRouter()
router.register('hello-viewsets', views.HelloViewsets,
                basename='hello-viewsets')
router.register('profile', views.UserProfileViewsets)
router.register('feed', views.ProfileFeedItemViewsets)


urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),

]
