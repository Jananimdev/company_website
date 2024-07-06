
from django.shortcuts import render, get_object_or_404, redirect
from .models import details
from .forms import blogsform
from .forms import ContactForm
from .models import Contact
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render

def send_email_to_admin(request):
    if request.method == 'POST':
        subject = 'New Contact Form Submission'
        message = 'Name: {}\nEmail: {}\nMessage: {}'.format(
            request.POST.get('name'),
            request.POST.get('email'),
            request.POST.get('message')
        )
        from_email = settings.EMAIL_HOST_USER
        to_email = 'admin@example.com'  # Replace with admin's email address
        
        send_mail(subject, message, from_email, [to_email])
        return render(request, 'confirmation.html', {'message': 'Email sent successfully!'})
    return render(request, 'contact_form.html')



def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process form data and save to database
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            message = form.cleaned_data['message']
            
            # Example of saving to database
            contact = Contact(full_name=full_name, email=email, phone_number=phone_number, message=message)
            contact.save()
            
            print("Contact saved:", contact)  # Debug statement

            # Redirect to a success page or back to contact page
            return redirect('contact_success')  # Replace with your URL name or path
        else:
            print("Form is invalid")  # Debug statement
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})



def index(request):
    posts = details.objects.all()
    return render(request, 'index.html', {'posts': posts})

def post(request, post_id):
    post = get_object_or_404(details, id=post_id)
    return render(request, 'post.html', {'post': post})


def sampletemplate(request):
    return render(request, 'sampletemplate/index.html')

def about(request):
    return render(request, 'sampletemplate/about.html')

def form(request):
    form=blogsform()
    if request.method=='POST':
        form=blogsform(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)
        
    else:
        form=blogsform()
    return render(request,'form.html',{'form':form})



def index_html(request):
    return render(request, 'sampletemplate/index.html')


def about_html(request):
    return render(request, 'sampletemplate/about.html')


def services(request):
    return render(request, 'sampletemplate/services.html')


def blog(request):
    return render(request, 'sampletemplate/blog.html')


def test(request):
    return render(request, 'sampletemplate/testimonial.html')


def contact(request):
    return render(request, 'sampletemplate/contact.html')



def success_view(request):
    return render(request, 'sampletemplate/success.html')