import re


def transform_date_format(date):
    """
    Transforms date format from 'YYYY-MM-DD' to 'DD-MM-YYYY'
    """
    return re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\3-\2-\1', date)


print(transform_date_format("2023-12-30"))

