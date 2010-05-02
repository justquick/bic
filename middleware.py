from django.shortcuts import render_to_response
from django.template import RequestContext

class UnderConstructionMiddleware(object):
    def process_request(self, request):
        if request.path.startswith('/media') or request.path.startswith('/admin') or request.user.is_authenticated():
            return
        return render_to_response('construction.html', {},
                                  context_instance=RequestContext(request))