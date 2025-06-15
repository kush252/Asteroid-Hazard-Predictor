import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling  import SMOTE
# import matplotlib.pyplot as plt
# import seaborn as sns
# from sklearn.metrics import roc_curve, roc_auc_score
# from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
from today_risk import fetch_risky_neo

def my_model():
    data=pd.read_csv("neo.csv")
    df=pd.DataFrame(data)

    y = df['hazardous']
    df['avg_diameter'] = (df['est_diameter_min'] + df['est_diameter_max']) / 2
    x = df[['avg_diameter', 'est_diameter_min','est_diameter_max','relative_velocity', 'miss_distance', 'absolute_magnitude']]
    X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

    smote=SMOTE(sampling_strategy='auto', random_state=42)
    x_smo,y_smo=smote.fit_resample(X_train,y_train)

    # clf=DecisionTreeClassifier()
    clf = RandomForestClassifier(class_weight='balanced')
    clf.fit(x_smo,y_smo)

    min_dia=float(input("Enter neo's estimated mininum diameter:\n"))
    max_dia=float(input("Enter neo's estimated maximum diameter:\n"))
    rela_vel=float(input("Enter neo's relative velocity:\n"))
    miss_dis=float(input("Enter neo's estimated miss distance:\n"))
    abs_mag=float(input("Enter neo's estimated absolute magnitude:\n"))
    avg_dia=(min_dia+max_dia)/2

    feature_names = ['avg_diameter','est_diameter_min', 'est_diameter_max', 'relative_velocity', 'miss_distance', 'absolute_magnitude']
    input_val=pd.DataFrame([[avg_dia,min_dia,max_dia,rela_vel,miss_dis,abs_mag]], columns=feature_names)

    y_pred=clf.predict(X_test)

    if y_pred[0]:
        print("The Near Earth Object is hazardous and should be monitored.")
    else:
        print("The Near Earth Object is not hazardous.")

def main():

    print("Welcome to AstroGuard\nPlease select an option corresponding to the action you wish to perform.\n1)Predict the hazard potential of an asteroid using its known details.\n2)Discover asteroids making dangerously close approaches to Earth on a specific date.\n")
    model_opt = int(input("Enter option number: "))
    
    if model_opt==1:
        my_model()

    elif model_opt==2:
        print("\nPlease select an option corresponding to the action you wish to perform.\n1)Today’s Possibly Hazardous NEOs.\n2)Possibly Hazardous NEOs for some other date.")
        option = int(input("Enter Option number: "))
        today_data=fetch_risky_neo(option)
        if today_data:
            for val in today_data:
                print(f"Name: {val[1]} Avg diameter:{(val[2]+val[3])/2} Velocity: {val[4]} Miss distance: {val[5]}")
            print("Want to predict hazard level for any of these?\n1)yes\n2)no")
            inner_opt=input("Enter option number: ")
            if inner_opt == 1:
                my_model()
            else:
                print("Alright then, have a great day ahead.")
        else:
            print("Sorry, no data available for this date.")

    else:
        print("Invalid Option")
    
if __name__ == "__main__":
    main()



# print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
# print("\nClassification Report:\n", classification_report(y_test, y_pred))