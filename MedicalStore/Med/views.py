from django.shortcuts import render,redirect
from Med.forms import UsrReg,UsPerm
from django.core.mail import EmailMessage
#from django.core.mail import mail_admins
from MedicalStore import settings
from Med.models import User
# Create your views here.

def home(request):
	return render(request,'html/home.html')

def register(request):
	if request.method == "POST":
		t = UsrReg(request.POST)
		if t.is_valid():
			t.save()
			return redirect('/lgn')
	t = UsrReg()
	return render(request,'html/register.html',{'y':t})

def mainpage(request):
	return render(request,'html/mainpage.html')

def usercrdntls(request):
	if request.method == "POST":
		u = request.POST.get('uname')
		ut = request.POST.get('utype')
		ud = request.POST.get('uid')
		em = request.POST.get('email')
		ms = request.POST.get('msg')
		at = request.FILES['fe']
		y = "Hi Welcome "+u+" Regarding User type request as "+ut+" Your id is: "+ud
		t = EmailMessage("UserRole Change",y,settings.EMAIL_HOST_USER,[settings.ADMINS[0][1],em])
		#t=mail_admins("User Role",y)
		t.content_subtype = 'html'
		t.attach(at.name,at.read(),at.content_type)
		t.send()
		if t == 1:
			return redirect('/usrq')
	return render(request,'html/usercrnt.html')

def peruser(request):
	ty=User.objects.all()
	return render(request,'html/peruser.html',{'q':ty})

def gvper(request,k):
	r=User.objects.get(id=k)
	if request.method=="POST":
		k=UsPerm(request.POST,instance=r)
		if k.is_valid():
			k.save()
			return redirect('/prm')
	k2=UsPerm(instance=r)
	return render(request,'html/gvp.html',{'y':k2})