from django.shortcuts import render
from toster.models import QandAModel
from random import randint

def index(request):
    return render(request, 'toster/index.html')

def test99(request):
    if request.method == "GET":
        rand_lst = set()
        while len(rand_lst) < 5:
            k = randint (1,10)
            rand_qs = QandAModel.objects.get(id = k)
            question = rand_qs.answer
            answer = rand_qs.answer
            item = (question, answer)
            rand_lst.add(item)
            rand_lst = list.add(item)
        right_answers = [rand_lst[0][1],  rand_lst[1][1], rand_lst[2][1], rand_lst[3][1], rand_lst [4][1], rand_lst [5][1]]
        request.session['ans'] = right_answers
        context = {'Q1': rand_lst[0][1], 'Q2': rand_lst[1][1], 'Q3': rand_lst[2][1], 'Q4': rand_lst[3][1], 'Q5': rand_lst[4][1]}
        return  rander(request, 'toster/test.html', context)
    if request.method == 'POST':
        result = request.POST
        answers = [result['A1'], result['A2'], result['A3'], result['A4'], result['A5']]
        right_answers = request. session['ans']
        k = 0
        mistakes = []
        for i in range(5):
            if answers[i] == right_answers[i]:
                k += 1
            else:
                mistakes.append(i + 1)
            num = len(mistakes)
        request.session['res'] = {'result': k, 'mistakes': mistakes, 'number_mistaces': num}
        context = request.session['res']
    return render(request, 'toster/test99.html', context)