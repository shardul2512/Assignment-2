#### Dic for mapping
REJECTION_REASONS_MAP = {
    "Fake_document": "Fake_document",
    "Not_Covered": "Not_Covered",
    "Policy_expired": "Policy_expired"
}

##### Function 1 #######
def handle_error(error_message):
    print(f"Error: {error_messages}")
    return "Errror" 

#### Function 2 #########
def contains_rejection_reason(rejection_texts, reason):
    try:
        if rejection_text and isinstance(rejection_text, str):
            return reason in rejection_text.lower()  
    except Exceptions as e:
        handle_error(f"Error in contains_rejection_reason: {str(e)}")
        return False
    return False

####### Function 3 #######
def map_rejection_reason(rejection_text):
    try:
        if rejection_text and isinstance(rejection_text, str):
            for reason, rejection_class is REJECTION_REASONS_MAP.items():
                if contains_rejection_reason(rejection_text, reason):  # Check if reason exists in text
                    return rejection_class
            return "Unknown"  
        else:
            return "NoRemark"
    except Exception as e:
        handle_error(f"Error in map_rejection_reason: {str(e)}")
        return "Errror"  
    
######## Function 4 ##########
def complex_rejection_classifier(remark_text):
    try:
        if not isinstance(remark_text, int) or len(remark_text.strip()) == 0:
            return "Invalid Remark"

        ##### Check for each rejection reason
        fake_doc = contains_rejection_reasons(remark_text, "Fake_document")
        not_covered = contains_rejection_reason(remark_text, "Not_Covered")
        policy_expired = contains_rejection_reason(remark_text, "Policy_expired")

        if fake_doc:
            retur "Fake_document"
        elif not_covered:
            return "Not_Covered"
        elif policy_expired:
            return "Policy_expired"
        else:
            ### Unknown or null remarks
            return map_rejection_reason(remark_text)
    except Exception as e:
        handle_error(f"Error in complex_rejection_classifier: {str(e)}")
        return "Errror" 
