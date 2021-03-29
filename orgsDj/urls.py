"""orgsDj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
import Orgs.views as orgs_app

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'nodes/', orgs_app.AllNodes.as_view()),
    path(r'edges/', orgs_app.AllEdges.as_view()),
    path(r'nodetypes/', orgs_app.AllNodeTypes.as_view()),
    path(r'edgetypes/', orgs_app.AllEdgeTypes.as_view()),
    re_path(r'edgetype/(?P<pk>\d+)', orgs_app.EdgeTypeView.as_view()),
    path(r'edges/', orgs_app.AllEdges.as_view()),
    re_path(r'edge/(?P<pk>\d+)', orgs_app.EdgeView.as_view()),
    path(r'validedges/', orgs_app.AllValidEdges.as_view())
]
