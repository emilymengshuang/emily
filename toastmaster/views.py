from django.shortcuts import render
from .models import meetings

# Create your views here.

def index(request):
    mets = meetings.objects.all()

    return render(request, "index.html", {'mets': mets})



    # mets = [meeting1, meeting2, meeting3, meeting4, meeting5, meeting6]

    # meeting1 = meetings()
    # meeting1.theme = 'Clutural Bridge'
    # meeting1.desc= 'nice'
    # meeting1.img = 'meeting1.jpg'
    # meeting1.date= '7-10-2019'
    
    # meeting2 = meetings()
    # meeting2.theme = 'Courage'
    # meeting2.desc= 'nice'
    # meeting2.img = 'meeting2.jpg'
    # meeting2.date= '7-24-2019'

    # meeting3 = meetings()
    # meeting3.theme = 'Ice-Cream'
    # meeting3.desc= 'nice'
    # meeting3.img = 'meeting3.jpg'
    # meeting3.date= '8-14-2019'

    # meeting4 = meetings()
    # meeting4.theme = 'Dating'
    # meeting4.desc= 'nice'
    # meeting4.img = 'meeting4.jpg'
    # meeting4.date= '8-28-2019'

    # meeting5 = meetings()
    # meeting5.theme = 'Mooncake Festive!'
    # meeting5.desc= 'nice'
    # meeting5.img = 'meeting5.jpg'
    # meeting5.date= '9-11-2019'

    # meeting6= meetings()
    # meeting6.theme = 'Autumn is in the Air'
    # meeting6.desc= 'nice'
    # meeting6.img = 'meeting6.jpg'
    # meeting6.date= '9-25-2019'
