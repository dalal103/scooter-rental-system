# ============================================================
# Scooter Rental Management System
# SWE-320: Object Oriented Programming
# By: Dalal Almansoori (202310976)
# ============================================================

import datetime


# ============================================================
# CLASS: Station
# Represents a scooter docking station
# ============================================================
class Station:
    """Class to represent a scooter docking station."""

    def __init__(self, station_id="", name="", location="", capacity=0):
        self.__stationID = station_id
        self.__name = name
        self.__location = location
        self.__capacity = capacity
        self.__scooters = []  # List of Scooter objects (Composition)

    # Getters and Setters
    def getStationID(self):
        return self.__stationID

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getLocation(self):
        return self.__location

    def setLocation(self, location):
        self.__location = location

    def getCapacity(self):
        return self.__capacity

    def getScooters(self):
        return self.__scooters

    def getAvailableCount(self):
        """Returns number of scooters with AVAILABLE status."""
        count = 0
        for scooter in self.__scooters:
            if scooter.getStatus() == "AVAILABLE":
                count += 1
        return count

    def addScooter(self, scooter):
        """Add a scooter to this station if capacity allows."""
        if len(self.__scooters) < self.__capacity:
            self.__scooters.append(scooter)
            scooter.setStationID(self.__stationID)
            print("Scooter " + scooter.getScooterID() + " added to station " + self.__name)
        else:
            print("Station " + self.__name + " is at full capacity.")

    def removeScooter(self, scooter_id):
        """Remove a scooter from this station by ID."""
        for scooter in self.__scooters:
            if scooter.getScooterID() == scooter_id:
                self.__scooters.remove(scooter)
                print("Scooter " + scooter_id + " removed from station " + self.__name)
                return scooter
        print("Scooter " + scooter_id + " not found at station " + self.__name)
        return None

    def displayStation(self):
        """Display station details."""
        print("--- Station Details ---")
        print("ID       : " + self.__stationID)
        print("Name     : " + self.__name)
        print("Location : " + self.__location)
        print("Capacity : " + str(self.__capacity))
        print("Available: " + str(self.getAvailableCount()))


# ============================================================
# CLASS: Scooter
# Represents a scooter in the system
# ============================================================
class Scooter:
    """Class to represent a scooter."""

    def __init__(self, scooter_id="", scooter_type="STANDARD", battery=100):
        self.__scooterID = scooter_id
        self.__type = scooter_type        # STANDARD or PREMIUM
        self.__batteryLevel = battery
        self.__status = "AVAILABLE"       # AVAILABLE, RESERVED, IN_USE, MAINTENANCE
        self.__stationID = ""

    # Getters and Setters
    def getScooterID(self):
        return self.__scooterID

    def getType(self):
        return self.__type

    def getBatteryLevel(self):
        return self.__batteryLevel

    def setBatteryLevel(self, level):
        self.__batteryLevel = level

    def getStatus(self):
        return self.__status

    def setStatus(self, status):
        self.__status = status

    def getStationID(self):
        return self.__stationID

    def setStationID(self, station_id):
        self.__stationID = station_id

    def unlock(self):
        """Unlock scooter when rental starts."""
        if self.__status == "AVAILABLE" or self.__status == "RESERVED":
            self.__status = "IN_USE"
            print("Scooter " + self.__scooterID + " is now unlocked and IN_USE.")
        else:
            print("Scooter " + self.__scooterID + " cannot be unlocked. Status: " + self.__status)

    def reportFault(self):
        """Mark scooter as under maintenance."""
        self.__status = "MAINTENANCE"
        print("Scooter " + self.__scooterID + " reported faulty. Status: MAINTENANCE.")

    def displayScooter(self):
        """Display scooter details."""
        print("Scooter ID : " + self.__scooterID)
        print("Type       : " + self.__type)
        print("Battery    : " + str(self.__batteryLevel) + "%")
        print("Status     : " + self.__status)
        print("Station    : " + self.__stationID)


