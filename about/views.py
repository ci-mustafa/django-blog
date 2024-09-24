from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm
# Create your views here.


def about(request):
    about = About.objects.order_by("-updated_on").first()
    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(request, messages.SUCCESS, 
            message="Collaboration request received! I endeavour to respond within 2 working days.")     
    collaborate_form = CollaborateForm()
    return render(request, "about/about.html", {"about": about, "collaborate_form": collaborate_form})
