import pandas as pd

# initialize list of lists
political_leadership = [['Very weak', 6], ['Weak', 9], ['Neutral', 22], ['Strong', 40], ['Very strong', 23]]
bankruptcy = [['Holiday homes,\napartments,\nhostels etc.', 9], ['Mountain\nrailway/carrier', 13],
              ['Other categories', 19], ['Hotels', 23], ['Gastronomy', 27], ['Shipping', 40]]

# Create the pandas DataFrame
df1 = pd.DataFrame(political_leadership, columns=['label', 'val'])
df2 = pd.DataFrame(bankruptcy, columns=['label', 'val'])
# print dataframe.
df1.to_csv('survey_leadership.csv')
df2.to_csv('survey_bankruptcy.csv')