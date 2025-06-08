Model Description: Asteroid Hazard Prediction
This classification model is designed to predict whether a Near-Earth Object (NEO) is potentially hazardous based on its physical and orbital parameters. 
The model uses supervised machine learning techniques implemented with Python’s Scikit-learn library, focusing on basic yet effective algorithm like Random Forests.

Input Features
The model takes the following key parameters as input:
Average Diameter (km): Mean size of the asteroid, calculated from estimated minimum and maximum diameters.
Estimated Diameter Minimum (km): Lower bound of the asteroid’s estimated size.
Estimated Diameter Maximum (km): Upper bound of the asteroid’s estimated size.
Relative Velocity (km/h): Speed of the asteroid relative to Earth.
Miss Distance (km): Closest distance the asteroid will approach Earth.
Absolute Magnitude: A measure of the asteroid’s brightness, indirectly related to size and reflectivity.

Output
Hazardous: A binary classification label (`True` or `False`) indicating whether the asteroid is classified as a potential hazard based on its parameters.

Model Workflow
1. Data preprocessing: Cleansing, feature engineering (e.g., average diameter calculation), and handling class imbalance using oversampling techniques.
2. Training: The model is trained on historical NEO data with known hazard labels using a Random Forest classifier.
3. Evaluation: Performance is assessed via accuracy, precision, recall, F1-score, and confusion matrix to understand classification effectiveness, particularly for the minority hazardous class.
4. Prediction: Once trained, the model can classify new asteroid data input by users to assess potential hazard.

**The model currently achieves 92% accuracy with moderate recall (54%) on hazardous asteroid detection, indicating room for improvement in identifying rare but critical cases.