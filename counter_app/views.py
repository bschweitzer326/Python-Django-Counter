from django.shortcuts import render, redirect

def root(request):

    if 'count' in request.session:
        request.session['count'] += 1
    else:
        request.session['count'] = 1
    if 'visit' in request.session:
        request.session['visit'] += 1
    else:
        request.session['visit'] = 1
    
    context = {
        'count' : request.session['count'],
        'visit' : request.session['visit'],
    }

    return render(request, "counter.html",context)

def destroy(request):
    del request.session['count']
    del request.session['visit']
    return redirect("/")

def two(request):

    if 'count' in request.session:
        request.session['count'] += 1
    
    return redirect("/")

def any(request):

    if 'count' in request.session:
        request.session['count'] += int(request.POST['num'])-1

    return redirect("/")