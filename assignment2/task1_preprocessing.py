import datetime

def preprocess_claims_csv(file_path):
    """
    Reads and cleans the insurance claims CSV file.
    Returns a list of cleaned dictionaries (one per row).
    """
    cleaned_data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    # Remove BOM if present
    if lines[0].startswith('\ufeff'):
        lines[0] = lines[0][1:]
    # Parse header
    header = [h.strip() for h in lines[0].strip().split(',')]
    for line in lines[1:]:
        if not line.strip():
            continue  # skip empty lines
        row = [col.strip() for col in line.strip().split(',')]
        if len(row) != len(header):
            continue  # skip malformed rows
        record = dict(zip(header, row))
        # Clean and convert data types
        # CLAIM_ID: string, required
        record['CLAIM_ID'] = record['CLAIM_ID'] if record['CLAIM_ID'] else None
        # CLAIM_DATE: date, required (format: YYYY-MM-DD)
        try:
            record['CLAIM_DATE'] = datetime.datetime.strptime(record['CLAIM_DATE'], '%Y-%m-%d').date()
        except Exception:
            record['CLAIM_DATE'] = None
        # CUSTOMER_ID: string, required
        record['CUSTOMER_ID'] = record['CUSTOMER_ID'] if record['CUSTOMER_ID'] else None
        # CLAIM_AMOUNT: float, required, >=0
        try:
            amt = float(record['CLAIM_AMOUNT'])
            record['CLAIM_AMOUNT'] = amt if amt >= 0 else 0.0
        except Exception:
            record['CLAIM_AMOUNT'] = 0.0
        # PREMIUM_COLLECTED: float, required, >=0
        try:
            prem = float(record['PREMIUM_COLLECTED'])
            record['PREMIUM_COLLECTED'] = prem if prem >= 0 else 0.0
        except Exception:
            record['PREMIUM_COLLECTED'] = 0.0
        # PAID_AMOUNT: float, required, >=0
        try:
            paid = float(record['PAID_AMOUNT'])
            record['PAID_AMOUNT'] = paid if paid >= 0 else 0.0
        except Exception:
            record['PAID_AMOUNT'] = 0.0
        # CITY: string, required, fallback to 'UNKNOWN'
        record['CITY'] = record['CITY'] if record['CITY'] else 'UNKNOWN'
        # REJECTION_REMARKS: string, optional, blank if not rejected
        if record['PAID_AMOUNT'] == 0.0:
            record['REJECTION_REMARKS'] = record['REJECTION_REMARKS'] if record['REJECTION_REMARKS'] else 'REJECTED'
        else:
            record['REJECTION_REMARKS'] = ''
        cleaned_data.append(record)
    return cleaned_data




def save_cleaned_data_to_csv(cleaned_data, output_file):
    if not cleaned_data:
        print("No data to save.")
        return
    # Get the header from the first record
    header = list(cleaned_data[0].keys())
    with open(output_file, 'w', encoding='utf-8') as f:
        # Write header
        f.write(','.join(header) + '\n')
        # Write each row
        for record in cleaned_data:
            row = []
            for key in header:
                value = record[key]
                # Convert date objects to string
                if isinstance(value, (datetime.date, datetime.datetime)):
                    value = value.strftime('%Y-%m-%d')
                elif value is None:
                    value = ''
                else:
                    value = str(value)
                row.append(value.replace(',', ' '))  # Remove commas from values to avoid CSV issues
            f.write(','.join(row) + '\n')

cleaned = preprocess_claims_csv(r'C:\a project\Insurance_auto_data.csv')
save_cleaned_data_to_csv(cleaned, r'C:\a project\Cleaned_Insurance_auto_data.csv')