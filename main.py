class Car:
    def __init__(self, markasi, modeli, yili):
        self.markasi = markasi
        self.modeli = modeli
        self.yili = yili

    def info(self):
        return f"Markasi: {self.markasi}, Modeli: {self.modeli}, Yili: {self.yili}-yil"



class Student:
    def __init__(self, ism, yosh, kurs):
        self.ism = ism
        self.yosh = yosh
        self.kurs = kurs

    def info(self):
        return f"Talaba: {self.ism}, Yoshi: {self.yosh}da, Kursi: {self.kurs}-kurs"



class Book:
    def __init__(self, nomi, muallifi, sahifalar_soni):
        self.nomi = nomi
        self.muallifi = muallifi
        self.sahifalar_soni = sahifalar_soni

    def __str__(self):
        return f"Kitob: '{self.nomi}', Muallifi: {self.muallifi}, Sahifalar soni: {self.sahifalar_soni} bet"


class House:
    def __init__(self, manzil, xonalar_soni, narxi):
        self.manzil = manzil
        self.xonalar_soni = xonalar_soni
        self.narxi = narxi

    def info(self):
        return f"Manzil: {self.manzil}, Xonalar soni: {self.xonalar_soni} xona, Narxi: {self.narxi}"



class Restaurant:
    def __init__(self, nomi, taom_turi, ochilish_vaqti):
        self.nomi = nomi
        self.taom_turi = taom_turi
        self.ochilish_vaqti = ochilish_vaqti

    def qisqa_info(self):
        return f"Restoran nomi: {self.nomi}, Taom turi: {self.taom_turi}"



if __name__ == "__main__":
    print("--- 1-Topshiriq: Avtomobillar ---")
    car1 = Car("Chevrolet", "Gentra", 2024)
    car2 = Car("BYD", "Song Plus", 2025)
    print(car1.info())
    print(car2.info())
    print("-" * 50)

    print("--- 2-Topshiriq: Talabalar ---")
    student1 = Student("Nurmuhammad", 20, 3)
    student2 = Student("Sardor", 19, 2)
    print(student1.info())
    print(student2.info())
    print("-" * 50)

    print("--- 3-Topshiriq: Kitoblar ---")
    book1 = Book("O'tkan kunlar", "Abdulla Qodiriy", 350)
    book2 = Book("Sariq devni minib", "Xudoyberdi To'xtaboyev", 280)
    print(book1)
    print(book2)
    print("-" * 50)

    print("--- 4-Topshiriq: Uylar ---")
    house1 = House("Toshkent sh., Chilonzor tumani", 3, "65,000 USD")
    house2 = House("Samarqand sh., Registon ko'chasi", 4, "80,000 USD")
    print(house1.info())
    print(house2.info())
    print("-" * 50)

    print("--- 5-Topshiriq: Restoranlar ---")
    rest1 = Restaurant("Rayhon", "Milliy taomlar", "08:00")
    rest2 = Restaurant("EVOS", "Fast Food", "09:00")
    print(rest1.qisqa_info())
    print(rest2.qisqa_info())
    print("-" * 50)