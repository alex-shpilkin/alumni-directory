from django.conf.urls import url
from views import (
    GradeListView,
    GradeStudentListView,
    StudentDetailView,
    StudentCreateView,
    FieldValueCreateView,
    VoteCreateView,
)


urlpatterns = [
    url(r'^$', GradeListView.as_view(), name='grade-list'),
    url(r'^(?P<grade_id>[0-9]+)/$', GradeStudentListView.as_view(),
        name='student-list'),
    url(r'^students/(?P<pk>[0-9]+)/$', StudentDetailView.as_view(),
        name='student-detail'),
    url(r'^students/add/$', StudentCreateView.as_view(),
        name='student-create'),
    url(r'^(?P<grade_id>[0-9]+)/students/add/$', StudentCreateView.as_view(),
        name='grade-student-create'),
    url(r'^students/(?P<pk>[0-9]+)/add_value/$', FieldValueCreateView.as_view(),
        name='student-value-create'),
    url(r'^fields/(?P<pk>[0-9]+)/(?P<vote_type>\w+)/$', VoteCreateView.as_view(),
        name='field-vote'),
]
