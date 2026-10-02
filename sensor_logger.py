import csv, random, statistics
from datetime import datetime

THRESHOLD = 30  # alert above this temp (°C)

def generate_readings(n=50):
    # simulate a sensor: values cluster around 25°C
    return [round(random.gauss(25, 3), 2) for _ in range(n)]

def save_csv(readings, path="data.csv"):
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["time", "temp_c"])
        for r in readings:
            now = datetime.now().isoformat(timespec="seconds")
            writer.writerow([now, r])

def analyze(path="data.csv"):
    with open(path) as f:
        temps = [float(row["temp_c"]) for row in csv.DictReader(f)]
    return temps, {
        "count": len(temps),
        "mean": statistics.mean(temps),
        "min": min(temps),
        "max": max(temps),
        "stdev": statistics.stdev(temps),
    }

def main():
    save_csv(generate_readings())
    temps, stats = analyze()
    for name, value in stats.items():
        print(f"{name}: {value:.2f}")
    alerts = [t for t in temps if t > THRESHOLD]
    print(f"{len(alerts)} readings above {THRESHOLD}°C")

if __name__ == "__main__":
    main()
