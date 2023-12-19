# views.py
from django.shortcuts import render  
from django.http import HttpResponse  

from myapp.forms import SampleForm  


def sample_post(request, *args, **kwargs):  
    form = SampleForm(request.POST or None)  

    if form.is_valid():  
        # form.cleaned_data now contains the validated data  
        print(f'form.cleaned_data = {form.cleaned_data}')
        return HttpResponse('<p class="success">Form submitted successfully! ✅</p>')  
    else:  
        # form.errors contains the form validation errors  
        return HttpResponse(f'<p class="error">Your form submission was unsuccessful ❌. Please would you correct the errors? The current errors: {form.errors}</p>')


def example(request):  
    return render(request, 'example.html')
