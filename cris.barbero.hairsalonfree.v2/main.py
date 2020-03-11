import random
import datetime
from dataclasses import dataclass
from typing import List

CUSTOMER_MIN_TIME = 1
CUSTOMER_MAX_TIME = 20
HAIRCUT_MIN_TIME = 20
HAIRCUT_MAX_TIME = 40
CUSTOMER_WAIT_MIN_BEFORE_LEAVE = 30 # time a customer will wait before leaving impatiently
SALON_SIZE = 15 # Number of customers who can fit in the salon

class CustomerBuilder:
    '''Builds new customers at a random interval'''
    def __init__(self):
        self.count = 0
        self.mins_until_next_customer = 0

    def try_get_new_customer(self):
        '''Returns a new customer on a random schedule'''

        if self.mins_until_next_customer == 0:
            # Determine random time to wait for next customer to arrive
            self.mins_until_next_customer = random.randint(CUSTOMER_MIN_TIME, CUSTOMER_MAX_TIME)
            self.count += 1
            return Customer(f'Customer_{self.count}')
        else:
            self.mins_until_next_customer -= 1


@dataclass
class Stylist:
    name: str

@dataclass
class Customer:
    name: str

@dataclass
class WaitingCustomer:
    customer: Customer
    time_waiting: int = 0

@dataclass
class HairCut:
    customer: Customer
    stylist: Stylist
    time_remaining: int

