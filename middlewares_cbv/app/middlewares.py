class MyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('\n One time initialization \n')

    def __call__(self, request):
        print('\n This is before view')
        print('Before hitting the view \n')

        response = self.get_response(request)
        print('\n This is after view')
        print('After hitting the view \n')

        return response