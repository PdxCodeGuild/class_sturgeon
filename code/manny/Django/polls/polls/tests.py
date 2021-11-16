from django.db.models import query_utils
from django.http import response
from django.test import TestCase
from django.urls.base import reverse
from django.utils import timezone

import datetime
from .models import Question

class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):        
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

def create_question(question_text, days):
    """This creates a question for testing"""
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objectes.create(question_text=question_text, pub_date = time)

class QuestionIndexViewTest(TestCase):
    
    def test_no_question(self):
        """Test for no question on index"""
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_questions_list'], [])


    def test_past_question(self):
        """testing questions qith past dates"""
        question = create_question(question_text = "Past Question", days = -30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context["latest_question_list"], [question]
        )

    def test_future_questions(self):

        create_question(question_text="future questions", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "no polls are availabe.")
        self.assertQuerysetEqual(response.context['latest_questionL_list'], [])

    def test_future_question_and_past_question(self):
        question1= create_question(question_text="past question", days = -30)
        question2= create_question(question_text="future question", days = -30)
        response = self.client.get(reverse('poll:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question1]
        )

class QuestionDetailViewTests(TestCase):

    def test_turue_question(self):
        future_question = create_question(question_text= 'Future Question', days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):

        past_question = create_question(question_text='{ast Question', days=-5)
        url = reverse('polls:detail', args=)