# ============================================================
# CLASS: MaintenanceRecord
# Records maintenance events for a scooter
# ============================================================
class MaintenanceRecord:
    """Class to represent a maintenance record for a scooter."""

    def __init__(self, record_id="", scooter_id="", description=""):
        self.__recordID = record_id
        self.__scooterID = scooter_id
        self.__description = description
        self.__reportedDate = datetime.datetime.now()
        self.__resolvedDate = None
        self.__technicianID = ""

    # Getters and Setters
    def getRecordID(self):
        return self.__recordID

    def getScooterID(self):
        return self.__scooterID

    def getDescription(self):
        return self.__description

    def getTechnicianID(self):
        return self.__technicianID

    def setTechnicianID(self, tech_id):
        self.__technicianID = tech_id

    def markRepaired(self, technician_id):
        """Close the maintenance record after repair."""
        self.__resolvedDate = datetime.datetime.now()
        self.__technicianID = technician_id
        print("Maintenance record " + self.__recordID + " closed. Repaired by: " + technician_id)

    def displayRecord(self):
        """Display maintenance record details."""
        print("Record ID   : " + self.__recordID)
        print("Scooter ID  : " + self.__scooterID)
        print("Description : " + self.__description)
        print("Reported    : " + str(self.__reportedDate))
        resolved = str(self.__resolvedDate) if self.__resolvedDate else "Not yet resolved"
        print("Resolved    : " + resolved)

# ============================================================
# CLASS: Payement
# Represents a payement transaction for a rental
# ============================================================
class Payment:
    """Class to represent a payment for a scooter."""

    def __init__(self, payment_id="", amount=0.0, method="Credit Card"):
        self.__paymentID = payment_id
        self.__amount = amount
        self.__method = method
        self.__timestamp = datetime.datetime.now()
        self.__status = "PENDING"  # PENDING, COMPLETED, FAILED, REFUNDED

    # Getters
    def getPaymentID(self):
        return self.__paymentID

    def getAmount(self):
        return self.__amount

    def getStatus(self):
        return self.__status

    def processPayment(self):
        """Simulate processing the payment."""
        self.__status = "COMPLETED"
        print("Payment " + self.__paymentID + " of $" + str(round(self.__amount, 2)) + " processed successfully.")
        return True

    def refund(self):
        """Handle payment refund."""
        self.__status = "REFUNDED"
        print("Payment " + self.__paymentID + " has been refunded.")

    def displayPayment(self):
        """Display payment details."""
        print("Payment ID : " + self.__paymentID)
        print("Amount     : $" + str(round(self.__amount, 2)))
        print("Method     : " + self.__method)
        print("Timestamp  : " + str(self.__timestamp))
        print("Status     : " + self.__status)

