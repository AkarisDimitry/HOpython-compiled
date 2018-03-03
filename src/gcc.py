import os 
os.system('gcc -c -fPIC add_two.c ')
os.system('gcc -c -fPIC arrays.c ')

os.system('gcc -shared arrays.o add_two.o -o libmymath.so')
os.system('gcc -shared arrays.o -o libmymath1.so')

#os.system('nm -n libmymath.so')
os.system('nm -n arrays.o')




