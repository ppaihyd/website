from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.template.response import TemplateResponse
from django.shortcuts import HttpResponse, render
from django.http import HttpResponseRedirect
from wagtail.models import Page
from wagtail.search.models import Query
from django.http import FileResponse


from django.shortcuts import render, redirect
from home.models import Values, Admin

from django.contrib import messages
from datetime import datetime


def search(request):
    search_query = request.GET.get("query", None)
    page = request.GET.get("page", 1)

    # Search
    if search_query:
        search_results = Page.objects.live().search(search_query)
        query = Query.get(search_query)

        # Record hit
        query.add_hit()
    else:
        search_results = Page.objects.none()

    # Pagination
    paginator = Paginator(search_results, 10)
    try:
        search_results = paginator.page(page)
    except PageNotAnInteger:
        search_results = paginator.page(1)
    except EmptyPage:
        search_results = paginator.page(paginator.num_pages)

    return TemplateResponse(
        request,
        "search/search.html",
        {
            "search_query": search_query,
            "search_results": search_results,
        },
    )

# Create your views here.


def homepage(request):
    request.session['msg'] = 'search/base.html'
    return render(request, 'search/index.html')

def adminlogin(request):
    return render(request, 'search/adminlogin.html')

def alogout(request):
    request.session.flush()
    return redirect('/admin-login/') 

def adminhome(request):
    if(request.session.get('admin-username')):
        request.session['msg'] = 'search/adminbase1.html'
        result = Values.objects.all()
        return render(request, 'search/adminhome.html', {'result':result})
    else:
        return redirect('/admin-login/')

def alogin(request):
    if(request.method=='POST'):
        if(request.POST.get('admin-username') and request.POST.get('admin-password')):
            request.session['admin-username'] = request.POST.get('admin-username')
            result = Admin.objects.filter(username=request.POST.get('admin-username'))
            if(len(result)<=0):
                messages.error(request, 'Invalid credentials')
                return redirect('/admin-login/')
            for i in result:
                request.session['admin-username'] = request.POST.get('admin-username')
                if(i.username == request.POST.get('admin-username') and i.password==request.POST.get('admin-password')):
                    return redirect('/admin-home/')
                else:
                    messages.error(request, 'Invalid credentials')
                    return render(request, 'search/adminlogin.html')
        else:
            return render(request, 'search/adminlogin.html')
    else:
        return render(request, 'search/adminlogin.html')

def pendingdetails(request):
    if(request.session.get('admin-username')):
        request.session['msg'] = 'search/adminbase1.html'
        result = Values.objects.filter(member="pending")
        return render(request, 'search/pendingdetails.html', {'result':result})
    else:
        return redirect('/admin-login/')

def verify(request, id):
    result = Values.objects.filter(id=id)
    for i in result:
        result.update(member=i.appliedfor)
    return redirect('/pending-details/')

def remove(request, id):
    result = Values.objects.filter(id=id).delete()
    return redirect('/pending-details/')

def index(request):
    request.session['msg'] = 'search/base.html'
    return render(request, 'search/index.html')

def index1(request):
    if(request.session.get('username')):
        request.session['msg'] = 'search/base1.html'
        # url = 'search/base1.html'
        return render(request, 'search/index.html')
    # return render(request, 'search/index1.html')

def index2(request):
    if(request.session.get('membership')):
        request.session['msg'] = 'search/base2.html'
        # url = 'search/base1.html'
        return render(request, 'search/index.html')
    # return render(request, 'search/index2.html')

def membership(request):
    request.session['msg'] = 'search/base.html'
    return render(request,'search/membership.html')

def membership1(request):
    if(request.session.get('username')):
        request.session['msg'] = 'search/base1.html'
        # url = 'search/base1.html'
        return render(request,'search/membership.html')


def membership2(request):
    if(request.session.get('membership')):
        request.session['msg'] = 'search/base2.html'
        # url = 'search/base1.html'
        return render(request,'search/membership.html')


def directory(request):
    if(request.session.get('membership')):
        result = Values.objects.filter(member='life') | Values.objects.filter(member='student') | Values.objects.filter(member='annual')
        return render(request, 'search/directory.html', {'result':result})
    else:
        return render(request, 'search/404.html')

