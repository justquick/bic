from django.conf.urls.defaults import *
from django.utils.simplejson import dumps
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from events.models import Event

event_dict = {
	'queryset': Event.on_site.all(),
	'template_object_name': 'event'
}

def eventlist(request):
	def _mapper(e):
		d = {
			'id':e.pk,
			'url':e.get_absolute_url(),
			'title':unicode(e),
		}
		if e.start:
			d['start'] = e.start
		if e.end:
			d['end'] = e.end
		return d
	return HttpResponse(dumps(map(_mapper, Event.on_site.upcoming()), cls=DjangoJSONEncoder), mimetype='application/json')

urlpatterns = patterns('django.views.generic',
	(r'^events.json$', eventlist),
	url(r'^event-(?P<object_id>\d+)/$', 'list_detail.object_detail', event_dict, name="event-detail"),
	url(r'^(?P<year>\d{4})/$','date_based.archive_year', dict(event_dict, allow_future=True, date_field='start', allow_empty=True, make_object_list=True)),
	url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$','date_based.archive_month', dict(event_dict, allow_future=True, date_field='start', allow_empty=True)),
)
