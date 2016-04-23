from django.shortcuts import get_object_or_404, render
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.http import HttpResponse
import json
from django.template.loader import render_to_string
from django.shortcuts import render_to_response
from django.template import loader, RequestContext

from .models import Choice, Question


def index(request):
    latest_question_list = Question.objects.filter(pub_date__lte=timezone.now(), choice__isnull = False).distinct().order_by('-pub_date')
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question.objects.filter(pub_date__lte=timezone.now(), choice__isnull = False).distinct(), pk = question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id,choice):
    question = get_object_or_404(Question.objects.filter(pub_date__lte=timezone.now(), choice__isnull = False).distinct(), pk=question_id)
    choices = Choice.objects.filter(question=question_id).order_by('-votes')
    print question
    total = Choice.objects.filter(question=question_id).aggregate(total = Sum('votes'))
    total = total.get('total')
    choice = question.choice_set.get(pk=choice)
    print "Total votes:" , total
    return render(request, 'polls/results.html', {'question': question,'choices': choices,'totalVotes':total,'userChoice':choice})


def vote(request, question_id):
    if request.method == 'POST':
        question = get_object_or_404(Question, pk=question_id)
        data= {}
        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            # Redisplay the question voting form.
            return render(request, 'polls/detail.html', {
                'question': question,
                'error_message': "You didn't select a choice!!!",})
        else:
            selected_choice.votes += 1
            selected_choice.save()
            question = get_object_or_404(Question.objects.filter(pub_date__lte=timezone.now(), choice__isnull = False).distinct(), pk=question_id)
            total = Choice.objects.filter(question=question_id).aggregate(total = Sum('votes'))
            total = total.get('total')
            # data['question']= question
            data['total']= total
            data['userChoice']=selected_choice.choice_text
            print data

            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            # html = render(request,'polls/result.html', {'total':total,'userChoice':selected_choice.choice_text})
            # return render_to_response('polls/detail.html', {'total':total,'userChoice':selected_choice.choice_text},context_instance=RequestContext(request))
            # return HttpResponse(html)
            return HttpResponseRedirect(reverse('polls:results', args=(question.id,request.POST['choice'],)))




