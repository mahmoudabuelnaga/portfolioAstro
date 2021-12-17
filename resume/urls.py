from django.urls import path
from .views import portfolio, portfolioDetailView

app_name = 'resume'

urlpatterns = [   
    path('', portfolio, name='portfolio'),
    path('<id>/<slug>/', portfolioDetailView.as_view(), name='post-detail')
]