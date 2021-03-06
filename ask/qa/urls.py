"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.urls import path, re_path
from qa import views

urlpatterns = [
    path( '',  views.questions_list, name='index' ),
    path( "question/<int:id>/",  views.details_question, name='details' ),
    path( 'popular/',  views.popular, name='popular' ),
    path( 'ask/', views.ask_new, name='ask_new'),
    path( 'signup/', views.signup, name='signup'),
    path( 'login/', views.login_view, name='login'),
    path( 'logout/', views.logout_view, name='logout'),
]

# /
# /login/
# /signup/
# /question/<123>/    # вместо <123> - произвольный ID
# /ask/
# /popular/
# /new/