from python_libtemplate import algebra
from python_libtemplate.exceptions import NoRealSolutionError


def test_solve_linear_equation():
    # Test a case where there are infinite solutions.
    assert algebra.solve_linear_equation(0, 0) == "Infinite solutions"

    # Test a case where there's no solution.
    assert algebra.solve_linear_equation(0, 5) == "No solution"

    # Test a standard case.
    assert algebra.solve_linear_equation(2, 8) == -4

    # Another standard case.
    assert algebra.solve_linear_equation(-3, 9) == 3


def test_quadratic_formula_no_real_solution():
    # Custom exception test.
    import pytest
    with pytest.raises(NoRealSolutionError,
                       match="The quadratic equation has no real solution."):
        algebra.quadratic_formula(1, 0, 1)
