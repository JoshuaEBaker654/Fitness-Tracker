import tkinter as tk
from tkinter import ttk
import csv
import datetime
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ── Colors ──────────────────────────────────────────
BG        = "#FFFFFF"
PANEL     = "#3C5737"
ACCENT    = "#8b8b8b"
RED       = "#ff4444"
TEXT      = "#ffffff"
SUBTEXT   = "#aaaaaa"
ENTRY_BG  = "#3a3a5e"

# ── Root window ─────────────────────────────────────
root = tk.Tk()
root.title("Fitness Tracker")
root.geometry("1100x650")
root.resizable(True, True)
root.configure(bg=BG)

# ── Notebook ────────────────────────────────────────
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

home_tab    = tk.Frame(notebook, bg=BG)
lifting_tab = tk.Frame(notebook, bg=BG)
cardio_tab  = tk.Frame(notebook, bg=BG)
metrics_tab = tk.Frame(notebook, bg=BG)

notebook.add(home_tab,    text="Home")
notebook.add(lifting_tab, text="Lifting")
notebook.add(cardio_tab,  text="Cardio")
notebook.add(metrics_tab, text="Metrics")

# ── Left panel (LiftingTab) ─────────────────────────
left = tk.Frame(lifting_tab, bg=PANEL, width=320)
left.pack(side="left", fill="y", padx=10, pady=10)
left.pack_propagate(False)

tk.Label(left, text="Fitness Tracker", font=("Arial", 20, "bold"),
         bg=PANEL, fg=TEXT).pack(pady=20)

# Dropdown
tk.Label(left, text="Exercise", font=("Arial", 11),
         bg=PANEL, fg=TEXT).pack(pady=(10,2))
exercise_var = tk.StringVar()
exercise_dropdown = ttk.Combobox(left, textvariable=exercise_var, width=26)
exercise_dropdown.pack(pady=2)

# Weight
tk.Label(left, text="Weight (lbs)", font=("Arial", 11),
         bg=PANEL, fg=TEXT).pack(pady=(10,2))
weight_entry = tk.Entry(left, width=28, bg=ENTRY_BG, fg=TEXT,
                        insertbackground=TEXT, relief="flat")
weight_entry.pack(pady=2, ipady=4)

# Reps
tk.Label(left, text="Reps", font=("Arial", 11),
         bg=PANEL, fg=TEXT).pack(pady=(10,2))
reps_entry = tk.Entry(left, width=28, bg=ENTRY_BG, fg=TEXT,
                      insertbackground=TEXT, relief="flat")
reps_entry.pack(pady=2, ipady=4)

# ── Right panel (LiftingTab) ────────────────────────
right = tk.Frame(lifting_tab, bg=BG)
right.pack(side="right", fill="both", expand=True, padx=10, pady=10)

# Table frame
table_frame = tk.Frame(right, bg=PANEL)
table_frame.pack(fill="x", pady=(0,10))

style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview",
                background=PANEL,
                foreground=TEXT,
                fieldbackground=PANEL,
                rowheight=28,
                font=("Arial", 10))
style.configure("Treeview.Heading",
                background=ENTRY_BG,
                foreground=ACCENT,
                font=("Arial", 10, "bold"))

columns = ["Exercise", "Weight (lbs)", "Reps", "Date"]
tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=8)
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150)
tree.pack(fill="x", padx=5, pady=5)

# Chart frame
chart_frame = tk.Frame(right, bg=PANEL)
chart_frame.pack(fill="both", expand=True)

chart_label = tk.Label(chart_frame, text="Select an exercise and click Show Progress",
                       bg=PANEL, fg=SUBTEXT, font=("Arial", 12))
chart_label.pack(expand=True)

# ── Home Tab ─────────────────────────────────────────
home_top = tk.Frame(home_tab, bg=BG)
home_top.pack(fill="x", padx=20, pady=(20,10))

tk.Label(home_top, text="Welcome Back 💪", font=("Arial", 24, "bold"),
         bg=BG, fg=PANEL).pack(anchor="w")