# ============================================================
# CLASS: Rental
# Records a scooter rental transaction
# ============================================================
class Rental:
    """Class to represent a scooter rental."""

    # Rate per minute for each scooter type
    STANDARD_RATE = 0.10
    PREMIUM_RATE  = 0.20

    def __init__(self, rental_id="", user_id="", scooter_id="", scooter_type="STANDARD"):
        self.__rentalID   = rental_id
        self.__userID     = user_id
        self.__scooterID  = scooter_id
        self.__scooterType = scooter_type
        self.__startTime  = None
        self.__endTime    = None
        self.__totalCost  = 0.0
        self.__status     = "INITIATED"  # INITIATED, ACTIVE, COMPLETED, CANCELLED
        self.__payment    = None

    # Getters
    def getRentalID(self):
        return self.__rentalID

    def getUserID(self):
        return self.__userID

    def getScooterID(self):
        return self.__scooterID

    def getStatus(self):
        return self.__status

    def getTotalCost(self):
        return self.__totalCost

    def startRental(self):
        """Start the rental — record start time and set status to ACTIVE."""
        self.__startTime = datetime.datetime.now()
        self.__status = "ACTIVE"
        print("Rental " + self.__rentalID + " started at " + str(self.__startTime))

    def endRental(self):
        """End the rental — record end time, calculate cost, set COMPLETED."""
        self.__endTime = datetime.datetime.now()
        self.__status = "COMPLETED"
        self.calculateCost()
        pay_id = "PAY-" + self.__rentalID
        self.__payment = Payment(pay_id, self.__totalCost, "Credit Card")
        self.__payment.processPayment()

        print("Rental " + self.__rentalID + " completed. Total cost: $" + str(round(self.__totalCost, 2)))

    def calculateCost(self):
        """Calculate rental cost based on duration and scooter type."""
        if self.__startTime and self.__endTime:
            duration = self.__endTime - self.__startTime
            minutes = duration.total_seconds() / 60
            if self.__scooterType == "PREMIUM":
                self.__totalCost = minutes * Rental.PREMIUM_RATE
            else:
                self.__totalCost = minutes * Rental.STANDARD_RATE
        return self.__totalCost

    def cancelRental(self):
        """Cancel the rental before scooter is used."""
        if self.__status == "INITIATED":
            self.__status = "CANCELLED"
            print("Rental " + self.__rentalID + " has been cancelled.")
        else:
            print("Cannot cancel rental " + self.__rentalID + ". Status: " + self.__status)

    def displayRental(self):
        """Display rental details."""
        print("Rental ID  : " + self.__rentalID)
        print("User ID    : " + self.__userID)
        print("Scooter ID : " + self.__scooterID)
        print("Status     : " + self.__status)
        print("Total Cost : $" + str(round(self.__totalCost, 2)))


# ============================================================
# CLASS: Reservation
# Records a scooter reservation by a registered user
# ============================================================
class Reservation:
    """Class to represent a scooter reservation."""

    def __init__(self, reservation_id="", user_id="", scooter_id=""):
        self.__reservationID = reservation_id
        self.__userID        = user_id
        self.__scooterID     = scooter_id
        self.__reservedTime  = datetime.datetime.now()
        self.__status        = "ACTIVE"  # ACTIVE, CONFIRMED, EXPIRED, CANCELLED

    # Getters
    def getReservationID(self):
        return self.__reservationID

    def getUserID(self):
        return self.__userID

    def getScooterID(self):
        return self.__scooterID

    def getStatus(self):
        return self.__status

    def confirm(self):
        """Confirm the reservation."""
        self.__status = "CONFIRMED"
        print("Reservation " + self.__reservationID + " confirmed.")

    def cancel(self):
        """Cancel the reservation."""
        self.__status = "CANCELLED"
        print("Reservation " + self.__reservationID + " cancelled.")

    def expire(self):
        """Expire the reservation if not used in time."""
        self.__status = "EXPIRED"
        print("Reservation " + self.__reservationID + " has expired.")

    def displayReservation(self):
        """Display reservation details."""
        print("Reservation ID : " + self.__reservationID)
        print("User ID        : " + self.__userID)
        print("Scooter ID     : " + self.__scooterID)
        print("Reserved At    : " + str(self.__reservedTime))
        print("Status         : " + self.__status)


# ============================================================
# CLASS: User  (Parent / Abstract-like base class)
# Represents any user accessing the system
# ============================================================
class User:
    """Base class representing any user of the system."""

    def __init__(self, user_id="", name="", email="", phone=""):
        self._userID = user_id
        self._name   = name
        self._email  = email
        self._phone  = phone

    # Getters and Setters
    def getUserID(self):
        return self._userID

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def getEmail(self):
        return self._email

    def setEmail(self, email):
        self._email = email

    def getPhone(self):
        return self._phone

    def setPhone(self, phone):
        self._phone = phone

    def viewAvailability(self, stations):
        """View all available scooters across all stations."""
        print("\n=== Available Scooters ===")
        found = False
        for station in stations:
            for scooter in station.getScooters():
                if scooter.getStatus() == "AVAILABLE":
                    print("Scooter: " + scooter.getScooterID() +
                          " | Type: " + scooter.getType() +
                          " | Battery: " + str(scooter.getBatteryLevel()) + "%" +
                          " | Station: " + station.getName())
                    found = True
        if not found:
            print("No scooters are currently available.")

    def viewStations(self, stations):
        """View all station locations."""
        print("\n=== Station Locations ===")
        for station in stations:
            print("Station: " + station.getName() +
                  " | Location: " + station.getLocation() +
                  " | Available: " + str(station.getAvailableCount()))

    def __str__(self):
        return "User[" + self._userID + "] " + self._name


