# class Human:
#     # name = "Mustafa"

#     #built-in
#     #constructor yapıcı blok
#     #initialize     class nesne ürettiğinde çalışan fonksiyon
#     # her nesne üretildiğindde çalışır

#     def __init__(self,name):
#         self.name = name
#         print("Bir human instance üretildi")


#     def __str__(self):  # print(human1) değer döndürmesi istendiğinde kullanılır.
#         return f"STR fONKSİYONUNDAN DÖNEN DEĞER : {self.name}"
    

#     def talk(self,sentences):  # self yerine başka keyword lerde kullanılabilir
#         # print("Human is talking")
#         name = "ercan"  # name i burda almak doğru değil dışarıda almak daha sağlıklı
#         print(f"{self.name},{name} : {sentences}") # self class içerisindeki diğer alanlara gidiyor. fonksiyon dışına çıkıyor.
#         # self.walk()
#     def walk(self):
#         print(f"{self.name}Human is walking")
#instance =>Örnek

from human import Human


human1 = Human("Enes")
# human1.name = "Enes"  contructor içine name alarak değişiklik yapılabilir.
human1.talk("Merhaba")
human1.walk()
print(human1)

human2 = Human("Halit")
human2.name = "Cem"
human2.talk("Selam")
human2.walk()
print(human2)

# Human("hhh").talk("hhhh") bu şekildede kullanılabilir.


























