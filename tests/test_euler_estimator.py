import sys
sys.path.append('src')
from euler_estimator import EulerEstimator

euler = EulerEstimator(derivative = (lambda x: x+1),  point = (1,4))

assert euler.point == (1,4), 'Wrong Point'
assert euler.calc_derivative_at_point() == 2, 'Wrong Derivative'     

euler.step_forward(0.1)
assert euler.point == (1.1, 4.2), 'Wrong Point' 

assert euler.calc_derivative_at_point() == 2.1, 'Wrong Derivative'
euler.step_forward(-0.5)
assert euler.point == (0.6, 3.15), 'wrong point' 
euler.go_to_input(3, 0.5)

assert euler.point == (3, 9.29), 'Weong Point'

print('ALL TESTS PASSED')