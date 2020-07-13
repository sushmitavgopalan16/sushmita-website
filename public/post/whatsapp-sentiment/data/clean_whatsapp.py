import pandas as pd
# nikhil
df = pd.read_csv('nikhil_chat.txt', sep = ']')
df.columns = ['datetime','message']
df.dropna(inplace = True)

df['sender'] = df.apply(lambda row: 'Sush' if ('Sush:' in row['message']) else 'Nikhil', axis = 1)
df['text'] = df.apply(lambda row: row['message'].split(":")[1], axis = 1)
df['datetime'] = df.apply(lambda row: row['datetime'][1:], axis = 1)

df = df[['datetime','sender','text']]
df.to_csv('nikhil_p_whatsapp.csv')

# didige
df = pd.read_csv('didige_chat.txt', sep = ']', error_bad_lines = False)
df.columns = ['datetime','message']
df.dropna(inplace = True)

df['sender'] = df.apply(lambda row: 'Sush' if ('Sush:' in row['message']) else 'Didige', axis = 1)
df['text'] = df.apply(lambda row: row['message'].split(":")[1], axis = 1)
df['datetime'] = df.apply(lambda row: row['datetime'][1:], axis = 1)

df = df[['datetime','sender','text']]
df.to_csv('didige_whatsapp.csv')

# pranathi
df = pd.read_csv('pranathi_chat.txt', sep = ']', error_bad_lines = False)
df.columns = ['datetime','message']
df.dropna(inplace = True)

df['sender'] = df.apply(lambda row: 'Sush' if ('Sush:' in row['message']) else 'Pranathi', axis = 1)
df['text'] = df.apply(lambda row: row['message'].split(":")[1], axis = 1)
df['datetime'] = df.apply(lambda row: row['datetime'][1:], axis = 1)

df = df[['datetime','sender','text']]
df.to_csv('pranathi_whatsapp.csv')

# riddhima
df = pd.read_csv('riddhima_chat.txt', sep = ']', error_bad_lines = False)
df.columns = ['datetime','message']
df.dropna(inplace = True)

df['sender'] = df.apply(lambda row: 'Sush' if ('Sush:' in row['message']) else 'Riddhima', axis = 1)
df['text'] = df.apply(lambda row: row['message'].split(":")[1], axis = 1)
df['datetime'] = df.apply(lambda row: row['datetime'][1:], axis = 1)

df = df[['datetime','sender','text']]
df.to_csv('riddhima_whatsapp.csv')
