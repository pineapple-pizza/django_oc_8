import factory
from factory.django import DjangoModelFactory
from authentication.models import User

class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: 'usertest%d' % n)
    password = factory.Sequence(lambda n: 'password%d' % n)
    email = factory.Sequence(lambda n: 'test%d@test.com' % n)