# ============================================================
# CLASS: Guest  (Child of User)
# Represents an unauthenticated visitor
# ============================================================
class Guest(User):
    """Class representing a guest (unauthenticated) user."""

    def __init__(self, user_id="", name="Guest"):
        User.__init__(self, user_id, name, "", "")

    def browseScooters(self, stations):
        """Browse available scooters without logging in."""
        print("\n[Guest] Browsing scooters...")
        self.viewAvailability(stations)

    def __str__(self):
        return "Guest[" + self._userID + "] " + self._name


# ============================================================
# CLASS: RegisteredUser  (Child of User)
# Represents an authenticated registered member
# ============================================================
class RegisteredUser(User):
    """Class representing a registered and authenticated user."""

    def __init__(self, user_id="", name="", email="", phone="", password=""):
        User.__init__(self, user_id, name, email, phone)
        self.__password      = password
        self.__paymentInfo   = "Visa **** 1234"
        self.__registrationDate = datetime.datetime.now()
        self.__rentalHistory = []       # List of Rental objects
        self.__reservations  = []       # List of Reservation objects
        self.__isLoggedIn    = False

    # Getters
    def getRentalHistory(self):
        return self.__rentalHistory

    def getReservations(self):
        return self.__reservations

    def isLoggedIn(self):
        return self.__isLoggedIn

    def login(self, password):
        """Authenticate the user with their password."""
        if password == self.__password:
            self.__isLoggedIn = True
            print("User " + self._name + " logged in successfully.")
            return True
        else:
            print("Login failed. Incorrect password.")
            return False

    def logout(self):
        """Log the user out of the system."""
        self.__isLoggedIn = False
        print("User " + self._name + " logged out.")

    def rentScooter(self, scooter, station, rental_id):
        """Rent an available scooter from a station."""
        if not self.__isLoggedIn:
            print("Please login first.")
            return None

        # Check scooter is available
        if scooter.getStatus() != "AVAILABLE" and scooter.getStatus() != "RESERVED":
            print("Scooter " + scooter.getScooterID() + " is not available. Status: " + scooter.getStatus())
            return None

        # Check station has available scooters
        if station.getAvailableCount() == 0:
            print("No available scooters at station " + station.getName())
            return None

        # Create rental record
        rental = Rental(rental_id, self._userID, scooter.getScooterID(), scooter.getType())

        # Unlock the scooter (include: Unlock Scooter)
        scooter.unlock()

        # Start the rental
        rental.startRental()

        # Add to rental history
        self.__rentalHistory.append(rental)

        print("Rental started for " + self._name + " on scooter " + scooter.getScooterID())
        return rental

    def returnScooter(self, rental, scooter, station):
        """Return the scooter to a station and complete the rental."""
        if not self.__isLoggedIn:
            print("Please login first.")
            return

        # End the rental and calculate cost (include: Calculate Rental Cost)
        rental.endRental()

        # Update scooter availability (include: Update Scooter Availability)
        scooter.setStatus("AVAILABLE")
        scooter.setStationID(station.getStationID())
        station.addScooter(scooter)

        print("Scooter " + scooter.getScooterID() + " returned to station " + station.getName())

    def reserveScooter(self, scooter, reservation_id):
        """Reserve an available scooter in advance."""
        if not self.__isLoggedIn:
            print("Please login first.")
            return None

        if scooter.getStatus() != "AVAILABLE":
            print("Scooter " + scooter.getScooterID() + " is not available for reservation.")
            return None

        # Create reservation and update scooter status
        reservation = Reservation(reservation_id, self._userID, scooter.getScooterID())
        scooter.setStatus("RESERVED")
        self.__reservations.append(reservation)

        print("Scooter " + scooter.getScooterID() + " reserved by " + self._name)
        return reservation

    def reportFault(self, scooter, description):
        """Report a faulty scooter."""
        if not self.__isLoggedIn:
            print("Please login first.")
            return None

        scooter.reportFault()
        record = MaintenanceRecord("MR-" + scooter.getScooterID(), scooter.getScooterID(), description)
        print(self._name + " reported fault: " + description)
        return record

    def viewHistory(self):
        """Display all past rentals for this user."""
        if not self.__isLoggedIn:
            print("Please login first.")
            return

        print("\n=== Rental History for " + self._name + " ===")
        if len(self.__rentalHistory) == 0:
            print("No rental history found.")
        else:
            for rental in self.__rentalHistory:
                rental.displayRental()
                print("---")

    def __str__(self):
        return "RegisteredUser[" + self._userID + "] " + self._name


