import numpy as np
from numpy.lib.mixins import NDArrayOperatorsMixin


class HashMixin:
    def __hash__(self):
        return int(np.sum(self.data))


class FileMixin:
    def to_file(self, filename, fmt="%d"):
        np.savetxt(filename, self.data, fmt=fmt)


class DisplayMixin:
    def __str__(self):
        return str(self.data)


class Matrix(NDArrayOperatorsMixin, HashMixin, FileMixin, DisplayMixin):
    def __init__(self, data):
        self._data = np.array(data)
        self._mult_cache = {}

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = np.array(value)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        inputs = (x.data if isinstance(x, Matrix) else x for x in inputs)
        result = getattr(ufunc, method)(*inputs, **kwargs)
        if isinstance(result, tuple):
            return tuple(self.__class__(x) for x in result)
        else:
            return self.__class__(result)

    def __matmul__(self, other):
        key = (hash(self), hash(other))
        if key in self._mult_cache:
            return self._mult_cache[key]

        if self.data.shape[1] != other.data.shape[0]:
            raise ValueError("Incompatible dimensions for matrix multiplication")

        result_matrix = self.__class__(np.matmul(self.data, other.data))
        self._mult_cache[key] = result_matrix
        return result_matrix


np.random.seed(0)


A = Matrix(np.random.randint(0, 10, (3, 3)))
B = Matrix(np.random.randint(0, 10, (3, 3)))


C_data = A.data.copy()
C_data[0, 0] += 1
C_data[0, -1] -= 1

while np.array_equal(C_data, A.data):
    C_data[0, 0] += 1
    C_data[0, -1] -= 1


C = Matrix(C_data)


D = Matrix(B.data.copy())


assert hash(A) == hash(B), "Hashes of A and C do not match"
assert not np.array_equal(A.data, C.data), "Matrices A and C should not be equal"
assert np.array_equal(B.data, D.data), "Matrices B and D should be equal"
assert not np.array_equal(
    (A @ B).data, (C @ D).data
), "Products A @ B and C @ D should not be equal"


A.to_file("A.txt")
B.to_file("B.txt")
C.to_file("C.txt")
D.to_file("D.txt")

AB_result = A @ B
CD_result = C @ D

AB_result.to_file("AB.txt")
CD_result.to_file("CD.txt")


with open("hash.txt", "w") as f:
    f.write(f"Hash of AB: {hash(AB_result)}\n")
    f.write(f"Hash of CD: {hash(CD_result)}\n")