def workshopt(request):
    request.session['msg'] = 'search/base.html'
    return redirect('/workshop/')

def workshop1(request):
    if(request.session.get('username')):
        request.session['msg'] = 'search/base1.html'
        # url = 'search/base1.html'
        return redirect('/workshop/')

def workshop2(request):
    if(request.session.get('membership')):
        request.session['msg'] = 'search/base2.html'
        # url = 'search/base1.html'
        return redirect('/workshop/')

def downloadst(request):
    request.session['msg'] = 'search/base.html'
    return redirect('/downloads/')

def downloads1(request):
    if(request.session.get('username')):
        request.session['msg'] = 'search/base1.html'
        # url = 'search/base1.html'
        return redirect('/downloads/')

def downloads2(request):
    if(request.session.get('membership')):
        request.session['msg'] = 'search/base2.html'
        # url = 'search/base1.html'
        return redirect('/downloads/')

def nationalconferencest(request):
    request.session['msg'] = 'search/base.html'
    return redirect('/nationalconference/')

def nationalconferences1(request):
    if(request.session.get('username')):
        request.session['msg'] = 'search/base1.html'
        # url = 'search/base1.html'
        return redirect('/nationalconference/')

def nationalconferences2(request):
    if(request.session.get('membership')):
        request.session['msg'] = 'search/base2.html'
        # url = 'search/base1.html'
        return redirect('/nationalconference/')

def internationalconferencest(request):
    request.session['msg'] = 'search/base.html'
    request.session['range']=range(10)
    return redirect('/internationalconference/')

def internationalconferences1(request):
    if(request.session.get('username')):
        request.session['msg'] = 'search/base1.html'
        # url = 'search/base1.html'
        return redirect('/internationalconference/')

def internationalconferences2(request):
    if(request.session.get('membership')):
        request.session['msg'] = 'search/base2.html'
        # url = 'search/base1.html'
        return redirect('/internationalconference/')

def awardst(request):
    request.session['msg'] = 'search/base.html'
    return redirect('/awards/')

def awards1(request):
    if(request.session.get('username')):
        request.session['msg'] = 'search/base1.html'
        # url = 'search/base1.html'
        return redirect('/awards/')
    

def awards2(request):
    if(request.session.get('membership')):
        request.session['msg'] = 'search/base2.html'
        # url = 'search/base1.html'
        return redirect('/awards/')

def registration11(request):
    if(request.session.get('username')):
        request.session['msg'] = 'search/base1.html'
        # url = 'search/base1.html'
        return render(request, 'search/registration01.html')

def registration12(request): #new
    if(request.session.get('username')):
        request.session['msg'] = 'search/base1.html'
        # url = 'search/base1.html'
        return render(request, 'search/registration02.html')

def registration01(request):
    request.session['msg'] = 'search/base.html'
    return render(request,'search/registration01.html')

def registration02(request): #new
    request.session['msg'] = 'search/base.html'
    return render(request,'search/registration02.html')


def society(request):
    request.session['msg'] = 'search/base.html'
    return render(request,'search/society.html')

def society1(request):
    if(request.session.get('username')):
        request.session['msg'] = 'search/base1.html'
        # url = 'search/base1.html'
        return render(request,'search/society.html')

def society2(request):
    if(request.session.get('membership')):
        request.session['msg'] = 'search/base2.html'
        # url = 'search/base1.html'
        return render(request,'search/society.html')


def council(request):
    request.session['msg'] = 'search/base.html'
    return render(request,'search/council.html')

def council1(request):
    if(request.session.get('username')):
        request.session['msg'] = 'search/base1.html'
        # url = 'search/base1.html'
        return render(request, 'search/council.html')

def council2(request):
    if(request.session.get('membership')):
        request.session['msg'] = 'search/base2.html'
        # url = 'search/base1.html'
        return render(request, 'search/council.html')
    
def legendary(request):
    request.session['msg'] = 'search/base.html'
    return render(request,'search/legendary.html')

def legendary1(request):
    request.session['msg'] = 'search/base1.html'
    return render(request,'search/legendary.html')

