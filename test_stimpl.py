from stimpl import *

if __name__=='__main__':
  run_stimpl_sanity_tests()
  run_stimpl_robustness_tests()
  #program = While(Lt(Variable("i"), IntLiteral(10)),  Sequence( Assign(Variable("i"), Add(Variable("i"), IntLiteral(10)))))
  #print(run_stimpl(program))
  