tk.Label(home_top, text="Here's your fitness snapshot",
         font=("Arial", 12), bg=BG, fg=SUBTEXT).pack(anchor="w")

# ── Top row of cards ─────────────────────────────────
cards_top = tk.Frame(home_tab, bg=BG)
cards_top.pack(fill="x", padx=20, pady=10)

# Lifting PR card
lifting_pr_card = tk.Frame(cards_top, bg=PANEL, padx=15, pady=15)
lifting_pr_card.pack(side="left", fill="both", expand=True, padx=(0,10))
tk.Label(lifting_pr_card, text="🏋️ Top Lifting PR", font=("Arial", 11, "bold"),
         bg=PANEL, fg=SUBTEXT).pack(anchor="w")
lifting_pr_label = tk.Label(lifting_pr_card, text="--", font=("Arial", 20, "bold"),
                             bg=PANEL, fg=TEXT)
lifting_pr_label.pack(anchor="w", pady=(5,0))
lifting_pr_detail = tk.Label(lifting_pr_card, text="", font=("Arial", 10),
                              bg=PANEL, fg=SUBTEXT)
lifting_pr_detail.pack(anchor="w")

# Cardio PR card
cardio_pr_card = tk.Frame(cards_top, bg=PANEL, padx=15, pady=15)
cardio_pr_card.pack(side="left", fill="both", expand=True, padx=(0,10))
tk.Label(cardio_pr_card, text="🏃 Top Cardio PR", font=("Arial", 11, "bold"),
         bg=PANEL, fg=SUBTEXT).pack(anchor="w")
cardio_pr_label = tk.Label(cardio_pr_card, text="--", font=("Arial", 20, "bold"),
                            bg=PANEL, fg=TEXT)
cardio_pr_label.pack(anchor="w", pady=(5,0))
cardio_pr_detail = tk.Label(cardio_pr_card, text="", font=("Arial", 10),
                             bg=PANEL, fg=SUBTEXT)
cardio_pr_detail.pack(anchor="w")

# Streak card
streak_card = tk.Frame(cards_top, bg=PANEL, padx=15, pady=15)
streak_card.pack(side="left", fill="both", expand=True)
tk.Label(streak_card, text="🔥 Current Streak", font=("Arial", 11, "bold"),
         bg=PANEL, fg=SUBTEXT).pack(anchor="w")
streak_label = tk.Label(streak_card, text="--", font=("Arial", 20, "bold"),
                         bg=PANEL, fg=TEXT)
streak_label.pack(anchor="w", pady=(5,0))
tk.Label(streak_card, text="days in a row", font=("Arial", 10),
         bg=PANEL, fg=SUBTEXT).pack(anchor="w")

# ── Bottom row of cards ───────────────────────────────
cards_bottom = tk.Frame(home_tab, bg=BG)
cards_bottom.pack(fill="x", padx=20, pady=10)

# Body metrics card
metrics_card = tk.Frame(cards_bottom, bg=PANEL, padx=15, pady=15)
metrics_card.pack(side="left", fill="both", expand=True, padx=(0,10))
tk.Label(metrics_card, text="📊 Current Body Metrics", font=("Arial", 11, "bold"),
         bg=PANEL, fg=SUBTEXT).pack(anchor="w")
metrics_weight_label = tk.Label(metrics_card, text="Weight: --", font=("Arial", 13),
                                 bg=PANEL, fg=TEXT)
metrics_weight_label.pack(anchor="w", pady=(5,0))
metrics_fat_label = tk.Label(metrics_card, text="Body Fat: --", font=("Arial", 13),
                              bg=PANEL, fg=TEXT)
metrics_fat_label.pack(anchor="w")
metrics_muscle_label = tk.Label(metrics_card, text="Muscle Mass: --", font=("Arial", 13),
                                 bg=PANEL, fg=TEXT)
metrics_muscle_label.pack(anchor="w")

