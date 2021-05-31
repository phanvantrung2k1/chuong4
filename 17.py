import math
n = int(input("Nhập số nguyên dương n = "));
print ("Tất cả các số nhỏ hơn", n,'có tổng ước lớn hơn nó' );
i = 1;
a = 0;
while (i < (n/2)):
    if n % i == 0:
        a = a + i;          
        i = i + 1;
        if a > n:
            print(n)
