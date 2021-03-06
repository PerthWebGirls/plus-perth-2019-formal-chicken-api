"""sistergifter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include               
from rest_framework import routers                    
from sista_regifta import views    
from rest_framework_simplejwt import views as jwt_views
# from sista_regifta.views import emailtest 

                        
router = routers.DefaultRouter()                      
router.register(r'gift', views.GiftView, 'gift')    
router.register(r'swap', views.SwapView, 'swap')   
router.register(r'user', views.UserViewSet, 'user')  
router.register(r'profile', views.ProfileView, 'profile') 
# router.register(r'email', emailtest, 'email')   

urlpatterns = [
    path('admin/', admin.site.urls),         
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('sista_regifta/', include('sista_regifta.urls')),
    # path('^gift/(?P<sender>.+)/$', GiftView.as_view()),
]
    # path('email/', emailtest, name='emailtest')   
    # path('email/', send_mail, name='send_mail')           