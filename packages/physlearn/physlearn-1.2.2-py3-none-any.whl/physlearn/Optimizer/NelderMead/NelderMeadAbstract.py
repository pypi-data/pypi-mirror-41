import math
import sys
import time

import numpy
from tqdm import tqdm

from physlearn.Optimizer import OptimizeResult
from physlearn.Optimizer.OptimizerAbstract import OptimizerAbstract


class NelderMeadAbstract(OptimizerAbstract):
    # Переменные, в которых хранятся точки симплеска и значения функции в них
    x_points = None
    y_points = None
    # Минимальный и максимальный элементы при случайной генерации точек симплкса
    min_element = -1
    max_element = 1
    # Размерность оптимизируемой функции
    dim = None
    # Параметры алгоритма
    alpha = 1
    beta = 0.5
    gamma = 2
    # Оптимизируемая функция
    func = None
    # Ряд переменных, необходимых для работы алгоритма
    h_index, g_index, l_index = None, None, None
    x_center = None
    x_reflected = None
    # Переменные необходимые для работы прогресс бара
    dot_str = ''
    print_str = ''
    start_time = 0
    speed = 0
    percent_done = 0
    update_pb_iter = 1000
    amount_of_dots = 0
    current_best_point = None
    progress_bar = 'self'
    show_progress_bar = True

    epsilon = 0.5
    search_depth = 100

    break_point = -1

    def __init__(self, min_element=-1, max_element=1, progress_bar='self'):
        super().__init__(min_element, max_element)
        # Переменные, в которых хранятся точки симплеска и значения функции в них
        self.x_points = None
        self.y_points = None
        # Размерность оптимизируемой функции
        self.dim = None
        # Параметры алгоритма
        self.alpha = 1
        self.beta = 0.5
        self.gamma = 2
        # Оптимизируемая функция
        self.func = None
        # Ряд переменных, необходимых для работы алгоритма
        self.h_index, self.g_index, self.l_index = None, None, None
        self.x_center = None
        self.x_reflected = None
        # Переменные необходимые для работы прогресс бара
        self.dot_str = ''
        self.print_str = ''
        self.start_time = 0
        self.speed = 0
        self.percent_done = 0
        self.update_pb_iter = 1000
        self.amount_of_dots = 0
        self.current_best_point = None

        self.epsilon = 0.5
        self.search_depth = 100

        self.break_point = -1
        self.alpha = 1
        self.beta = 0.5
        self.gamma = 2
        self.method_types = [0, 0, 0, 0]
        self.types_list = []
        self.cost_list = []
        self.variance_list = []
        self.progress_bar = progress_bar

    def parse_params(self, params_dict):
        if not (params_dict.get('alpha') is None):
            self.alpha = params_dict['alpha']

        if not (params_dict.get('beta') is None):
            self.beta = params_dict['beta']

        if not (params_dict.get('alpha') is None):
            self.gamma = params_dict['gamma']

        if not (params_dict.get('epsilon') is None):
            self.epsilon = params_dict['epsilon']

        if not (params_dict.get('search_depth') is None):
            self.search_depth = params_dict['search_depth']

    # Установка параметров алгоритма
    def set_params(self, alpha, beta, gamma):
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma

    def set_epsilon_and_sd(self, epsilon, search_depth):
        self.epsilon = epsilon
        self.search_depth = search_depth

    # Метод, который вычисляет значение функции от параметров params
    def func(self, params):
        return []

    def type_of_progress_bar(self, params):
        if self.progress_bar == 'self':
            self.show_progress_bar = True
            return params
        elif self.progress_bar == 'tqdm':
            self.show_progress_bar = False
            return tqdm(params)
        else:
            self.show_progress_bar = False
            return params

    def optimize(self, func, dim, end_cond, min_cost=1e-5):
        # func - оптимизируемая функция, должна принимать numpy.array соотвесвтующей размерности в качесвте параметра
        # dim - размерность функции
        # end_method - условие останова
        # 'variance' - дисперсия набора значений функции симплкса должна быть меньше end_cond
        # 'max_iter' - остановка при достижении end_cond итераций
        self.func = func
        self.dim = dim
        self.x_points = self.create_points()  # Создаем точки
        # Вычисляем значение функции в точках
        self.y_points = numpy.zeros(self.dim + 1)
        for index, x in enumerate(self.x_points):
            self.y_points[index] = self.func(x)

        self.method_types = [0, 0, 0, 0]
        self.types_list = []  # В данном списке сохраняются типы работы алгоритма

        # Переменные, в которых сохраняется результат
        reason_of_break = ''  # Причина выхода
        amount_of_iterations = 0  # Количество выполненных итераций
        exit_code = -100  # Код выхода
        is_converged = False  # Сошелся алгоритм или нет
        self.cost_list = []  # Список, содержащий значения лучшей функции на каждой итерации

        # Строка с точками для прогресс бара
        self.dot_str = ''

        exit_point = end_cond
        self.start_time = time.time()  # Время начала работы
        prev_update_time = time.time()
        self.print_str = ''
        for i in self.type_of_progress_bar(range(end_cond)):
            if self.show_progress_bar:
                cur_time = time.time()
                if (cur_time - prev_update_time) >= 1:
                    delta = cur_time - self.start_time
                    self.speed = i / delta
                    self.percent_done = math.floor(i * 100 / end_cond)
                    self.update_progress_bar(i)
                    prev_update_time = cur_time

            method_type = self.iteration()
            self.types_list.append(method_type)
            cur_cost = numpy.min(self.y_points)
            self.cost_list.append(cur_cost)
            if cur_cost < min_cost:
                reason_of_break = 'Minimum cost reached'
                exit_code = 0
                amount_of_iterations = i
                is_converged = True
                break
            self.method_types[method_type] += 1
            last_method_types = self.types_list[-self.search_depth:]
            bad_variant_percent = last_method_types.count(3) / self.search_depth
            if bad_variant_percent >= self.epsilon:
                reason_of_break = 'Local minimum reached'
                exit_code = 1
                amount_of_iterations = i
                is_converged = True
                break
                # break
            if i == (end_cond - 1):
                reason_of_break = 'Maximum iterations reached'
                exit_code = -1
                amount_of_iterations = i + 1
                is_converged = False

            if i == exit_point:
                reason_of_break = 'Maximum iterations reached'
                exit_code = -1
                amount_of_iterations = i
                is_converged = False
                break

        end_time = time.time()
        total_time = end_time - self.start_time
        self.percent_done = math.floor(amount_of_iterations * 100 / end_cond)
        if self.show_progress_bar:
            self.update_progress_bar(amount_of_iterations)
        _, _, l_index = self.find_points()  # Определяем точку с нименьшим значением функции
        result = OptimizeResult(is_converged, amount_of_iterations, total_time, self.cost_list, exit_code,
                                reason_of_break, self.x_points[l_index])
        return result

    def update_progress_bar(self, i):
        if self.progress_bar:
            eraser = ''.ljust(len(self.print_str))
            sys.stderr.write('\r' + eraser)
            if self.amount_of_dots == 4:
                self.dot_str = ''
                self.amount_of_dots = 0
            self.dot_str += '.'
            self.amount_of_dots += 1
            speed_str = '{:.3f}'.format(self.speed)
            self.print_str = self.dot_str.ljust(5) + str(i) + ' (' + str(
                self.percent_done) + '%) ' + speed_str + ' it\s'
            sys.stderr.write('\r' + self.print_str)

    def iteration(self):
        self.h_index, self.g_index, self.l_index = self.find_points()  # Находим точки h, g и l
        self.current_best_point = self.x_points[self.l_index]
        self.x_center = self.calculate_center()  # Вычисляем центр масс
        self.x_reflected = self.calculate_reflected_point()  # Вычисляем отраженную
        # точку
        y_reflected = self.func(self.x_reflected)
        # Далее мы делаем ряд действий, в зависимости от соотношения между значениями функции в найденных точках
        # Объяснять подробно нет смысла, так что смотри просто "Метод Нелдера - Мида" в вики
        if y_reflected < self.y_points[self.l_index]:
            method_type = 0
            x_stretch = self.calculate_stretched_point()
            y_stretch = self.func(x_stretch)
            if y_stretch < self.y_points[self.l_index]:
                self.x_points[self.h_index] = x_stretch
                self.y_points[self.h_index] = y_stretch
            else:
                self.x_points[self.h_index] = self.x_reflected
                self.y_points[self.h_index] = y_reflected

        elif y_reflected <= self.y_points[self.g_index]:
            method_type = 1
            self.x_points[self.h_index] = self.x_reflected
            self.y_points[self.h_index] = y_reflected

        else:
            if y_reflected < self.y_points[self.h_index]:
                self.x_points[self.h_index] = self.x_reflected
                self.y_points[self.h_index] = y_reflected

            x_compress = self.calculate_compressed_point()
            y_compress = self.func(x_compress)
            if y_compress < self.y_points[self.h_index]:
                method_type = 2
                self.x_points[self.h_index] = x_compress
                self.y_points[self.h_index] = y_compress
            else:
                method_type = 3
                self.compress_simplex()
                for index, point in enumerate(self.x_points):
                    self.y_points[index] = self.func(point)
        return method_type

    def create_points(self):
        points = []
        for i in range(self.dim + 1):  # Создаем массив точек размера dim + 1 (так требуется по методу)
            points.append(numpy.random.uniform(self.min_element, self.max_element, self.dim))
        return numpy.array(points)

    def find_points(self):
        # В данном методе мы находим три точки: h - точка с наибользим значением оптимизируемой функции,
        # g - следующая за точкой с наибольишм значение, l - с наименьшим значением.
        # Далее мы задаем начальные парамтры...
        h_point = -sys.maxsize
        g_point = -sys.maxsize
        l_point = sys.maxsize
        h_index = 0
        g_index = 0
        l_index = 0
        # ...и проводим стандарнтый поиск.
        for index, item in enumerate(self.y_points):
            if item > h_point:
                g_point = h_point
                h_point = item
                g_index = h_index
                h_index = index
            elif (item > g_point) and (item != h_point):
                g_point = item
                g_index = index
            if item < l_point:
                l_point = item
                l_index = index

        return h_index, g_index, l_index

    def calculate_center(self):
        # Вычисляем "центр масс" всех точек, за исключением h
        sum_data = 0
        n = len(self.x_points) - 1
        for index, item in enumerate(self.x_points):
            if index != self.h_index:
                sum_data += item

        return sum_data / n

    def calculate_reflected_point(self):
        # В данной функции выполняется отражение точки h относительно центра масс
        pass

    def calculate_stretched_point(self):
        # В данной функции выполняется растяжение в направлении, соединяющим h, center и reflected
        x_stretch = (self.gamma * self.x_reflected) + ((1 - self.gamma) * self.x_center)
        return x_stretch

    def calculate_compressed_point(self):
        x_h = self.x_points[self.h_index]
        # В данной функции выполняется сжатие к center
        x_compress = (self.beta * x_h) + ((1 - self.beta) * self.x_center)
        return x_compress

    def compress_simplex(self):
        # В данной функции происходит схатие всего симплекса к l
        x_l = self.x_points[self.l_index]
        for index, x_i in enumerate(self.x_points):
            self.x_points[index] = 0.5 * (x_i + x_l)

    def return_method_types(self):
        return self.method_types

    def return_types_list(self):
        return self.types_list
