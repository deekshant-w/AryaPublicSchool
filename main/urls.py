from django.urls import path
import main.views as mv

urlpatterns = [
    path('', mv.landing, name='landing'),
    path('dkTemp',mv.dkTemp),
    path('dynamicPage',mv.dynamicPage),
    path('notice',mv.notice),
    path('information',mv.information),
    
] + [path('<path:p>/',mv.dynamicPage),]
