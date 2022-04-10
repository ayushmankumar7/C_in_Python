import ctypes 

dll = ctypes.CDLL("./output.dll")
print("Output of Prime(9):", dll.prime(9))
print("Output of Prime(13):", dll.prime(13))
print("Output of odd_even(17):", dll.odd_even(17))
print("Output of odd_even(8):", dll.odd_even(8))