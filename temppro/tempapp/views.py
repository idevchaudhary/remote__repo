from django.shortcuts import render
import datetime

# Create your views here.
def temp(request):
    date=datetime.datetime.now()
    name="Dev"
    s=int(date.strftime('%H'))
    if s<12:
        msg="Guten Morgen !!"
    elif s<16:
        msg='Guten Nachmittag'
    elif s<22:
        msg="Guten Abend"
    else:
        msg='Guten Nacht'
    d={'time':date,'msg':msg,'name':name,}
    return render(request,'tempapp/wish.html',context=d)