# ============================================================
# CLASS: ScooterRentalSystem
# Main system class that manages everything
# ============================================================
class ScooterRentalSystem:
    """Main system class for the Scooter Rental Management System."""

    def __init__(self):
        self.__stations          = []   # List of Station objects
        self.__users             = []   # List of RegisteredUser objects
        self.__maintenanceRecords = []  # List of MaintenanceRecord objects
        self.__rentalCounter     = 1
        self.__reservationCounter = 1

    def addStation(self, station):
        """Add a station to the system."""
        for s in self.__stations:
            if s.getStationID() == station.getStationID():
                print("Station ID " + station.getStationID() + " already exists.")
                return
        self.__stations.append(station)
        print("Station " + station.getName() + " added to system.")

    def addUser(self, user):
        """Register a new user in the system."""
        for u in self.__users:
            if u.getUserID() == user.getUserID():
                print("User ID " + user.getUserID() + " already exists.")
                return
        self.__users.append(user)
        print("User " + user.getName() + " registered.")

    def findScooter(self, scooter_id):
        """Find a scooter by ID across all stations."""
        for station in self.__stations:
            for scooter in station.getScooters():
                if scooter.getScooterID() == scooter_id:
                    return scooter, station
        return None, None

    def findUser(self, user_id):
        """Find a registered user by ID."""
        for user in self.__users:
            if user.getUserID() == user_id:
                return user
        return None

    def generateRentalID(self):
        """Generate a unique rental ID."""
        rental_id = "R-" + str(self.__rentalCounter).zfill(4)
        self.__rentalCounter += 1
        return rental_id

    def generateReservationID(self):
        """Generate a unique reservation ID."""
        res_id = "RES-" + str(self.__reservationCounter).zfill(4)
        self.__reservationCounter += 1
        return res_id

    def markMaintenance(self, scooter_id, description, technician_id=""):
        """Mark a scooter for maintenance and create a record."""
        scooter, station = self.findScooter(scooter_id)
        if scooter:
            scooter.reportFault()
            record = MaintenanceRecord("MR-" + scooter_id, scooter_id, description)
            self.__maintenanceRecords.append(record)
            print("Maintenance record created for scooter " + scooter_id)
            return record
        else:
            print("Scooter " + scooter_id + " not found.")
            return None

    def repairScooter(self, scooter_id, technician_id):
        """Repair a scooter and restore it to AVAILABLE."""
        scooter, station = self.findScooter(scooter_id)
        if scooter and scooter.getStatus() == "MAINTENANCE":
            scooter.setStatus("AVAILABLE")
            # Close the maintenance record
            for record in self.__maintenanceRecords:
                if record.getScooterID() == scooter_id:
                    record.markRepaired(technician_id)
            print("Scooter " + scooter_id + " repaired and restored to AVAILABLE.")
        else:
            print("Scooter " + scooter_id + " is not under maintenance.")

    def viewAllStations(self):
        """Display all stations."""
        for station in self.__stations:
            station.displayStation()
            print()

    def viewMaintenanceRecords(self):
        """Display all maintenance records."""
        print("\n=== Maintenance Records ===")
        if len(self.__maintenanceRecords) == 0:
            print("No maintenance records found.")
        else:
            for record in self.__maintenanceRecords:
                record.displayRecord()
                print("---")

    def getStations(self):
        return self.__stations


