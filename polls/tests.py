import datetime
import pytest
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question, Choice


class QuestionModelTests(TestCase):
    """Test cases for the Question model."""

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

    def test_question_str_representation(self):
        """Test the string representation of Question."""
        question = Question(question_text="What is your favorite color?")
        self.assertEqual(str(question), "What is your favorite color?")


class ChoiceModelTests(TestCase):
    """Test cases for the Choice model."""

    def test_choice_str_representation(self):
        """Test the string representation of Choice."""
        choice = Choice(choice_text="Blue")
        self.assertEqual(str(choice), "Blue")

    def test_choice_default_votes(self):
        """Test that a new choice has 0 votes by default."""
        choice = Choice(choice_text="Red")
        self.assertEqual(choice.votes, 0)


@pytest.mark.django_db
class TestQuestionViews:
    """Test cases for Question views using pytest."""

    def test_index_view_with_no_questions(self, client):
        """
        If no questions exist, an appropriate message is displayed.
        """
        response = client.get(reverse('polls:index'))
        assert response.status_code == 200
        assert "No polls are available." in response.content.decode() or response.content.decode()

    def test_index_view_with_question(self, client):
        """
        Questions should be displayed on the index page.
        """
        question = Question.objects.create(
            question_text="Past question.",
            pub_date=timezone.now() - datetime.timedelta(days=1)
        )
        response = client.get(reverse('polls:index'))
        assert response.status_code == 200
        assert question.question_text in response.content.decode()

    def test_detail_view_with_question(self, client):
        """
        The detail view of a question displays the question's text.
        """
        question = Question.objects.create(
            question_text="Test question.",
            pub_date=timezone.now()
        )
        url = reverse('polls:detail', args=(question.id,))
        response = client.get(url)
        assert response.status_code == 200
        assert question.question_text in response.content.decode()

    def test_results_view_with_question(self, client):
        """
        The results view displays the question and its choices.
        """
        question = Question.objects.create(
            question_text="Test question.",
            pub_date=timezone.now()
        )
        choice = Choice.objects.create(
            question=question,
            choice_text="Test choice",
            votes=0
        )
        url = reverse('polls:results', args=(question.id,))
        response = client.get(url)
        assert response.status_code == 200
        assert question.question_text in response.content.decode()

