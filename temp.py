import pandas as pd
import os

DATA_PATH = os.path.join(os.getcwd(), 'data.csv')

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"], 
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset,)
myvar.index.name = 'ID'

print(myvar)

myvar.to_csv(DATA_PATH)