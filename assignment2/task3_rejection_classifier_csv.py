import pandas as pd

# Define the rejection reasons
REJECTION_REASONS_MAP = {
    "fake_document": "Fake_document",
    "not_covered": "Not_Covered",
    "policy_expired": "Policy_expired"
}

# Error handler
def handle_error(error_message):
    print(f"Error: {error_message}")
    return "Error"

# Keyword matcher
def contains_rejection_reason(rejection_text, reason):
    try:
        if rejection_text and isinstance(rejection_text, str):
            return reason.lower() in rejection_text.lower()
    except Exception as e:
        handle_error(f"Error in contains_rejection_reason: {str(e)}")
        return False
    return False

# Mapper
def map_rejection_reason(rejection_text):
    try:
        if rejection_text and isinstance(rejection_text, str):
            for reason, rejection_class in REJECTION_REASONS_MAP.items():
                if contains_rejection_reason(rejection_text, reason):
                    return rejection_class
            return "Unknown"
        else:
            return "No Remark"
    except Exception as e:
        handle_error(f"Error in map_rejection_reason: {str(e)}")
        return "Error"

# Main classifier function
def complex_rejection_classifier(remark_text):
    try:
        if not remark_text or not isinstance(remark_text, str) or len(remark_text.strip()) == 0:
            return "Invalid Remark"

        if contains_rejection_reason(remark_text, "fake_document"):
            return "Fake_document"
        elif contains_rejection_reason(remark_text, "not_covered"):
            return "Not_Covered"
        elif contains_rejection_reason(remark_text, "policy_expired"):
            return "Policy_expired"
        else:
            return map_rejection_reason(remark_text)
    except Exception as e:
        handle_error(f"Error in complex_rejection_classifier: {str(e)}")
        return "Error"

# Load CSV, classify, and save
def process_csv(input_path, output_path):
    try:
        df = pd.read_csv(input_path)
        if 'REJECTION_REMARKS' not in df.columns:
            print("Column 'REJECTION_REMARKS' not found in the CSV.")
            return

        df['REJECTION_CLASS'] = df['REJECTION_REMARKS'].apply(
            lambda r: complex_rejection_classifier(r) if pd.notna(r) else "No Remark"
        )

        df.to_csv(output_path, index=False)
        print(f"Processed file saved to: {output_path}")
    except Exception as e:
        print(f"Failed to process CSV: {str(e)}")

# Example usage
if __name__ == "__main__":
    input_csv = 'C:\ project\Cleaned_Insurance_auto_data.csv'     
    output_csv = "rejection_output.csv"
    process_csv(input_csv, output_csv)
