from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question, Answer


def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    answer_list = Answer.objects.filter(question_id = question_id)
    context = {'question': question, 'answer_list': answer_list}
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    #form에 POST된 내용을 바탕으로 question 객체에 연결되는 answer 객체를 생성
    answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
    answer.save()
    return redirect('pybo:detail', question_id=question.id)



def question_form(request):
    return render(request, 'pybo/question_form.html')


def question_create(request):
    author = request.user
    question = Question(author = author, subject = request.POST.get('subject'), content=request.POST.get('content'), create_date=timezone.now())
    question.save()
    return redirect('pybo:index')
    #return redirect('pybo:detail', question_id=question.id)


    