from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Message

@login_required
def inbox(request):
    mensajes = Message.objects.filter(receiver=request.user).order_by("-created_at")
    return render(request, "mensajes/inbox.html", {"mensajes": mensajes})


@login_required
def send_message(request):
    if request.method == "POST":
        receiver_id = request.POST["receiver"]
        content = request.POST["content"]

        receiver = User.objects.get(id=receiver_id)

        Message.objects.create(
            sender=request.user,
            receiver=receiver,
            content=content
        )
        return redirect("inbox")

    users = User.objects.exclude(id=request.user.id)
    return render(request, "mensajes/send_message.html", {"users": users})
