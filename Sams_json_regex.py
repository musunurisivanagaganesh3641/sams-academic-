import json
import re
from datetime import datetime, timezone


# Regular expression patterns
EMAIL_PATTERN = r'^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$'
PHONE_PATTERN = r'^[6-9]\d{9}$'
ROLL_PATTERN = r'^SAMS\d{2}[A-Z]{2}\d{3}$'


# Sample JSON data
sample_json = '''
[
    {
        "name": "Ananya Rao",
        "roll_no": "SAMS24CS014",
        "email": "ananya.rao@edutech.edu",
        "phone": "9876543210"
    },
    {
        "name": "Zoya Khan",
        "roll_no": "SAMS24CS099",
        "email": "bad-email",
        "phone": "1234567890"
    }
]
'''


def parse_admissions(json_text):
    """Convert JSON text into Python data."""
    return json.loads(json_text)


def validate_email(email):
    """Validate email address."""
    return bool(re.match(EMAIL_PATTERN, email))


def validate_phone(phone):
    """Validate phone number."""
    return bool(re.match(PHONE_PATTERN, phone))


def validate_roll_no(roll_no):
    """Validate roll number."""
    return bool(re.match(ROLL_PATTERN, roll_no))


def validate_student(student):
    """Validate all student details."""

    return {
        "name": student.get("name"),
        "roll_no_valid": validate_roll_no(student.get("roll_no", "")),
        "email_valid": validate_email(student.get("email", "")),
        "phone_valid": validate_phone(student.get("phone", "")),
        "imported_at": datetime.now(timezone.utc).isoformat(
            timespec="seconds"
        )
    }


def main():
    """Main program."""

    students = parse_admissions(sample_json)

    print("=== SAMS External Data Validation ===")

    for student in students:
        result = validate_student(student)
        print(result)


if __name__ == "__main__":
    main()