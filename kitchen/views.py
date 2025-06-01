from django.shortcuts import render
from django.http import JsonResponse
from .models import Category, Project, Inquiry
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Contact
from django.conf import settings
from django.core.mail import send_mail


# Fetch All Categories



def home_page(request):
    return render(request, "home.html")
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # Compose email content
        full_message = f"""
        Name: {name}
        Email: {email}
        Phone: {phone}
        Subject: {subject}
        
        Message:
        {message}
        """

        try:
            send_mail(
                subject=f"New Contact Form Submission: {subject}",
                message=full_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=["sattukhatkar@gmail.com"],
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent successfully!")
        except Exception as e:
            messages.error(request, f"Error sending message: {e}")

        return redirect("contact")

    return render(request, "contact.html")

def about_page(request):
    return render(request, "about.html")
def kitchen_page(request):
    return render(request, "kitchen.html")
def kitchen_U_page(request):
    return render(request, "u_shaped.html")
def product_page(request):
    return render(request, "product.html")
def gallery_page(request):
    return render(request, "gallery.html")
def walkin_wardrobe(request):
    return render(request, 'walkin.html')
def hinged_wardrobe(request):
    return render(request, 'hinged.html')
def sliding_wardrobe(request):
    return render(request, 'sliding_wardrobe.html')
def g_shaped(request):
    return render(request, 'g_shaped.html')
def inline_kitchen(request):
    return render(request, 'inline_kitchen.html')
def island_kitchen(request):
    return render(request, 'island_kitchen.html')
def italian_kitchen(request):
    return render(request, 'italian_kitchen.html')
def german_kitchen(request):
    return render(request, 'german_kitchen.html')

def Parallel_kitchen(request):
    return render(request, 'Parallel_kitchen.html')
def get_categories(request):
    categories = list(Category.objects.values())  
    return JsonResponse({"categories": categories}, safe=False)

# Fetch All Projects
def get_projects(request):
    projects = list(Project.objects.values('id', 'title', 'category__name', 'description', 'image'))
    return JsonResponse({"projects": projects}, safe=False)

# Contact Inquiry Form Handling
@csrf_exempt
def submit_inquiry(request):
    if request.method == "POST":
        data = json.loads(request.body)
        Inquiry.objects.create(name=data["name"], email=data["email"], message=data["message"])
        return JsonResponse({"message": "Inquiry submitted successfully!"}, status=201)
    return JsonResponse({"error": "Invalid request"}, status=400)
