class Matrix:
    def __init__(self, input_data):
        if isinstance(input_data, list):
            self.data = input_data
            self.shape = (len(input_data), len(input_data[0]))
        elif isinstance(input_data, tuple):
            self.data = [
                [0 for _ in range(input_data[1])] for _ in range(input_data[0])
            ]
            self.shape = input_data
        else:
            raise TypeError("Wrong input data type")

    # add : only matrices of same dimensions.
    def __add__(self, other):
        if (
            isinstance(self, Vector)
            and isinstance(other, Vector)
            and self.shape == other.shape
        ):
            if self.shape[0] == 1 and other.shape[0] == 1:
                added_data = [
                    self.data[j] + other.data[j] for j in range(self.shape[1])
                ]
                return Vector([added_data])
            elif self.shape[0] == 1 and other.shape[1] == 1:
                added_data = [
                    [self.data[j] + other.data[j][0]]
                    for j in range(self.shape[1])
                ]
                return Vector(added_data)
            elif self.shape[1] == 1 and other.shape[1] == 1:
                added_data = [
                    [self.data[i][0] + other.data[i][0]]
                    if isinstance(self.data[i], list)
                    and isinstance(other.data[i], list)
                    else [self.data[i] + other.data[i]]
                    for i in range(self.shape[0])
                ]
                return Vector(added_data)
            elif self.shape[1] == 1 and other.shape[0] == 1:
                added_data = [
                    [self.data[i][0] + other.data[i]]
                    if isinstance(self.data[i], list)
                    else [self.data[i] + other.data[i]]
                    for i in range(self.shape[0])
                ]
                return Vector(added_data)
            else:
                raise TypeError("Shape mismatch")
        elif isinstance(other, Matrix) and self.shape == other.shape:
            return Matrix(
                [
                    [self.data[i][j] + other.data[i][j]
                        for j in range(self.shape[1])]
                    for i in range(self.shape[0])
                ]
            )
        else:
            raise TypeError("Wrong input data type or dimensions")

    # __radd__ is called when the left operand does not support the operation
    def __radd__(self, other):
        return self.__add__(other)

    # sub : only matrices of same dimensions.
    def __sub__(self, other):
        if (
            isinstance(self, Vector)
            and isinstance(other, Vector)
            and self.shape == other.shape
        ):
            if self.shape[0] == 1 and other.shape[0] == 1:
                subtracted_data = [
                    self.data[j] - other.data[j] for j in range(self.shape[1])
                ]
                return Vector([subtracted_data])
            elif self.shape[0] == 1 and other.shape[1] == 1:
                subtracted_data = [
                    [self.data[j] - other.data[j][0]]
                    for j in range(self.shape[1])
                ]
                return Vector(subtracted_data)
            elif self.shape[1] == 1 and other.shape[1] == 1:
                subtracted_data = [
                    [self.data[i][0] - other.data[i][0]]
                    if isinstance(self.data[i], list)
                    and isinstance(other.data[i], list)
                    else [self.data[i] - other.data[i]]
                    for i in range(self.shape[0])
                ]
                return Vector(subtracted_data)
            elif self.shape[1] == 1 and other.shape[0] == 1:
                subtracted_data = [
                    [self.data[i][0] - other.data[i]]
                    if isinstance(self.data[i], list)
                    else [self.data[i] - other.data[i]]
                    for i in range(self.shape[0])
                ]
                return Vector(subtracted_data)
            else:
                raise TypeError("Shape mismatch")
        elif isinstance(other, Matrix) and self.shape == other.shape:
            return Matrix(
                [
                    [self.data[i][j] - other.data[i][j]
                        for j in range(self.shape[1])]
                    for i in range(self.shape[0])
                ]
            )
        else:
            raise TypeError("Wrong input data type or dimensions")

    def __rsub__(self, other):
        return self.__sub__(other)

    # div : only scalars.
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Matrix(
                [
                    [self.data[i][j] / other for j in range(self.shape[1])]
                    for i in range(self.shape[0])
                ]
            )
        else:
            raise TypeError("Wrong input data type")

    def __rtruediv__(self, other):
        return self.__truediv__(other)

    # mul : scalars, vectors and matrices.
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Matrix(
                [
                    [self.data[i][j] * other for j in range(self.shape[1])]
                    for i in range(self.shape[0])
                ]
            )
        elif isinstance(other, Vector) and max(other.shape) == self.shape[1]:
            # if the vector is a row vector.
            if other.shape[0] == 1:
                return Vector(
                    [
                        sum(
                            self.data[i][j] * other.data[j]
                            for j in range(self.shape[1])
                        )
                        for i in range(self.shape[0])
                    ]
                )
            # if the vector is a column vector.
            elif other.shape[1] == 1:
                return Vector(
                    [
                        [
                            sum(
                                self.data[i][j] * other.data[j]
                                for j in range(self.shape[1])
                            )
                        ]
                        for i in range(self.shape[0])
                    ]
                )
            else:
                raise TypeError("Vector must be a row or column vector")
        elif isinstance(other, Matrix) and self.shape[1] == other.shape[0]:
            return Matrix(
                [
                    [
                        sum(
                            self.data[i][k] * other.data[k][j]
                            for k in range(self.shape[1])
                        )
                        for j in range(other.shape[1])
                    ]
                    for i in range(self.shape[0])
                ]
            )
        else:
            raise TypeError("Wrong input data type or dimensions")

    def __rmul__(self, other):
        return self.__mul__(other)

    # user-friendly representation of the matrix.
    def __str__(self):
        matrix_rows = ["[" + ", ".join(map(str, row)) + "]"
                       for row in self.data]
        return "Matrix([" + ", ".join(matrix_rows) + "])"

    # developer-friendly representation of the matrix.
    def __repr__(self):
        return f"Matrix(data={self.data}, shape={self.shape})"

    # returns the transposed matrix.
    def T(self):
        return Matrix(
            [
                [self.data[j][i] for j in range(self.shape[0])]
                for i in range(self.shape[1])
            ]
        )


# vector inherits from matrix.
class Vector(Matrix):
    def __init__(self, input_data):
        # super() is used to call the parent class constructor.
        super().__init__(input_data)
        rows, cols = self.shape
        if rows == 1:
            self.data = input_data[0]
        elif cols == 1:
            self.data = [row[0] for row in input_data]
        else:
            raise TypeError("rows or cols must be equal to 1")

    # returns the dot product of two vectors.
    def dot(self, other):
        if isinstance(other, Vector) and len(self) == len(other):
            return sum(self[i] * other[i] for i in range(len(self)))
        else:
            raise TypeError("Wrong input data type or dimensions")

    def __str__(self):
        if self.shape[0] == 1:  # Row vector
            return "Vector([" + ", ".join(map(str, self.data)) + "])"
        else:  # Column vector
            column_repr = ", ".join(["[" + str(item) + "]"
                                     for item in self.data])
            return "Vector([" + column_repr + "])"