# ============================================================
# MAIN – Test the System
# ============================================================
if __name__ == "__main__":

    print("=" * 50)
    print("  Scooter Rental Management System")
    print("=" * 50)

    # ── Create the system ─────────────────────────────────
    system = ScooterRentalSystem()

    # ── Create stations ───────────────────────────────────
    station1 = Station("ST-001", "Central Station", "Downtown", 5)
    station2 = Station("ST-002", "Marina Station", "Marina District", 3)
    system.addStation(station1)
    system.addStation(station2)

    # ── Create scooters ───────────────────────────────────
    scooter1 = Scooter("SC-001", "STANDARD", 95)
    scooter2 = Scooter("SC-002", "PREMIUM", 80)
    scooter3 = Scooter("SC-003", "STANDARD", 60)
    scooter4 = Scooter("SC-004", "PREMIUM", 100)

    # ── Add scooters to stations (Composition) ────────────
    station1.addScooter(scooter1)
    station1.addScooter(scooter2)
    station1.addScooter(scooter3)
    station2.addScooter(scooter4)

    # ── Create registered users ───────────────────────────
    user1 = RegisteredUser("U-001", "Ahmed Ali", "ahmed@email.com", "0501234567", "pass123")
    user2 = RegisteredUser("U-002", "Sara Hassan", "sara@email.com", "0507654321", "pass456")
    system.addUser(user1)
    system.addUser(user2)

    print("\n" + "=" * 50)
    print("  DEMO: Guest browsing")
    print("=" * 50)

    # ── Guest browsing (no login required) ────────────────
    guest = Guest("G-001")
    guest.browseScooters(system.getStations())
    guest.viewStations(system.getStations())

    print("\n" + "=" * 50)
    print("  DEMO: User Login and Rental")
    print("=" * 50)

    # ── User 1 logs in and rents a scooter ────────────────
    user1.login("pass123")
    rental1 = user1.rentScooter(scooter1, station1, system.generateRentalID())

    print("\n" + "=" * 50)
    print("  DEMO: User 2 Reserves a Scooter")
    print("=" * 50)

    # ── User 2 logs in and reserves a scooter ────────────
    user2.login("pass456")
    reservation1 = user2.reserveScooter(scooter2, system.generateReservationID())
    if reservation1:
        reservation1.displayReservation()

    print("\n" + "=" * 50)
    print("  DEMO: Return Scooter")
    print("=" * 50)

    # ── User 1 returns the scooter ────────────────────────
    if rental1:
        user1.returnScooter(rental1, scooter1, station1)

    print("\n" + "=" * 50)
    print("  DEMO: View Rental History")
    print("=" * 50)

    user1.viewHistory()

    print("\n" + "=" * 50)
    print("  DEMO: Report Fault and Maintenance")
    print("=" * 50)

    # ── Report a fault on scooter3 ────────────────────────
    record = user1.reportFault(scooter3, "Brakes not working properly")
    if record:
        system.markMaintenance(scooter3.getScooterID(), "Brakes not working properly")

    # ── Admin repairs the scooter ─────────────────────────
    system.repairScooter(scooter3.getScooterID(), "TECH-001")

    print("\n" + "=" * 50)
    print("  DEMO: View Maintenance Records")
    print("=" * 50)

    system.viewMaintenanceRecords()

    print("\n" + "=" * 50)
    print("  DEMO: View All Stations")
    print("=" * 50)

    system.viewAllStations()

    # ── Logout ─────────────────────────────────────────────
    user1.logout()
    user2.logout()

    print("\n" + "=" * 50)
    print("  System Demo Complete")
    print("=" * 50)
