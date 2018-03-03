! file: fib1.f90
subroutine fib(a,n)
 !
 ! calculate first n fibonacci numbers
 !
 integer n
 real*8 a(n)
 do i=1,n
 if (i.eq.1) then
 a(i) = 0.0d0
 elseif (i.eq.2) then
 a(i) = 1.0d0
 else
 a(i) = a(i-1) + a(i-2)
 endif
 enddo
end subroutine fib