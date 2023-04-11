class Human:
    # name = "Mustafa"

    #built-in
    #constructor yapıcı blok
    #initialize     class nesne ürettiğinde çalışan fonksiyon
    # her nesne üretildiğindde çalışır

    def __init__(self,name):

        self.name = name
        self.name = str(input("İsim girin"))
        print("Bir human instance üretildi")


    def __str__(self):  # print(human1) değer döndürmesi istendiğinde kullanılır.
        return f"STR fONKSİYONUNDAN DÖNEN DEĞER : {self.name}"
    

    def talk(self,sentences):  # self yerine başka keyword lerde kullanılabilir
        # print("Human is talking")
        name = "ercan"  # name i burda almak doğru değil dışarıda almak daha sağlıklı
        print(f"{self.name},{name} : {sentences}") # self class içerisindeki diğer alanlara gidiyor. fonksiyon dışına çıkıyor.
        # self.walk()
    def walk(self):
        print(f"{self.name}Human is walking")