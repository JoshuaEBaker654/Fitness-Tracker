# Fitness Tracker

(https://github.com/JoshuaEBaker654/Fitness-Tracker/issues)

A desktop fitness tracking application built with Python, Tkinter, and Matplotlib. The app helps you log strength workouts, visualize progress over time, and provides a foundation for cardio and body-metrics tracking.

---

## Table of contents
- [Features](#features)
- [Installation](#installation)
- [Data storage / CSV format](#data-storage--csv-format)
- [How progress is calculated](#how-progress-is-calculated)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

## Features
### 🏋️ Lifting Tracker
- Record workouts including exercise name, weight, and repetitions.
- Automatically stores workouts in `workouts.csv`.
- Displays workout history in a table.
- Highlights personal records (highest weight per exercise).
- Delete previously logged workouts.

### 📈 Progress Visualization
- Generates progress graphs per exercise (embedded Matplotlib figures).
- Visualizes workout volume over time (see formula below).

### ❤️ Cardio Tracker (in progress)
- UI fields for cardio activity, distance, duration, calories.
- Backend partly implemented — more features planned.

### 📊 Body Metrics (planned)
- Dedicated tab for weight, body fat, and other health metrics.

## Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/JoshuaEBaker654/Fitness-Tracker.git
   cd Fitness-Tracker
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   python main.py
   ```

If you don't have a `requirements.txt` yet, a minimal one might include:
```
tk
matplotlib
pandas
```
(Use `pip freeze > requirements.txt` after confirming working dependencies.)

## Data storage / CSV format
Workouts are stored in `workouts.csv` in the repository root (or in a configurable data dir). Example header and sample row:

```csv
date,exercise,weight,reps,notes
2026-07-30,Bench Press,100,5,Warmup+workset
```

If you plan to support timezones, durations, or more cardio fields, include columns like `duration_minutes`, `distance_km`, and `calories`.

## How progress is calculated
Progress graphs currently plot "volume" per session:
Volume = Weight × Reps

Consider adding:
- One-rep max estimates (e.g., Epley formula)
- Moving averages (7/28 day) to smooth noise

## Roadmap
- [x] Lifting tracker: log workouts, CSV persistence, table view
- [x] Matplotlib visualization for lifting volume
- [x] Complete cardio backend and persistence
- [x] Implement body-metrics tracking (weight/history)
- [ ] Add import/export (CSV) and backup features
- [ ] Add unit tests and CI

## Contributing
Contributions welcome — please:
1. Open an issue to discuss new features or bugs.
2. Fork the repo and create a branch per feature: `feature/<name>`.
3. Open a pull request with a clear description.

Add a `CONTRIBUTING.md` file to standardize guidelines.

## Troubleshooting
- If the app fails to start with a Tkinter error, ensure Python was installed with Tk support, or try installing your platform's tk/tcl packages.
- If graphs do not render, check Matplotlib backend settings or run `python -m pip install matplotlib`.

## License
This project is available under the MIT License. See `LICENSE` for details.

## Contact
Created by Joshua E. Baker — open issues or contact via GitHub profile.
