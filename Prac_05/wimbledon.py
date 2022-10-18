FILENAME = "wimbledon.csv"


def main():
    records = get_records(FILENAME)
    countries, champion_to_times_won = process_data(records)


def get_records(filename):
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Remove header from columns
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


def process_data(records):
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


if __name__ == '__main__':
    main()
