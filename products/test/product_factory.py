import factory
import datetime
from factory.django import DjangoModelFactory
from products.models import Product

class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    category = "sauces"
    name = factory.Sequence(lambda n: 'nametest%d' % n)
    url = factory.Sequence(lambda n: 'urltest%d' % n)
    nutrition_grade = factory.Sequence(lambda n: 'nutriscoretest%d' % n)
    substitut = factory.Sequence(lambda n: 'subtest%d' % n)
    owner = factory.Sequence(lambda n: 'usertest%d' % n)
    date = factory.LazyFunction(datetime.datetime.now)
