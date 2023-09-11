from kassa import Kassa
from person import Person
from train import Train


if __name__ == "__main__":
    print("Главная программа", __name__)

    ilon = Person("Ilon Mask", 55)
    ilon.earn(97000)
    ilon.pay(11111)
    ilon.show()

    almaty1 = Kassa()

    almaty1.register_train("Алматы", "Ош")
    almaty1.register_train("Ош", "Нью-Йорк")
    almaty1.register_train("Шымкент", "Астана")
    almaty1.register_train("Ош", "Бишкек")
    print(almaty1.registered_train)

    price = almaty1.get_price("Алматы", "Ош")
    almaty1.buy_ticket("Алматы", "Сантьяго", ilon)
    almaty1.buy_ticket("Ош", "Бишкек", ilon)
    almaty1.buy_ticket("Астана", "Калькутта", ilon)


    train = Train(almaty1, "Алматы", "Сантьяго")
    train = Train(almaty1, "Ош", "Нью-Йорк")
    train.show()

    print(almaty1.tickets)
    train.board(ilon)
    print(almaty1.tickets)

