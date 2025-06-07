import pandas as pd 
import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
from sklearn.model_selection import train_test_split
# from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import classification_report, confusion_matrix

import sklearn.metrics as skm
data=pd.read_csv("neo.csv")
df=pd.DataFrame(data)


y = df['hazardous']
df['avg_diameter'] = (df['est_diameter_min'] + df['est_diameter_max']) / 2
x = df[['avg_diameter', 'est_diameter_min','est_diameter_max','relative_velocity', 'miss_distance', 'absolute_magnitude']]


X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

# clf=DecisionTreeClassifier()
clf = RandomForestClassifier(class_weight='balanced')
clf.fit(X_train,y_train)

min_dia=float(input("Enter neo's estimated mininum diameter:\n"))
max_dia=float(input("Enter neo's estimated maximum diameter:\n"))
rela_vel=float(input("Enter neo's relative velocity:\n"))
miss_dis=float(input("Enter neo's estimated miss distance:\n"))
abs_mag=float(input("Enter neo's estimated absolute magnitude:\n"))
avg_dia=(min_dia+max_dia)/2

feature_names = ['avg_diameter','est_diameter_min', 'est_diameter_max', 'relative_velocity', 'miss_distance', 'absolute_magnitude']
input=pd.DataFrame([[avg_dia,min_dia,max_dia,rela_vel,miss_dis,abs_mag]], columns=feature_names)
# print(X.head())
# print(X_test.head())


y_pred=clf.predict(input)
# print(y_pred)
# print(y_test)
if y_pred[0]:
    print("The Near Earth Object is hazardous and should be monitored.")
else:
    print("The Near Earth Object is not hazardous.")

# print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
# print("\nClassification Report:\n", classification_report(y_test, y_pred))
