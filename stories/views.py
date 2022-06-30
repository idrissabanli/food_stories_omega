from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib import messages

from stories.models import Story, Category
from stories.forms import ContactForm, StoryForm
from stories.models import Contact
from stories.tasks import process_func


def home(request):
    context = {
        'ad': 'Idris', 
        'soyad': 'Sabanli'
    }
    return render(request, 'index.html', context)


def recipes(request):
    return render(request, 'recipes.html')


def stories(request):
    story_list = Story.objects.all()
    s = 'salam necesen?'
    context = {
        'stories': story_list,
        's': s
    }
    return render(request, 'stories.html', context)


class StoryListView(ListView):
    template_name = 'stories.html'
    model = Story
    # context_object_name = 'stories'
    ordering = ('created_at', )
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.GET.get('category_id') # 1
        if category_id:
            queryset = queryset.filter(category__id=category_id)
        return queryset



def story_detail(request, id):
    story = get_object_or_404(Story, id=id)
    context = {
        'story': story
    }

    return render(request, 'single.html', context)


class StoryDetailView(DetailView):
    model = Story
    template_name = 'single.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all() # Category.objects.filter(stories__isnull=False).distinct()
        return context
        
        # context = {
        # 'story': story,
        # 'category': []
        # }


def export(request):
    process_func.delay()
    return redirect('/')


def contact_page(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Mesajiniz qeyde alindi!')
            return redirect(reverse_lazy('home'))
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)


class ContactView(CreateView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('home')
    # context_object_name = 
    # model = Contact
    # fields = '__all__'


    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     del context['form']
    #     return context


    def form_valid(self, form):
        result = super().form_valid(form)
        messages.add_message(self.request, messages.SUCCESS, 'Mesajiniz qeyde alindi!')
        return result



def like_story(request, id):
    request.session['liked_stories']= f"{request.session.get('liked_stories', '')} {id}"
    print('request.session', request.session['liked_stories'])
    messages.add_message(request, messages.SUCCESS, 'Siz mehsulu beyendiniz!')
    return redirect(reverse_lazy('home'))


def liked_stories(request):
    liked_stories = request.session.get('liked_stories',)
    stories = None
    if liked_stories:
        print('liked_stories', 3*'\n', liked_stories, 3*'\n',)
        splited_liked_stories = liked_stories.split()
        print(splited_liked_stories)
        liked_stories = list(map(int, splited_liked_stories))
        print(liked_stories)
        stories = Story.objects.filter(id__in=liked_stories)
    context = {
        'stories': stories
    }
    return render(request, 'liked_stories.html', context)


class CreateStoryView(LoginRequiredMixin, CreateView):
    form_class = StoryForm
    template_name = 'create_story.html'
    # success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateStoryView(LoginRequiredMixin, UpdateView):
    form_class = StoryForm
    model = Story
    template_name = 'create_story.html'