# Last workout card
last_workout_card = tk.Frame(cards_bottom, bg=PANEL, padx=15, pady=15)
last_workout_card.pack(side="left", fill="both", expand=True, padx=(0,10))
tk.Label(last_workout_card, text="📅 Last Workout", font=("Arial", 11, "bold"),
         bg=PANEL, fg=SUBTEXT).pack(anchor="w")
last_workout_label = tk.Label(last_workout_card, text="--", font=("Arial", 13),
                               bg=PANEL, fg=TEXT, wraplength=200, justify="left")
last_workout_label.pack(anchor="w", pady=(5,0))

# Month to month card
progress_card = tk.Frame(cards_bottom, bg=PANEL, padx=15, pady=15)
progress_card.pack(side="left", fill="both", expand=True)
tk.Label(progress_card, text="📈 Month to Month", font=("Arial", 11, "bold"),
         bg=PANEL, fg=SUBTEXT).pack(anchor="w")
monthly_label = tk.Label(progress_card, text="--", font=("Arial", 13),
                          bg=PANEL, fg=TEXT, wraplength=200, justify="left")
monthly_label.pack(anchor="w", pady=(5,0))

# ── Cardio tab ───────────────────────────
left_cardio_panel = tk.Frame(cardio_tab, bg=PANEL, width=320)
left_cardio_panel.pack(side="left", fill="y", padx=10, pady=10)
left_cardio_panel.pack_propagate(False)

tk.Label(left_cardio_panel, text="Cardio Tracker", font=("Arial", 20, "bold"),
         bg=PANEL, fg=TEXT).pack(pady=20)

tk.Label(left_cardio_panel, text="Cardio Type", font=("Arial", 11),
         bg=PANEL, fg=TEXT).pack(pady=(10,2))
activity_var = tk.StringVar()
activity_dropdown = ttk.Combobox(left_cardio_panel, textvariable=activity_var, width=26)
activity_dropdown.pack(pady=2)

tk.Label(left_cardio_panel, text="Distance (miles)", font=("Arial", 11),
         bg=PANEL, fg=TEXT).pack(pady=(10,2))
distance_entry = tk.Entry(left_cardio_panel, width=28, bg=ENTRY_BG, fg=TEXT,
                          insertbackground=TEXT, relief="flat")
distance_entry.pack(pady=2, ipady=4)

tk.Label(left_cardio_panel, text="Duration (minutes)", font=("Arial", 11),
         bg=PANEL, fg=TEXT).pack(pady=(10,2))
duration_entry = tk.Entry(left_cardio_panel, width=28, bg=ENTRY_BG, fg=TEXT,
                          insertbackground=TEXT, relief="flat")
duration_entry.pack(pady=2, ipady=4)

tk.Label(left_cardio_panel, text="Calories Burned", font=("Arial", 11),
         bg=PANEL, fg=TEXT).pack(pady=(10,2))
calories_entry = tk.Entry(left_cardio_panel, width=28, bg=ENTRY_BG, fg=TEXT,
                          insertbackground=TEXT, relief="flat")
calories_entry.pack(pady=2, ipady=4)

# Cardio Tab Right Panel
right_panel_cardio = tk.Frame(cardio_tab, bg=BG)
right_panel_cardio.pack(side="right", fill="both", expand=True, padx=10, pady=10)

# Cardio chart
cardio_chart = tk.Frame(right_panel_cardio, bg=PANEL)
cardio_chart.pack(fill="x", pady=(0,10))

cardio_style = ttk.Style()
cardio_style.theme_use("clam")
cardio_style.configure("Treeview",
                background=PANEL,
                foreground=TEXT,
                fieldbackground=PANEL,
                rowheight=28,
                font=("Arial", 10))
cardio_style.configure("Treeview.Heading",
                background=ENTRY_BG,
                foreground=ACCENT,
                font=("Arial", 10, "bold"))

cardio_columns = ["Type", "Distance", "Duration", "Calories", "Date"]
cardio_tree = ttk.Treeview(cardio_chart, columns=cardio_columns, show="headings", height=8)
for col in cardio_columns:
    cardio_tree.heading(col, text=col)
    cardio_tree.column(col, width=150)
