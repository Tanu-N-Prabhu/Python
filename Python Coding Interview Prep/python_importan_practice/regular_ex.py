# Exercise: make a regular expression that will match an email
import re


def test_email(your_pattern):
    repattern = re.compile(your_pattern)
    emails = ["john@example.com", "python-list@python.org",
              "wha.t.`1an?ug{}ly@email.com", "dhiraj@gcol.co.in"]
    for email in emails:
        if not re.fullmatch(repattern, email):
            print("You failed to match %s" % email)
        elif not your_pattern:
            print("Forgot to enter a pattern!")
        else:
            print("Pass")


# Your pattern here!
# pattern = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?"
pattern = r'\b[^0-9_][\w._-]+@[a-zA-Z]+\.[a-zA-Z]{1,3}\b'
test_email(pattern)

def transform_date_format(date):
   return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', date)
date_input = "2021-08-01"
print(transform_date_format(date_input))


  str = 'purple alice-b@google.com monkey dishwasher'
  match = re.search(r'([\w.-]+)@([\w.-]+)', str)
  if match:
    print match.group()   ## 'alice-b@google.com' (the whole match)
    print match.group(1)  ## 'alice-b' (the username, group 1)
    print match.group(2)  ## 'google.com' (the host, group 2)


  ## Suppose we have a text with many email addresses
  str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'

  ## Here re.findall() returns a list of all the found email strings
  emails = re.findall(r'[\w\.-]+@[\w\.-]+', str) ## ['alice@google.com', 'bob@abc.com']
  for email in emails:
    # do something with each found email string
    print email
    