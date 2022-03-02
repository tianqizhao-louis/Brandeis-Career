import pandas as pd 

with open('data.json', encoding='utf-8') as inputfile:
    df = pd.read_json(inputfile)


df[['j1','j2', 'j3', 'j4', 'j5', 'j6', 'j7', 'j8', 'j9', 'j10']] = pd.DataFrame(df.job.tolist(), index= df.index)

df[["Job1", "Job1Year"]] = pd.DataFrame(df.j1.apply(pd.Series))
df[["Job2", "Job2Year"]] = pd.DataFrame(df.j2.apply(pd.Series))
df[["Job3", "Job3Year"]] = pd.DataFrame(df.j3.apply(pd.Series))
df[["Job4", "Job4Year"]] = pd.DataFrame(df.j4.apply(pd.Series))
df[["Job5", "Job5Year"]] = pd.DataFrame(df.j5.apply(pd.Series))
df[["Job6", "Job6Year"]] = pd.DataFrame(df.j6.apply(pd.Series))
df[["Job7", "Job7Year"]] = pd.DataFrame(df.j7.apply(pd.Series))
df[["Job8", "Job8Year"]] = pd.DataFrame(df.j8.apply(pd.Series))
df[["Job9", "Job9Year"]] = pd.DataFrame(df.j9.apply(pd.Series))
df[["Job10", "Job10Year"]] = pd.DataFrame(df.j10.apply(pd.Series))


df = df.drop('firstName', 1)
df = df.drop('lastName', 1)
df = df.drop('gender', 1)
df = df.drop('classYear', 1)
df = df.drop('major', 1)
df = df.drop('job', 1)
df = df.drop('j1', 1)
df = df.drop('j2', 1)
df = df.drop('j3', 1)
df = df.drop('j4', 1)
df = df.drop('j5', 1)
df = df.drop('j6', 1)
df = df.drop('j7', 1)
df = df.drop('j8', 1)
df = df.drop('j9', 1)
df = df.drop('j10', 1)


df.to_csv('dataOutput.csv', encoding='utf-8', index=True)
