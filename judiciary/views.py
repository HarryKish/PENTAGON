from django.shortcuts import render, reverse, redirect
from . models import Criminal
from . forms import CriminalForm, UserForm
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, DetailView
from django.contrib.auth import login, logout, authenticate



# Create your views here.

class CriminalCreateView(CreateView):

    model = Criminal

    fields = ['firstname', 'middlename', 'lastname', 'mugshot', 'mugshot_no', 'fingerprint', 'sentence_date', 'felony_description', 'sentencing_description', 'prisonname']

    def get_success_url(self):
        return reverse('judiciary:index')

class CriminalUpdateView(UpdateView):
    model = Criminal

    fields = ['firstname', 'middlename', 'lastname', 'mugshot', 'mugshot_no', 'fingerprint', 'sentence_date', 'felony_description', 'sentencing_description', 'prisonname']

    def get_success_url(self):
        return reverse('judiciary:index')

    def form_valid(self, form):
        return super().form_valid(form)

class CriminalDeleteView(DeleteView):
    model = Criminal
    success_url = '/'


class CriminalListView(ListView):

    model = Criminal
    template_name = 'judiciary/index.html'
    context_object_name = 'criminals'

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                criminals = Criminal.objects.filter(user=request.user)
                return render(request, 'judiciary/index.html', {'criminals': criminals})

    return render(request, 'judiciary/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                criminals = Criminal.objects.all()
                return render(request, 'judiciary/index.html', {'criminals': criminals})
    return render(request, 'judiciary/login.html')

def logout_user(request):
    logout(request)
    return redirect('judiciary:login_user')

class CriminalDetailView(DetailView):

    model = Criminal
    template_name = 'judiciary/more.html'
    context_object_name = 'criminal'







