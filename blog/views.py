from django.urls import reverse_lazy, reverse
from pytils.translit import slugify
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView

from blog.functions.utils import send_email
from blog.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'slug', 'content', 'preview', 'created_at')
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()
        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'slug', 'content', 'preview', 'created_at')

    def form_valid(self, form):
        if form.is_valid():
            new_data = form.save()
            new_data.slug = slugify(new_data.title)
            new_data.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:view', args=[self.kwargs.get('pk')])


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(published=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views += 1
        self.object.save()

        if self.object.views == 100:
            send_email(self.object)

        return self.object


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')
