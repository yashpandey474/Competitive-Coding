def validate_email(email: str) -> bool:
    if '@' not in email or email[0] == ' ' or email[-1]== ' ':
        return False
    
    index = email.index('@')
    domain = email[index+1:]
    
    if '.'not in domain:
        return False
        
    return True
    
