import re
import pandas as pd

def strip_space_and_periods(df_column):
  df_column_spaceless = df_column.strip()
  df_column_array = df_column_spaceless.split()
  df_column_no_period = map(lambda x: x.replace('.',''), df_column_array)
  return df_column_no_period

def find_degrees(df):
  degrees = df[' degree']
  d = {}
  for degree_raw in degrees:
    degree_array = strip_space_and_periods(degree_raw)
    for degree in degree_array:
      if degree in d.keys():
        d[degree] += 1
      else:
        d[degree] = 1
  return d



def find_titles(df):
  titles = df[' title']
  d = {}
  for title_raw in titles:
    title = title_raw.strip()
    regex_match =re.match(r'[^.]*professor', title, re.IGNORECASE)
    if regex_match.group() in d.keys():
      d[regex_match.group()] += 1
    else:
      d[regex_match.group()] = 1
  return d

def email_address(df):
  emails = df[' email']
  return emails.tolist()

def email_domain(email_list):
  d = {}
  for email in email_list:
    regex_match = re.search(r'(?<=@)[^;]*edu', email)
    if regex_match.group() in d.keys():
      d[regex_match.group()] += 1
    else:
      d[regex_match.group()] = 1

  return d.keys()

filepath = '/Users/lilliantong/ds/metis/metisgh/prework/dsp/python/faculty.csv'
df = pd.read_csv(filepath)

degree_dict = find_degrees(df)

title_dict = find_titles(df)

email_list = email_address(df)
print email_list

email_domains = email_domain(email_list)
print email_domains
