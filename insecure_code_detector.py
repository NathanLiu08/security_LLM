import re

def detect_sql_injection(code):
    sql_injection_patterns = [
        r"'.*--", 
        r"'.*;",  
        r"\".*--", 
        r"\".*;"  
    ]
    for pattern in sql_injection_patterns:
        if re.search(pattern, code):
            return True
    return False

def detect_xss(code):
    xss_patterns = [
        r"<script>.*</script>",  
        r"javascript:",        
        r"on\w+=['\"]?.*['\"]?"  
    ]
    for pattern in xss_patterns:
        if re.search(pattern, code, re.IGNORECASE):
            return True
    return False

def detect_buffer_overflow(code):
    buffer_overflow_patterns = [
        r"strcpy\(",
        r"gets\(",    
        r"scanf\(", 
        r"memcpy\("
    ]
    for pattern in buffer_overflow_patterns:
        if re.search(pattern, code):
            return True
    return False

def insecure_code_detector(code):
    if detect_sql_injection(code):
        print("Potential SQL injection vulnerability detected.")
    if detect_xss(code):
        print("Potential XSS vulnerability detected.")
    if detect_buffer_overflow(code):
        print("Potential buffer overflow vulnerability detected.")
    if not (detect_sql_injection(code) or detect_xss(code) or detect_buffer_overflow(code)):
        print("No significant vulnerabilities detected.")