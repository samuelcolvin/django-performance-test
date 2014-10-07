import os
import random
from time import time

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
import django
django.setup()

from performance.models import PerformanceTest

ROWS = 100000
STEPS = 200
LOOKUPS = 10
COL_LEN = 5


def rand_string():
    return ''.join(random.choice('abcde') for _ in range(2))


def rand_int():
    return random.randint(1, 25)


def create_data():
    if PerformanceTest.objects.count() == 0:
        pts = [PerformanceTest(char_field=rand_string(),
                               pos_int=rand_int(),
                               char_field_index=rand_string(),
                               pos_int_index=rand_int()) for _ in range(ROWS)]
        PerformanceTest.objects.bulk_create(pts)
        print 'created %d rows' % PerformanceTest.objects.count()
    else:
        print 'not creating data, already %d rows' % PerformanceTest.objects.count()


def test_direct(field_name):
    if field_name in ('char_field', 'char_field_index'):
        gen = rand_string
    else:
        gen = rand_int
    for step in range(STEPS):
        lookup_val = gen()
        for _ in range(LOOKUPS):
            qs = PerformanceTest.objects.filter(**{field_name: lookup_val})
            qs.count()


def test_in(field_name):
    if field_name in ('char_field', 'char_field_index'):
        gen = rand_string
    else:
        gen = rand_int
    for step in range(STEPS):
        lookup_val = [gen() for _ in range(COL_LEN)]
        for _ in range(LOOKUPS):
            field_name__in = field_name + '__in'
            qs = PerformanceTest.objects.filter(**{field_name__in: lookup_val})
            qs.count()


if __name__ == "__main__":
    # PerformanceTest.objects.all().delete()
    create_data()
    for test in (test_direct, test_in):
        for fn in ('char_field', 'pos_int', 'char_field_index', 'pos_int_index'):
            print test.__name__, fn,
            s = time()
            test(fn)
            print 'time taken %0.3f' % (time() - s)
