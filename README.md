# Employee Time & Attendance Tracker

## Overview

The **Employee Time and Attendance Tracker** is a Python-based application designed to simulate real-world workforce management. The system collects employee clock-in and clock-out times, validates inputs, applies attendance policies, and generates a structured weekly report.

This project demonstrates core concepts in **data validation, time processing, rule-based logic, and reporting**, making it applicable to environments such as healthcare operations, corporate workforce management, and IT systems.


## Features

* Tracks **Monday–Friday attendance**
* Supports **multiple employees**
* Accepts real-time input format (e.g., `8:00 AM`, `5:00 PM`)
* Built-in **input validation**
* Detects:

  * Late arrivals (after 8:07 AM)
  * Missed clock-outs
*  Calculates:

  * Daily occurrences
  * Weekly total occurrences
*  Generates a **clean, formatted attendance report**
*  Option to **export report to file**

---

##  Business Logic

The system applies the following rules:

* Employees are considered **late** if clock-in time is after **8:07 AM**
* A **missed clock-out** (entered as `0`) counts as an occurrence
* **3 or more occurrences** in a week triggers:

  * **Manager/HR review recommendation**
* Otherwise:

  * Employee is marked as **compliant**

---

## Technologies Used

* **Python 3**
* Standard libraries only (no external dependencies)

---

##  How to Run the Program

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/employee-time-tracker.git
cd employee-time-tracker
```

### 2. Run the script

```bash
python tracker.py
```

### 3. Enter input when prompted

Example input:

```text
8:00 AM
5:00 PM
0   (for missed clock-out)
```

---

##  Example Output

```text
===================================================
      TIME AND ATTENDANCE TRACKER REPORT
===================================================

Employee: Marcus Graham
---------------------------------------------------
Day          Clock-In     Clock-Out     Occurrences     Notes
---------------------------------------------------
Monday       8:00 AM      5:00 PM       0               Compliant
Tuesday      8:15 AM      5:00 PM       1               Late arrival
Wednesday    8:00 AM      0             1               Missed clock-out
---------------------------------------------------
Total Occurrences: 2
Status: Attendance within acceptable range
```

##  Project Structure

```text
employee-time-tracker/
│── tracker.py
│── README.md
│── weekly_attendance_report.txt (optional output file)
```

##  Key Concepts Demonstrated

* Input validation using loops and conditionals
* Time conversion and comparison logic
* Use of:

  * Lists
  * Dictionaries
  * Functions
* Structured data storage and reporting
* Basic business rule implementation


##  Limitations

* Uses manual user input (no real-time system integration)
* No database storage (data resets each run)
* Simplified attendance policies


##  Future Enhancements

* Integration with a **database (SQL)**
* Export reports to **Excel or CSV**
* Build a **web or GUI interface**
* Add **real-time clock tracking**
* Implement **advanced HR policies**


##  Author

**Marcus Graham**



##  License

This project is for educational and demonstration purposes
