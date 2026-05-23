from django.shortcuts import render, redirect
from .forms import MemberForm

def home(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MemberForm()
    return render(request, 'myapp/home.html', {'form': form})
