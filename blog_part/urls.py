from django.conf.urls import url
# from django.contrib.auth.forms import AuthenticationForm

from .views import PostList, LoginFormView, LogoutView, RegisterFormView, ShowPost, add_comment, \
					comment_approve, comment_remove, show_404, Arhives, AboutMe, search

app_name = 'blog_part'
handler404 = 'show_404'

urlpatterns = [
    url(r'^$', PostList.as_view(), name='PostList'),
    url(r'^login/$', LoginFormView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^sign-up/$', RegisterFormView.as_view(), name='sign-up'),
    url(r'^arhives/$', Arhives.as_view(), name='arhives'),
    url(r'^about-me/$', AboutMe.as_view(), name='about-me'),
    url(r'^search/$', search, name='search'),
    url(r'^detail/(?P<pk>[0-9]+)/$', ShowPost.as_view(), name='detail'),
    url(r'^detail/(?P<pk>[0-9]+)/add-comment/$', add_comment, name='add-comment'),
    url(r'^comment/(?P<pk>\d+)/approve/$', comment_approve, name='comment_approve'),
	url(r'^comment/(?P<pk>\d+)/remove/$', comment_remove, name='comment_remove'),
	
    
]