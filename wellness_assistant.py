import csv
import os
from datetime import datetime, timedelta
DAILY_LOG_FILE = "daily_log.csv"
TASKS_FILE = "tasks.csv"
DEFAULT_TASKS_FILE = "daily_life_tasks.csv" 
def ensure_files_exist():
    if not os.path.exists(DAILY_LOG_FILE):
        with open(DAILY_LOG_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["date", "sleep_hours", "study_hours", "mood", "steps", "notes"])
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["name", "due_date", "importance"])
def parse_date(date_str):
    """Convert 'YYYY-MM-DD' string to datetime.date."""
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
        return None
def add_daily_log():
    print("\n--- Add Daily Log ---")
    date_str = input("Date (YYYY-MM-DD, blank for today): ").strip()
    if date_str == "":
        date = datetime.today().date()
    else:
        date = parse_date(date_str)
        if date is None:
            return
    try:
        sleep = float(input("Sleep hours: "))
        study = float(input("Study hours: "))
        mood = int(input("Mood (1-5, 1=very bad, 5=very good): "))
        steps = int(input("Steps / activity minutes (approx): "))
    except ValueError:
        print("Invalid number. Log cancelled.")
        return
    notes = input("Notes (optional): ")
    with open(DAILY_LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date.isoformat(), sleep, study, mood, steps, notes])
    print("Daily log saved!")
def add_task():
    print("\n--- Add Task / Exam / Assignment ---")
    name = input("Task name: ")
    due_str = input("Due date (YYYY-MM-DD): ").strip()
    due_date = parse_date(due_str)
    if due_date is None:
        return
    try:
        importance = int(input("Importance (1-5): "))
    except ValueError:
        print("Invalid importance. Task cancelled.")
        return
    with open(TASKS_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, due_date.isoformat(), importance])
    print("Task saved!")
