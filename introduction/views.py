from django.shortcuts import render

from introduction.form import ReplyForm
from introduction.models import Experience, Work, Ability, Contact


def index(request):
    experiences = Experience.objects.all()
    works = Work.objects.all()
    abilities = Ability.objects.all()
    reply = ReplyForm()
    if request.method == 'POST':
        reply = ReplyForm(request.POST)
        if reply.is_valid():
            Contact.objects.create(name=request.POST['name'], email=request.POST['email'],
                                   message=request.POST['message'])
            reply = ReplyForm()
    return render(request, "index.html", locals())

# Create your views here.
