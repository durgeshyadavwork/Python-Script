# phone_formatter.py

import csv
from phonenumbers import parse, is_valid_number, format_number, PhoneNumberFormat, NumberParseException

enabled_countries = {
    'IN': '91',
    'US': '1',
    'GB': '44',
    'AU': '61',
    'CA': '1',
    'DE': '49',
    'FR': '33',
    'IT': '39',
    'ES': '34',
    'RU': '7',
    'CN': '86',
    'BR': '55',
    'ZA': '27',
    'NG': '234',
    'PK': '92',
    'BD': '880'
}

mobile_prefixes = {
    'IN': ['6', '7', '8', '9'],
    'US': [],
    'GB': ['7'],
    'AU': ['4'],
    'CA': [],
    'DE': ['15', '16', '17'],
    'FR': ['6', '7'],
    'IT': ['3'],
    'ES': ['6', '7'],
    'RU': ['9'],
    'CN': ['13', '14', '15', '16', '17', '18', '19'],
    'BR': ['9'],
    'ZA': ['6', '7', '8'],
    'NG': ['7', '8', '9'],
    'PK': ['3'],
    'BD': ['1']
}

def plausible_length(cc):
    return {
        'IN': 10, 'US': 10, 'GB': 10, 'AU': 9, 'CA': 10, 'DE': 10,
        'FR': 9, 'IT': 10, 'ES': 9, 'RU': 10, 'CN': 11, 'BR': 11,
        'ZA': 9, 'NG': 10, 'PK': 10, 'BD': 10
    }.get(cc, 10)

def smart_detect_format(raw):
    number = ''.join(filter(str.isdigit, str(raw)))
    
    if raw.startswith('+'):
        try:
            p = parse(raw, None)
            if is_valid_number(p):
                return format_number(p, PhoneNumberFormat.E164)
        except:
            return None

    for cc, code in enabled_countries.items():
        prefixes = mobile_prefixes.get(cc, [])
        expected_length = plausible_length(cc)

        if number.startswith(code):
            tail = number[len(code):]
            if any(tail.startswith(p) for p in prefixes) and len(tail) == expected_length:
                try:
                    p = parse(f"+{code}{tail}", None)
                    if is_valid_number(p):
                        return format_number(p, PhoneNumberFormat.E164)
                except: pass

        if any(number.startswith(p) for p in prefixes) and len(number) == expected_length:
            try:
                p = parse(number, cc)
                if is_valid_number(p):
                    return format_number(p, PhoneNumberFormat.E164)
            except: pass
    return None

def process_csv(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        writer.writerow(['Original Number', 'Formatted Number'])

        for row in reader:
            number = row[0].strip()
            formatted = smart_detect_format(number)
            writer.writerow([number, formatted or "INVALID"])

if __name__ == "__main__":
    process_csv('uploads/raw_numbers.csv', 'cleaned_numbers.csv')
    print("✅ Processing complete. Output saved to cleaned_numbers.csv")
