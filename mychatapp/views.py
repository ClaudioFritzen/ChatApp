from django.shortcuts import render
from .models import Profile, Friend
from .forms import ChatMessage
# Create your views here.
def index(request):
    user = request.user.profile
    friends = user.friends.all()
    context = {'user': user, 'friends': friends}
    return render(request, "mychatapp/index.html", context )


def detail(request, pk):
    friend = Friend.objects.get(profile_id= pk)
    form = ChatMessage()

    context = {'friend': friend, 'form': form}
    return render(request, 'mychatapp/detail.html', context)

