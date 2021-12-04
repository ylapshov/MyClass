# https://github.com/ylapshov/MyClass


# Movie Ticket Booking Application

## class User:

User Class represents the user entity of the booking application. This class is responsible for storing user deatils(name, age).

## \_\_init\_\_(self,name, age):

This is a constructor method, for creating and instance of User Class. This method accepts name and age as arguments.

## \_\_name

A variable to user name.

## \_\_age

A variable to user age.

### get_name(self):

This is getter method and returns the property **name** stored by the class user instance.

### get_age(self):

This is getter method and returns the property **age** stored by the class user instance.

### set_name(self, name):

This is a setter method and this sets the **name** property of the User class instance.

### set_age(self, name):

This is a setter method and this sets the **age** property of the User class instance.

## class TicketBooking:

The TicketBooking class is responsible for booking and cancelling of seats. if any of these operations failed, it will rise error.

## \_\_init\_\_(self,no_of_seats):

This is a constructor method, for creating and instance of TicketBooking Class. This method accepts no_of_seats as arguments.

## \_\_no_of_seats

A variabel to store total nunber of seats.

## \_\_seats

A variabel to store list of User who booked the seats, if a seat is not booked then **None** is stored .

## \_\_validate_seat_no(self,seat_no):

This method reqires seat_no args for computation.
This is private class method which is used to validate seat number based on total number of seats. Rise error if any. This method returns nothing.

## book_seat(self,seat_no, new_user):

This method accepts seat_no and new_user as arguments, returns nothing.
This is a public method and it mark the seat_no as booked by storing the new_user, if its already booked it will rise an error.

## cancel_booking(self,seat_no):

This method accepts seat_no as argument and returns nothing.
This is a public method and it mark the seat_no as None (not booked), if its already not booked it will rise an error.

## get_seats(self):

This is a public getter method. This method accepts no arguments and will return the seats array.

## get_seat_status(self, seat_no):

This method accepts seat_no as argument and return a string based on the status of the seat(i.e. booked / not booked).
