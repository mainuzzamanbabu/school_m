"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

from members.views import (
    MemberCreateView,
    MemberDeleteView,
    MemberDetailView,
    MemberListView,
    MemberUpdateView,
)
from notice.views import (
    NoticeCreateView,
    NoticeDeleteView,
    NoticeDetailView,
    NoticeListView,
    NoticeUpdateView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('abc/', TemplateView.as_view(template_name='abc.html'), name='abc'),
    # path('xyz/', TemplateView.as_view(template_name='xyz.html'), name='xyz'),
    path("members/", MemberListView.as_view(), name="members"),
    path("members/create/", MemberCreateView.as_view(), name="member_create"),
    path("members/<int:pk>/", MemberDetailView.as_view(), name="member_detail"),
    path("members/<int:pk>/edit/", MemberUpdateView.as_view(), name="member_update"),
    path("members/<int:pk>/delete/", MemberDeleteView.as_view(), name="member_delete"),
    path("notices/", NoticeListView.as_view(), name="notices"),
    path("notices/create/", NoticeCreateView.as_view(), name="notice_create"),
    path("notices/<int:pk>/", NoticeDetailView.as_view(), name="notice_detail"),
    path("notices/<int:pk>/edit/", NoticeUpdateView.as_view(), name="notice_update"),
    path("notices/<int:pk>/delete/", NoticeDeleteView.as_view(), name="notice_delete"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
