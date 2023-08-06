import ctypes
import sys
import os
import time
import math

import numpy

from physlearn.Optimizer.NelderMead import NelderMeadAbstract
from physlearn.Optimizer.OptimizeResult import OptimizeResult


class NelderMeadCtypes(NelderMeadAbstract):
    prev_update_time = 0

    module = str(sys.modules['physlearn.Optimizer.NelderMead'])
    split_path = module.split('\'')
    dir_path = os.path.split(split_path[3])

    lib = ctypes.CDLL(dir_path[0] + '/bin/neldermead.so')

    c_set_simplex = lib.set_simplex
    c_set_params = lib.set_params
    c_iteration = lib.iteration
    c_optimize = lib.optimize
    c_return_best_point = lib.return_best_point
    c_free_simplex = lib.free_simplex

    def __init__(self, min_element=-1, max_element=1):
        self.dot_str = ''
        self.amount_of_dots = 0
        self.print_str = ''
        self.func = None
        super().__init__(min_element, max_element)
        self.update_iter = -1

    def calc_func(self, params):
        return self.func(params)

    def update_progress_b(self, i, speed, percent):
        eraser = ''.ljust(len(self.print_str))
        sys.stderr.write(eraser + '\r')
        if self.amount_of_dots == 4:
            self.dot_str = ''
            self.amount_of_dots = 0
        self.dot_str += '.'
        self.amount_of_dots += 1
        speed_str = '{:.3f}'.format(speed)
        self.print_str = self.dot_str.ljust(5) + str(i) + ' (' + str(
            percent) + '%) ' + speed_str + ' it\s'
        sys.stderr.write(self.print_str + '\r')

    def optimize(self, func, dim, end_cond, min_cost=1e-5):
        # func - оптимизируемая функция, должна принимать numpy.array соотвесвтующей размерности в качесвте параметра
        # dim - размерность функции
        # end_method - условие останова
        # 'variance' - дисперсия набора значений функции симплкса должна быть меньше end_cond
        # 'max_iter' - остановка при достижении end_cond итераций
        self.func = func

        def temp_func(temp_x, temp_dim):
            true_x = numpy.array(temp_x[:temp_dim])
            return self.func(true_x)

        self.dim = dim

        double = ctypes.c_double
        c_func_a = ctypes.CFUNCTYPE(double, ctypes.POINTER(double), ctypes.c_int)
        c_func = c_func_a(temp_func)

        self.x_points = self.create_points()  # Создаем точки
        # Вычисляем значение функции в точках
        self.y_points = numpy.zeros(self.dim + 1)
        for index, x in enumerate(self.x_points):
            self.y_points[index] = self.calc_func(x)

        c_dim = ctypes.c_int(self.dim)
        c_x_points = numpy.ctypeslib.as_ctypes(self.x_points)
        c_y_points = numpy.ctypeslib.as_ctypes(self.y_points)
        c_alpha = double(self.alpha)
        c_beta = double(self.beta)
        c_gamma = double(self.gamma)
        self.c_set_simplex(c_dim, c_x_points, c_y_points)
        self.c_set_params(c_alpha, c_beta, c_gamma)
        self.dot_str = ''
        self.print_str = ''

        def update_pb(i):
            cur_time = time.time()
            if (cur_time - self.prev_update_time) >= 1:
                delta = cur_time - self.start_time
                self.speed = i / delta
                self.percent_done = math.floor(i * 100 / end_cond)
                self.update_progress_bar(i)
                self.prev_update_time = cur_time

        c_upb_a = ctypes.CFUNCTYPE(None, ctypes.c_int)
        c_upb = c_upb_a(update_pb)

        self.start_time = time.time()
        self.prev_update_time = 0
        self.c_optimize(c_func, c_upb, ctypes.c_int(end_cond))

        best_point = numpy.zeros(self.dim)
        c_best_point = numpy.ctypeslib.as_ctypes(best_point)
        self.c_return_best_point(c_best_point)
        best_point = numpy.ctypeslib.as_array(c_best_point, self.dim)

        end_time = time.time()
        total_time = end_time - self.start_time

        result = OptimizeResult(False, 1, total_time, [0], 0,
                                "HUI", best_point)
        self.c_free_simplex()
        return result
