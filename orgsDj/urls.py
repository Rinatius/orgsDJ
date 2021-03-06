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
    path(r'orgs/', orgs_app.AllOrgs.as_view()),
    re_path(r'org/(?P<pk>\d+)', orgs_app.OrgView.as_view()),
    path(r'persons/', orgs_app.AllPersons.as_view()),
    re_path(r'person/(?P<pk>\d+)', orgs_app.PersonView.as_view()),
    path(r'positions/', orgs_app.AllPositions.as_view()),
    re_path(r'position/(?P<pk>\d+)', orgs_app.PositionView.as_view()),
    path(r'positionnames/', orgs_app.AllPositionNames.as_view()),
    re_path(r'positionname/(?P<pk>\d+)', orgs_app.PositionNameView.as_view()),
    path(r'employments/', orgs_app.AllEmployments.as_view()),
    re_path(r'employment/(?P<pk>\d+)', orgs_app.EmploymentView.as_view()),
    path(r'orghierarchies/', orgs_app.AllOrgsHierarchyRels.as_view()),
    re_path(r'orghierarchy/(?P<pk>\d+)',
            orgs_app.OrgsHierarchyRelView.as_view()),
    path(r'orgstructures/', orgs_app.AllOrgsStructuralRels.as_view()),
    re_path(r'orgstructure/(?P<pk>\d+)',
            orgs_app.OrgsStructuralRelView.as_view()),
    path(r'posorghierarchies/', orgs_app.AllPositionOrgHierarchyRels.as_view()),
    re_path(r'posorghierarchy/(?P<pk>\d+)',
            orgs_app.PositionOrgHierarchyRelView.as_view()),
    path(r'orgposhierarchies/', orgs_app.AllOrgPositionHierarchyRels.as_view()),
    re_path(r'orgposhierarchy/(?P<pk>\d+)',
            orgs_app.OrgPositionHierarchyRelView.as_view()),
    path(r'poshierarchies/', orgs_app.AllPositionsHierarchyRels.as_view()),
    re_path(r'poshierarchy/(?P<pk>\d+)',
            orgs_app.OrgsHierarchyRelView.as_view()),
    path(r'orgprofiles/', orgs_app.AllOrgProfiles.as_view()),
]
