from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

import datetime

from .models import Question



# ------- MODEL TESTS ------------- #
class QuestionModelTests (TestCase):

    def test_was_published_recently_with_future_question (self):
        # future questions showing as recently published
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
    
    def test_was_published_recently_with_old_question (self):
        # Ensures question older than a day dont show recent
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)
    
    def test_was_published_recently_with_recent_question (self):
        # ensures True result from recently posted Question
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)
    


def create_question (question_text, days):
    # creates question for testing
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)



# ---------- INDEX TESTS ------------ #

class QuestionIndexViewTest (TestCase):
    
    def test_no_questions (self):
        # tests for no questions on index
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question (self):
        # testing questions with past pub_dates
        question = create_question(question_text="Past question", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question]
        )
    
    def test_future_questions (self):
        # tests to make sure future posts dont show
        create_question(question_text='future questions', days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_question_and_past_question (self):
        # tests one of each, future and past question
        question1 = create_question(question_text='Past question', days=-30)
        question2 = create_question(question_text='Future question', days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question1]
        )
    
    def test_two_past_questions (self):
        #checks for more than one past question
        question1 = create_question(question_text='Past question 1', days=-30)
        question2 = create_question(question_text='Past question 2', days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question2, question1]
        )



# --------- DETAIL TESTS --------- #

class QuestionDetailViewTests (TestCase):

    def test_future_question (self):
        # tests to ensure future posts cant be seen in detail view
        future_question = create_question(question_text='Future question', days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question (self):
        # tests to ensure questions older than now show properly
        past_question = create_question(question_text='Past question', days=-5)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)
    

