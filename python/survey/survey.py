class AnonymousSurvey():

    def __init__(self, question):
        self.question = question
        self.response = []

    def show_question(self):
        print(self.question)

    def store_response(self, new_response):
        self.response.append(new_response)

    def show_result(self):
        print("Survey result:")
        for res in self.response:
            print('-' +  res)

