#alias => takma ad kullanma 
import matematik as m  # matematik dosyasındaki fonk kullanılabilir

from workshop11_04_ import Human  # fonksiyonları import ettiğimiz gibi class, değişkenleride import edebiliriz.

human1 = Human("Mirza")
human1.talk("Mehaba")



from  matematik import topla as toplamaIslemi   #matematik dosyasından belli modulleri import etmek için kullanılır
#kullanılırkende direk import edilen fonksiyon kullanılır
# print(topla(5,8))
print(toplamaIslemi(5,2))

#built-in modules
import random

#package dışarıdan alınanlar

# print(matematik.topla(10,20))
print(m.topla(10,20))

print(random.randint(0,100))


#packages















