from datetime import datetime

def get_date_string():
    """Get the current date in a human-readable format."""
    return datetime.now().strftime("%a %b %-d, %Y")