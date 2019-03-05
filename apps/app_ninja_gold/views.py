from django.shortcuts import render, redirect, HttpResponse
import random
from time import strftime, localtime

def index(request):
    if 'total' not in request.session:
        request.session['total'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
    return render(request,"index.html")

def process_money(request):
    value = request.POST['hidden']
    time = strftime("%b %d, %Y, %-I:%M %p", localtime())
    if value == 'Farm':
        num = random.randint(10,20)
        request.session['total'] += num
    if value == 'Cave':
        num = random.randint(5,10)
        request.session['total'] += num
    if value == 'House':
        num = random.randint(2,5)
        request.session['total'] += num
    if value == 'Casino':
        num = random.randint(-50,50)
        request.session['total'] += num
    if num >= 0:
        request.session['activities'].insert(0,f"Earned {num} golds from the {value}! ({time})")
    elif num < 0:
        request.session['activities'].insert(0,f"Lost {num} golds to the {value}... Bummer ({time})")
    print("*" * 50)
    print(time)
    print(num)
    print(request.session['total'])
    print(request.session['activities'])
    for activity in request.session['activities']: 
        if activity.startswith('Earned'):
            print(activity)
    print("*" * 50)
    return redirect('/')

def reset(request):
    request.session.flush()
    return redirect('/')
