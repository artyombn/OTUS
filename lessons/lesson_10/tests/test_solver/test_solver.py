"""
python -m unittest -v lessons.lesson_10.tests.test_solver.test_solver

pytest lessons/lesson_10/tests/test_solver -s -vv
pytest lessons/lesson_10/tests/test_solver -v --last-failed

"""

from unittest import TestCase

import pytest

from lessons.lesson_10.solver.solver import Solver
class SolverTestCase(TestCase):

    # выносим в фикстуру (fixture), чтобы не повторять код
    def setUp(self): # зафиксировано, есть всегда
        self.s = Solver(3, 4)

    def test_add(self):
        # solver = Solver(3, 4)
        # res = solver.add()
        # self.assertEqual(7, res)
        res = self.s.add()
        self.assertEqual(res, self.s.a + self.s.b)

    def test_add_second(self):
        solver = Solver(1, 2)
        res = solver.add()
        self.assertEqual(3, res)

# Чтобы не писать постоянно отдельную ф-цию для проверки, делаем цикл

    def test_add_multi(self):
        for a, b, expected in [(1, 2, 3), (4, 5, 9), (3, 4, 7)]:
            with self.subTest(f'{a} + {b} = {expected}',  # Позволяет проверить остальные тесты в случае падения одного из тестов
                              a=a, b=b, expected=expected):
                solver = Solver(a, b)
                res = solver.add()
                self.assertEqual(expected, res)

    def test_mul(self):
        # solver = Solver(3, 4)
        # res = solver.mul()
        # self.assertEqual(12, res)
        res = self.s.mul()
        self.assertEqual(res, self.s.a * self.s.b)

    def test_raises(self):
        solver = Solver(1, "a")
        # solver.add() # тест провалится
        with self.assertRaises(TypeError):  # используется для проверки того, что определенный кусок кода вызывает ожидаемое исключение
            solver.add() # блок кода в котором ожидаем исключение


# PYTEST
@pytest.fixture()
def solver():
    return Solver(3, 4)

@pytest.fixture(
    params=[
        pytest.param((3, 4), id="3*4=12"),
        pytest.param((5, 6), id="5*6=30"),
    ]
)
def solver_multi(request):
    a, b = request.param
    return Solver(a, b)

class TestSolver:

    # def test_add_single(self):
    #     solver = Solver(3, 4)
    #     res = solver.add()
    #     assert res == 7

    def test_add_single(self, solver):
        res = solver.add()
        assert res == solver.a + solver.b

    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (1, 2, 3),
            (4, 5, 9),
            (3, 4, 7),
            pytest.param(3, 4, 7, id="to seven"),
        ],
    )

    def test_mul(self, solver_multi: Solver):
        assert solver_multi.mul() == solver_multi.a * solver_multi.b


    def test_add_multi(self, a, b, expected, solver):
        solver.a = a
        solver.b = b
        res = solver.add()
        assert res == expected