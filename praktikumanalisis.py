import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

data = pd.read_csv('nilai_siswa.csv')
print(data.info())
print(data.head())
print(data.describe())

print("Rata-rata:", data['Nilai'].mean())
print("Median:", data['Nilai'].median())
print("Modus:", data['Nilai'].mode())

matematika = data[data['Matpel'] == 'Matematika']
print(matematika)

Inggris = data[data['Matpel'] == 'Bahasa Inggris']
print(Inggris) 
  
data.groupby('Matpel')['Nilai'].agg(['max','min'])
rata = data.groupby('Matpel')['Nilai'].mean()
rata.plot(kind='bar' , color=['blue', '#ff7f0e', '#2ca02c', '#ffa7a0', '#2fa06c' ])
plt.title('Rata-Rata Nilai per Matpel')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai Rata-Rata')
plt.show()

sn.boxplot(x='Matpel', y='nilai', data=data)
plt.title('sebaran nilai per mata pelajaran')
plt.tight_layout()
plt.show
