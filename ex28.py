from ex28_funcs import *

totals = {'Correct': 0, 'Incorrect': 0}

ask_question(totals, "True and True", True and True)
ask_question(totals, "False and True", False and True)
ask_question(totals, "1 == 1 and 2 == 1", 1 == 1 and 2 == 1)
ask_question(totals, '"test" == "test"', "test" == "test")
ask_question(totals, "1 == 1 or 2 != 1", 1 == 1 or 2 != 1)
ask_question(totals, "True and 1 == 1", True and 1 == 1)
ask_question(totals, "False and 0 != 0", False and 0 != 0)
ask_question(totals, "True or 1 == 1", True or 1 == 1)
ask_question(totals, '"test" == "testing"', "test" == "testing")
ask_question(totals, "1 != 0 and 2 == 1", 1 != 0 and 2 == 1)
ask_question(totals, '"test" != "testing"', "test" != "testing")
ask_question(totals, '"test" == 1', "test" == 1)
ask_question(totals, "not (True and False)", not (True and False))
ask_question(totals, "not (1 == 1 and 0 != 1)", not (1 == 1 and 0 != 1))
ask_question(totals, "not (10 == 1 or 1000 == 1000)", not (10 == 1 or 1000 == 1000))
ask_question(totals, "not (1 != 10 or 3 == 4)", not (1 != 10 or 3 == 4))
ask_question(totals, 'not ("testing" == "testing" and "Zed" == "Cool Guy")', not ("testing" == "testing" and "Zed" == "Cool Guy"))
ask_question(totals, '1 == 1 and not ("testing" == 1 or 1 == 0)', 1 == 1 and not ("testing" == 1 or 1 == 0))
ask_question(totals, '"chunky" == "bacon" and not (3 == 4 or 3 == 3)', "chunky" == "bacon" and not (3 == 4 or 3 == 3))
ask_question(totals, '3 == 3 and not ("testing" == "testing" or "Python" == "Fun")', 3 == 3 and not ("testing" == "testing" or "Python" == "Fun"))

print "************"
score = 100 * float(totals['Correct']) / float(totals['Incorrect'] + totals['Correct'])
print "Your Score: %3.2f %%" % score
print "You answered %i correctly!" % totals['Correct']
print "You answered %i incorrectly" % totals['Incorrect']
print "************"
