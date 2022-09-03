import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Question
from django.urls import reverse


class UrlForPolls(TestCase):
    def test_pollspage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions from the future
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)


def create_question(question_text, days):
    """
    Create a question with the given `question_text` and published the given number of `days`.
    :param question_text: Text to be the body of the question.
    :param days: number of day(s) offset to now (negative to publish in the past, positive to publish in the future).
    :return: A question.
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):

    def test_no_questions(self):
        """ If no questions exist, an appropriate message is displayed. """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_questions(self):
        """ Questions with a pub_date in the past are displayed on the index page."""
        past_question = create_question(question_text='Past question', days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], [past_question])

    def test_future_question(self):
        """  Questions with a pub_date in the future aren't displayed on the index page."""
        fut_question = create_question(question_text='Past question', days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_and_future_question(self):
        """Even if both past and future questions exist, only past questions are displayed."""
        past_question = create_question(question_text='Past question', days=-30)
        fut_question = create_question(question_text='Past question', days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], [past_question])

    def test_two_past_questions(self):
        """Two past questions are displayed."""
        past_question_1 = create_question(question_text='Past question', days=-30)
        past_question_2 = create_question(question_text='Past question', days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], [past_question_2, past_question_1])


class QuestionDetailViewTest(TestCase):

    def test_future_question(self):
        """Return 404 (not found) for questions in the future"""
        fut_question = create_question(question_text='future question', days=5)
        url = reverse('polls:detail', args=(fut_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """The detail view of a question with a pub_date in the past displays the question's text."""
        past_question = create_question(question_text='past question', days=-5)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)


class ChoiceCreationTest(TestCase):

    def test_create_choice(self):
        question = create_question('teste', -1)
        choice = question.choice_set.create(choice_text='Choice1', votes=0)
        self.assertContains(Question.choice_set.all(), choice.choice_text)
