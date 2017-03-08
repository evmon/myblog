from django.shortcuts import render
from django.views.generic import ListView, FormView, View, DetailView, CreateView
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response, redirect

from .models import Post
from .form import PostForm

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class PostList(ListView):
    
    model = Post
    template_name = 'blog_part/posts.html'
    context_object_name = 'post_list'
    paginate_by = 7
    queryset = Post.objects.all().order_by('-id')
 

class LoginFormView(FormView):

    form_class = AuthenticationForm
    # Similarly registration, use authentication pattern
    template_name = "blog_part/login.html"
    # link for redirect after successful authentication

    success_url = "/"

    def form_valid(self, form):
        # Get the user object based on the entered data in the form.
        self.user = form.get_user()
        # Perform user authentication.
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):

    def get(self, request):
        # Perform output for the user requesting this view.
        logout(request)
        # After that redirect the user to the main page.
        return redirect('/')


class RegisterFormView(FormView):

    form_class = UserCreationForm
    success_url = "/login/"
    template_name = "blog_part/signup.html"

    def form_valid(self, form):
        # create user if form is valid
        form.save()
        # call the base class method
        return super(RegisterFormView, self).form_valid(form)


class ShowPost(DetailView):

    model = Post
    template_name = 'blog_part/detail.html'
    


# class AddPost(CreateView):
    
#     model = Post
#     template_name = 'blog_part/add_post.html'
#     form_class = PostForm
    
#     def get_success_url(self):
#         return '/'

#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.save()        
#         return HttpResponseRedirect(self.get_success_url())