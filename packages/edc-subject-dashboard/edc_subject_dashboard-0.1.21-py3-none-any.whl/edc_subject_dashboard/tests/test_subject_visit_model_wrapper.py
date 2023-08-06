from django.test import TestCase, tag
from edc_appointment.models import Appointment
from edc_base.utils import get_utcnow

from ..model_wrappers import SubjectVisitModelWrapper
from .models import SubjectVisit


class MySubjectVisitModelWrapper(SubjectVisitModelWrapper):

    model = "edc_subject_dashboard.subjectvisit"


class TestModelWrapper(TestCase):
    def setUp(self):
        self.subject_identifier = "12345"

    def test_(self):
        model_obj = SubjectVisit()
        wrapper = MySubjectVisitModelWrapper(model_obj=model_obj)
        self.assertEqual(wrapper.model, "edc_subject_dashboard.subjectvisit")
        self.assertEqual(wrapper.model_cls, SubjectVisit)

    def test_knows_appointment(self):
        appointment = Appointment.objects.create(
            subject_identifier=self.subject_identifier,
            appt_datetime=get_utcnow(),
            appt_reason="scheduled",
        )
        subject_visit = SubjectVisit.objects.create(appointment=appointment)
        wrapper = MySubjectVisitModelWrapper(model_obj=subject_visit)
        self.assertEqual(str(appointment.id), wrapper.appointment)
