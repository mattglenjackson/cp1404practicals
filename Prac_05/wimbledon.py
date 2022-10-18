FILENAME = "wimbledon.csv"


def main():
    """Wimbledon.py main function"""
    records = get_records(FILENAME)
    countries, champion_to_times_won = process_data(records)
    print_results(countries, champion_to_times_won)


def get_records(filename):
    """Gets record from file."""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Remove header from columns
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


def process_data(records):
    """Processes data into dictionary and set"""
    countries = set()
    champion_to_times_won = {}
    count = 0
    for record in records:
        countries.add(record[1])
        champion = record[2]
        if champion in champion_to_times_won:
            count = 1
            champion_to_times_won[champion] = champion_to_times_won[champion] + count
        else:
            count = 1
            champion_to_times_won[champion] = count

    return countries, champion_to_times_won


def print_results(countries, champion_to_times_won):
    """Prints results of champions and winning countries of Wimbledon."""
    print("Wimbledon Champions:")
    for champion in champion_to_times_won:
        print(f"{champion} {champion_to_times_won[champion]}")
    print()
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(",".join(country for country in sorted(countries)))


if __name__ == '__main__':
    main()
