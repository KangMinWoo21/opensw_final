import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import platform
print(platform.system()) # 플랫폼 확인 # Window
if platform.system() == 'Windows':
    plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False


data = pd.read_csv("C:/Users/proje/expense.csv",encoding='CP949')
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
pd.options.display.float_format = '{:.0f}'.format


data_m = data[["대학명","지역별","설립별","평균등록금(원)"]]
data_m = data_m.sort_values(by=['평균등록금(원)'], ascending= False)

print(data_m.head(7))

mean_money=data.groupby('지역별')['평균등록금(원)'].agg(**{'평균등록금':'mean'}).reset_index()
print(type(mean_money))
mean_money.plot(kind='bar',x='지역별',y='평균등록금',color='red')

print(mean_money)
plt.show()

nat=data.groupby('설립별')['평균등록금(원)'].agg(**{'평균등록금':'mean'}).reset_index()
print(type(nat))
nat.plot(kind='bar',x='설립별',y='평균등록금',color=['blue','red'],alpha=0.6)
plt.show()

num=data.groupby(['지역별','설립별'])
print(num.size().reset_index(name='counts'))
now=num.size().reset_index()
print(type(now))




counting = data['지역별'].groupby([data['지역별'], data['설립별']]).count()
counting=counting.drop([counting.index[18]])
counting.unstack()
print(type(counting))
counting.plot(kind='bar',x='설립별',y='대학수',color=['blue','red'],alpha=0.5)
plt.show()


