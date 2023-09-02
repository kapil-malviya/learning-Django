from django.shortcuts import render

# Create your views here.


def session(request):
    count = request.session.get('count', 0)
    newcount = count + 1
    request.session['count'] = newcount
    print(request.session.get_expiry_age())
    print(request.session.get_expiry_date())
    return render(request, 'testapp/count.html', {'count': newcount})