def load_default_tasks():
    tasks = []
    if not os.path.exists(DEFAULT_TASKS_FILE):
        return tasks
    with open(DEFAULT_TASKS_FILE, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row.get("task", "").strip()
            if not name:
                continue
            priority_str = row.get("priority", "").strip().lower()
            if priority_str == "high":
                importance = 5
            elif priority_str == "low":
                importance = 1
            else:  
                importance = 3
            due_date = datetime.today().date()
            tasks.append({
                "name": name,
                "due_date": due_date,
                "importance": importance
            })
    return tasks
def load_tasks(include_default=True):
    tasks = []
    names_seen = set()
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                name = row["name"]
                t = {
                    "name": name,
                    "due_date": parse_date(row["due_date"]),
                    "importance": int(row["importance"])
                }
                tasks.append(t)
                names_seen.add(name)

    if include_default:
        for t in load_default_tasks():
            if t["name"] not in names_seen:
                tasks.append(t)
                names_seen.add(t["name"])
    return tasks
def load_daily_logs():
    logs = []
    if not os.path.exists(DAILY_LOG_FILE):
        return logs
    with open(DAILY_LOG_FILE, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            logs.append({
                "date": parse_date(row["date"]),
                "sleep": float(row["sleep_hours"]),
                "study": float(row["study_hours"]),
                "mood": int(row["mood"]),
                "steps": int(row["steps"]),
                "notes": row["notes"]
            })
    return logs
def import_default_tasks_to_main():
    default_tasks = load_default_tasks()
    if not default_tasks:
        print("\nNo default tasks found (is daily_life_tasks.csv in this folder?).")
        return
    existing_names = set()
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                existing_names.add(row["name"])
    imported_count = 0
    with open(TASKS_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        for t in default_tasks:
            if t["name"] in existing_names:
                continue
            writer.writerow([t["name"], t["due_date"].isoformat(), t["importance"]])
            imported_count += 1
            existing_names.add(t["name"])

    print(f"\nImported {imported_count} new daily-life tasks into your main task list.")
def filter_last_n_days(logs, n=7):
    if not logs:
        return []
    today = datetime.today().date()
    cutoff = today - timedelta(days=n - 1)
    return [log for log in logs if log["date"] and log["date"] >= cutoff]
def compute_averages(logs):
    if not logs:
        return None
    n = len(logs)
    avg_sleep = sum(log["sleep"] for log in logs) / n
    avg_study = sum(log["study"] for log in logs) / n
    avg_mood = sum(log["mood"] for log in logs) / n
    avg_steps = sum(log["steps"] for log in logs) / n
    return {
        "avg_sleep": avg_sleep,
        "avg_study": avg_study,
        "avg_mood": avg_mood,
        "avg_steps": avg_steps,
        "count": n
    }
def burnout_risk(logs):
    last3 = filter_last_n_days(logs, n=3)
    if not last3:
        return "Unknown"
    stats = compute_averages(last3)
    if stats is None:
        return "Unknown"
    sleep = stats["avg_sleep"]
    mood = stats["avg_mood"]
    if sleep < 6 and mood <= 2:
        return "High"
    elif sleep < 7 or mood <= 3:
        return "Medium"
    else:
        return "Low"
def calculate_task_urgency(tasks):
    today = datetime.today().date()
    scored = []
    for t in tasks:
        days_left = (t["due_date"] - today).days if t["due_date"] else 999
        if days_left <= 0:
            urgency = 999 
        else:
            urgency = t["importance"] * (1 / days_left)
        scored.append((urgency, days_left, t))
    scored.sort(key=lambda x: x[0], reverse=True)
    return scored
def generate_recommendations(logs, tasks):
    recs = []
    risk = burnout_risk(logs)
    recs.append(f"Burnout risk level: {risk}")
    if risk == "High":
        recs.append("• Aim for at least 7 hours of sleep tonight.")
        recs.append("• Take a 10–15 minute walk or light stretch.")
        recs.append("• Do one small, focused study block (20–25 mins).")
    elif risk == "Medium":
        recs.append("• Try to regularize sleep (maintain ~7 hours).")
        recs.append("• Plan 2 focused study blocks today.")
        recs.append("• Take short breaks instead of long social media sessions.")
    elif risk == "Low":
        recs.append("• Keep up your routine – it's working!")
        recs.append("• Plan study early for upcoming exams or deadlines.")
        recs.append("• Add some physical activity to maintain energy.")
    else:
        recs.append("• Add at least 3 days of logs to get personalized suggestions.")
    if tasks:
        urgency_list = calculate_task_urgency(tasks)
        recs.append("\nTop urgent tasks:")
        for i, (urg, days_left, t) in enumerate(urgency_list[:3], start=1):
            due_str = t["due_date"].isoformat()
            recs.append(f"  {i}. {t['name']} (due {due_str}, in {days_left} days)")
    else:
        recs.append("\nNo tasks added yet. Add your exams/assignments to plan better.")

    return recs
def show_dashboard():
    print("\n=== DAILY WELLNESS DASHBOARD ===")
    logs = load_daily_logs()
    tasks = load_tasks(include_default=True)

    last7 = filter_last_n_days(logs, n=7)
    stats = compute_averages(last7)
    if stats:
        print(f"\nData from last {stats['count']} day(s):")
        print(f"  Avg sleep:  {stats['avg_sleep']:.2f} hours")
        print(f"  Avg study:  {stats['avg_study']:.2f} hours")
        print(f"  Avg mood:   {stats['avg_mood']:.2f} / 5")
        print(f"  Avg steps:  {stats['avg_steps']:.0f}")
    else:
        print("\nNo data yet. Add a daily log first.")

    recs = generate_recommendations(logs, tasks)
    print("\n--- Recommendations ---")
    for line in recs:
        print(line)
def print_task_list(scored_tasks):
    print("\n#   Task Name                         Due Date    Days Left  Importance")
    print("---------------------------------------------------------------------")
    for idx, (urg, days_left, t) in enumerate(scored_tasks, start=1):
        name_display = (t["name"][:28] + "..") if len(t["name"]) > 30 else t["name"]
        due_str = t["due_date"].isoformat()
        print(f"{idx:>2}. {name_display:<32} {due_str}   {days_left:>5}      {t['importance']}")

def task_browser_menu():
    while True:
        tasks = load_tasks(include_default=True)
        if not tasks:
            print("\nNo tasks available. Add tasks from the main menu first.")
            return
        print("\n========== TASK BROWSER ==========")
        print("1. View all tasks (sorted by urgency)")
        print("2. View top 5 urgent tasks")
        print("3. Choose a task to focus on now")
        print("4. Back to main menu")
        choice = input("Choose an option (1-4): ").strip()
        scored = calculate_task_urgency(tasks)
        if choice == "1":
            print_task_list(scored)
        elif choice == "2":
            print_task_list(scored[:5])
        elif choice == "3":
            print_task_list(scored[:10])
            try:
                num = int(input("\nEnter task number to focus on (0 to cancel): "))
            except ValueError:
                print("Invalid input.")
                continue
            if num == 0:
                continue
            if not (1 <= num <= len(scored[:10])):
                print("Number out of range.")
                continue
            _, days_left, t = scored[num - 1]
            print(f"\nYou selected: {t['name']}")
            print(f"Due in {days_left} day(s), importance {t['importance']}.")
            print("Suggestion: Do one 25-minute focused session on this task now.")
        elif choice == "4":
            return
        else:
            print("Invalid choice. Try again.")
def main_menu():
    ensure_files_exist()
    while True:
        print("\n==============================")
        print(" Student Wellness Assistant")
        print("==============================")
        print("1. Add daily log")
        print("2. Add task / exam / assignment")
        print("3. Show dashboard & recommendations")
        print("4. Import daily-life tasks from CSV into my task list")
        print("5. Task browser (view & select tasks)")
        print("6. Exit")
        choice = input("Choose an option (1-6): ").strip()
        if choice == "1":
            add_daily_log()
        elif choice == "2":
            add_task()
        elif choice == "3":
            show_dashboard()
        elif choice == "4":
            import_default_tasks_to_main()
        elif choice == "5":
            task_browser_menu()
        elif choice == "6":
            print("Goodbye! Take care of yourself :)")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main_menu()
