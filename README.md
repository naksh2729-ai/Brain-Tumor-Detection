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
