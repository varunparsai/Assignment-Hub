from django.shortcuts import render, redirect
from .forms import UploadForm
# Create your views here.

def upload_assignment(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'uploads/success.html')
    else:
        form = UploadForm()
    return render(request, 'uploads/upload.html', {'form': form})
