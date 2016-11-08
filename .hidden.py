import logging

from django.http import HttpResponseRedirect
from django.views.generic import View

logger = logging.getLogger('django')


class UserRedirect(View):
    def get(self, request):
        if request.user.is_authenticated():
            logger.info('authorized user')
            return HttpResponseRedirect('/user/' + request.user.username)
        else:
            logger.info('unauthorized user')
            return HttpResponseRedirect('/login/')
