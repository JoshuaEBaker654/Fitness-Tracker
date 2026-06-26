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
         bg=PANEL, fg=ACCENT).pack(pady=20)

# Dropdown
tk.Label(left, text="Exercise", font=("Arial", 11),
         bg=PANEL, fg=SUBTEXT).pack(pady=(10,2))
exercise_var = tk.StringVar()
exercise_dropdown = ttk.Combobox(left, textvariable=exercise_var, width=26)
exercise_dropdown.pack(pady=2)

# Weight
tk.Label(left, text="Weight (lbs)", font=("Arial", 11),
         bg=PANEL, fg=SUBTEXT).pack(pady=(10,2))
weight_entry = tk.Entry(left, width=28, bg=ENTRY_BG, fg=TEXT,
                        insertbackground=TEXT, relief="flat")
weight_entry.pack(pady=2, ipady=4)

# Reps
tk.Label(left, text="Reps", font=("Arial", 11),
         bg=PANEL, fg=SUBTEXT).pack(pady=(10,2))
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

# ── Home tab placeholder ─────────────────────────────
tk.Label(home_tab, text="🏠 Home", font=("Arial", 24, "bold"),
         bg=BG, fg=ACCENT).pack(pady=20)
tk.Label(home_tab, text="Your highlights will appear here",
         font=("Arial", 12), bg=BG, fg=SUBTEXT).pack(pady=10)

# ── Cardio tab ───────────────────────────
left_cardio_panel = tk.Frame(cardio_tab, bg=PANEL, width=320)
left_cardio_panel.pack(side="left", fill="y", padx=10, pady=10)
left_cardio_panel.pack_propagate(False)

tk.Label(left_cardio_panel, text="Cardio Tracker", font=("Arial", 20, "bold"),
         bg=PANEL, fg=ACCENT).pack(pady=20)

tk.Label(left_cardio_panel, text="Cardio Type", font=("Arial", 11),
         bg=PANEL, fg=SUBTEXT).pack(pady=(10,2))
activity_var = tk.StringVar()
activity_dropdown = ttk.Combobox(left_cardio_panel, textvariable=activity_var, width=26)
activity_dropdown.pack(pady=2)

tk.Label(left_cardio_panel, text="Distance (miles)", font=("Arial", 11),
         bg=PANEL, fg=SUBTEXT).pack(pady=(10,2))
distance_entry = tk.Entry(left_cardio_panel, width=28, bg=ENTRY_BG, fg=TEXT,
                          insertbackground=TEXT, relief="flat")
distance_entry.pack(pady=2, ipady=4)

tk.Label(left_cardio_panel, text="Duration (minutes)", font=("Arial", 11),
         bg=PANEL, fg=SUBTEXT).pack(pady=(10,2))
duration_entry = tk.Entry(left_cardio_panel, width=28, bg=ENTRY_BG, fg=TEXT,
                          insertbackground=TEXT, relief="flat")
duration_entry.pack(pady=2, ipady=4)

tk.Label(left_cardio_panel, text="Calories Burned", font=("Arial", 11),
         bg=PANEL, fg=SUBTEXT).pack(pady=(10,2))
calories_entry = tk.Entry(left_cardio_panel, width=28, bg=ENTRY_BG, fg=TEXT,
                          insertbackground=TEXT, relief="flat")
calories_entry.pack(pady=2, ipady=4)

# Cardio Tab Right Panel
right_panel_cardio = tk.Frame(cardio_tab, bg=BG)
right_panel_cardio.pack(side="right", fill="y", padx=10, pady=10)

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

cardio_columns = ["Type", "Distance", "Duration", "Calories"]
cardio_tree = ttk.Treeview(cardio_chart, columns=cardio_columns, show="headings", height=8)
for col in cardio_columns:
    cardio_tree.heading(col, text=col)
    cardio_tree.column(col, width=150)
cardio_tree.pack(fill="x", padx=5, pady=5)

# cardio chart frame
cardio_chart_frame = tk.Frame(right_panel_cardio, bg=PANEL)
cardio_chart_frame.pack(fill="both", expand=True)

cardio_chart_label = tk.Label(cardio_chart_frame, text="Cardio Activities", 
                              bg=PANEL, fg=SUBTEXT, font=("Arial", 12))
cardio_chart_label.pack(expand=True)

# ── Body Metrics tab placeholder ─────────────────────
tk.Label(metrics_tab, text="📊 Body Metrics", font=("Arial", 24, "bold"),
         bg=BG, fg=ACCENT).pack(pady=20)
tk.Label(metrics_tab, text="Body metrics tracking coming soon",
         font=("Arial", 12), bg=BG, fg=SUBTEXT).pack(pady=10)

# ── Functions ────────────────────────────────────────
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

def get_cardio():
    cardio=[]
    try:
        with open("cardio.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                cardio.append(row)
    except FileNotFoundError:
        pass
    return cardio

# def get_personal_records(cardio):
#     pr = 0
#     try:
#         with open("cardio.csv", "r") as file:
#             reader = csv.reader(file)
#             for row in reader:
#                 if row[2] != '' and float(row[2]) > pr:
#                     pr = float(row[2])
#     except FileNotFoundError:
#         pass
#     return pr

# def load_cardio():
#     for row in cardio_tree.get_children():
#         cardio_tree.delete(row)
#     try:
#         with open("cardio.csv", "r") as file:
#             reader = csv.reader(file)
#             for row in reader:
#                 if row[1] != '':
#                     if float(row[1]) > 0:
#                         cardio_tree.insert("", "end", values=row, tags=

# ── Buttons ──────────────────────────────────────────
tk.Button(left, text="Save Workout", command=save_workout,
          font=("Arial", 12, "bold"), bg=ACCENT, fg="#000000",
          relief="flat", cursor="hand2").pack(pady=(20,5), ipadx=10, ipady=6)

tk.Button(left, text="Show Progress", command=show_progress,
          font=("Arial", 12, "bold"), bg="#4444ff", fg="#000000",
          relief="flat", cursor="hand2").pack(pady=5, ipadx=10, ipady=6)

tk.Button(left, text="Delete Workout", command=delete_workout,
          font=("Arial", 12, "bold"), bg=RED, fg="#000000",
          relief="flat", cursor="hand2").pack(pady=5, ipadx=10, ipady=6)

load_workouts()
root.mainloop()