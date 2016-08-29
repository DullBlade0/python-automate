#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

import random

# The quiz data. Keys are states and values are their capitals.
# This is using a dictionary btw.

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 
   'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 
   'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quizNum in range(35):
  #Create the quiz and answers files.
  quizFile = open('capitalquiz%s.txt' % (quizNum + 1), 'w')
  answerKeyFile = open('capitalquiz_answers%s.txt' % (quizNum+1),'w')

  #Write out the header on each quiz
  quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
  quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum+1))
  quizFile.write('\n\n')

  #Shuffle the order of the states.
  states = list(capitals.keys()) # This part inserts the keys/states into a list
  random.shuffle(states)  #Shuffles the list of states so the quizzes are different

  #Loop through all 50 states, making a question for each.
  for questionNum in range(50):
    #Get right and wrong answers
    correctAnswer = capitals[states[questionNum]] # states gives the key for capitals to generate the right answer from the dictinary
    wrongAnswers = list(capitals.values())  #Creates a new list for the wrong answers values() is the value assigned to a key
    del wrongAnswers[wrongAnswers.index(correctAnswer)] #index to delete the correct answer from wrong answer list.
    wrongAnswers = random.sample(wrongAnswers, 3) #Chooses randomly three wrong answers and replaces the current wrong list
    answerOptions = wrongAnswers + [correctAnswer] #Creates a list for the given question
    random.shuffle(answerOptions) #Shuffles the answers

    #Write the question and the answer options to the quiz file.
    quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1, states[questionNum])) #Writes the question for the current question
    for i in range(4):
      quizFile.write(' % s. %s\n' % ('ABCD'[i], answerOptions[i]))   #Places the answers.
    quizFile.write('\n')  
    answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)])) #Writes to the answer file
  quizFile.close()
  answerKeyFile.close()

