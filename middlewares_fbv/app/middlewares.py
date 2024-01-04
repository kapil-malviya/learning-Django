def my_middleware(get_response):
    print('\n One Time Initialization \n')

    def my_function(request):
        print('\n This is before view')
        print('before hitting view \n')

        response = get_response(request)
        print('\n This is after view')
        print('After hitting view \n')

        return response
    
    return my_function


# for activating this middleware, add this into MIDDLEWARE in settings.py file 