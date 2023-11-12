from itertools import count

from django.db.models import Count

from.models import Category,Course
def load_courses(params={}):
    q = Course.objects.filter(active = True)
    kw = params.get('kw')
    if kw:
        q = q.filter(subject__incotains = True)
    cate_id = params('cate_it')
    if cate_id:
        q = q.filter(cate_id=cate_id)
    return q
def count_courses_by_cate():
    return Category.objects.annotate(count=Count('courses__id')).values('id', 'subject', 'name').orderby('count')