cardio_tree.pack(fill="x", padx=5, pady=5)

# cardio chart frame
cardio_chart_frame = tk.Frame(right_panel_cardio, bg=PANEL)
cardio_chart_frame.pack(fill="both", expand=True)

cardio_chart_label = tk.Label(cardio_chart_frame, text="Cardio Activities", 
                              bg=PANEL, fg=TEXT, font=("Arial", 12))
cardio_chart_label.pack(expand=True)

# ── Body Metrics tab (left) ───────────────────── 

left_metrics_panel = tk.Frame(metrics_tab, bg=PANEL, width=320)
left_metrics_panel.pack(side="left", fill="y", padx=10, pady=10)
left_metrics_panel.pack_propagate(False)

tk.Label(left_metrics_panel, text="Body Metrics", font=("Arial", 20, "bold"),
         bg=PANEL, fg=TEXT).pack(pady=20)

tk.Label(left_metrics_panel, text="Body Weight (lbs)", font=("Arial", 11),
         bg=PANEL, fg=TEXT).pack(pady=(10,2))
body_weight_var = tk.StringVar()
body_weight_entry = tk.Entry(left_metrics_panel, textvariable=body_weight_var, width=26)
body_weight_entry.pack(pady=2)

tk.Label(left_metrics_panel, text="Body Fat (%)", font=("Arial", 11),
         bg=PANEL, fg=TEXT).pack(pady=(10,2))
body_fat_entry = tk.Entry(left_metrics_panel, width=26, bg=ENTRY_BG, fg=TEXT,
                          insertbackground=TEXT, relief="flat")
body_fat_entry.pack(pady=2)

tk.Label(left_metrics_panel, text="Muscle Mass (lbs)", font=("Arial", 11),
         bg=PANEL, fg=TEXT).pack(pady=(10,2))
muscle_mass_entry = tk.Entry(left_metrics_panel, width=26, bg=ENTRY_BG, fg=TEXT,
                             insertbackground=TEXT, relief="flat")
muscle_mass_entry.pack(pady=2)

# Body Metrics tab (right) ─────────────────────
right_metrics_panel = tk.Frame(metrics_tab, bg=BG)
right_metrics_panel.pack(side="right", fill="both", expand=True, padx=10, pady=10)

metrics_chart = tk.Frame(right_metrics_panel, bg=PANEL)
metrics_chart.pack(fill="x", pady=(0,10))

metrics_style = ttk.Style()
metrics_style.theme_use("clam")
metrics_style.configure("Treeview",
                background=PANEL,
                foreground=TEXT,
                fieldbackground=PANEL,
                rowheight=28,
                font=("Arial", 10))
metrics_style.configure("Treeview.Heading",
                background=ENTRY_BG,
                foreground=ACCENT,
                font=("Arial", 10, "bold"))

metrics_columns = ["Weight", "Body Fat", "Muscle Mass", "Date"]
metrics_tree = ttk.Treeview(metrics_chart, columns=metrics_columns, show="headings", height=8)
for col in metrics_columns:
    metrics_tree.heading(col, text=col)
    metrics_tree.column(col, width=150)
metrics_tree.pack(fill="x", padx=5, pady=5)

# metrics chart frame
metrics_chart_frame = tk.Frame(right_metrics_panel, bg=PANEL)
metrics_chart_frame.pack(fill="both", expand=True)

metrics_chart_label = tk.Label(metrics_chart_frame, text="Metrics", 
                              bg=PANEL, fg=TEXT, font=("Arial", 12))
metrics_chart_label.pack(expand=True)

