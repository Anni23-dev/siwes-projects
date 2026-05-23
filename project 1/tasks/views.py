from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm

# 1. Dashboard View (Protected)
@login_required(login_url='login')
def dashboard(request):
    if request.method == 'POST' and 'submit_task' in request.POST:
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # Assign task to the logged-in user
            task.save()
            messages.success(request, "🚀 Task captured successfully!")
            return redirect('dashboard')
        else:
            messages.error(request, "❌ Validation failed.")
    else:
        form = TaskForm()

    if request.method == 'POST' and 'update_status' in request.POST:
        task_id = request.POST.get('task_id')
        new_status = request.POST.get('status')
        task = get_object_or_404(Task, id=task_id, user=request.user) # Check ownership
        task.status = new_status
        task.save()
        messages.info(request, f"🔄 Updated '{task.title}'.")
        return redirect('dashboard')

    # Query only the tasks belonging to the logged-in user
    tasks = Task.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'tasks/dashboard.html', {'tasks': tasks, 'form': form})

# 2. Delete Task View
@login_required(login_url='login')
def delete_task(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id, user=request.user)
        task.delete()
        messages.warning(request, f"🗑️ Task '{task.title}' has been deleted.")
    return redirect('dashboard')

# 3. Sign Up View
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Automatically log in after registration
            messages.success(request, "🎉 Account created successfully! Welcome!")
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'tasks/register.html', {'form': form})

# 4. Log In View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'tasks/login.html', {'form': form})

# 5. Log Out View
def logout_view(request):
    logout(request)
    messages.info(request, "Logged out successfully.")
    return redirect('login')

# 6. Delete Account View
@login_required(login_url='login')
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.delete() # Deletes user and cascadingly removes all their tasks
        messages.warning(request, "⚠️ Your account has been permanently deleted.")
        return redirect('register')
    return redirect('dashboard')
