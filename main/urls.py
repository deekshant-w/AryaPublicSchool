from django.urls import path
import main.views as mv

urlpatterns = [
    path('', mv.landing, name='landing'),
    path('dkTemp',mv.dkTemp),
    path('dynamicPage',mv.dynamicPage),
    path('<path:p>/',mv.dynamicPage)
]
