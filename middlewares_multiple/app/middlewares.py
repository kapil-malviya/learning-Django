from django.shortcuts import HttpResponse


class Middleware1:
    def __init__(self, get_response):
        self.get_response = get_response
        print('\n One time initialization of  -->  Middleware1 \n')

    def __call__(self, request):
        print('\n This is Middleware1 before view')
        print('Before hitting the view \n')
        response = self.get_response(request)
        print('\n This is Middleware1 after view')
        print('After hitting the view')
        return response
    

class Middleware2:
    def __init__(self, get_response):
        self.get_response = get_response
        print('\n One time initialization of  -->  Middleware2')

    def __call__(self, request):
        print('\n This is Middleware2 before view')
        print('Before hitting the view \n')
        # response = self.get_response(request)
        response = HttpResponse('\t -->|*|*|<-- \t')  # this wont let execute Middleware3 and Views.function, because here itself it is giving HttpResponse
        print('\n This is Middleware2 after view')
        print('After hitting the view \n')
        return response
    

class Middleware3:
    def __init__(self, get_response):
        self.get_response = get_response
        print('\n One time initialization of  -->  Middleware3')

    def __call__(self, request):
        print('\n This is Middleware3 before view')
        print('Before hitting the view \n')
        response = self.get_response(request)
        print('\n This is Middleware3 after view')
        print('After hitting the view \n')
        return response