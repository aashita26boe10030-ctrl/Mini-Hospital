# Mini Hospital / Patient Record System

A simple **Python console-based Hospital Patient Record Management System** developed using Object-Oriented Programming (OOP) concepts.

## 📌 Project Overview

The Mini Hospital / Patient Record System allows users to manage basic patient records through a command-line interface.

The system can:

* Add new patients
* Search patients by ID or name
* Display all patient records
* Assign or update doctors and departments
* Update consultation status
* Delete patient records
* Prevent duplicate Patient IDs

The project is designed as an educational application to demonstrate Python programming, classes, objects, dictionaries, methods, loops, conditional statements, and basic data management.

---

## 🛠️ Technologies Used

| Technology    | Purpose                              |
| ------------- | ------------------------------------ |
| Python 3      | Core programming language            |
| OOP           | Patient and hospital system modeling |
| Dictionary    | In-memory patient storage            |
| Console / CLI | User interface                       |
| Git / GitHub  | Version control                      |

No external Python packages are required.

---

## 📂 Project Structure

```text
Mini-Hospital-Patient-Record-System/
│
├── main.py
├── Database/
│   └── .gitkeep
│
├── Statement/
│   └── Project_Statement.md
│
├── README.md
│
└── .gitignore
```

---

## ⚙️ Features

### 1. Add Patient

Users can enter:

* Patient ID
* Patient Name
* Age
* Gender
* Assigned Doctor
* Department
* Consultation Status

If the consultation status is left blank, the system automatically assigns:

```text
Scheduled
```

The system also prevents duplicate Patient IDs.

---

### 2. Search Patient

Patients can be searched using:

```text
Patient ID
```

or

```text
Patient Name
```

The search is case-insensitive.

Example:

```text
Enter Patient ID or Name to search: p101
```

will match:

```text
P101
```

---

### 3. Display All Patients

The system can display every patient currently stored in memory.

Example:

```text
========================================
Patient ID          : P101
Name                : Rahul Sharma
Age                 : 35
Gender              : Male
Assigned Doctor     : Dr. Mehta
Department          : Cardiology
Consultation Status : Scheduled
========================================
```

---

### 4. Assign / Update Doctor and Department

An existing patient's assigned doctor and department can be modified.

The current values are displayed before updating.

Pressing Enter without entering a new value keeps the existing value.

---

### 5. Update Consultation Status

The system provides four predefined statuses:

```text
1. Scheduled
2. In Progress
3. Completed
4. Cancelled
```

A custom status can also be entered.

---

### 6. Delete Patient

A patient record can be removed using the Patient ID.

Example:

```text
Enter Patient ID to delete: P101

Patient record P101 has been removed.
```

---

## 🧱 Object-Oriented Design

The project contains two primary classes.

### Patient

The `Patient` class represents an individual patient.

```python
class Patient:
```

It stores:

```text
patient_id
name
age
gender
doctor
department
consultation_status
```

### HospitalRecordSystem

The `HospitalRecordSystem` class manages the patient records and provides operations such as:

```text
add_patient()
search_patient()
display_all_patients()
assign_doctor_department()
update_consultation_status()
delete_patient()
```

---

## 💾 Data Storage

Currently, patient records are stored in a Python dictionary:

```python
self.patients = {}
```

The Patient ID acts as the dictionary key.

Conceptually:

```text
Patient ID
    ↓
P101 ──────→ Patient Object
P102 ──────→ Patient Object
P103 ──────→ Patient Object
```

### Important

This version uses **in-memory storage**.

Therefore, patient records are lost when the program terminates.

A future version can use:

* SQLite
* MySQL
* PostgreSQL
* MongoDB

for persistent storage.

---

## ▶️ How to Run

### Step 1 — Install Python

Install Python 3 on your system.

Verify installation:

```bash
python --version
```

or:

```bash
python3 --version
```

### Step 2 — Clone the Repository

```bash
git clone <repository-url>
```

### Step 3 — Navigate to the Project

```bash
cd Mini-Hospital-Patient-Record-System
```

### Step 4 — Run the Program

```bash
python main.py
```

or:

```bash
python3 main.py
```

---

## 🖥️ Main Menu

When the application starts:

```text
==== Mini Hospital / Patient Record System ====

1. Add Patient
2. Search Patient
3. Display Patient Details (All Records)
4. Assign / Update Doctor and Department
5. Update Consultation Status
6. Delete Patient Record
7. Exit

Select an option (1-7):
```

---

## 🔄 Application Workflow

```text
                ┌───────────────┐
                │     Start     │
                └───────┬───────┘
                        ↓
             ┌─────────────────────┐
             │ Create Hospital     │
             │ Record System       │
             └──────────┬──────────┘
                        ↓
             ┌─────────────────────┐
             │    Display Menu     │
             └──────────┬──────────┘
                        ↓
             ┌─────────────────────┐
             │  Read User Choice   │
             └──────────┬──────────┘
                        ↓
       ┌────────────────┼────────────────┐
       ↓                ↓                ↓
   Add/Search       Update/Delete      Exit
       │                │                │
       └────────────────┼────────────────┘
                        ↓
                 Return to Menu
```

---

## 🧪 Example

```text
Select an option (1-7): 1

Enter Patient ID: P101
Enter Patient Name: Rahul Sharma
Enter Age: 35
Enter Gender: Male
Enter Assigned Doctor: Dr. Mehta
Enter Assigned Department: Cardiology
Enter Consultation Status ... [Default: Scheduled]:

Patient 'Rahul Sharma' added successfully.
```

Search:

```text
Select an option (1-7): 2

Enter Patient ID or Name to search: P101

========================================
Patient ID          : P101
Name                : Rahul Sharma
Age                 : 35
Gender              : Male
Assigned Doctor     : Dr. Mehta
Department          : Cardiology
Consultation Status : Scheduled
========================================
```

---

## ⚠️ Current Limitations

This is a basic educational project and currently does not provide:

* Database persistence
* User authentication
* Role-based access control
* GUI
* Web interface
* Appointment scheduling
* Billing
* Prescription management
* Medical history
* Laboratory records
* Backup and recovery
* Audit logging

It should therefore not be used as a production hospital information system or with real patient data without appropriate security, privacy, validation, and compliance controls.

---

## 🚀 Future Enhancements

Possible improvements include:

1. SQLite/MySQL database integration
2. Login and authentication
3. Admin/Doctor/Receptionist roles
4. Web-based interface
5. Patient appointment management
6. Doctor management
7. Department management
8. Medical history
9. Prescription management
10. Billing management
11. Search and filtering
12. Database backup
13. Audit logs
14. REST API
15. Dashboard and analytics

---

## 📈 Future Architecture

A larger version could follow:

```text
                Frontend
                   │
                   ↓
             REST API
                   │
                   ↓
          Backend Application
                   │
        ┌──────────┴──────────┐
        ↓                     ↓
 Authentication          Business Logic
                              │
                              ↓
                         Database
                              │
                ┌─────────────┼─────────────┐
                ↓             ↓             ↓
             Patients      Doctors      Departments
```

---

## 🎓 Learning Outcomes

This project demonstrates:

* Python fundamentals
* Object-Oriented Programming
* Classes and objects
* Constructors
* Instance attributes
* Methods
* Dictionaries
* List comprehensions
* Conditional statements
* Loops
* User input
* Basic validation
* CRUD-style operations
* Software project organization

---

## 📜 License

This project is intended for educational and learning purposes.

---

## 👨‍💻 Author

**Mini Hospital / Patient Record System**

Developed as a Python Object-Oriented Programming project.
