def ask_question (totals, string_question, question):
        print "What is:"
        your_answer = raw_input(string_question + "\n")
        real_answer = str(question)
        if your_answer == real_answer:
                print "You are correct!"
                totals['Correct'] += 1
        else:
                print "You are wrong!"
                print "You said %r, but the real answer is %r" % (your_answer, real_answer)
                totals['Incorrect'] += 1
