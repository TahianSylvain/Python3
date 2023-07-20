"""We need dataframe in which SalesAmount is greater than $1400."""
result_data=data_frame[data_frame['Sale Amount'].astype(float)>1400.0]



"""Checking if paid or billed goodies"""
truth = ['paid', 'billed']
result_data=df[df["Status"].isin(truth)]



"""Checking if the name startswith J"""
result_data=df[df["Name"].str.startswith('J')


"""         loc() / iloc()          """
result_data=df.iloc[:,[1:4]]