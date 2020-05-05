from survey import AnonymousSurvey

question = 'What language did you first learn to speak ?'
my_survey = AnonymousSurvey(question)

my_survey.show_question()

print("Enter q at many time to quit. /n")
while True:
    response = input("Language:")
    if response == 'q':
        break
    else:
        my_survey.store_response(response)

print("\nThank you to enveryone who participated in the survey!")
my_survey.show_result()