def legendary2(request):
    request.session['msg'] = 'search/base2.html'
    return render(request,'search/legendary.html')

def journals(request):
    request.session['msg'] = 'search/base.html'
    return render(request,'search/journals.html')

def journals1(request):
    if(request.session.get('username')):
        request.session['msg'] = 'search/base1.html'
        # url = 'search/base1.html'
        return render(request, 'search/journals.html')

def journals2(request):
    if(request.session.get('membership')):
        request.session['msg'] = 'search/base2.html'
        # url = 'search/base1.html'
        return render(request, 'search/journals.html')
    
def editorial(request):
    request.session['msg'] = 'search/base.html'
    return render(request,'search/editorial.html')

def editorial1(request):
    request.session['msg'] = 'search/base1.html'
    return render(request,'search/editorial.html')

def editorial2(request):
    request.session['msg'] = 'search/base2.html'
    return render(request,'search/editorial.html')

def books(request):
    request.session['msg'] = 'search/base.html'
    return render(request,'search/books.html')

def books1(request):
    request.session['msg'] = 'search/base1.html'
    return render(request,'search/books.html')

def books2(request):
    request.session['msg'] = 'search/base2.html'
    return render(request,'search/books.html')

def newslettert(request):
    request.session['msg'] = 'search/base.html'
    return redirect('/newsletter/')

def newsletter1(request):
    request.session['msg'] = 'search/base1.html'
    return redirect('/newsletter/')

def newsletter2(request):
    request.session['msg'] = 'search/base2.html'
    return redirect('/newsletter/')

def nomination(request):
    request.session['msg'] = 'search/base.html'
    return render(request,'search/nomination.html')

def nomination1(request):
    request.session['msg'] = 'search/base1.html'
    return render(request,'search/nomination.html')

def nomination2(request):
    request.session['msg'] = 'search/base2.html'
    return render(request,'search/nomination.html')


def annualreportt(request):
    request.session['msg'] = 'search/base.html'
    return redirect('/annualreport/')

def annualreport1(request):
    request.session['msg'] = 'search/base1.html'
    return redirect('/annualreport/')

def annualreport2(request):
    request.session['msg'] = 'search/base2.html'
    return redirect('/annualreport/')


def election(request):
    request.session['msg'] = 'search/base.html'
    return render(request,'search/election.html')

def election1(request):
    if(request.session.get('username')):
        request.session['msg'] = 'search/base1.html'
        # url = 'search/base1.html'
        return render(request, 'search/election.html')

def election2(request):
    if(request.session.get('membership')):
        request.session['msg'] = 'search/base2.html'
        # url = 'search/base1.html'
        return render(request, 'search/election.html')

def logout(request):
    result = Values.objects.filter(username=request.session.get('username'))
    for i in result:
        if(i.member=="no"):
            Values.objects.filter(username=request.session.get('username')).update(firstname="", lastname="", dob="", qualification="", email="", organisation="" , phone="", designation="", city="", address="", state="")
    request.session.flush()
    # return render(request,'search/index.html')
    return redirect('/')

def insertmemberinfo1(request):
    mydate = datetime.now().date()
    if(request.method=='POST'):
        if(request.POST.get("firstname") and request.POST.get("lastname") and request.POST.get("dob") and request.POST.get("qualification") and request.POST.get("email") and request.POST.get("organisation") and request.POST.get("phone") and request.POST.get("designation")):
            Values.objects.filter(username=request.session.get('username')).update(firstname=request.POST.get("firstname"), lastname=request.POST.get("lastname"), dob =request.POST.get("dob"), qualification=request.POST.get("qualification"), email=request.POST.get("email"), organisation=request.POST.get("organisation"), phone=request.POST.get("phone"), designation=request.POST.get("designation") )
            return render(request, 'search/registration02.html')
        elif(request.POST.get("city") and request.POST.get("address") and request.POST.get("state") and request.POST.get("transactionid")):
            # Values.objects.filter(username=request.session.get('username')).update(member=request.session.get('member'))
            Values.objects.filter(username=request.session.get('username')).update(member="pending")
            result = Values.objects.filter(transactionid=request.POST.get('transactionid'))
            if(len(result)>0):
                messages.success(request, 'Transaction id is not unique')
                return redirect('/index1/')
            Values.objects.filter(username=request.session.get('username')).update(date=mydate, city=request.POST.get('city'), address=request.POST.get('address'), state=request.POST.get('state'), transactionid=request.POST.get('transactionid'), appliedfor=request.session.get('member'))
            return redirect('/login/')

