from django.shortcuts import render, HttpResponse, redirect
import random, datetime

def index(request):
    if 'goldcount' not in request.session:
        request.session['goldcount'] = 0
    
    if 'activity' not in request.session:
        request.session['activity'] = []
    
    if 'goldwon' not in request.session:
        request.session['goldwon'] = 0
    goldwon = 0

    return render(request, 'ninja_gold/index.html')

def result(request):
    if request.method == 'POST':

        request.session['building'] = request.POST['building']

        if request.session['building'] == 'reset':
            request.session.clear()
            return redirect('/')

        if request.session['building'] == 'farm':
            goldwon = random.randrange(10, 21)
            request.session['goldcount'] += goldwon
        if request.session['building'] == 'cave':
            goldwon = random.randrange(5, 11)
            request.session['goldcount'] += goldwon
        if request.session['building'] == 'house':
            goldwon = random.randrange(2, 5)
            request.session['goldcount'] += goldwon
        if request.session['building'] == 'casino':
            goldwon = random.randrange(-50, 51)
            request.session['goldcount'] += goldwon
        
        if request.session['goldcount'] < 0:
            request.session['goldcount'] = 0

        print "redirect here"
        
        request.session['activity'] += [(request.POST['building'],goldwon,datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p"))]

        return redirect('/')
    else:
        return redirect('/')



