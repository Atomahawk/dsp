import pandas as pd
from pandas import Series

# filename = 'faculty.csv'
filename = '/users/eastblue/ds/metis/metisgh/prework/dsp/python/faculty.csv'

df = pd.read_csv(filename, delimiter=' *, *', engine='python')

BSF_emails = []
for x in df['email']:
    BSF_emails.append(x)

emails = pd.Series(BSF_emails)
emails.to_csv('/users/eastblue/ds/metis/metisgh/prework/dsp/python/emails.csv', index=False)