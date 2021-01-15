def calculate_coefficients(self):
    final_dict = {}
    matr_structure = [[1 for x in list(self.df.data_dict.values())[0][0]]]
    mat_dict = {}
    for key in self.df.data_dict:
      if key != self.dependent_variable:
        mat_dict[key] = self.df.data_dict[key]
    for row in range(len(mat_dict)):
      mat.append(list(self.df.data_dict.values())[row][0])
    matr = Matrix(matr_structure)
    matr_tpose = matr.transpose()
    square_matr = matr_tpose.matrix_multiply(matr)
    square_inv = square_matr.inverse()
    matr_pseudoinv = square_inv.matrix_multiply(matr_tpose)
    y_values = [[num] for num in list(self.df.data_dict.values())[1][0]]
    coefficents = mat_pseudoinv.matrix_multiply(Matrix(y_values))
    for num in range(len(multiplier_mat.elements)):
      if num == 0:
        key = 'constant'
      else:
        key = list(self.df.data_dict.keys())[num-1]
      coefficient_dict[key] = [row[0] for row in multiplier_mat.elements][num]
    return coefficient_dict