# ── Functions ────────────────────────────────────────
# Home Tab Functions -----------------------------------
def top_lifting_pr():
    pr = 0
    exercise = ""
    try:
        with open("workouts.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[1] != '':
                    weight = float(row[1])
                    if weight > pr:
                        pr = weight
                        exercise = row[0]
    except FileNotFoundError:
        pass
    return exercise, pr

def top_cardio_pr():
    best_records = get_personal_records()
    if not best_records:
        return "", 0
    top_activity = max(best_records.items(), key=lambda x: x[1].get("calories", 0))
    return top_activity[0], top_activity[1].get("calories", 0)

def current_streak():
    try:
        with open("cardio.csv", "r") as file:
            reader = csv.reader(file)
            dates = [datetime.datetime.strptime(row[4], "%Y-%m-%d %H:%M:%S").date() for row in reader if len(row) >= 5 and row [4] != '']
            dates = sorted(set(dates), reverse=True)
            streak = 0
            today = datetime.date.today()
            for i, date in enumerate(dates):
                if i == 0 and date == today:
                    streak += 1
                elif i > 0 and (dates[i-1] - date).days == 1:
                    streak += 1
                else:
                    break
            return streak
    except FileNotFoundError:
        return 0


def load_home():
    # Lifting PR
    exercise, pr = top_lifting_pr()
    if exercise:
        lifting_pr_label.config(text=f"{pr} lbs")
        lifting_pr_detail.config(text=exercise)
    else:
        lifting_pr_label.config(text="No data yet")

    # Cardio PR
    activity, calories = top_cardio_pr()
    if activity:
        cardio_pr_label.config(text=f"{calories} cal")
        cardio_pr_detail.config(text=activity)
    else:
        cardio_pr_label.config(text="No data yet")

    # Current Streak
    streak = current_streak()
    streak_label.config(text=str(streak))

    # Body Metrics
    try:
        with open("metrics.csv", "r") as file:
            rows = list(csv.reader(file))
            if rows:
                last = rows[-1]
                metrics_weight_label.config(text=f"Weight: {last[0]} lbs")
                metrics_fat_label.config(text=f"Body Fat: {last[1]}%")
                metrics_muscle_label.config(text=f"Muscle Mass: {last[2]} lbs")
    except FileNotFoundError:
        pass

    # Last Workout
    try:
        with open("workouts.csv", "r") as file:
            rows = list(csv.reader(file))
            if rows:
                last = rows[-1]
                last_workout_label.config(text=f"{last[0]}\n{last[1]} lbs x {last[2]} reps\n{last[3]}")

    except FileNotFoundError:
        pass

    # Month to Month
    try:
        with open("workouts.csv", "r") as file:
            reader = csv.reader(file)
            this_month, last_month = [], []
            today = datetime.date.today()
            for row in reader:
                if len(row) >= 4 and row[1] != '':
                    date = datetime.datetime.strptime(row[3], "%Y-%m-%d %H:%M:%S").date()
                    volume = float(row[1]) * float(row[2])
                    if date.month == today.month and date.year == today.year:
                        this_month.append(volume)
                    elif date.month == (today.month - 1 or 12) and date.year == (today.year if today.month > 1 else today.year - 1):
                        last_month.append(volume)

            if this_month and last_month:
                avg_this = sum(this_month) / len(this_month)
                avg_last = sum(last_month) / len(last_month)
                change = ((avg_this - avg_last) / avg_last) * 100
                arrow = "📈" if change > 0 else "📉"
                monthly_label.config(text=f"{arrow} {change:+.1f}% vs last month")
            elif this_month:
                monthly_label.config(text="No data from last month to compare")
            else:
                monthly_label.config(text="No data this month yet")
    except FileNotFoundError:
        pass

# Lifting Functions -----------------------------------
def get_exercises():
    exercises = []
    try:
        with open("workouts.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] not in exercises:
                    exercises.append(row[0])
    except FileNotFoundError:
        pass
    return exercises

def get_personal_record(exercise):
    pr = 0
    try:
        with open("workouts.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == exercise and row[1] != '':
                    weight = float(row[1])
                    if weight > pr:
                        pr = weight
    except FileNotFoundError:
        pass
    return pr

def load_workouts():
    for row in tree.get_children():
        tree.delete(row)
    try:
        with open("workouts.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[1] != '':
                    pr = get_personal_record(row[0])
                    if float(row[1]) == pr:
                        tree.insert("", "end", values=row, tags=("PR",))
                    else:
                        tree.insert("", "end", values=row)
    except FileNotFoundError:
        pass
    tree.tag_configure("PR", background="#2a5a3a", foreground="white")
    exercise_dropdown["values"] = get_exercises()

def save_workout():
    exercise = exercise_dropdown.get() 
    weight = weight_entry.get()
    reps = reps_entry.get()
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("workouts.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([exercise, weight, reps, date])

    weight_entry.delete(0, tk.END)
    reps_entry.delete(0, tk.END)

    load_workouts()
    print("Workout saved!")

def delete_workout():
    selected_item = tree.selection()
    if not selected_item:
        print("No workout selected.")
        return
    row_values = tree.item(selected_item, "values")
    rows = []
    with open("workouts.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            rows.append(row)
    with open("workouts.csv", "w", newline="") as file:
        writer = csv.writer(file)
        for row in rows:
            if row != [str(v) for v in row_values]:
                writer.writerow(row)
    load_workouts()
    print("Workout deleted!")

def show_progress():
    exercise = exercise_dropdown.get()
    dates, volumes = [], []
    try:
        with open("workouts.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == exercise and row[1] != '' and row[2] != '':
                    volumes.append(float(row[1]) * float(row[2]))
                    dates.append(row[3])
    except FileNotFoundError:
        pass

    dates_formatted = [datetime.datetime.strptime(d, "%Y-%m-%d %H:%M:%S") for d in dates]

    for widget in chart_frame.winfo_children():
        widget.destroy()

    fig, ax = plt.subplots(figsize=(6, 3.5))
    fig.patch.set_facecolor("#2a2a3e")
    ax.set_facecolor("#1e1e2e")
    ax.plot(dates_formatted, volumes, marker="o", color="#00ff88", linewidth=2)
    ax.set_title(f"{exercise} Progress", fontsize=12, fontweight="bold",
                 color=TEXT)
    ax.set_xlabel("Date", fontsize=10, color=SUBTEXT)
    ax.set_ylabel("Volume (Weight x Reps)", fontsize=10, color=SUBTEXT)
    ax.tick_params(colors=SUBTEXT)
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%m/%d"))
    fig.autofmt_xdate()
    plt.tight_layout()

    canvas = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

# Cardio Functions -------------------------------------

def get_cardio(activity=None):
    cardio = []
    try:
        with open("cardio.csv", "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if not row or len(row) < 4:
                    continue
                if activity and row[0] != activity:
                    continue

                try:
                    distance = float(row[1]) if row[1] else 0.0
                except ValueError:
                    distance = 0.0

                try:
                    duration = float(row[2]) if row[2] else 0.0
                except ValueError:
                    duration = 0.0

                try:
                    calories = float(row[3]) if row[3] else 0.0
                except ValueError:
                    calories = 0.0

                cardio.append({
                    "activity": row[0],
                    "distance": distance,
                    "duration": duration,
                    "calories": calories,
                })
    except FileNotFoundError:
        pass
    return cardio

def get_personal_records(cardio_records=None):
    """Return the top cardio entry for each activity type.

    The best entry is selected by the highest calories value, with distance
    and duration as secondary tie-breakers.
    """
    if cardio_records is None:
        cardio_records = get_cardio()

    best_records = {}
    for record in cardio_records:
        activity = record.get("activity")
        if not activity:
            continue

        current = best_records.get(activity)
        if current is None:
            best_records[activity] = record
            continue

        compare_fields = ["calories", "distance", "duration"]
        for field in compare_fields:
            current_value = current.get(field, 0.0)
            record_value = record.get(field, 0.0)
            if record_value > current_value:
                best_records[activity] = record
                break
            elif record_value < current_value:
                break

    return best_records

def get_activities():
    activities = set()
    try:
        with open("cardio.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[0]:
                    activities.add(row[0])
    except FileNotFoundError:
        pass
    return activities

def load_cardio():
    """Loads cardio activities from the cardio.csv file to be displayed in the chart"""
    for row in cardio_tree.get_children():
        cardio_tree.delete(row)
    try:
        with open("cardio.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) >= 5:
                    pr = get_personal_records(get_cardio()).get(row[0])
                    if pr and float(row[3]) == pr.get("calories"):
                        cardio_tree.insert("", "end", values=row, tags=("PR",))
                    else:
                        cardio_tree.insert("", "end", values=row)
    except FileNotFoundError:
        pass
    cardio_tree.tag_configure("PR", background="#2a5a3a", foreground="white")
    activity_dropdown["values"] = list(get_activities())

def save_cardio():
    activity = activity_dropdown.get()
    distance = distance_entry.get()
    duration = duration_entry.get()
    calories = calories_entry.get()
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("cardio.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([activity, distance, duration, calories, date])

    distance_entry.delete(0, tk.END)
    duration_entry.delete(0, tk.END)
    calories_entry.delete(0, tk.END)

    load_cardio()
    print("Cardio activity saved!")

def delete_cardio():
    selected_item = cardio_tree.selection()
    if not selected_item:
        print("No cardio activity selected.")
        return
    row_values = cardio_tree.item(selected_item, "values")
    rows = []
    with open("cardio.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)
    with open("cardio.csv", "w", newline="") as file:
        writer = csv.writer(file)
        for row in rows:
            if row != [str(v) for v in row_values]:
                writer.writerow(row)
    load_cardio()

def show_cardio_progress():
    activity = activity_dropdown.get()
    dates, calories = [], []
    try:
        with open("cardio.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == activity and row[3] != '':
                    calories.append(float(row[3]))
                    dates.append(row[4])
    except FileNotFoundError:
        pass

    dates_formatted = [datetime.datetime.strptime(d, "%Y-%m-%d %H:%M:%S") for d in dates]

    for widget in cardio_chart_frame.winfo_children():
        widget.destroy()

    fig, ax = plt.subplots(figsize=(6, 3.5))
    fig.patch.set_facecolor("#2a2a3e")
    ax.set_facecolor("#1e1e2e")
    ax.plot(dates_formatted, calories, marker="o", color="#00ff88", linewidth=2)
    ax.set_title(f"{activity} Progress", fontsize=12, fontweight="bold",
                 color=TEXT)
    ax.set_xlabel("Date", fontsize=10, color=SUBTEXT)
    ax.set_ylabel("Calories Burned", fontsize=10, color=SUBTEXT)
    ax.tick_params(colors=SUBTEXT)
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%m/%d"))
    fig.autofmt_xdate()
    plt.tight_layout()

    canvas = FigureCanvasTkAgg(fig, master=cardio_chart_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

# Metrics Functions -----------------------------------

def load_metrics():
    for row in metrics_tree.get_children():
        metrics_tree.delete(row)
    try:
        with open("metrics.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] != '':
                    metrics_tree.insert("", "end", values=row)
    except FileNotFoundError:
        pass
    
def save_metrics():
    body_weight = body_weight_entry.get()
    body_fat = body_fat_entry.get()
    muscle_mass = muscle_mass_entry.get()
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("metrics.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([body_weight, body_fat, muscle_mass, date])

    body_weight_entry.delete(0, tk.END)
    body_fat_entry.delete(0, tk.END)
    muscle_mass_entry.delete(0, tk.END)

    load_metrics()
    print("Metrics saved!")

def show_metrics_progress():
    dates, weights, body_fats, muscle_masses = [], [], [], []
    try:
        with open("metrics.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] != '':
                    weights.append(float(row[0]))
                    body_fats.append(float(row[1]))
                    muscle_masses.append(float(row[2]))
                    dates.append(row[3])
    except FileNotFoundError:
        pass

    dates_formatted = [datetime.datetime.strptime(d, "%Y-%m-%d %H:%M:%S") for d in dates]

    for widget in metrics_chart_frame.winfo_children():
        widget.destroy()

    fig, ax = plt.subplots(figsize=(6, 3.5))
    fig.patch.set_facecolor("#2a2a3e")
    ax.set_facecolor("#1e1e2e")
    ax.plot(dates_formatted, weights, marker="o", color="#00ff88", linewidth=2, label="Weight")
    ax.plot(dates_formatted, body_fats, marker="o", color="#ff4444", linewidth=2, label="Body Fat")
    ax.plot(dates_formatted, muscle_masses, marker="o", color="#4444ff", linewidth=2, label="Muscle Mass")
    ax.set_title("Body Metrics Progress", fontsize=12, fontweight="bold",
                 color=TEXT)
    ax.set_xlabel("Date", fontsize=10, color=SUBTEXT)
    ax.set_ylabel("Metrics", fontsize=10, color=SUBTEXT)
    ax.tick_params(colors=SUBTEXT)
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%m/%d"))
    ax.legend()
    fig.autofmt_xdate()
    plt.tight_layout()

    canvas = FigureCanvasTkAgg(fig, master=metrics_chart_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

def delete_metrics():
    selected_item = metrics_tree.selection()
    if not selected_item:
        print("No metrics entry selected.")
        return
    row_values = metrics_tree.item(selected_item, "values")
    rows = []
    with open("metrics.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)
    with open("metrics.csv", "w", newline="") as file:
        writer = csv.writer(file)
        for row in rows:
            if row != [str(v) for v in row_values]:
                writer.writerow(row)
    load_metrics()

# ── Buttons ──────────────────────────────────────────
# Lifting Tab Buttons
tk.Button(left, text="Save Workout", command=save_workout,
          font=("Arial", 12, "bold"), bg=TEXT, fg="#000000",
          relief="flat", cursor="hand2").pack(pady=(20,5), ipadx=10, ipady=6)

tk.Button(left, text="Show Progress", command=show_progress,
          font=("Arial", 12, "bold"), bg="#4444ff", fg="#000000",
          relief="flat", cursor="hand2").pack(pady=5, ipadx=10, ipady=6)

tk.Button(left, text="Delete Workout", command=delete_workout,
          font=("Arial", 12, "bold"), bg=RED, fg="#000000",
          relief="flat", cursor="hand2").pack(pady=5, ipadx=10, ipady=6)

# Cardio Tab Buttons
tk.Button(left_cardio_panel, text="Save Cardio", command=save_cardio,
          font=("Arial", 12, "bold"), bg=TEXT, fg="#000000",
          relief="flat", cursor="hand2").pack(pady=(20,5), ipadx=10, ipady=6)

tk.Button(left_cardio_panel, text="Show Cardio Progress", command=show_cardio_progress,
          font=("Arial", 12, "bold"), bg="#4444ff", fg="#000000",
          relief="flat", cursor="hand2").pack(pady=5, ipadx=10, ipady=6)

tk.Button(left_cardio_panel, text="Delete Cardio", command=delete_cardio,
          font=("Arial", 12, "bold"), bg=RED, fg="#000000",
          relief="flat", cursor="hand2").pack(pady=5, ipadx=10, ipady=6)

# Metrics Tab Buttons
tk.Button(left_metrics_panel, text="Save Metrics", command=save_metrics,
          font=("Arial", 12, "bold"), bg=TEXT, fg="#000000",
          relief="flat", cursor="hand2").pack(pady=(20,5), ipadx=10, ipady=6)

tk.Button(left_metrics_panel, text="Show Metrics Progress", command=show_metrics_progress,
          font=("Arial", 12, "bold"), bg="#4444ff", fg="#000000",
          relief="flat", cursor="hand2").pack(pady=5, ipadx=10, ipady=6)

tk.Button(left_metrics_panel, text="Delete Metrics", command=delete_metrics,
          font=("Arial", 12, "bold"), bg=RED, fg="#000000",
          relief="flat", cursor="hand2").pack(pady=5, ipadx=10, ipady=6)

load_workouts()
load_cardio()
load_metrics()
load_home()
root.mainloop()
