from django.shortcuts import render, redirect
from django.contrib import messages

from .models import TestResult, Result, Question, Test
from lectures.models import Lecture
from .forms import *


def getForm(answers, data=None):
    if answers[1]:
        form = ManyResponsesForm(data=data)
    else:
        form = OneAnswerForm(data=data)
    return form


def test_create(request, lecture_id):
    if request.user.is_teacher == False:
        messages.error(request, 'Недостаточно прав для выполнения операции')
        return redirect('..')
    if request.method == 'POST':
        form = AddTest(data=request.POST)
        if form.is_valid():
            test = form.save(commit=False)
            test.lecture = Lecture.objects.get(id=lecture_id)
            test.save()
            messages.success(request, 'Вы успешно создали тест. Теперь вы можете добавить вопросы')
            return redirect('..')
    else:
        form = AddTest()
    
    context = {
        'form': form
    }
    return render(request, 'tests/add_test.html', context)



def tests_list(request):
    if request.user.is_teacher():
        lectures = Lecture.objects.filter(creator=request.user)
        tests = Test.objects.filter(lecture__in=lectures)
        results = TestResult.objects.filter(test_id__in=tests)
    else:
        results = TestResult.objects.filter(user=request.user)

    context = {
        'test_results': results
    }

    return render(request, 'tests/tests_list.html', context=context)


def question_create(request, lecture_id, type):
    if request.user.is_teacher == False:
        messages.error(request, 'Недостаточно прав для выполнения операции')
        return redirect('..')
    if request.method == 'POST':
        if type == 1:
            form = AddManyResponsesForm(data=request.POST)
        else:
            form = AddOneAnswerForm(data=request.POST)

        if form.is_valid():
            question = form.save(commit=False)
            question.test = Test.objects.get(lecture_id=lecture_id)
            question.save()
            messages.success(request, 'Вы успешно добавили вопрос в тест')
            return redirect('..')
    else:
        if type == 1:
            form = AddManyResponsesForm()
        else:
            form = AddOneAnswerForm()

    context = {
        'form': form
    }
    return render(request, 'tests/question_add.html', context=context)
    


def question_list(request, lecture_id):
    questions = Question.objects.filter(test_id=lecture_id)
    test = Test.objects.filter(lecture_id=lecture_id).first()

    if request.user.is_teacher() == False and TestResult.objects.filter(user=request.user, test=test):
        messages.error(request, 'Вы уже проходили данное тестирование')
        return redirect('..')

    if request.method == 'POST':
        results = Result.objects.filter(question__in=questions, user=request.user)
        correct_count = results.filter(correctly=True).count()
        all_count = results.count()
        max_point = questions.first().test.possible_points
        points = int((max_point / all_count) * correct_count)

        test = Test.objects.get(lecture_id=lecture_id)
        test_result = TestResult(user=request.user, test=test, points=points)
        test_result.save()
        messages.success(request, f'Вы заработали {points} баллов')
        return redirect('..')

    context = {
        'test': test,
        'questions': questions,
        'lecture_id': lecture_id
    }

    return render(request, 'tests/tests_home.html', context=context)


def question_view(request, lecture_id, question_id):
    question = Question.objects.get(id=question_id)
    answers = [question.answer1, question.answer2, question.answer3, question.answer4]

    # Выход из страницы
    results = Result.objects.filter(question=question, user=request.user)
    if results.exists():
        messages.warning(request, 'Вы уже отвечали на этот вопрос')
        return redirect('..')

    if request.method == 'POST':
        form = getForm(answers, request.POST)

        if form.is_valid():
            user_answer = request.POST['answer']
            if user_answer == question.correct_answer:
                is_correct = True
                messages.success(request, 'Верно')
            elif (type(form) == ManyResponsesForm):
                try:
                    if answers[int(user_answer) - 1] == question.correct_answer:
                        is_correct = True
                        messages.success(request, 'Верно')
                finally:
                    pass
            else:
                is_correct = False
                messages.warning(request, 'Неверно')
            result = Result(question=question, user=request.user, correctly=is_correct)
            result.save()
            return redirect('..')
    else:
        form = getForm(answers)

    context = {
        'question': question.question_str,
        'answers': answers,
        'form': form
    }

    return render(request, 'tests/question_detail.html', context=context)
