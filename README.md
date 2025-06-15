## *AstroGuard*-Asteroid Hazard Prediction 

A machine learning project that predicts whether a Near-Earth Object (NEO) is potentially hazardous using physical and orbital characteristics. Built using **Python** and **Scikit-learn**, the model uses a **Random Forest Classifier** to perform binary classification with a focus on real-world NEO data from NASA.

---

### Key Features
- **Inputs**:
  - Estimated Diameter Min/Max (km)
  - Average Diameter (computed)
  - Relative Velocity (km/h)
  - Miss Distance (km)
  - Absolute Magnitude  
- **Output**: `True` or `False` — whether the NEO is potentially hazardous.

---

### Model Workflow
1. **Data Preprocessing**:
   - Cleansing and feature engineering (e.g., calculating average diameter)
   - Class imbalance handled via oversampling techniques  
2. **Training**:
   - Supervised learning with **Random Forest** on labeled NEO data  
3. **Evaluation**:
   - Accuracy: ~92%, with moderate recall (~54%) on hazardous cases  
4. **Prediction**:
   - Model predicts hazard risk from user-provided asteroid details

---

### NASA API Integration
- Integrated **NASA NEO Feed API** to fetch real-time or historical asteroid approach data
- Users can:
  - Retrieve NEOs approaching Earth on a specific date
  - View physical/orbital parameters of each asteroid
  - Input fetched data into the model for hazard prediction

---

### Interface
- **Command-Line Interface (CLI)** with interactive options:
  1. Predict hazard of a known asteroid using manual input
  2. Discover close-approaching NEOs on any given date using NASA API
  3. Reuse fetched NEO data for classification