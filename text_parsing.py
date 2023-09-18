import re

def parse_aadhaar_info(extracted_text):
    aadhaar_number_match = re.search(r'\d{4} \d{4} \d{4}', extracted_text)
    birthdate_match = re.search(r'\d{2}/\d{2}/\d{4}', extracted_text)
    enrolment_match = re.search(r'Enrolment No.:\s*(.*)', extracted_text)
    
    if aadhaar_number_match and birthdate_match and enrolment_match:
        aadhaar_number = aadhaar_number_match.group()
        birthdate = birthdate_match.group()
        enrolment_number = enrolment_match.group(1)
        
        aadhaar_info = {
            'aadhaar_number': aadhaar_number,
            'birthdate': birthdate,
            'enrolment_number': enrolment_number,
        }
        
        return aadhaar_info
    else:
        return None
