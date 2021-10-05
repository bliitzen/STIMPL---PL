from stimpl import *

if __name__=='__main__':
  run_stimpl_sanity_tests()
  run_stimpl_robustness_tests()
  #program = Divide(Assign(Variable("i"),IntLiteral(10)), Add(Variable("i"), Assign(Variable("j"), IntLiteral(10))))
  #print(run_stimpl(program))
  
