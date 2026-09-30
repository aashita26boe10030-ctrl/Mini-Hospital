class Patient:
    def __init__(self, patient_id, name, age, gender, doctor, department, consultation_status="Scheduled"):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.doctor = doctor
        self.department = department
        self.consultation_status = consultation_status

    def display_details(self):
        print("\n" + "=" * 40)
        print(f"Patient ID          : {self.patient_id}")
        print(f"Name                : {self.name}")
        print(f"Age                 : {self.age}")
        print(f"Gender              : {self.gender}")
        print(f"Assigned Doctor     : {self.doctor}")
        print(f"Department          : {self.department}")
        print(f"Consultation Status : {self.consultation_status}")
        print("=" * 40)


class HospitalRecordSystem:
    def __init__(self):
        self.patients = {}

    def add_patient(self):
        pid = input("Enter Patient ID: ").strip()
        if pid in self.patients:
            print("Error: A patient with this ID already exists.")
            return

        name = input("Enter Patient Name: ").strip()
        age = input("Enter Age: ").strip()
        gender = input("Enter Gender: ").strip()
        doctor = input("Enter Assigned Doctor: ").strip()
        department = input("Enter Assigned Department: ").strip()
        status = input("Enter Consultation Status (e.g., Scheduled, In Progress, Completed) [Default: Scheduled]: ").strip()

        if not status:
            status = "Scheduled"

        self.patients[pid] = Patient(pid, name, age, gender, doctor, department, status)
        print(f"\nPatient '{name}' added successfully.")

    def search_patient(self):
        query = input("Enter Patient ID or Name to search: ").strip().lower()
        matches = [p for p in self.patients.values() if p.patient_id.lower() == query or p.name.lower() == query]

        if not matches:
            print("No matching patient records found.")
            return

        for patient in matches:
            patient.display_details()

    def display_all_patients(self):
        if not self.patients:
            print("No patient records available.")
            return

        for patient in self.patients.values():
            patient.display_details()

    def assign_doctor_department(self):
        pid = input("Enter Patient ID to update doctor/department: ").strip()
        patient = self.patients.get(pid)

        if not patient:
            print("Patient not found.")
            return

        new_doctor = input(f"Enter New Doctor (Current: {patient.doctor}): ").strip()
        new_department = input(f"Enter New Department (Current: {patient.department}): ").strip()

        if new_doctor:
            patient.doctor = new_doctor
        if new_department:
            patient.department = new_department

        print("Doctor and Department assignment updated successfully.")

    def update_consultation_status(self):
        pid = input("Enter Patient ID to update consultation status: ").strip()
        patient = self.patients.get(pid)

        if not patient:
            print("Patient not found.")
            return

        print("\nSelect Consultation Status:")
        print("1. Scheduled")
        print("2. In Progress")
        print("3. Completed")
        print("4. Cancelled")
        choice = input("Enter option number or type a custom status: ").strip()

        status_mapping = {
            "1": "Scheduled",
            "2": "In Progress",
            "3": "Completed",
            "4": "Cancelled"
        }

        patient.consultation_status = status_mapping.get(choice, choice)
        print(f"Consultation status updated to: {patient.consultation_status}")

    def delete_patient(self):
        pid = input("Enter Patient ID to delete: ").strip()
        if pid in self.patients:
            del self.patients[pid]
            print(f"Patient record {pid} has been removed.")
        else:
            print("Patient ID not found.")


def main():
    hospital = HospitalRecordSystem()

    menu = """
==== Mini Hospital / Patient Record System ====
1. Add Patient
2. Search Patient
3. Display Patient Details (All Records)
4. Assign / Update Doctor and Department
5. Update Consultation Status
6. Delete Patient Record
7. Exit
"""

    while True:
        print(menu)
        choice = input("Select an option (1-7): ").strip()

        if choice == "1":
            hospital.add_patient()
        elif choice == "2":
            hospital.search_patient()
        elif choice == "3":
            hospital.display_all_patients()
        elif choice == "4":
            hospital.assign_doctor_department()
        elif choice == "5":
            hospital.update_consultation_status()
        elif choice == "6":
            hospital.delete_patient()
        elif choice == "7":
            print("Exiting system.")
            break
        else:
            print("Invalid selection. Please choose an option between 1 and 7.")


if __name__ == "__main__":
    main()
