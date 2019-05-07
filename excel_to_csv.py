import sys
import pandas as pd

for xlsx in sys.argv[1:]:
    df = pd.read_excel(xlsx + '.xlsx', header=0) #, sheetname='<your sheet>'
    df.to_csv(xlsx + '.csv', index=False, float_format='%.f', sep='|')

