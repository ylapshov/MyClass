class User:
    def __init__(self, name, age):      # Constructor
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age


class TicketBoking:
    def __init__(self, no_of_seats: int):       #Constructor
        self.__no_of_seats = no_of_seats
        self.__seats = [None] * no_of_seats

    def __validate_seat_no(self, seat_no: int):
        if len(self.__seats) <= seat_no-1 or seat_no-1 < 0:
            raise Exception("Invalid seat number")

    def book_seat(self, seat_no: int, new_user: User):
        self.__validate_seat_no(seat_no)
        if self.__seats[seat_no-1] is not None:
            raise Exception("Seat already booked")
        print("Booking confirmed by " + new_user.get_name())
        self.__seats[seat_no-1] = new_user

    def cancel_booking(self, seat_no: int):
        self.__validate_seat_no(seat_no)
        if self.__seats[seat_no-1] is None:
            raise Exception(
                "Seat not booked, Only booked seats can be cancelled")
        print("Booking cancelled by " + self.__seats[seat_no-1].get_name())
        self.__seats[seat_no-1] = None

    def get_seats(self) -> list[User]:
        return self.__seats

    def get_seat_status(self, seat_no: int) -> str:
        if self.__seats[seat_no] is None:
            return "Seat is free"
        else:
            return "Seat is booked by " + self.__seats[seat_no].get_name()


def main():
    booking = TicketBoking(no_of_seats=10)    # Creating object for the class TicketBoking
    booking.book_seat(seat_no=1, new_user=User("John", 30))
    booking.book_seat(seat_no=2, new_user=User("Joe", 26))
    booking.book_seat(seat_no=3, new_user=User("Kabi", 20))
    booking.cancel_booking(seat_no=2)
    print(booking.get_seats())


if __name__ == "__main__":
    main()
