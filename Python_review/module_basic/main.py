
import test_module as test

radius = test.number_input()
print(test.get_circumference(radius))
print(test.get_circle_area(radius))


import test_module

print("#메인의__name__출력")
print(__name__)
print()