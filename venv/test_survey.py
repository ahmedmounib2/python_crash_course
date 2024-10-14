import unittest
from survey import  AnnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """tests for the class AnonymousSurvey"""
    def test_store_single_response(self):
        """check that a single response is stored properly"""
        question = 'what languages do you speak'
        my_survey = AnnonymousSurvey(question)
        my_survey.store_response('english')
        self.assertIn('english',my_survey.responses)
    def test_store_three_responses(self):
        """test that three individual responses are stored properly"""
        question = 'what languages do you speak'
        my_survey = AnnonymousSurvey(question)
        responses = ['english','spanish', 'mandarin']
        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)

if __name__ == '__main__':
    unittest.main()

# the set up method

import unittest
from survey import AnnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """tests for the class AnonymousSurvey"""
    def setUp(self):
        """ create a survey and a set of responses to use in all test methods"""
        question = "what languages do you speak"
        self.my_survey = AnnonymousSurvey(question)
        self.responses = ['English', ' Spanish', ' Mandarin']

    def test_store_single_response(self):
        """test that a single response is stored properly"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)

    def test_store_three_responses(self):
        """test that three responses are stored properly"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response,self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()
