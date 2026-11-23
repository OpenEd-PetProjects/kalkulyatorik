# Kalkulyatorik

`calculator.evaluate(expression)` evaluates decimal numbers, `+`, `-`, `*`, `/`, and parentheses using Python 3.10 or later. Invalid or unsupported expressions raise `ValueError`; division by zero raises `ZeroDivisionError`.

```python
from calculator import evaluate

assert evaluate("2 + 2 * 3") == 8
```

Run `just test` to run the same tests as GitHub Actions.
