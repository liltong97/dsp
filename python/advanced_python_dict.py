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
    split_names_orig = name.split()
    if len(split_names_orig[0]) < 3:
      split_names = [split_names_orig[1], split_names_orig[0], split_names_orig[2]]
    else:
      split_names = split_names_orig
    name_array.append((split_names[-1], split_names[0]))
  return name_array

def faculty_dictionary(df):
  faculty_dict = {}
  name_array = first_last_name_tuple_array(df)
  for line in df.itertuples(name = None):
    index = line[0]
    if name_array[index][0] in faculty_dict.keys():
      faculty_dict[name_array[index][0]].append([line[2].strip(), line[3], line[4]])
    else:
      faculty_dict[name_array[index][0]] = [[line[2].strip(), line[3], line[4]]]
  return faculty_dict

def better_faculty_dictionary(df):
  better_faculty_dict = {}
  name_array = first_last_name_tuple_array(df)
  for line in df.itertuples(name = None):
    index = line[0]
    curr_name = name_array[index]
    curr_name = curr_name[::-1]
    if curr_name in better_faculty_dict.keys():
      better_faculty_dict[curr_name].append([line[2].strip(), line[3], line[4]])
    else:
      better_faculty_dict[curr_name] = [line[2].strip(), line[3], line[4]]
  return better_faculty_dict

def print_by_last_name(better_faculty_dict):
  keys = better_faculty_dict.keys()
  keys.sort(key=lambda x: x[1])
  for key in keys:
    print str(key) + ': ' + str(better_faculty_dict[key])


filepath = '/Users/lilliantong/ds/metis/metisgh/prework/dsp/python/faculty.csv'
df = pd.read_csv(filepath)
faculty_dict = faculty_dictionary(df)
better_faculty_dict = better_faculty_dictionary(df)
print_by_last_name(better_faculty_dict)



