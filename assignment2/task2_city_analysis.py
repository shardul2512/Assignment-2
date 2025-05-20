def list_unique_cities(csv_file):
    """
    Helper function to list unique CITY values in the file.
    Helps debug mismatched formatting or unexpected city names.
    """
    city_set = set()
    with open(csv_file, 'r', encoding='utf-8') as f:
        header = f.readline().strip().split(',')
        try:
            city_idx = header.index('CITY')
        except ValueError:
            print("CITY column not found.")
            return

        for line in f:
            if not line.strip():
                continue
            cols = line.strip().split(',')
            if len(cols) <= city_idx:
                continue
            city_set.add(cols[city_idx].strip())

    print("Unique cities found in the data:")
    for city in sorted(city_set):
        print(f"- {city}")


def analyze_city_for_closure(csv_file):
    """
    Analyzes claim data and recommends which city to consider for closure
    among Pune, Kolkata, Ranchi, and Guwahati, based on lowest total paid amount.
    """
    target_cities = {'Pune', 'Kolkata', 'Ranchi', 'Guwahati'}
    city_stats = {}

    with open(csv_file, 'r', encoding='utf-8') as f:
        header = f.readline().strip().split(',')
        try:
            city_idx = header.index('CITY')
            paid_idx = header.index('PAID_AMOUNT')
        except ValueError:
            print("Required columns CITY or PAID_AMOUNT not found.")
            return

        for line in f:
            if not line.strip():
                continue
            cols = line.strip().split(',')
            if len(cols) <= max(city_idx, paid_idx):
                continue

            city = cols[city_idx].strip().title()
            try:
                paid = float(cols[paid_idx])
            except Exception:
                paid = 0.0

            if city not in target_cities:
                continue

            if city not in city_stats:
                city_stats[city] = {'total_paid': 0.0, 'num_claims': 0}
            city_stats[city]['total_paid'] += paid
            city_stats[city]['num_claims'] += 1

    print("City-wise claim statistics for April 2025 (filtered to 4 target cities):")
    print("------------------------------------------------------------")

    if not city_stats:
        print("No data available for target cities.")
        return

    for city, stats in city_stats.items():
        print(f"{city}: Total Paid = {stats['total_paid']:.2f}, Number of Claims = {stats['num_claims']}")

    # Recommend city with lowest total paid amount
    candidate_city = min(city_stats, key=lambda c: city_stats[c]['total_paid'])
    print(f"\nRecommendation: Consider closing operations in '{candidate_city}' (lowest total paid amount).")


# Example usage:
csv_path = 'Cleaned_Insurance_auto_data.csv'

# (Optional) Step 1: Debug CITY values
list_unique_cities(csv_path)

# Step 2: Perform the city analysis
analyze_city_for_closure(csv_path)
