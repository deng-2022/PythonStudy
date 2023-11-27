import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")
sns.lineplot(x="total_bill", y="tip", data=data)
plt.xlabel('总账单')
plt.ylabel('小费')
plt.title('Seaborn折线图示例')
plt.show()
