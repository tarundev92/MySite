from django.db import models
from django.utils import timezone
import datetime

from django.core.urlresolvers import reverse

from django.test import TestCase

from .models import Question

def create_question(question_text, days):
    """
    Creates a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text,pub_date=time)

def create_single_choice(choice, choice_text):
    """
    Creates a choice to the given object with the given `choice_text`.
    """
    return choice.choice_set.create(choice_text=choice_text)


class QuestionMethodTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertEqual(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=30)
        old_question = Question(pub_date=time)
        self.assertEqual(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() should return True for questions whose
        pub_date is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=1)
        recent_question = Question(pub_date=time)
        self.assertEqual(recent_question.was_published_recently(), True)

    
class QuestionViewTests(TestCase):

   def test_index_view_with_no_questions(self):
        """
        If no questions exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

   def test_index_view_with_a_past_question_and_a_choice(self):
        """
        Questions with a pub_date in the past should be displayed on the
        index page.
        """
        past_question=create_question(question_text="Past question.", days=-30)
        create_single_choice(past_question, choice_text='Past Choice')
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(	
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

   def test_index_view_with_a_future_question_and_a_choice(self):
        """
        Questions with a pub_date in the future should not be displayed on
        the index page.
        """
        future_question=create_question(question_text="Future question.", days=30)
        create_single_choice(future_question, choice_text='Future Choice')        
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls available.", status_code=200)
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

   def test_index_view_with_future_question_with_choice_and_past_question_with_choice(self):
        """
        Even if both past and future questions exist, only past questions
        should be displayed.
        """
        past_question=create_question(question_text="Past question.", days=-30)
        create_single_choice(past_question, choice_text='Past Choice')
        future_question=create_question(question_text="Future question.", days=30)
        create_single_choice(future_question, choice_text='Future Choice')        
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: Past question.>'])

   def test_index_view_with_two_past_questions_with_choice(self):
        """
        The questions index page may display multiple questions.
        """
        past_question1=create_question(question_text="Past question 1.", days=-30)
        create_single_choice(past_question1, choice_text='Past question 1 Choice')
        past_question2=create_question(question_text="Past question 2.", days=-5)
        create_single_choice(past_question2, choice_text='Past question 2 Choice')
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: Past question 2.>', '<Question: Past question 1.>'])

   def test_index_view_with_a_question_no_coices(self):
       """
       The question index page should not display questio with no choice
       """
       create_question(question_text="No choice question.", days=0)
       response = self.client.get(reverse('polls:index'))
       self.assertContains(response, "No polls available.", status_code=200)
        
class QuestionIndexDetailTests(TestCase):

    def test_detail_view_with_a_future_question(self):
        """
        The detail view of a question with a pub_date in the future should
        return a 404 not found.
        """
        future_question = create_question(question_text='Future question.',
                                          days=5)
        create_single_choice(future_question, choice_text='Future Choice')
        response = self.client.get(reverse('polls:detail',args=(future_question.id,)))
        self.assertEqual(response.status_code, 404)

    def test_detail_view_with_a_past_question(self):
        """
        The detail view of a question with a pub_date in the past should
        display the question's text.
        """
        past_question = create_question(question_text='Past Question.',
                                        days=-5)
        create_single_choice(past_question, choice_text='Choice')
        response = self.client.get(reverse('polls:detail',
                                   args=(past_question.id,)))
        self.assertContains(response, past_question.question_text,
                            status_code=200)

