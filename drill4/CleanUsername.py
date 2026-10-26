def clean_username(value):
    return value.strip().lower().replace(" ", "_")