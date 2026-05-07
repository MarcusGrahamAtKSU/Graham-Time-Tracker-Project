# Employee Time and Attendance Tracker
# Beginner-friendly version with:
# - Multiple employees
# - Monday-Friday schedule
# - Real time format
# - Input validation
# - Clear report output


# -----------------------------
# FUNCTION: Convert time to minutes
# -----------------------------
# This function turns times like "8:15 AM" into total minutes.
# Example: 8:15 AM = 495 minutes
def convert_time_to_minutes(time_text):
    time_text = time_text.strip().upper()

    # Split the time into two parts: time and AM/PM
    time_parts = time_text.split()

    if len(time_parts) != 2:
        return None

    clock_time = time_parts[0]
    am_pm = time_parts[1]

    if am_pm != "AM" and am_pm != "PM":
        return None

    if ":" not in clock_time:
        return None

    hour_minute = clock_time.split(":")

    if len(hour_minute) != 2:
        return None

    hour = hour_minute[0]
    minute = hour_minute[1]

    if not hour.isdigit() or not minute.isdigit():
        return None

    hour = int(hour)
    minute = int(minute)

    if hour < 1 or hour > 12:
        return None

    if minute < 0 or minute > 59:
        return None

    # Convert to 24-hour time minutes
    if am_pm == "AM":
        if hour == 12:
            hour = 0
    else:
        if hour != 12:
            hour = hour + 12

    total_minutes = hour * 60 + minute
    return total_minutes


# -----------------------------
# FUNCTION: Get valid time input
# -----------------------------
# This function keeps asking until the user enters a valid time.
# It also allows "0" for missed clock-out.
def get_valid_time(prompt, allow_zero=False):
    while True:
        user_time = input(prompt)

        # Allow 0 only when checking missed clock-out
        if allow_zero and user_time == "0":
            return "0", 0

        converted_time = convert_time_to_minutes(user_time)

        if converted_time is not None:
            return user_time.upper(), converted_time
        else:
            print("Invalid time. Please enter time like 8:00 AM or 5:00 PM.")


# -----------------------------
# MAIN PROGRAM
# -----------------------------

# Work days
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# Policy rule:
# Late after 8:07 AM
late_time = convert_time_to_minutes("8:07 AM")

# This list will store all employee records
employees = []

# Ask how many employees to enter
while True:
    employee_count = input("How many employees do you want to enter? ")

    if employee_count.isdigit() and int(employee_count) > 0:
        employee_count = int(employee_count)
        break
    else:
        print("Please enter a whole number greater than 0.")


# Loop through each employee
for employee_number in range(employee_count):

    print("\n====================================")
    print("Entering record for employee", employee_number + 1)
    print("====================================")

    employee_name = input("Enter employee name: ")

    # Store one employee's data
    employee_record = {
        "name": employee_name,
        "days": [],
        "total": 0
    }
    # Loop Monday-Friday
    for day in days:
        print("\n---", day, "---")

        # Ask for clock-in and clock-out using real time format
        clock_in_text, clock_in_minutes = get_valid_time(day + " clock-in time (example 8:00 AM): ")

        clock_out_text, clock_out_minutes = get_valid_time(
            day + " clock-out time (example 5:00 PM or 0 for missed clock-out): ",
            allow_zero=True
        )

        # Start daily occurrence count at 0
        occurrence = 0
        notes = []

        # Check late arrival
        if clock_in_minutes > late_time:
            occurrence = occurrence + 1
            notes.append("Late arrival")

        # Check missed clock-out
        if clock_out_text == "0":
            occurrence = occurrence + 1
            notes.append("Missed clock-out")

        # If no issues, mark as compliant
        if occurrence == 0:
            notes.append("Compliant")

        # Add daily occurrence to total
        employee_record["total"] = employee_record["total"] + occurrence

        # Store daily record
        employee_record["days"].append({
            "day": day,
            "clock_in": clock_in_text,
            "clock_out": clock_out_text,
            "occurrences": occurrence,
            "notes": notes
        })

    # Store the employee record
    employees.append(employee_record)


# -----------------------------
# OUTPUT REPORT
# -----------------------------
print("\n\n===================================================")
print("      TIME AND ATTENDANCE TRACKER REPORT")
print("===================================================")

for employee in employees:

    print("\nEmployee:", employee["name"])
    print("---------------------------------------------------")
    print("Day          Clock-In     Clock-Out     Occurrences     Notes")
    print("---------------------------------------------------")

    for day_record in employee["days"]:
        day_name = day_record["day"]
        clock_in = day_record["clock_in"]
        clock_out = day_record["clock_out"]
        occurrence = day_record["occurrences"]
        notes = ", ".join(day_record["notes"])

        print(f"{day_name:<12} {clock_in:<12} {clock_out:<13} {occurrence:<15} {notes}")

    print("---------------------------------------------------")
    print("Total Occurrences:", employee["total"])

    if employee["total"] >= 3:
        print("Status: ACTION NEEDED - Manager/HR Review Recommended")
    else:
        print("Status: Attendance within acceptable range")

print("\nEnd of report.")