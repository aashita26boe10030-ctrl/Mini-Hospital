class Patient:
    def __init__(self, patient_id, name, age, gender, department, doctor, status="Pending"):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.department = department
        self.doctor = doctor
        self.status = status

    def display(self):
        print(f"ID: {self.patient_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Department: {self.department}")
        print(f"Assigned Doctor: {self.doctor}")
        print(f"Consultation Status: {self.status}")
        print("-" * 35)


class HospitalRecordSystem:
    def __init__(self):
        self.patients = {}

    def add_patient(self):
        pid = input("Enter Patient ID: ").strip()
        if pid in self.patients:
            print("Patient ID already exists.\n")
            return
        name = input("Enter Patient Name: ").strip()
        age = input("Enter Age: ").strip()
        gender = input("Enter Gender: ").strip()
        department = input("Enter Department: ").strip()
        doctor = input("Enter Assigned Doctor: ").strip()
        
        self.patients[pid] = Patient(pid, name, age, gender, department, doctor)
        print("Patient record added successfully.\n")

    def search_patient(self):
        query = input("Enter Patient ID or Name to search: ").strip().lower()
        found = False
        for patient in self.patients.values():
            if query == patient.patient_id.lower() or query == patient.name.lower():
                print("\n--- Patient Found ---")
                patient.display()
                found = True
        if not found:
            print("No matching record found.\n")

    def display_all_patients(self):
        if not self.patients:
            print("No patient records available.\n")
            return
        print("\n--- All Patient Records ---")
        for patient in self.patients.values():
            patient.display()

    def update_assignment(self):
        pid = input("Enter Patient ID to reassign: ").strip()
        if pid not in self.patients:
            print("Patient ID not found.\n")
            return
        patient = self.patients[pid]
        new_department = input("Enter New Department (leave blank to keep current): ").strip()
        new_doctor = input("Enter New Assigned Doctor (leave blank to keep current): ").strip()
        
        if new_department:
            patient.department = new_department
        if new_doctor:
            patient.doctor = new_doctor
        print("Assignment updated successfully.\n")

    def update_status(self):
        pid = input("Enter Patient ID to update status: ").strip()
        if pid not in self.patients:
            print("Patient ID not found.\n")
            return
        print("Select Status: [1] Pending  [2] In Consultation  [3] Completed")
        choice = input("Enter choice (1-3): ").strip()
        status_map = {"1": "Pending", "2": "In Consultation", "3": "Completed"}
        if choice in status_map:
            self.patients[pid].status = status_map[choice]
            print("Consultation status updated.\n")
        else:
            print("Invalid status selection.\n")


def main():
    system = HospitalRecordSystem()
    while True:
        print("=== Mini Hospital Record System ===")
        print("1. Add Patient")
        print("2. Search Patient")
        print("3. Display All Patients")
        print("4. Assign Doctor / Department")
        print("5. Update Consultation Status")
        print("6. Exit")
        
        choice = input("Enter choice (1-6): ").strip()
        print()
        
        if choice == "1":
            system.add_patient()
        elif choice == "2":
            system.search_patient()
        elif choice == "3":
            system.display_all_patients()
        elif choice == "4":
            system.update_assignment()
        elif choice == "5":
            system.update_status()
        elif choice == "6":
            print("Exiting application.")
            break
        else:
            print("Invalid selection. Please try again.\n")


if __name__ == "__main__":
    main()
