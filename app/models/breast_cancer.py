#import pickle
#import os
#from sklearn.datasets import load_breast_cancer
#from sklearn.model_selection import train_test_split
#from sklearn.ensemble import RandomForestClassifier

# Load the breast cancer dataset
#data = load_breast_cancer()
#X = data.data  # Features
#y = data.target  # Labels

# Split the dataset into training and testing sets
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
#model = RandomForestClassifier(random_state=42)
#model.fit(X_train, y_train)

# Save the model as a pickle file in the specified directory
#model_path = os.path.join('app\models', 'model.pkl')
#with open(model_path, 'wb') as model_file:
   # pickle.dump(model, model_file)
    
    
import pickle
import os    
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# 1. Load the breast cancer dataset

data = load_breast_cancer()
X = data.data   #  Features
y = data.target #  Labels

# 2. Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Data standardization
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 4. Create and train the SVM model 
model_svc = SVC(kernel='rbf', C=1, gamma='scale', class_weight='balanced')  
model_svc.fit(X_train, y_train)

# 5. Prediction on test data
y_pred = model_svc.predict(X_test)

# 6. Prediction results as 0 and 1
model= y_pred

# 7. Save the model as a pickle file in the specified directory
model_path = os.path.join('app\models', 'model.pkl')
with open(model_path, 'wb') as model_file:
    pickle.dump(model, model_file)
   
# 5. prediction on test data
#y_pred = model.predict(X_test)

# 6. Model evaluation
# #accuracy = accuracy_score(y_test, y_pred)    