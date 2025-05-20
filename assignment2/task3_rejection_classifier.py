# task3_rejection_classifier.py

# Mapping of keywords to rejection classes
REJECTION_REASONS_MAP = {
    "fake_document": "Fake_document",
    "not_covered": "Not_Covered",
    "policy_expired": "Policy_expired"
}

def handle_error(error_message):
    print(f"Error: {error_message}")
    return "Error"

def contains_rejection_reason(rejection_text, reason):
    try:
        if rejection_text and isinstance(rejection_text, str):
            return reason.lower() in rejection_text.lower()
    except Exception as e:
        handle_error(f"Error in contains_rejection_reason: {str(e)}")
        return False
    return False

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

def complex_rejection_classifier(remark_text):
    try:
        if not remark_text or not isinstance(remark_text, str) or len(remark_text.strip()) == 0:
            return "Invalid Remark"

        fake_doc = contains_rejection_reason(remark_text, "fake_document")
        not_covered = contains_rejection_reason(remark_text, "not_covered")
        policy_expired = contains_rejection_reason(remark_text, "policy_expired")

        if fake_doc:
            return "Fake_document"
        elif not_covered:
            return "Not_Covered"
        elif policy_expired:
            return "Policy_expired"
        else:
            return map_rejection_reason(remark_text)
    except Exception as e:
        handle_error(f"Error in complex_rejection_classifier: {str(e)}")
        return "Error"

# Example usage with test data
if __name__ == "__main__":
    test_remarks = [
        "Policy rejected: policy_expired noted.",
        "Fake_document submitted.",
        "Not_covered under policy.",
        "This is a vague rejection reason.",
        "",
        None
    ]

    print("Rejection Classification Results:")
    for remark in test_remarks:
        result = complex_rejection_classifier(remark) if remark else "No Remark"
        print(f"Remark: {repr(remark)} -> Class: {result}")



# python task3_rejection_classifier.py
