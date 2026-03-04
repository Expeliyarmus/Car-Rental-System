# Car-Rental-System
# 🚗 Vehicle Rental System

A simple console-based **Vehicle Rental System** built in Python as a first-year ECE project by **Kunal Kapur**.

---

## 📋 Description

This program simulates a basic vehicle rental system that allows users to rent either a **Car** or a **Bike**. It collects vehicle details, checks availability, and calculates the total rental cost based on the number of days.

---

## ✨ Features

- Supports two types of vehicles: **Car** and **Bike**
- Collects vehicle information (name, rent per day, availability)
- Bike-specific detail: engine capacity (cc)
- Car-specific detail: number of seats
- Displays a summary of the vehicle details
- Calculates and displays the **total rental cost**

---

## 🛠️ Technologies Used

- **Language:** Python 3
- **Concepts:** Object-Oriented Programming (OOP), Inheritance, Classes

---

## 🏗️ Project Structure

```
Vehicle Rental System
│
├── class vehicle          # Base class with name, rent/day, availability
│   ├── class car          # Inherits vehicle; adds number of seats
│   └── class bike         # Inherits vehicle; adds engine capacity (cc)
│
└── main logic             # Input collection and rental cost calculation
```

---

## 🚀 How to Run

1. Make sure **Python 3** is installed on your system.
2. Download or clone the project file.
3. Open a terminal and navigate to the project directory.
4. Run the script:

```bash
python "project by Kunal kapur ECE First year.py"
```

5. Follow the on-screen prompts to enter vehicle details and rental duration.

---

## 💡 Sample Usage

```
Vehicle Rental System
Type of Vehicles Available Here: Car, Bike

Enter the vehicle type that you want to rent: Car
Enter the name of the vehicle: Toyota Corolla
Enter the rent of the vehicle: 1500
Enter Available Or Rented: Available
Enter no. of seats: 5

name        rent    availability    seats
Toyota Corolla  1500    Available       5

Enter the no. of days to be taken for rent: 3
Total cost of rent: 4500
```

---

## 📚 Concepts Demonstrated

- **Classes and Objects** — `vehicle`, `car`, `bike`
- **Inheritance** — `car` and `bike` extend the base `vehicle` class
- **`super()`** — Used to call the parent class constructor
- **User Input Handling** — `input()` and `int()` for type conversion
- **Conditional Logic** — `if` statements to handle different vehicle types

---

## 👤 Author

**Kunal Kapur**  
ECE — First Year  

---

## 📌 Notes

This is a beginner-level academic project focused on demonstrating core Python OOP concepts. Future improvements could include:

- Input validation and error handling
- A menu-driven interface
- Storing and retrieving multiple vehicle records
- File or database integration for persistent data
