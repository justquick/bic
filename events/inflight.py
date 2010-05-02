# The Inflight module definition for your module
from cms import modules

class Events:
    
    label = 'events'  # internal
    urls = 'events.urls'  # urls file gets added to URLs for inflight when module is active
    tab_text = 'Events'
    tab_url = '/inflight/events/'
    admin_required = True   # does the user need to be an admin to access this module?
    public_url = '^events/'
    
modules.site.register(Events, 'events')

from django.template.defaultfilters import truncatewords_html, striptags
from events.models import Event

class SearchableEvent(object):	
	def get_results(self, keywords):
		results = []
		for event in Event.on_site.upcoming():
			title_score = event.name.lower().count(keywords) * 5 # Name has five times the relevance of description
			desc_score = event.description.lower().count(keywords)
			total_score = title_score + desc_score
			snippet = event.description
			if total_score > 0:
				import textile
				snippet = truncatewords_html(textile.textile(snippet.encode('ascii','xmlcharrefreplace')), 25)
				results.append((event, event.name, snippet, total_score))
		return results