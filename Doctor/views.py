from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView, ListView, DeleteView
from .models import Post
from django.views.generic.edit import FormMixin
from .forms import PostModelForm, CommentModelForm


class PostCreateView(LoginRequiredMixin, CreateView):
    form_class = PostModelForm
    template_name = 'Forum/discussion_new.html'
    success_url = '/forum/list/'
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        form.instance.autori = self.request.user
        return super(PostCreateView, self).form_valid(form)


class PostUpdateView(UpdateView):
    queryset = Post.objects.all()
    form_class = PostModelForm
    template_name = 'Forum/discussion_edit.html'
    success_url = '/update'

    def dispatch(self, request, *args, **kwargs):  # new
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super(PostUpdateView, self).dispatch(request, *args, **kwargs)


class PostDetailView(FormMixin, DetailView):
    template_name = 'Forum/discussion_detail.html'
    queryset = Post.objects.all()
    model = Post
    form_class = CommentModelForm

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['form'] = CommentModelForm(initial={'post': self.object})
        context['posts_all'] = Post.objects.order_by('-data')[:3]
        return context

    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get("pk")
        return Post.objects.get(id=pk)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.autori = self.request.user
        form.save()
        return super(PostDetailView, self).form_valid(form)


class PostListView(ListView):
    queryset = Post.objects.all()
    template_name = 'Forum/discussion_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PostListView, self).get_context_data(*args, **kwargs)
        context['object_list'] = Post.objects.all().order_by('-data')
        return context


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'Forum/discussion_delete.html'
    success_url = reverse_lazy('list')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super(PostDeleteView, self).dispatch(request, *args, **kwargs)
