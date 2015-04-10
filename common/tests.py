from django.contrib.auth import get_user_model
from model_mommy import mommy


class BehaviorTestCaseMixin(object):

    def get_model(self):
        return getattr(self, 'model')

    def create_instance(self, **kwargs):
        raise NotImplementedError("Implement me!")


class TimestampableTestCase(BehaviorTestCaseMixin):

    def test_timestamped(self):
        obj = self.create_instance()
        self.assertTrue(obj.created)
        self.assertTrue(obj.modified)


class AuthorableTestCase(BehaviorTestCaseMixin):

    def test_authorable(self):
        obj = self.create_instance()
        self.assertTrue(obj.author)

    def test_authorable_by_author(self):
        author = mommy.make(get_user_model())
        obj = self.create_instance(author=author)

        self.assertIn(obj, self.get_model().objects.by_author(author))