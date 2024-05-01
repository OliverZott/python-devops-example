"""For local module testing

- python setup.py sdist bdist_wheel
- pip install dist/velosaurus_sum-1.0.4-py3-none-any.whl
- python .\\src\test_package\test.py
"""

import velosaurus_sum

print(velosaurus_sum.calculator.sum(2, 4))
print(velosaurus_sum.sum(4, 5))