def InsertValue(request):
    # mydate = datetime.now().date()
    if(request.method=='POST'):
        if(request.POST.get('username') and request.POST.get('password')):
            result = Values.objects.filter(username=request.POST.get('username'))
            if(len(result)>0):
                messages.error(request, 'This username already exists')
                return render(request, 'search/myregistration.html')
            else:
                saverecord = Values()
                # saverecord.date = mydate
                saverecord.username = request.POST.get('username')
                saverecord.password = request.POST.get('password')
                saverecord.transactionid = request.POST.get('username')+" - not member"
                # saverecord.membership = request.POST.get('membership')
                saverecord.save()
                return render(request, 'search/login.html')
    else:
        return render(request, 'search/index.html')

def welcome(request):
    return render(request, 'search/index.html')

def login(request):
    return render(request, 'search/login.html')

def register(request):
    return render(request, 'search/myregistration.html')

def gallery(request):
    return render(request, 'search/gallery.html')

def getmembership(request):
    if(request.session.get('username')):
        request.session['msg'] = 'search/base1.html'
        if(request.method=='POST'):
            if(request.POST.get('life')):
                # Values.objects.filter(username=request.session.get('username')).update(member="life")
                # request.session['member'] = request.POST.get('life')
                request.session['member'] = 'life'
                return render(request, 'search/registration01.html')
            elif(request.POST.get('student')):
                # Values.objects.filter(username=request.session.get('username')).update(member="student")
                request.session['member'] = 'student'
                return render(request, 'search/registration01.html')
            elif(request.POST.get('annual')):
                # Values.objects.filter(username=request.session.get('username')).update(member="annual")
                request.session['member'] = 'annual'
                return render(request, 'search/registration01.html')
    else:
        return redirect('/login/')


def ShowValues(request):
    if(request.method=='POST'):
        if(request.POST.get('username') and request.POST.get('password')):
            result = Values.objects.filter(username=request.POST.get('username'))
            if(len(result)==0):
                messages.error(request, 'Invalid credentials')
                return render(request, 'search/login.html')
            else:
                request.session['username'] = request.POST.get('username')
                for i in result:
                    if(i.member=="no" or i.member=="pending"):
                        if(i.username == request.POST.get('username') and i.password== request.POST.get('password')):
                            return redirect('/index1/')
                        else:
                            messages.error(request, 'Invalid credentials')
                            return render(request, 'search/login.html')
                    elif(i.member!="no"):
                        request.session['membership'] = i.member
                        if(i.username == request.POST.get('username') and i.password== request.POST.get('password')):
                            d1 = datetime.strptime(i.date, "%Y-%m-%d")
                            d2 = datetime.strptime(str(datetime.now().date()), "%Y-%m-%d")
                            diff = int((d2-d1).days)
                            # diff = datetime.now().date()-i.date
                            if((i.member=="annual" or i.member=="student") and diff<=365):
                                # return render(request, 'search/index1.html', {'name':request.POST.get('username')})
                                return redirect('/index2/')
                            elif((i.member=="annual" or i.member=="student") and diff>365):
                                messages.error(request, 'Your membership time has finished. Please renew')
                                # return render(request, 'search/membership.html')
                                return redirect('/membership/') 
                            elif(i.member=="life"):
                                # return render(request, 'search/index1.html', {'name':request.POST.get('username')})
                                return redirect('/index2/')
                        else:
                            messages.error(request, 'Invalid credentials')
                            return render(request, 'search/login.html')
                    else:
                        messages.error(request, 'Invalid credentials')
                        return render(request, 'search/login.html')
        else:
            return render(request, 'search/login.html')

    else:
        return render(request, 'search/login.html')



