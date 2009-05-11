import datetime
from django.db import models
from django.contrib.contenttypes.models import ContentType
from bookmarks import feedparser

class BaseModel(models.Model):
    content_type =  models.ForeignKey(ContentType, editable=False,
            related_name="content_type_set_for_%(class)s")

    def save(self, **kwargs):
        if not self.content_type_id:
            self.content_type = ContentType.objects.get_for_model(self.__class__)
        super(BaseModel, self).save(**kwargs)

    def _get_model_class(self):
        if self.content_type_id:
            return self.content_type.model_class()
        return self.__class__
    model_class = property(_get_model_class)

    def _get_original(self):
        return self.model_class.objects.get(pk=self.pk)
    original = property(_get_original)

    class Meta:
        abstract = True

class ItemNode(BaseModel):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('bookmarks.ItemNode', blank=True, null=True, db_index=True)
    note = models.TextField(blank=True)
    ctime = models.DateTimeField(default=datetime.datetime.now)

    def __unicode__(self):
        return self.name

class Category(ItemNode):
    pass

class Bookmark(ItemNode):
    url = models.URLField(verify_exists=False, unique=True)

class Feed(Bookmark):
    # todo: cache
    def _get_feeds(self):
        if not self.url:
            return None
        return feedparser.parse(self.url)
    feeds = property(_get_feeds)
