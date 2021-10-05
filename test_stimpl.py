from stimpl import *

if __name__=='__main__':
  run_stimpl_sanity_tests()
  run_stimpl_robustness_tests()
  #program = If(And(BooleanLiteral(True), BooleanLiteral(False)), Print(StringLiteral("Then")), Print(StringLiteral("Else")))
  #print(run_stimpl(program))
  
