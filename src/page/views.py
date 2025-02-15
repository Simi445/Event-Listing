from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import logout,authenticate, login
from django.shortcuts import redirect,render
from django.contrib.auth.models import User
from .models import Event, Contacts, Comment, Ticket
from django.utils import timezone
from django.shortcuts import get_object_or_404

# Create your views here.
def login_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        return redirect('front-page')

    next_url = request.GET.get('next', 'front-page')
    template_name = request.GET.get('template_name', 'default.html')

    if request.method == "POST":
        next_url = request.POST.get('next', 'front-page')
        template_name = request.POST.get('template_name', 'default.html')
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(next_url)
        else:
            return render(
                request, "login.html", {"error": "Invalid credentials", "next": next_url, "template_name": template_name}
            )
    return render(request, "login.html", {"next": next_url, "template_name": template_name})

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')


def register_view(request, *args, **kwargs):
    next_url = request.GET.get('next', 'login')
    if request.method == "POST":
        next_url = request.POST.get('next', 'login')
        if User.objects.filter(username=request.POST.get("username")).exists():
            return render(request, "register.html", {"error": "Username already exists", "next": next_url})
        if request.POST.get("password") != request.POST.get("confirm_password"):
            return render(request, "register.html", {"error": "Passwords do not match", "next": next_url})
        user = User.objects.create_user(username=request.POST.get("username"), password=request.POST.get("password"))

        user = authenticate(request, username=request.POST.get("username"), password=request.POST.get("password"))
        if user is not None:
            login(request, user)
            return redirect(next_url)
    return render(request, "register.html", {"next": next_url})


def dashboard_view(request, *args, **kwargs):
        events = Event.objects.all()
        return render(request, "dashboard.html", {"events": events, "user": request.user})

def user_profile(request):
    if request.user.is_authenticated:
        tickets = Ticket.objects.filter(user=request.user)
        return render(request, 'user_profile.html', {'tickets': tickets})


def contact_view(request, *args, **kwargs):
          if request.method == "POST":
            Contacts.objects.create(
                first_name=request.POST.get("first_name"),
                last_name=request.POST.get("last_name"),
                email=request.POST.get("email"),
                phone=request.POST.get("phone"),
                message=request.POST.get("message")
            )
            return redirect('front-page')
          elif request.method == "GET":
              return render(request, "contacts.html")

def about_view(request, *args, **kwargs):
    return render(request, "about.html")


def post_comment(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            print(request.POST)
            comment_text = request.POST.get('comment')
            event_id = request.POST.get('event_id')
            event = get_object_or_404(Event, id=event_id)
            if comment_text:
                Comment.objects.create(
                    user=request.user,
                    comment=comment_text,
                    event=event,
                    created_at=timezone.now()
                )
            # return redirect('your_concert_page_view', event_id=event_id)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def concert_view_UT(request, event_id):
    event = Event.objects.filter(id=event_id).first()
    comments = Comment.objects.filter(event=event).order_by('-created_at')
    return render(request, 'concert-pages/UT.html', {'event': event, 'comments': comments})

def concert_view_RS(request, event_id):
    event = Event.objects.filter(id=event_id).first()
    comments = Comment.objects.filter(event=event).order_by('-created_at')
    return render(request, 'concert-pages/RS.html', {'event': event, 'comments': comments})

def concert_view_WM(request, event_id):
    event = Event.objects.filter(id=event_id).first()
    comments = Comment.objects.filter(event=event).order_by('-created_at')
    return render(request, 'concert-pages/WM.html', {'event': event, 'comments': comments})

def concert_view_EC(request, event_id):
    event = Event.objects.filter(id=event_id).first()
    comments = Comment.objects.filter(event=event).order_by('-created_at')
    return render(request, 'concert-pages/EC.html', {'event': event, 'comments': comments})

def ticket_view(request, event_id):
    if request.user.is_authenticated:
        event = Event.objects.filter(id=event_id).first()
        if request.method == "POST":
            price = request.POST.get('total-price')
            price = float(price[1:])
            quantity = int(request.POST.get('quantity'))
            total_price = price * quantity
            card_number = request.POST.get('card_number')
            expiration_date = request.POST.get('expiration_date')
            cvv = request.POST.get('cvv')
            Ticket.objects.create(
                event=event,
                user=request.user,
                quantity=quantity,
                total_price=total_price,
                card_number=card_number,
                expiration_date=expiration_date,
                cvv=cvv
            )
            return redirect('purchase-success')
    return render(request, "ticket.html", {"event": event})


def purchase_view(request):
    if request.user.is_authenticated:
        return render(request, 'purchase.html')