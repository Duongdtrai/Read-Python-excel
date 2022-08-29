
# import pandas lib as pd
import pandas as pd
data = pd.read_excel(r'D:\ITPTIT\code PTIT\Python\Python PTIT\BTVN-1-read-file-excel\danhsachsv.xlsx')
fullName = data['Họ lót'] + ' ' + data['Tên']
print(fullName)


# url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
# df = pd.read_csv(url, sep='\t')
# print (df)