import pandas as pd

# initialize list of lists
political_leadership = [['Very weak', 6], ['Weak', 9], ['Neutral', 22], ['Strong', 40], ['Very strong', 23]]
bankruptcy = [['Holiday homes,\napartments,\nhostels etc.', 9], ['Mountain\nrailway/carrier', 13],
              ['Other categories', 19], ['Hotels', 23], ['Gastronomy', 27], ['Shipping', 40]]
fear = [[1,19], [2,21], [3,17], [4,24], [5,13], [6,7]]

# Create the pandas DataFrame
df1 = pd.DataFrame(political_leadership, columns=['label', 'val'])
df2 = pd.DataFrame(bankruptcy, columns=['label', 'val'])
df3 = pd.DataFrame(fear, columns=['label', 'val'])
# print dataframe.
#df1.to_csv('survey_leadership.csv')
#df2.to_csv('survey_bankruptcy.csv')
df3.to_csv('survey_fear.csv')