import pandas as pd


def strip_space_and_periods(df_column):
  df_column_spaceless = df_column.strip()
  df_column_array = df_column_spaceless.split()
  df_column_no_period = map(lambda x: x.replace('.',''), df_column_array)
  return df_column_no_period

def first_last_name_tuple_array(df):
  names = df['name']
  name_array = []
  for name in names:
    split_names = name.split()
    name_array.append((split_names[-1], split_names[0]))
  return name_array

def faculty_dictionary(df):
  faculty_dict = {}
  name_array = first_last_name_tuple_array(df)
  for line in df.itertuples(name = None):
    index = line[0]
    if name_array[index][1] in faculty_dict.keys():
    else:
      faculty_dict[name_array[index[1]]] =
  return faculty_dict



filepath = '/Users/lilliantong/ds/metis/metisgh/prework/dsp/python/faculty.csv'
df = pd.read_csv(filepath)
name_array =


