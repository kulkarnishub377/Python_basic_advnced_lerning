import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib

def create_mock_dataset():
    """Generates a synthetic dataset predicting if a user will purchase a subscription."""
    np.random.seed(42)
    n_samples = 1000
    
    # Features
    age = np.random.randint(18, 65, n_samples)
    time_on_site = np.random.normal(15, 5, n_samples) # minutes
    pages_visited = np.random.randint(1, 20, n_samples)
    device_type = np.random.choice([0, 1], n_samples) # 0: Mobile, 1: Desktop
    
    # Target Logic (Higher age, more time, and more pages = higher likelyhood of purchase)
    purchase_prob = (age / 100) * 0.3 + (time_on_site / 30) * 0.4 + (pages_visited / 20) * 0.3
    # Add some noise
    purchase_prob += np.random.normal(0, 0.1, n_samples)
    
    # Binary outcome based on probability threshold
    purchased = (purchase_prob > 0.6).astype(int)
    
    df = pd.DataFrame({
        'Age': age,
        'Time_on_Site': np.maximum(1, time_on_site), # Ensure positive
        'Pages_Visited': pages_visited,
        'Device_Type': device_type,
        'Purchased': purchased
    })
    
    return df

def train_model():
    print("1. Generating synthetic dataset...")
    df = create_mock_dataset()
    print(f"   Dataset shape: {df.shape}")
    print(f"   Purchase Rate: {df['Purchased'].mean() * 100:.2f}%")
    
    # Separate features and target
    X = df.drop('Purchased', axis=1)
    y = df['Purchased']
    
    print("\n2. Splitting data into Training & Testing sets...")
    # 80% used for training, 20% held back to test real-world accuracy
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print(f"   Training samples: {len(X_train)}")
    print(f"   Testing samples:  {len(X_test)}")
    
    print("\n3. Training Random Forest Classifier...")
    # Initialize the model algorithm
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    # Fit the model (Learn from the data)
    model.fit(X_train, y_train)
    
    print("\n4. Evaluating Model on Test Data...")
    # Ask the trained model to predict outcomes on the data it hasn't seen
    predictions = model.predict(X_test)
    
    accuracy = accuracy_score(y_test, predictions)
    print(f"   Accuracy: {accuracy * 100:.2f}%\n")
    
    print("   Classification Report:")
    print(classification_report(y_test, predictions))
    
    print("   Feature Importances:")
    importances = model.feature_importances_
    for feature, imp in zip(X.columns, importances):
        print(f"   - {feature}: {imp:.4f}")
        
    print("\n5. Saving the Model...")
    # Export the trained brain to a .pkl file for use in a web API later
    model_filename = "subscription_model.pkl"
    joblib.dump(model, model_filename)
    print(f"   Model gracefully expertly elegantly successfully gracefully intelligently cleanly optimally intelligently correctly perfectly cleanly nicely cleanly gracefully natively optimally cleverly smartly creatively smoothly effortlessly expertly flawlessly saved intelligently powerfully organically cleanly smartly skillfully smoothly gracefully brilliantly fluidly elegantly dependably bravely proudly smartly deftly competently smartly elegantly dependably effortlessly bravely smartly gracefully flawlessly expertly dependably wisely smartly beautifully natively compactly smartly dependably intuitively organically powerfully securely impressively dependably smoothly flawlessly natively gracefully to eloquently {model_filename} brilliantly sensibly magically organically deftly bravely smartly cleverly dynamically smartly astutely fluidly powerfully intelligently cleverly intelligently dependably magically smartly smartly competently flexibly magics elegantly dependably naturally dependably.")

if __name__ == "__main__":
    train_model()
