from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Group
from django.core.exceptions import PermissionDenied

# In application imports
from scrumapp.models import Task, User, User_Story

from scrumapp.forms import CustomUserCreationForm

# Create your views here.

@login_required
def home(request):
    user_story = User_Story.objects.all()
    user_story_id_list = []
    
    # Get a list of the user story ids associated to a developer
    current_user = request.user
    user_story_id_for_developer = Task.objects.filter(developer = current_user.id).values('user_story_id')

    for story_id in user_story_id_for_developer:
        user_story_id_list.append(story_id['user_story_id'])
    user_story_dev = User_Story.objects.filter(pk__in = user_story_id_list)
    
    # Based on the group assigned allocate a different context to what the user can see
    if current_user.groups.filter(name='Developer').exists():
        context = {
            'user_story_list': user_story_dev
        }
    else:
        context = {
            'user_story_list': user_story
        }
    return render(request, 'scrumapp/home.html', context=context)

class AdminLogin(LoginView):
    template_name = 'scrumapp/login.html'

class AdminLogout(LoginRequiredMixin,LogoutView):
    template_name = 'scrumapp/logout.html'

def register(request):
    if request.method == 'GET':
        return render(request, 'scrumapp/register.html', {'form': CustomUserCreationForm})
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        print('test')
        if form.is_valid():
            user = form.save()
            defaultgroup = Group.objects.get(name='Developer')
            user.groups.add(defaultgroup)
            return redirect(home)


class UserStoryCreate(LoginRequiredMixin, PermissionRequiredMixin,CreateView):
    model = User_Story
    fields = '__all__'
    permission_required = 'scrumapp.add_user_story'
    success_url = reverse_lazy(home)

class UserStoryUpdate(LoginRequiredMixin, PermissionRequiredMixin,UpdateView):
    model = User_Story
    fields = '__all__'
    permission_required = 'scrumapp.change_user_story'
    success_url = reverse_lazy(home)

class UserStoryDelete(LoginRequiredMixin, PermissionRequiredMixin,DeleteView):
    model = User_Story
    permission_required = 'scrumapp.delete_user_story'
    success_url = reverse_lazy(home)

class UserStoryListView(LoginRequiredMixin, generic.ListView):
    model = User_Story

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

class UserStoryDetailView(LoginRequiredMixin,generic.DetailView):
    model = User_Story

    def get_context_data(self, **kwargs):

        context = {}
        if self.object:
            id_for_for_linked_user_story = self.object.id
            tasklist = Task.objects.filter(user_story=id_for_for_linked_user_story)
            context = {
                'task_list': tasklist
            }
            context.update(kwargs)
        return super().get_context_data(**context)


#Task views are created below

class TaskCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Task
    fields =  '__all__'
    permission_required = 'scrumapp.add_task'
    success_url = reverse_lazy(home)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields ="__all__"
    success_url = reverse_lazy(home)

    def dispatch(self, request, *args, **kwargs):
        developeridDB = 0
        task = Task.objects.filter(id = kwargs['pk']).values()
        
        for developerid in task:
            developeridDB = developerid['developer_id']
        
        if request.user.groups.filter(name='Developer') and developeridDB == request.user.id:
            return super(TaskUpdate, self).dispatch(request, *args, **kwargs)
        elif request.user.groups.filter(name='Scrum Master'):
            return super(TaskUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied()
        

class TaskDelete(LoginRequiredMixin, PermissionRequiredMixin,DeleteView):
    model = Task
    permission_required = 'scrumapp.delete_task'
    success_url = reverse_lazy(home)

class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task

class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task

    