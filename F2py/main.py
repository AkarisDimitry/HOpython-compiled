#Lineas comunes a todos los ejemplos.
import ctypes as C
math = C.CDLL('./libmymath.so')


#llamado a funcion con argumentos enteros.
math.add_int(3, 4)


# llamado a funcion con argumentos flotantes
math.add_float.restype = C.c_float
math.add_float.argtypes = [C.c_float, C.c_float]
math.add_float(C.c_float(3), C.c_float(4))

# llamado por referencia en memoria de un entero
tres = C.c_int(3)
cuatro = C.c_int(4)
res = C.c_int()
math.add_int_ref(C.byref(tres), C.byref(cuatro), C.byref(res))
res.value

# llamado por referencia en memoria de un flotante
tres = C.c_float(3)
cuatro = C.c_float(4)
res = C.c_float()
math.add_int_ref(C.byref(tres), C.byref(cuatro), C.byref(res))
res.value

# llamado a funcion con argumento array con lista
in1 = (C.c_int * 3) # (1, 2, -5)
in2 = (C.c_int * 3) # (-1, 3, 3)
math.add_int_array(C.byref(in1), C.byref(in2), C.byref(out))
out[0], out[1], out[2]

# llamado a funcion con argumento array con array de numpy
import numpy as np 
intp = C.POINTER(C.c_int)
in1 = np.array([1,2,-5], dtype=C.c_int)
in2 = np.array([-1,3,3], dtype=C.c_int)
out = np.zeros(3, dtype = np.float16)
math.add_int_array(in1.ctypes.data_as(intp),
					in2.ctypes.data_as(intp),
					out.ctypes.data_as(intp),
					C.c_int(3))
out 


# llamado a funcion con argumento array con array de numpy
import numpy as np 
flp = C.POINTER(C.c_float) # para uqe esta esta linea 
in1 = np.array([1,2,-5], dtype=C.c_float)
in2 = np.array([-1,3,3], dtype=C.c_float)
out = math.add_int_array(in1.ctypes.data_as(flp),
					in2.ctypes.data_as(flp),
					C.c_int(3))
out 












