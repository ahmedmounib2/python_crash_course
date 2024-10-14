
class AnnonymousSurvey:
    """collect annonymous answers to a survey questions"""
    
    def __init__(self,question):
        """store a question and prepare to store a response"""
        self.question = question
        self.responses = []
        
    def show_question(self):
        """show the survey question"""
        print(self.question)
        
    def store_response(self,new_response):
        self.new_response = new_response
        self.responses.append(self.new_response)
        
    def show_results(self):
        """show all the responses that you have been given"""
        print("survey results")
        for response in self.responses:
            print(f"{response}")

