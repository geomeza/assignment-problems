import matplotlib.pyplot as plt

class EulerEstimator:

    def __init__(self, derivatives, point):
        self.derivatives = derivatives
        self.x_points = [point[0]]
        self.y_points = [[y for y in point[1]]]
        self.point = point

    def calc_derivative_at_point(self):
        return [self.derivatives[i](self.point[0],self.point[1]) for i in range(len(self.point[1]))]

    def step_forward(self, step_size):
        derivative = self.calc_derivative_at_point()
        y_points = [(self.point[1][i] + derivative[i] * step_size) for i in range(len(self.point[1]))]
        self.point = (self.point[0] + step_size, tuple(y_points))
        self.x_points.append(self.point[0])
        self.y_points.append([y for y in self.point[1]])

    # def go_to_input(self, input, step_size):
    #     while round(self.point[0],6) != round(input,6):
    #         if abs(step_size) > abs(input - self.point[0]):
    #             step_size = abs(input - self.point[0])
    #         if abs(self.point[0]) > abs(input):
    #             step_size = -1 * step_size
    #         print(self.point[0],input, abs(input - self.point[0]), step_size)
    #         self.step_forward(step_size)

    def go_to_input(self, input, step_size):
        while abs(self.point[0]) < abs(input - step_size):
            self.step_forward(step_size)
        self.step_forward(input - self.point[0])

    # def go_to_input(self, input, step_size):
    #     print(input, self.point[0], 'BEGINNING')
    #     while abs(self.point[0]) < abs(input - step_size):
    #         print(step_size)
    #         self.step_forward(step_size)
    #     print(step_size)
    #     self.step_forward(input - self.point[0])

    def plot(self, range_of_x, step_size, file_name):
        self.x_points = []
        self.y_points = []
        if self.point[0] == range_of_x[1]:
            all_points = self.get_line_points(range_of_x, -step_size)
        else:
            all_points = self.get_line_points(range_of_x, step_size)
        plt.style.use('bmh')
        for points_set in all_points:
            plt.plot(points_set[0], points_set[1])
        # legend = ['Susceptible', 'Infected', 'Recovered', 'Dead']
        plt.legend(['Line'+str(i) for i in range(len(self.point[1]))])
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Graph')
        plt.savefig(file_name)
        plt.show()

    def get_line_points(self, x_range, step_size):
        forward_x, forward_y = self.get_x_y_points(x_range[1], step_size)
        self.x_points = []
        self.y_points = []
        backward_x, backward_y = self.get_x_y_points(x_range[0], -1*step_size)
        backward_x.reverse()
        backward_y.reverse()
        backward_y.pop()
        backward_x.pop()
        complete_x = backward_x + forward_x
        complete_y = backward_y + forward_y
        self.y_points = []
        self.x_points = []
        all_points_separated = [[[] for i in range(2)] for j in range(len(self.point[1]))]
        for i in range(len(complete_y)):
            for j in range(len(complete_y[0])):
                all_points_separated[j][0].append(complete_x[i])
                all_points_separated[j][1].append(complete_y[i][j])
        return all_points_separated


    def get_x_y_points(self, input, step_size):
        self.go_to_input(input, step_size)
        return self.x_points, self.y_points

    # def get_x_y_points(self, range_of_x, step_size):
    #     if self.point[0] in range_of_x:
    #         if self.point[0] == range_of_x[1]:
    #             self.go_to_input(range_of_x[1], -step_size)
    #     # self.x_points.reverse()
    #     # self.y_points.reverse() 
    #     # if self.point[0] > range_of_x[0]:
    #     #     step_size = -1*abs(step_size)
    #     # self.go_to_input(range_of_x[0], step_size = step_size)
    #     # self.x_points.remove(self.x_points[0])
    #     # self.y_points.remove(self.y_points[0])
    #     # self.x_points.reverse()
    #     # self.y_points.reverse() 
    #     # step_size = abs(step_size)
    #     # self.go_to_input(range_of_x[1], step_size = step_size)
    #     all_points_separated = [[[] for i in range(2)] for j in range(len(self.point[1]))]
    #     for i in range(len(self.y_points)):
    #         for j in range(len(self.y_points[0])):
    #             all_points_separated[j][0].append(self.x_points[i])
    #             all_points_separated[j][1].append(self.y_points[i][j])
    #     return all_points_separated

        


# euler = EulerEstimator(
#                 derivatives = [
#                     (lambda t,x: -0.0003 * x[0] * x[1]),
#                     (lambda t,x: 0.0003 * x[0] * x[1] - 0.05 * x[1]),
#                     (lambda t,x: 0.02 * x[1]),
#                     (lambda t,x: 0.03 * x[1])
#                     ],
#                 point = (0,(1000, 1, 0, 0))
#             )

# print(euler.point)
# # (0, (0, 0, 0))
# print(euler.calc_derivative_at_point())
# # [1, 0, 0]

# euler.step_forward(0.1)
# print(euler.point)
# # (0.1, (0.1, 0, 0))

# print(euler.calc_derivative_at_point())
# # [1.1, 0.1, 0]
# euler.step_forward(-0.5)
# print(euler.point)
# # (-0.4, (-0.45, -0.05, 0))
# euler.go_to_input(5, step_size = 2)
# print(euler.point)
# print('PLOT')
# euler.plot([0, 365], step_size = 0.001, file_name = 'plot.png')
