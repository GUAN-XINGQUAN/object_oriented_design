from enum import Enum
from datetime import datetime, timedelta

class SpotType(Enum):
    REGULAR = 'regular'
    COMPACT = 'compact'
    HANDICAPPED = 'handicapped'
    LARGE = 'large'


class VehicleType(Enum):
    CAR = 'car'
    TRUCK = 'truck'
    VAN = 'van'
    MOTORCYCLE = 'motorcycle'


class PaymentStatus(Enum):
    UNPAID = 'unpaid'
    PAID = 'paid'


class Vehicle:
    def __init__(self, license_no: str, vehicle_type: 'VehicleType'):
        self.license_no = license_no
        self.vehicle_type = vehicle_type

    def assign_ticket(self, ticket: 'ParkingTicket'):
        self.ticket = ticket


class Payment:
    def __init__(self, ticket: 'Ticket', rate: float):
        self.ticket = ticket
        self.rate = rate

    def calculate_payment(self):
        # Calculate payment based on hourly rate
        entry_time = self.ticket.entry_time
        exit_time = self.ticket.exit_time
        hours_parked = (exit_time - entry_time).seconds // 3600
        amount_due = hours_parked * self.rate
        return amount_due


class ParkingSpot:
    def __init__(self, spot_id:str, spot_type: 'SpotType'):
        self.spot_id = spot_id
        self.spot_type = spot_type
        self.is_occupied = False

    def assign_vehicle(self, vehicle: 'Vehicle'):
        self.vehicle = vehicle
        self.is_occupied = True

    def remove_vehicle(self):
        self.vehicle = None
        self.is_occupied = False


class ParkingTicket:
    def __init__(self, vehicle: 'Vehicle', entry_time: datetime, exit_time: datetime = None):
        self.vehicle = vehicle
        self.entry_time = entry_time
        self.exit_time = exit_time
        self.status = PaymentStatus.UNPAID

    def assign_leaving_time(self, exit_time: datetime):
        self.exit_time = exit_time

    def set_status(self, status: 'PyamentStatus'):
        self.status = status
    
    def is_paid(self):
        print(self.status)
        return self.status == PaymentStatus.PAID


class Entrance:
    def __init__(self, entrance_id: str):
        self.entrance_id = entrance_id

    def get_ticket(self, vehicle):
        entry_time = datetime.now()
        return ParkingTicket(vehicle, entry_time)


class Exit:
    def __init__(self, exit_id: str):
        self.exit_id = exit_id

    def _process_ticket(self, ticket: 'ParkingTicket', exit_time: datetime):
        ticket.assign_leaving_time(exit_time)
        return ticket

    def _process_payment(self, ticket: 'ParkingTicket', rate: float):
        if ticket.is_paid():
            return f"Ticket is prepaid. Safe Trip!"
        payment = Payment(ticket, rate)
        amount_due = payment.calculate_payment()
        return f"Payment processed: {amount_due} USD"
    
    def exit_car(self, ticket: 'ParkingTicket', exit_time: datetime, rate: float):
        ticket = self._process_ticket(ticket, exit_time)
        info = self._process_payment(ticket, rate)
        return info


class ParkingLot:
    def __init__(self, capacity: int):
        self.capacity = capacity
        # Assume four types of parking spots are evenly allocated
        self.spots = {
            SpotType.HANDICAPPED: [ParkingSpot(f'{idx}', SpotType.HANDICAPPED) for idx in range(capacity//4)],
            SpotType.COMPACT: [ParkingSpot(f'{idx}', SpotType.COMPACT) for idx in range(capacity//4)],
            SpotType.REGULAR: [ParkingSpot(f'{idx}', SpotType.REGULAR) for idx in range(capacity//4)],
            SpotType.LARGE: [ParkingSpot(f'{idx}', SpotType.LARGE) for idx in range(capacity//4)],
        }
        self.entrance_points = []
        self.exit_points = []
        self.occupied_spots = 0

    def add_entrance_point(self, entrance: 'Entrance'):
        self.entrance_points.append(entrance)

    def add_exit_point(self, exit: 'Exit'):
        self.exit_points.append(exit)

    def park_vehicle(self, vehicle: 'Vehicle', spot_type: 'SpotType'):
        if self.occupied_spots < self.capacity:
            for spot in self.spots[spot_type]:
                if not spot.is_occupied:
                    spot.assign_vehicle(vehicle)
                    self.occupied_spots += 1
                    return True  # Vehicle parked successfully
            return False  # No available spot of the specified type
        else:
            return False  # Parking lot is full

    def remove_vehicle(self, vehicle: 'Vehicle', spot_type: 'SpotType'):
        for spot in self.spots[spot_type]:
            if spot.is_occupied and spot.vehicle == vehicle:
                spot.remove_vehicle()
                self.occupied_spots -= 1
                return True
        return False

    def display_free_spots(self):
        free_spots = {spot_type: sum(not spot.is_occupied for spot in spots) for spot_type, spots in self.spots.items()}
        return free_spots


# Example
if __name__ == "__main__":
    # Initialize a parking lot system
    parking_lot = ParkingLot(capacity=4)  # assume 4 spots for simplicity
    entrance = Entrance('entrance_01')
    exit_gate = Exit('exit_01')
    parking_lot.add_entrance_point(entrance)
    parking_lot.add_exit_point(exit_gate)
    hour_rate = 2  # 2 dollars per hour

    # A car enters the parking lot
    car = Vehicle('123456', VehicleType.CAR)
    ticket = entrance.get_ticket(car)
    print("Vehicle parked:", parking_lot.park_vehicle(car, SpotType.COMPACT))

    # A van enters the parking lot
    van = Vehicle('111111', VehicleType.VAN)
    van_ticket = entrance.get_ticket(van)
    print("Vehicle parked:", parking_lot.park_vehicle(van, SpotType.LARGE))

    # display the available spots after a car parks
    free_spots = parking_lot.display_free_spots()
    print("Free spots after enter:", free_spots)

    # 2 hours later, the car exits the parking lot
    exit_time = datetime.now() + timedelta(hours=2)
    payment_receipt = exit_gate.exit_car(ticket, exit_time, hour_rate)
    print(payment_receipt)

    # Remove the vehicle from the parking lot
    parking_lot.remove_vehicle(car, SpotType.COMPACT)

    # Display free spots after a vehicle has left
    free_spots = parking_lot.display_free_spots()
    print("Free spots after exit:", free_spots)
