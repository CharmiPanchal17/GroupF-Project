from django.test import TestCase
from django.utils import timezone
from django.core import mail
from django.contrib.auth import get_user_model

from .models import Student, Lecturer, Registrar, Department, Issue, Notification

User = get_user_model()

class UserModelTests(TestCase):

    def test_create_student_user(self):
        email = 'test@students.mak.ac.ug'
        password = 'studentpass123'
        user = User.objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertEqual(user.role, 'student')
        self.assertFalse(user.is_verified)
        self.assertTrue(user.verification_token is not None)

        # Check if email was sent
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn('Verify Your Email Address', mail.outbox[0].subject)

    def test_create_lecturer_user(self):
        email = 'lecturer@mak.ac.ug'
        password = 'lecturerpass123'
        user = User.objects.create_user(email=email, password=password)

        self.assertEqual(user.role, 'lecturer')

    def test_create_registrar_user(self):
        email = 'registrar1@mak.ac.ug'
        password = 'registrarpass123'
        user = User.objects.create_user(email=email, password=password)

        self.assertEqual(user.role, 'registrar')

    def test_superuser_creation(self):
        email = 'admin@mak.ac.ug'
        user = User.objects.create_superuser(email=email, password='adminpass')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_verified)


class ProfileModelTests(TestCase):
    def setUp(self):
        self.student_user = User.objects.create_user(email='john@students.mak.ac.ug', password='test123')
        self.lecturer_user = User.objects.create_user(email='jane@mak.ac.ug', password='test123')
        self.registrar_user = User.objects.create_user(email='registrar1@mak.ac.ug', password='test123')

    def test_student_profile_creation(self):
        student = Student.objects.create(
            user=self.student_user,
            student_no='2023-BCS-001',
            year=1,
            course='cs'
        )
        self.assertEqual(student.course, 'cs')

    def test_lecturer_and_department(self):
        dept = Department.objects.create(department_id=1, name="Computer Science")
        lecturer = Lecturer.objects.create(user=self.lecturer_user, department=dept)
        self.assertEqual(lecturer.department.name, "Computer Science")

    def test_registrar_profile_creation(self):
        registrar = Registrar.objects.create(user=self.registrar_user, college="Computing and IS")
        self.assertEqual(registrar.college, "Computing and IS")


class IssueModelTests(TestCase):
    def setUp(self):
        self.student_user = User.objects.create_user(email='student@students.mak.ac.ug', password='test123')
        self.lecturer_user = User.objects.create_user(email='lecturer@mak.ac.ug', password='test123')

    def test_issue_creation(self):
        issue = Issue.objects.create(
            year=2025,
            semester='1',
            course_unit='Data Structures',
            lecturer_name='Dr. Doe',
            issue_details='Exam marks not uploaded.',
            submitted_by=self.student_user,
            assigned_to=self.lecturer_user,
        )
        self.assertEqual(issue.status, 'pending')
        self.assertEqual(issue.course_unit, 'Data Structures')

    def test_issue_status_update(self):
        issue = Issue.objects.create(
            course_unit='OOP',
            lecturer_name='Prof. Smith',
            issue_details='Missing coursework marks',
            submitted_by=self.student_user
        )
        issue.status = 'resolved'
        issue.resolved_at = timezone.now()
        issue.save()
        self.assertEqual(issue.status, 'resolved')
        self.assertIsNotNone(issue.resolved_at)


class NotificationModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='user@mak.ac.ug', password='test123')

    def test_create_notification(self):
        notif = Notification.objects.create(user=self.user, message="Your issue has been resolved.")
        self.assertIn("resolved", notif.message)
        self.assertEqual(notif.user.email, self.user.email)
