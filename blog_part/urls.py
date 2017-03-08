from django.conf.urls import url
# from django.contrib.auth.forms import AuthenticationForm

from .views import PostList, LoginFormView, LogoutView, RegisterFormView, ShowPost

app_name = 'blog_part'

urlpatterns = [
    url(r'^$', PostList.as_view(), name='PostList'),
    url(r'^login/$', LoginFormView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^sign-up/$', RegisterFormView.as_view(), name='sign-up'),
    url(r'^detail/(?P<pk>[0-9]+)/$', ShowPost.as_view(), name='detail'),
    
]