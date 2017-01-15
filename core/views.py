# coding=utf-8
import itertools
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

from models import Grade, Student, FieldValue, AuthCode
from forms import StudentCreateForm, FieldValueForm


class GradeListView(ListView):
    model = Grade


class GradeStudentListView(ListView):
    model = Student

    def get(self, request, *args, **kwargs):
        if not Grade.objects.filter(id=self.kwargs.get('grade_id')).exists():
            raise Http404()
        return super(GradeStudentListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        qs = super(GradeStudentListView, self).get_queryset()
        return qs.filter(main_grade_id=self.kwargs.get('grade_id'))

    def get_context_data(self, **kwargs):
        context_data = super(GradeStudentListView, self).get_context_data(**kwargs)
        context_data['grade'] = Grade.objects.get(id=self.kwargs.get('grade_id'))
        return context_data


class StudentDetailView(DetailView):
    model = Student

    def get_context_data(self, **kwargs):
        context_data = super(StudentDetailView, self).get_context_data(**kwargs)

        grouped_modifications_iterator = itertools.groupby(
            self.object.modifications.order_by('field_name'),
            lambda modification: modification.field_name
        )
        context_data['grouped_modifications'] = {
            field_name: list(field_values)
            for field_name, field_values
            in grouped_modifications_iterator
        }

        return context_data


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentCreateForm

    def get_initial(self):
        """
        Если id класса есть в url, добавляем год и букву в initial
        """
        initial = super(StudentCreateView, self).get_initial()
        if 'grade_id' in self.kwargs:
            try:
                grade = Grade.objects.get(id=self.kwargs.get('grade_id'))
            except Grade.objects.DoesNotExist:
                pass
            else:
                initial['graduation_year'] = grade.graduation_year
                initial['grade_letter'] = grade.letter
        return initial

    def form_valid(self, form):
        self.object = form.save(commit=False)

        # Привязываем код авторизации и создаем для него запись в таблице кодов
        if 'auth_code' in form.cleaned_data:
            author_code = AuthCode.objects.get_by_code(
                form.cleaned_data['auth_code'])
            self.object.creator_code = author_code

        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class FieldValueCreateView(CreateView):
    model = FieldValue
    form_class = FieldValueForm

    def form_valid(self, form):
        self.object = form.save(commit=False)

        # Привязываем правку к выпускнику по id из урла
        student_id = self.kwargs.get('pk')
        try:
            self.object.target = Student.objects.get(id=student_id)
        except Student.objects.DoesNotExist:
            return Http404()

        # Привязываем код авторизации и создаем для него запись в таблице кодов
        if 'auth_code' in form.cleaned_data:
            author_code = AuthCode.objects.get_by_code(
                form.cleaned_data['auth_code'])
            self.object.author_code = author_code

        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('student-detail', args=[str(self.kwargs['pk'])])