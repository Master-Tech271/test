from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from .models import *
import random
from django.contrib.auth.decorators import login_required

import re
# Create your views here.
from django.utils import translation
No_of_questions = 10

#mail_with_body
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

#Views from here are defined for mobile view, can be removed later
def instructions(request):
    return render(request,'drivingtest/mobileview/instructions.html')

def mobilequestions(request):
    return render(request,'drivingtest/mobileview/mobilequestions.html')

def mobilequestionpanel(request):
    return render(request,'drivingtest/mobileview/mobilequestionpanel.html')

def mobilereviewpage(request):
    return render(request,'drivingtest/mobileview//mobilereviewpage.html')
#till here


@csrf_exempt
def home(request):
    logout(request)
    return redirect('drivingtest_test')


@csrf_exempt
def test(request):
    # if request.user.is_drivingtest:
        MOBILE_AGENT_RE=re.compile(r".*(iphone|mobile|androidtouch)",re.IGNORECASE)
        if request.POST:
            score = 0
            for q in request.POST.values():
                if not q == '':
                    if Option.objects.get(uid=q).answer:

                        score = score + 1
        #     try:
        #         se = request.session['testuid']
        #     except:
            # return render(request,'drivingtest/error.html')
            # t = TestUser.objects.get(uid=request.session['testuid'])
            # t.score = score
            # t.save()
            # try:
            #     del request.session['testuid']
            # except:
            #     pass
            # send_mail(
            #     'Driving Test | MoRTH | IRSC',
            #     'Your Score for driving test are '+ str(score) + '/' + str(No_of_questions) +' .\nClick the link to give another test - http://ww2.road-safety.co.in/drivingtest/ . \n\nRegards,\nIRSC Team',
            #     'no-reply@road-safety.co.in',
            #     [request.user.email,],
            #     fail_silently=True,
            # )
            # html_content = render_to_string('home/certificate.html', {'name':request.user.gsluser.name})
            # html = HTML(string=html_content, base_url=request.build_absolute_uri())
            # main_doc = html.render()
            # pdf = main_doc.write_pdf()
            # file_data = ContentFile(pdf)
            # c = Cert(test=t)
            # c.file.save('cert.pdf',file_data)
            # c.save()
            attemptQ=[u for u in request.POST.values() if not u==""]
            unattemptQLen=No_of_questions-len(attemptQ)
            incorrectQues=len(attemptQ)-score

            return render(request,'drivingtest/task.html',{
            'score':score,
            'No_of_questions':No_of_questions,
            'Qns':[Question.objects.get(uid= u) for u in request.session['qs']],
            'attemptQns':attemptQ,
            'unattemptQLen':unattemptQLen,
            'incorrectQues':incorrectQues,
            })
        else:
            # t = TestUser(user = request.user)
            # t.save()
            # try:
            #     del request.session['testuid']
            # except:
            #     pass
            # request.session['testuid'] = str(t.uid)
            qq = random.sample(list(Question.objects.all()), No_of_questions)
            request.session['qs'] = [q.uid for q in qq]
            if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
                return render(request,'drivingtest/mobileview/mobilequestions.html',{
                'questions':qq,
                })
            else:
                return render(request,'drivingtest/test.html',{
                'questions':qq,
                })



    # else:
    #     redirect('drivingtest_login')

def ques(request):
    return render(request,'drivingtest/questions.html',{'qs':Question.objects.all()})

def tutorial(request):
    return render(request,'drivingtest/tutorial.html')

def mail_with_body(username,no_of_questions,score,email):
    html_content = render_to_string('drivingtest/test_mailer.html', {'username':username,'no_of_questions':no_of_questions,'score':score}) # render with dynamic value
    text_content = strip_tags(html_content)
    mail = EmailMultiAlternatives('Driving Test | MoRTH | IRSC',text_content,'no-reply@road-safety.co.in',[email,])
    mail.attach_alternative(html_content, "text/html")
    mail.send()
    pass
