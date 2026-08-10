# Fitness Tracker

A desktop fitness tracking application built with Python, Tkinter, and Matplotlib. Log strength workouts, cardio sessions, and body metrics; see personal records and progress charts; and get an at-a-glance dashboard of where you stand.

Everything runs locally — your data lives in plain CSV files next to the app, with no accounts, no server, and no network access.

[Report a bug or request a feature](https://github.com/JoshuaEBaker654/Fitness-Tracker/issues)

---

## Table of contents
- [Features](#features)
- [Installation](#installation)
- [Data storage / CSV format](#data-storage--csv-format)
- [How the numbers are calculated](#how-the-numbers-are-calculated)
- [Known limitations](#known-limitations)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [Troubleshooting](#troubleshooting)

## Features

The app opens as a single window with four tabs: **Home**, **Lifting**, **Cardio**, and **Metrics**.

### 🏠 Home Dashboard
A read-only snapshot built from all three data files, shown in six cards:
- **Top Lifting PR** — the heaviest single weight ever logged, and which exercise it was.
- **Top Cardio PR** — the activity with your highest calorie burn.
- **Current Streak** — consecutive days with a logged cardio session, ending today.
- **Current Body Metrics** — your most recent weight, body fat %, and muscle mass.
- **Last Workout** — the most recently logged set.
- **Month to Month** — percent change in average training volume vs. last month.

### 🏋️ Lifting Tracker
- Log exercise, weight (lbs), and reps; the date and time are stamped automatically.
- The exercise dropdown is populated from your history, and you can type a new exercise name directly into it.
- Full workout history in a sortable-width table.
- Rows matching that exercise's personal record are highlighted green.
- Delete the selected workout.
- **Show Progress** plots training volume over time for the selected exercise.

### 🏃 Cardio Tracker
- Log activity type, distance (miles), duration (minutes), and calories burned, with an automatic timestamp.
- Activity dropdown is populated from your history and accepts new names.
- Full cardio history in a table, with each activity's PR row highlighted green.
- Delete the selected entry.
- **Show Cardio Progress** plots calories burned over time for the selected activity.

### 📊 Body Metrics
- Log body weight (lbs), body fat (%), and muscle mass (lbs), with an automatic timestamp.
- Full metrics history in a table.
- Delete the selected entry.
- **Show Metrics Progress** plots all three measurements over time on one chart.

## Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/JoshuaEBaker654/Fitness-Tracker.git
   ```

2. Create a virtual environment and install the one third-party dependency:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   pip install matplotlib
   ```
   On macOS/Linux use `source venv/bin/activate` instead. Everything else the app uses — `tkinter`, `csv`, `datetime` — ships with Python.

3. Run the app:
   ```bash
   python app.py
   ```

There is no build step and no configuration file. The app is a single script.

## Data storage / CSV format

Three CSV files are created in the working directory the first time you save each kind of entry. They are **headerless** — every line is a data row — and new entries are appended to the end. Dates are written as `YYYY-MM-DD HH:MM:SS`.

**`workouts.csv`** — `exercise, weight (lbs), reps, date`
```csv
Bench Press,185,5,2026-07-30 18:42:11
Squat,275,3,2026-07-31 17:05:48
```

**`cardio.csv`** — `activity, distance (miles), duration (minutes), calories, date`
```csv
Run,3.1,26,310,2026-07-30 07:15:02
Cycling,12.4,45,480,2026-08-01 06:58:33
```

**`metrics.csv`** — `body weight (lbs), body fat (%), muscle mass (lbs), date`
```csv
182.4,14.8,151.2,2026-07-30 06:30:00
```

Because the format is plain CSV, you can edit or back up your history in any spreadsheet or text editor. Keep the column order and the date format intact — the app reads columns by position, not by name.

## How the numbers are calculated

**Lifting volume** (the Lifting progress chart, and the Month to Month card):
```
Volume = Weight × Reps
```
Each logged set is one point on the chart.

**Month to Month** compares the *average* volume per logged set this calendar month against last calendar month, and reports the percent change. It needs data in both months; otherwise the card says so instead of showing a number.

**Lifting PR** is the single heaviest weight logged for an exercise, regardless of reps.

**Cardio PR** is the entry with the most calories burned for that activity, using distance and then duration as tie-breakers. The Home tab's Top Cardio PR is whichever activity's PR has the highest calorie count.

**Current Streak** counts back from today, adding a day for each consecutive calendar day that has at least one entry in `cardio.csv`. It stops at the first gap. Note that this is **cardio only** — lifting and metrics entries don't count toward the streak, and the streak reads 0 if you haven't logged cardio today.

## Known limitations

Honest notes on current behavior, so nothing surprises you:

- **No input validation.** Saving with an empty or non-numeric weight/reps writes that row to the CSV, which will then raise a `ValueError` when the table reloads. If the app stops opening, check the last line of your CSV files.
- **The Home tab only refreshes on startup.** Stats there won't update after you save a new entry until you restart the app.
- **Delete matches on values, not row identity.** Deleting an entry removes every row whose values are identical to the selected one, so true duplicates are removed together.
- **Metrics rows aren't PR-highlighted** the way lifting and cardio rows are.
- **Charts need a selection.** Clicking Show Progress with nothing chosen in the dropdown draws an empty chart rather than an error.
- **Distance and duration aren't charted.** Cardio progress plots calories only, even though all four fields are stored.

## Roadmap
- [x] Lifting tracker: log workouts, CSV persistence, table view, PR highlighting
- [x] Cardio tracker: full logging, persistence, PR highlighting, and charting
- [x] Body metrics tracking with multi-series chart
- [x] Home dashboard with PRs, streak, and month-over-month comparison
- [ ] Validate numeric input before saving, with inline error messages
- [ ] Refresh the Home dashboard after every save
- [ ] Chart cardio distance and pace, not just calories
- [ ] One-rep max estimates (Epley) and 7/28-day moving averages
- [ ] Import/export and backup features
- [ ] Unit tests and CI

## Contributing
Contributions welcome — please:
1. Open an issue to discuss new features or bugs.
2. Fork the repo and create a branch per feature: `feature/<name>`.
3. Open a pull request with a clear description.

## Troubleshooting

**The app won't start, or crashes on launch.** The most likely cause is a malformed row in one of the CSV files (see [Known limitations](#known-limitations)). Open `workouts.csv`, `cardio.csv`, and `metrics.csv` and remove any row with a blank or non-numeric value in a number column.

**`ModuleNotFoundError: No module named 'tkinter'`.** Your Python was built without Tk support. On Windows, re-run the installer and enable "tcl/tk and IDLE". On Debian/Ubuntu, `sudo apt install python3-tk`. On macOS, install Python from python.org or `brew install python-tk`.

**Charts are blank.** Make sure an exercise or activity is selected in the dropdown and that you have at least one saved entry for it.

## Contact
Created by Joshua E. Baker — open an issue or reach out via GitHub.
