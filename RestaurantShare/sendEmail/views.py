from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sendEmail(request):
    
    
#     checked_res_list=request.POST.getlist('checks')
#     inputReceiver=request.POST['inputReceiver']
#     inputTitle=request.POST['inputTitle']
#     inputContent=request.POST['inputContent']
#     return HttpResponse("".join(checked_res_list)+inputReceiver+inputTitle+inputContent)


    import smtplib

    gmail_user='22ndistinguishable@gmail.com'
    gmail_password='zcrrhsxixqtyvhix'
    
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    server.login(gmail_user,gmail_password)
    server.sendmail('22ndistinguishable@gmail.com',"jsitclub@gmail.com","Hello")


        
    return HttpResponse("sendEmail")
    