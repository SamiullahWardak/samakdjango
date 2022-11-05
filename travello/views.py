from django.shortcuts import render

from travello.models import Destenation

# Create your views here.

def travello(request):
    # dest1 = Destenation()
    # dest1.name='کابل'
    # dest1.price=10000
    # dest1.discr="په هر څه سمبال او ښه یخه هوا لري"
    # dest1.image="travel-icon.png"
    # dest1.offer=False
    
    # dest2 = Destenation()
    # dest2.name="هرات"
    # dest2.discr='ډېر ښایسته او لرغونی ځای دی'
    # dest2.price=20000
    # dest2.image="travel-icon2.png"
    # dest2.offer=True
    
    # dest3 = Destenation()
    # dest3.name="ننګرهار"
    # dest3.discr='تازه او شین ځای دی'
    # dest3.price=18000
    # dest3.image="travel-icon3.png"
    # dest3.offer=False

    # dest4 = Destenation()
    # dest4.name="کندهار"
    # dest4.discr='ښکلی او میله یي ځای دی'
    # dest4.price=16000
    # dest4.image="travel-icon4.png"
    # dest4.offer=True
    
    # dest5 = Destenation()
    # dest5.name="بلخ"
    # dest5.discr='تاریخي او لوکس ځای دی'
    # dest5.price=22000
    # dest5.image="travel-icon2.png"
    # dest5.offer=True
    
    # dest6 = Destenation()
    # dest6.name="کندز"
    # dest6.discr='شین دی او نرم مزاجه خلک یې دی'
    # dest6.price=21000
    # dest6.image="travel-icon.png"
    # dest6.offer=False
    # dests = [dest1, dest2, dest3, dest4, dest5, dest6]

    dests = Destenation.objects.all()
    
    return render(request, 'index.html', {'country': 'افغانستان', 'dests': dests})