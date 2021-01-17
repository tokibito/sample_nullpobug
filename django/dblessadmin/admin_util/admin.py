import json
import logging
from django.contrib.admin.models import LogEntry
from django.db import models

logger = logging.getLogger('django.admin')


class LoggingLogEntryManager(models.Manager):
    use_in_migrations = True

    def log_action(self, user_id, content_type_id, object_id, object_repr, action_flag, change_message=''):
        return logger.info(json.dumps(dict(
            user_id=user_id,
            content_type_id=content_type_id,
            object_id=str(object_id),
            object_repr=object_repr[:200],
            action_flag=action_flag,
            change_message=change_message,
        )))


LogEntry.objects.__class__ = LoggingLogEntryManager
