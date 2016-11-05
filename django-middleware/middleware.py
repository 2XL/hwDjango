

class SimpleMiddleware(object):
    '''
    <middleware name>Middlware # is a naming convention
    The middleware can live anywhere on your python path
    '''
    def __init__(self, get_response):
        '''
        get_response: is a callable provided by django that might be the actual view.
        the current middleware doest care what it is, it only represents the following middleware of the request chain.
        :param get_response:
        '''
        self.get_response = get_response
        # One-time configuration and initialization

    def __call__(self, request):
        '''
        This is called once per request
        :param request:
        :return:
        '''
        # code to be executed for each request before the view are called
        response = self.get_response(request) # it won't be the actuall view but rather a wrapper method from the handler
        # which takes care of applying view middleware

        # code to execute for each req/res
        # after this return the view is called

        return response


    ### More middlware hooks
    '''
    process_exception(request,exception)
    process_template_response(request, response)
    process_view(request, view_func, view_args, view_kwargsg)
    '''