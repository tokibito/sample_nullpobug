# Create your views here.
from django.conf import settings
from django.utils import simplejson
from django.http import HttpResponse
from django.core.exceptions import *
from bookmarks.models import *
from bookmarks import feedparser

def make_simple_response(data={}, msg=u'ok', status=200):
    c = {'msg': msg}
    c.update(data)
    #return HttpResponse(simplejson.dumps(data),
    #        content_type='application/json; charset=%s' % settings.DEFAULT_CHARSET)
    return HttpResponse(simplejson.dumps(c), status=status)

def make_simple_response404(msg=u'not found'):
    return make_simple_response(msg=msg, status=404)

def _make_item_dict(itemnode):
    item = {
        'id': itemnode.id,
        'name': itemnode.name,
        'note': itemnode.note,
        'content_type': itemnode.model_class.__name__
    }
    if isinstance(itemnode.original, Bookmark):
        item.update({
            'url': itemnode.original.url,
        })
    if isinstance(itemnode.original, Feed):
        item.update({
            'url': itemnode.original.url,
        })
    return item

def get_bookmarks(request):
    parent_id = request.GET.get('parent')
    itemnodes = ItemNode.objects.filter(parent=parent_id).order_by('content_type')

    return make_simple_response({
        'itemnodes': [_make_item_dict(itemnode) for itemnode in itemnodes]
    })

def get_feeds(request):
    url = request.GET.get('url')
    feed = feedparser.parse(url)
    return make_simple_response({
        'entries': [{
            'title': entry['title'],
            'link': entry['link']
        } for entry in feed.entries]
    })
