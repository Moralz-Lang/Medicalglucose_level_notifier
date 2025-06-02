# Medical Glucose Monitoring Script for Hospitals or Clinics

# Import os module to allow file deletion
import os

# Prompting the user (hospital data processor) to enter patient's full name
patient_name = input("Enter patient's full name: ")

# Prompting for patient's age
age = input("Enter patient's age: ")

# Prompting for patient's contact info (can be phone number or email)
contact_info = input("Enter patient's contact number or email: ")

# Prompting for patient's date of birth in YYYY-MM-DD format
birth_date = input("Enter patient's date of birth (YYYY-MM-DD): ")

# Asking for the patient's glucose level and converting it to an integer
# If the user enters a non-numeric value, the program will exit with an error message
try:
    glucose_level = int(input("Enter patient's glucose level (mg/dL): "))
except ValueError:
    print("Invalid input. Glucose level must be a number.")
    exit()

# Checking if glucose level is low
if glucose_level < 70:
    status_message = "Low glucose level"  # Set message for low glucose
# Checking if glucose level is high
elif glucose_level > 140:
    status_message = "High glucose level"  # Set message for high glucose
# If glucose level is between 70 and 140, it's considered normal
else:
    status_message = "Normal glucose level"  # Set message for normal glucose

# Display the status message to the screen
print(status_message)

# Create a formatted string that includes all patient information and the glucose status
record = (
    f"Patient Name: {patient_name}\n"
    f"Age: {age}\n"
    f"Contact: {contact_info}\n"
    f"Date of Birth: {birth_date}\n"
    f"Glucose Level: {glucose_level} mg/dL\n"
    f"Status: {status_message}\n"
    f"{'-'*40}\n"  # Adds a visual separator line
)

# Write patient record to 'patient_glucose_levels.txt' in the same folder as this script
with open('patient_glucose_levels.txt', 'a') as file:
    file.write(record)

# If glucose level is high, write an urgent message to another file
if glucose_level > 140:
    with open('urgent_notifications.txt', 'a') as alert_file:
        alert_file.write(
            f"URGENT: Notify {patient_name} at {contact_info} - High glucose level detected ({glucose_level} mg/dL).\n"
        )

# Optional: Ask if the user wants to delete the files after logging
delete_files = input("Do you want to delete all saved patient data files? (yes/no): ").lower()

# Delete both data files if user agrees
if delete_files == 'yes':
    try:
        os.remove('patient_glucose_levels.txt')
        os.remove('urgent_notifications.txt')
        print("Patient data files deleted successfully.")
    except FileNotFoundError:
        print("Some or all data files do not exist.")