class HairSalon:
    def __init__(self, time):
        self.is_open = False
        self.is_door_locked = True
        self.time = time
        self.first_shift_stylists = [
            Stylist('Anne'),
            Stylist('Ben'),
            Stylist('Carol'),
            Stylist('Derek')
        ] # type: List[Stylist]
        self.second_shift_stylists = [
            Stylist('Erin'),
            Stylist('Frank'),
            Stylist('Gloria'),
            Stylist('Heber')
        ] # type: List[Stylist]
        self.working_stylists = [] # type: List[Stylist]
        self.free_stylists = [] # type: List[Stylist]
        self.overtime_stylists = [] # type: List[Stylist]
        self.waiting_customers = [] # type: List[WaitingCustomer]
        self.active_hair_cuts = [] # type: List[HairCut]

    def total_customers(self):
        '''The total number of customers in the salon'''
        return (len(self.waiting_customers) + len(self.active_hair_cuts))

    def open(self):
        '''Open the salon for the day'''

        self.is_open = True
        self.is_door_locked = False
        print(f'[{self.time.current_time_to_string()}] Hair salon [opened]')

    def lock_doors(self):
        '''Lock the doors at the end of the day to prevent new customers from entering'''

        self.is_door_locked = True

    def close(self):
        '''Close the salon for the day after all customers and stylists have left'''

        self.is_open = False
        print(f'[{self.time.current_time_to_string()}] Hair salon [closed]')

    def first_shift_starts(self):
        '''Start the first shift of stylists'''

        for sylist in self.first_shift_stylists:
            self.stylist_clock_in(sylist)

    def first_shift_ends(self):
        '''End the first shift of stylists'''

        # clock out each free first shift stylist
        # if any are working, then check back on them when they finish
        for stylist in self.first_shift_stylists:
            if stylist in self.free_stylists:
                self.free_stylists.remove(stylist)
            else:
                self.overtime_stylists.append(stylist)

    def second_shift_starts(self):
        '''Start the first shift of stylists'''

        for sylist in self.second_shift_stylists:
            self.stylist_clock_in(sylist)

    def second_shift_ends(self):
        '''End the second shift of stylists'''

        for stylist in self.second_shift_stylists:
            if stylist in self.free_stylists:
                # clock out each free second shift stylist
                self.free_stylists.remove(stylist)
            else:
                # if any are working, then mark them as overtime so they know they can leave when they are finished
                self.overtime_stylists.append(stylist)

    def stylist_clock_in(self, stylist: Stylist):
        '''Clock in a stylist and make them free to do hair cuts'''

        self.working_stylists.append(stylist)
        self.free_stylists.append(stylist)
        print(
            f'[{self.time.current_time_to_string()}] [{stylist.name}] [started] shift')

    def stylist_clock_out(self, stylist: Stylist):
        '''Clock out a stylist at the end of their shift'''

        self.working_stylists.remove(stylist)
        if stylist in self.free_stylists:
            self.free_stylists.remove(stylist)
        print(
            f'[{self.time.current_time_to_string()}] [{stylist.name}] [ended] shift')

    def customer_enter(self, customer: Customer):
        '''Customer enters the salon for a haircut'''

        print(f'[{self.time.current_time_to_string()}] [{customer.name}] entered')
        if self.total_customers() >= SALON_SIZE:
            print(
                f'[{self.time.current_time_to_string()}] [{customer.name}] left [impatiently]')
        elif self.is_door_locked:
            print(
                f'[{self.time.current_time_to_string()}] [{customer.name}] left [cursing themselves]')
        else:
            self.waiting_customers.append(WaitingCustomer(customer))

    def customer_leaves_unfulfilled(self, waiting_customer: WaitingCustomer):
        '''Customer leaves unfulfilled because they didn't get a haircut'''

        self.waiting_customers.remove(waiting_customer)
        print(
            f'[{self.time.current_time_to_string()}] [{waiting_customer.customer.name}] left [unfulfilled]')

    def finish_hair_cut(self, hair_cut: HairCut):
        '''Finish a haircut for a customer'''

        print(
            f'[{self.time.current_time_to_string()}] [{hair_cut.customer.name}] left [satisfied]')
        self.active_hair_cuts.remove(hair_cut)
        if hair_cut.stylist in self.overtime_stylists:
            self.stylist_clock_out(hair_cut.stylist)
        else:
            self.free_stylists.append(hair_cut.stylist)

    def service_next_customer(self):
        '''Service the next Customer who's waiting'''

        stylist = self.free_stylists.pop()
        waiting_customer = self.waiting_customers.pop()
        hair_cut_time = random.randint(HAIRCUT_MIN_TIME, HAIRCUT_MAX_TIME)
        self.active_hair_cuts.append(HairCut(waiting_customer.customer, stylist, hair_cut_time))
        print(
            f'[{self.time.current_time_to_string()}] [{stylist.name}] [started] cutting [{waiting_customer.customer.name}]')

    def update_status(self):
        '''
        Update the status of the salon.
        This is the general working method that happens constantly throughout the day.
        '''

        # if busy_stylist time exceeded finish_with_customer
        for hair_cut in self.active_hair_cuts:
            if hair_cut.time_remaining == 0:
                self.finish_hair_cut(hair_cut)
            else:
                hair_cut.time_remaining -= 1

        # if free stylist and wating customer start_next_customer
        # note: we want to do this after finishing existing hair_cuts so that a stylist can get back to work immediately!! No Slacking!!
        while self.free_stylists and self.waiting_customers:
            self.service_next_customer()

        # if waiting customer > 30 mins: customer_leaves_unfulfilled
        for waiting_customer in self.waiting_customers:
            if(waiting_customer.time_waiting >= CUSTOMER_WAIT_MIN_BEFORE_LEAVE):
                self.customer_leaves_unfulfilled(waiting_customer)

        if self.is_door_locked and not self.active_hair_cuts:
            self.close()


class Time:
    '''A simple time simulator'''
    def __init__(self, hour, minute):
        self.datetime = datetime.datetime(
            year=2019, month=1, day=1, hour=hour, minute=minute)
        # self.hour = hour
        # self.minute = minute

    def current_time_to_string(self):
        return(self.datetime.strftime('%H:%M'))

    def tick_minute(self):
        self.datetime += datetime.timedelta(minutes=1)

    def is_time(self, hour, minute):
        return self.datetime.time().hour == hour and self.datetime.time().minute == minute



def run_simulation():
    '''Run our salon simulator'''

    customer_builder = CustomerBuilder()

    time = Time(9, 00)
    salon = HairSalon(time)
    salon.open()
    while salon.is_open:
        if time.is_time(9, 0):
            salon.first_shift_starts()
        elif time.is_time(13, 0):
            salon.first_shift_ends()
            salon.second_shift_starts()
        elif time.is_time(17, 0):
            salon.second_shift_ends()
            salon.lock_doors()

        customer = customer_builder.try_get_new_customer()
        if customer:
            salon.customer_enter(customer)

        salon.update_status()

        time.tick_minute()


if __name__ == "__main__":
    run_simulation()