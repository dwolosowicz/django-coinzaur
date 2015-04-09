from django.db.models import QuerySet


class AuthorableQuerySet(QuerySet):

    def by_author(self, author):
        """Filters the queryset by the author property"""
        return self.filter(author=author)