KEY = 'numbers_key.txt'
QUESTIONS = 'numbers_questions.txt'
RESPONSE = 'numbers_response.txt'


class read_file():

    def __init__(self,file_name):
        self.file_name = file_name
        self.fileStrings = []
        self.read()
        self.numStrings = len(self.fileStrings)

    def read(self):
        with open(self.file_name, 'r') as r:
            if r.readable:
                for line in r:
                    self.fileStrings.append(line)
            else:
                print('Error: File not Readable')

    def print(self):
        for i in range(self.numStrings):
            print(self.fileStrings[i])

    def print_line(self, line):
        if line < self.numStrings:
            print(self.fileStrings[line])
        else:
            print('Error: line overflow')


class assignment():


    def __init__(self, key, questions, response):
        self.score = {'Correct' : 0 ,
             'incorrect' : 0,
             'Total' : 0 ,
             'Percent' : 0,
             'missed questions' : []
             }
        self.key = read_file(key)
        self.questions = read_file(questions)
        self.response = response


    def admin_Test(self):
    
        answers = []

        for i in range(self.questions.numStrings):
            print(self.questions.fileStrings[i])
            answer = input()
            print('--------------------------------\n\n')
            answers.append(self.questions.fileStrings[i][0] + '. ' + answer + '\n')

        with open(self.response, 'w') as w:
            w.writelines(answers)


    def grade_assign(self):
        response = read_file(self.response)
        for i in range(self.key.numStrings):
            if self.key.fileStrings[i] == response.fileStrings[i]:
                self.score['Correct'] += 1
            else:
                self.score['incorrect'] += 1
                self.score['missed questions'].append(i +1)
            self.score['Total'] += 1
        self.score['Percent'] = (self.score['Correct'] / self.score['Total']) * 100


    def print_score(self):
        print('Results:')
        print()
        for t in self.score:
            print(t, ':', self.score[t])
        print('--------------------------------\n\n')

    def display_missed_questions(self):

        given_answers = read_file(self.response)

        for i in self.score['missed questions']:
             print(self.questions.fileStrings[i - 1])
             print('Answer given: ', given_answers.fileStrings[i-1], '\n')




def main():

    numbers = assignment(KEY, QUESTIONS, RESPONSE)

    numbers.admin_Test()

    numbers.grade_assign()

    numbers.print_score()

    numbers.display_missed_questions()


if __name__ == "__main__":
    main()