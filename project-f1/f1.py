import sys

# Function to load driver metadata from f1_drivers.txt
def load_driver_metadata(metadata_file):
    driver_info = {}
    try:
        with open(metadata_file, 'r') as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) < 4:
                    print(f"Skipping malformed line in metadata: {line.strip()}")
                    continue  # Skip malformed lines
                driver_code = parts[1].strip().upper()  # Normalize to uppercase
                real_name = parts[2].strip()
                team_name = parts[3].strip()
                driver_info[driver_code] = {
                    "name": real_name,
                    "team": team_name,
                }
    except FileNotFoundError:
        print(f"Error: Metadata file '{metadata_file}' not found.")
        sys.exit(1)
    return driver_info

# Function to process lap time files
def process_lap_times(file_name, driver_metadata):
    try:
        with open(file_name, 'r') as file:
            race_location = file.readline().strip()
            driver_lap_times = {}

            for line in file:
                line = line.strip()
                if not line:
                    continue
                driver_code = line[:3].strip().upper()  # Normalize to uppercase
                lap_time = float(line[4:])
                if driver_code not in driver_lap_times:
                    driver_lap_times[driver_code] = []
                driver_lap_times[driver_code].append(lap_time)

            fastest_driver = None
            fastest_time = float('inf')
            total_lap_time = 0
            total_laps = 0

            driver_fastest_times = {}
            driver_avg_times = {}

            for driver, laps in driver_lap_times.items():
                fastest_lap = min(laps)
                avg_lap = sum(laps) / len(laps)

                driver_fastest_times[driver] = fastest_lap
                driver_avg_times[driver] = avg_lap

                total_lap_time += sum(laps)
                total_laps += len(laps)

                if fastest_lap < fastest_time:
                    fastest_driver = driver
                    fastest_time = fastest_lap

            overall_avg_time = total_lap_time / total_laps if total_laps else 0

            print(f"\nRace Location: {race_location}")
            print(f"Fastest Lap: {fastest_driver} with {fastest_time:.3f} seconds\n")

            print("Driver Statistics (Fastest Times in Descending Order):")
            for driver in sorted(driver_fastest_times, key=lambda x: driver_fastest_times[x], reverse=True):
                metadata = driver_metadata.get(driver, None)
                if metadata:
                    team = metadata["team"]
                    name = metadata["name"]
                else:
                    team = "Unknown Team"
                    name = "Unknown Name"
                print(
                    f"{driver} ({name}, {team}): Fastest Lap = {driver_fastest_times[driver]:.3f}, "
                    f"Average Time = {driver_avg_times[driver]:.3f}, Total Laps = {len(driver_lap_times[driver])}"
                )

            print(f"\nOverall Average Time: {overall_avg_time:.3f} seconds")
    except FileNotFoundError:
        print(f"Error: Lap time file '{file_name}' does not exist.")
    except Exception as e:
        print(f"An error occurred while processing '{file_name}': {e}")

# Main function
def main():
    if len(sys.argv) < 3:
        print("Usage: python f1_timing_board.py <metadata_file> <lap_time_file1> [<lap_time_file2> ...]")
        sys.exit(1)

    metadata_file = sys.argv[1]
    lap_time_files = sys.argv[2:]

    # Load the driver metadata
    driver_metadata = load_driver_metadata(metadata_file)

    # Debugging: Print loaded metadata
    print("\nLoaded Driver Metadata:")
    for code, info in driver_metadata.items():
        print(f"{code}: {info}")

    # Process each lap time file
    for lap_time_file in lap_time_files:
        if lap_time_file == metadata_file:
            print(f"\nSkipping metadata file: {metadata_file}")
            continue
        print(f"\nProcessing file: {lap_time_file}")
        process_lap_times(lap_time_file, driver_metadata)

if __name__ == "__main__":
    main()
