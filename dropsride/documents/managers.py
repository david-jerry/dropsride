from django.db.models import Q, Manager, Count, Max, Avg
from django.db.models.query import QuerySet


class DocumentsQueryset(QuerySet):
    """Return most used querysets for drivers document

    Args:
        QuerySet (_type_): _description_
    """

    def approved_documents(self):
        return self.filter(approved=True)


class DocumentsManager(Manager):
    def get_queryset(self):
        return DocumentsQueryset(self.model, using=self._db)

    def approved_documents(self):
        return self.get_queryset().approved_documents()

