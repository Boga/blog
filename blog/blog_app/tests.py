import datetime

from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils import timezone

from .models import Note


def create_note(days, title='Note title', body=''):
    time = timezone.now() + datetime.timedelta(days=days)
    return Note.objects.create(title=title, body=body, pub_date=time)


class QuestionViewTests(TestCase):
    def test_index_view_with_no_questions(self):
        """
        If no questions exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('blog_app:notes_index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No notes are available.")
        self.assertQuerysetEqual(response.context['notes'], [])

    def test_index_view_with_a_past_question(self):
        note = create_note(title="Past note.", days=-30)
        response = self.client.get(reverse('blog_app:notes_index'))
        self.assertQuerysetEqual(
                response.context['notes'],
                ['<Note: %r Past note.>' % note.id]
        )

    def test_index_view_with_a_future_question(self):
        """
        Questions with a pub_date in the future should not be displayed on
        the index page.
        """
        create_note(title="Future question.", days=30)
        response = self.client.get(reverse('blog_app:notes_index'))
        self.assertContains(response, "No notes are available.",
                            status_code=200)
        self.assertQuerysetEqual(response.context['notes'], [])

    def test_index_view_with_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        should be displayed.
        """
        note_p = create_note(title="Past note.", days=-30)
        note_f = create_note(title="Future note.", days=30)
        response = self.client.get(reverse('blog_app:notes_index'))
        self.assertQuerysetEqual(
                response.context['notes'],
                ['<Note: %r Past note.>' % note_p.id]
        )

    def test_index_view_with_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        note1 = create_note(title="Past note 1.", days=-30)
        note2 = create_note(title="Past note 2.", days=-5)
        response = self.client.get(reverse('blog_app:notes_index'))
        self.assertQuerysetEqual(
                response.context['notes'],
                [
                    '<Note: %r Past note 2.>' % note2.id,
                    '<Note: %r Past note 1.>' % note1.id
                ]
        )


class QuestionIndexDetailTests(TestCase):
    def test_detail_view_with_a_future_question(self):
        """
        The detail view of a question with a pub_date in the future should
        return a 404 not found.
        """
        note_f = create_note(title='Future note.', days=5)
        response = self.client.get(reverse('blog_app:note_details',
                                           args=(note_f.id,)))
        self.assertEqual(response.status_code, 404)

    def test_detail_view_with_a_past_question(self):
        """
        The detail view of a question with a pub_date in the past should
        display the question's text.
        """
        note_p = create_note(title='Past note.', days=-5)
        response = self.client.get(reverse('blog_app:note_details',
                                           args=(note_p.id,)))
        self.assertContains(response, note_p.title,
                            status_code=200)
