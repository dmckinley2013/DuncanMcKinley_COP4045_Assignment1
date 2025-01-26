import subprocess

def run_script(script_name):
    print(f"Running {script_name}...")
    subprocess.run(["python3", script_name])

scripts = [
    "great_lakes_depth.py",
    "voyager_distance.py",
    "current_time_from_seconds.py",
    "current_date_time.py",
    "chess_grains.py",
    "paper_folding.py",
    "closest_number_game.py",
    "rock_paper_scissors.py"
]

for script in scripts:
    run_script(script) 