## PROJECT TITLE
## Student Wellness Assistant

## INTRODUCTION

The Student Wellness Assistant is a simple Python project I built to help students track their daily habits, academic workload, and overall well-being. The idea came from a common issue many students face—irregular routines, poor sleep schedules, stress building up before exams, and forgetting important tasks. This tool tries to put everything in one place so students can check how they’re doing and plan better.

## OVERVIEW

This project lets a student enter daily details like sleep hours, study time, mood, steps/activity, and personal notes. It also includes a task management system where the user can add assignments, exams, deadlines, or even everyday personal tasks. All the data gets stored in CSV files, and the program analyses it to show weekly averages, burnout levels, and urgent tasks.

The idea is to keep it simple, easy to use, and fully aligned with the project requirements such as modular code, clear input/output, workflow, and documentation. I also implemented a task browser and a basic recommendation system that gives the user quick suggestions based on their routine.

## FEATURES

• Daily Log Module

• Enter sleep, study hours, mood, steps, and notes

• Stores data in daily_log.csv

• Task Management Module

• Add exams, assignments, personal to-do items

• Deadline + importance level

• Stored in tasks.csv

• Wellness Dashboard Module

• Shows 7-day averages

• Estimates burnout risk (Low/Medium/High)

• Prioritizes tasks based on urgency

• Task Browser

• View all tasks sorted by urgency

• Check top 5 urgent tasks

• Select a task to focus on

• Daily-Life Task Import

• Imports default tasks from daily_life_tasks.csv

• Helps combine academic and personal routines

## NON FUCTIONAL REQUIREMENTS

**Usability:**
Simple menu-driven interface, easy for students to use.

**Performance:**
Works instantly since it’s lightweight and uses basic file operations.

**Maintainability:**
Code is written in modular functions, so updates or new features can be added easily.

**Reliability:**
All data is stored in CSV format, so nothing is lost unless manually deleted.

**Error Handling:**
Basic validation for dates, numbers, and menu options.

## TECHNOLOGIES USED

● Python (core logic and implementation)

● CSV storage for logs and tasks

● Pandas (used for reading the daily tasks file)

● Date and Time modules

● Standard Python libraries (csv, os, datetime)

## HOW TO INSTALL AND RUN

Install Python 3.8 or above.

Install the required library:

```
pip install pandas
```


Make sure these files are in the same folder:


wellness_assistant.py
daily_log.csv       (auto-created)
tasks.csv           (auto-created)
daily_life_tasks.csv (provided)



Run the program:

python wellness_assistant.py

## HOW TO USE

Option 1 → Add your daily wellness log

Option 2 → Add assignments/exams

Option 3 → View the dashboard

Option 4 → Import default daily-life tasks

Option 5 → Browse tasks and check urgent ones

Option 6 → Exit

## WHY I CHOOSE THIS PROJECT

I wanted to build something that students can actually relate to. Almost all of us struggle with routines—either too much work, no proper sleep, stress piling up, or tasks getting mixed up. This project helped me understand how tracking small things daily can give useful insights, and at the same time it fits well with the subject’s requirement of applying concepts like modular programming, data handling, workflows, and user interaction.

## FUTURE IMPROVEMENTS

A GUI using Tkinter or PyQt

Graphs for sleep and study trends

Notifications or reminders

Cloud storage or mobile app version

AI-based prediction of stress or productivity patterns

Cloud storage or mobile app version

AI-based prediction of stress or productivity patterns

## Screenshots

## **Screenshot of Program After Execution**

<img width="1256" height="234" alt="Screenshot 2025-11-25 222130" src="https://github.com/user-attachments/assets/6c8abe97-deb9-499b-8962-45d1d7e850f1" />

## **Uploading Logs in Program**

<img width="584" height="680" alt="Screenshot 2025-11-25 222249" src="https://github.com/user-attachments/assets/2145be2b-cf0f-4c01-bae9-edf62cf3916c" />

## **Updated CSV file**

<img width="1555" height="320" alt="Screenshot 2025-11-25 223755" src="https://github.com/user-attachments/assets/2b19aa2d-64d1-4b82-a838-9f9ffcce81b1" />

## **Updated Task in Program**

<img width="980" height="615" alt="Screenshot 2025-11-25 222815" src="https://github.com/user-attachments/assets/c5a03283-ea1d-4d29-ba1a-3b7cbff9d107" />

## **Updated Task in CSV File**

<img width="361" height="201" alt="Screenshot 2025-11-25 223002" src="https://github.com/user-attachments/assets/b923fbef-bb45-4fed-b6b3-1954ae18ee21" />

## **Dashboard in Program**

<img width="996" height="906" alt="Screenshot 2025-11-25 223102" src="https://github.com/user-attachments/assets/5ae3fad0-2201-4f84-8b91-7b44bb8144b5" />

## **Exception Handling**

<img width="953" height="574" alt="Screenshot 2025-11-25 223158" src="https://github.com/user-attachments/assets/55aaf333-3971-4f79-a648-73da6a757b96" />

## **Some Code Snippets**

<img width="883" height="391" alt="Screenshot 2025-11-25 223311" src="https://github.com/user-attachments/assets/aa2972c5-02bf-44ce-8339-67b9350b7f6f" />

<img width="843" height="397" alt="Screenshot 2025-11-25 223251" src="https://github.com/user-attachments/assets/d6ffa4bb-94fe-4bfe-9ee1-666e0358afa0" />

<img width="883" height="391" alt="Screenshot 2025-11-25 223311" src="https://github.com/user-attachments/assets/a057cb2a-bea5-46c3-ac58-0b4735d3e644" />

## Design Diagrams

## **Use Case Diagram**

<img width="1024" height="1024" alt="Use_Case_Diagram" src="https://github.com/user-attachments/assets/4e755369-3ede-4b7b-afe9-4787867f1e80" />

## **Activity Diagram**

<img width="1024" height="1536" alt="Activity_Diagram" src="https://github.com/user-attachments/assets/665133b1-973a-4468-b002-8738dd6f9c88" />

## **WorkFlow Diagram**

<img width="1024" height="1536" alt="Workflow_Diagram" src="https://github.com/user-attachments/assets/34c884e5-24a3-4f9e-9c69-babb2bd8ceee" />

## **Sequence Diagram**

<img width="1024" height="1536" alt="Sequence_Diagram" src="https://github.com/user-attachments/assets/e8091adf-b604-424c-af80-f3604d502e25" />

## **Component Diagram**

<img width="1024" height="1024" alt="Component_Diagram" src="https://github.com/user-attachments/assets/bd315fdc-2788-4af1-806f-afa4065ef1f6" />

## **ER Diagram**

<img width="1024" height="1024" alt="ER_Diagram" src="https://github.com/user-attachments/assets/f6ede8e2-2b9b-4a85-9800-da62240e42ca" />
