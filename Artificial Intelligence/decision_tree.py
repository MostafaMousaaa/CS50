import math
from collections import Counter
import json

class DecisionTree:
    def __init__(self, max_depth=None, min_samples_split=2):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.root = None
    
    def entropy(self, y):
        """Calculate entropy of a dataset"""
        if len(y) == 0:
            return 0
        
        proportions = list(Counter(y).values())
        proportions = [p/len(y) for p in proportions]
        
        entropy = 0
        for p in proportions:
            if p > 0:
                entropy -= p * math.log2(p)
        
        return entropy
    
    def information_gain(self, X_column, y, threshold):
        """Calculate information gain from a split"""
        # Parent entropy
        parent_entropy = self.entropy(y)
        
        # Split data
        left_indices = [i for i, x in enumerate(X_column) if x <= threshold]
        right_indices = [i for i, x in enumerate(X_column) if x > threshold]
        
        if len(left_indices) == 0 or len(right_indices) == 0:
            return 0
        
        # Children entropy
        n = len(y)
        n_left, n_right = len(left_indices), len(right_indices)
        
        left_y = [y[i] for i in left_indices]
        right_y = [y[i] for i in right_indices]
        
        e_left, e_right = self.entropy(left_y), self.entropy(right_y)
        
        # Weighted average
        child_entropy = (n_left/n) * e_left + (n_right/n) * e_right
        
        return parent_entropy - child_entropy
    
    def best_split(self, X, y):
        """Find the best feature and threshold to split on"""
        best_gain = -1
        best_feature = None
        best_threshold = None
        
        n_features = len(X[0])
        
        for feature in range(n_features):
            X_column = [row[feature] for row in X]
            thresholds = sorted(set(X_column))
            
            for threshold in thresholds:
                gain = self.information_gain(X_column, y, threshold)
                
                if gain > best_gain:
                    best_gain = gain
                    best_feature = feature
                    best_threshold = threshold
        
        return best_feature, best_threshold, best_gain
    
    def split_data(self, X, y, feature, threshold):
        """Split data based on feature and threshold"""
        left_X, left_y = [], []
        right_X, right_y = [], []
        
        for i, row in enumerate(X):
            if row[feature] <= threshold:
                left_X.append(row)
                left_y.append(y[i])
            else:
                right_X.append(row)
                right_y.append(y[i])
        
        return left_X, left_y, right_X, right_y
    
    def most_common_label(self, y):
        """Return the most common label in y"""
        return Counter(y).most_common(1)[0][0]
    
    def build_tree(self, X, y, depth=0):
        """Recursively build the decision tree"""
        # Stopping criteria
        if (len(set(y)) == 1 or  # Pure node
            len(y) < self.min_samples_split or  # Too few samples
            (self.max_depth and depth >= self.max_depth)):  # Max depth reached
            return {"label": self.most_common_label(y)}
        
        # Find best split
        feature, threshold, gain = self.best_split(X, y)
        
        if gain == 0:  # No information gain
            return {"label": self.most_common_label(y)}
        
        # Split data
        left_X, left_y, right_X, right_y = self.split_data(X, y, feature, threshold)
        
        # Recursively build subtrees
        left_subtree = self.build_tree(left_X, left_y, depth + 1)
        right_subtree = self.build_tree(right_X, right_y, depth + 1)
        
        return {
            "feature": feature,
            "threshold": threshold,
            "left": left_subtree,
            "right": right_subtree
        }
    
    def fit(self, X, y):
        """Train the decision tree"""
        self.root = self.build_tree(X, y)
    
    def predict_sample(self, sample, tree):
        """Predict a single sample"""
        if "label" in tree:
            return tree["label"]
        
        feature_value = sample[tree["feature"]]
        
        if feature_value <= tree["threshold"]:
            return self.predict_sample(sample, tree["left"])
        else:
            return self.predict_sample(sample, tree["right"])
    
    def predict(self, X):
        """Predict multiple samples"""
        return [self.predict_sample(sample, self.root) for sample in X]
    
    def print_tree(self, tree=None, indent="", feature_names=None):
        """Print the decision tree structure"""
        if tree is None:
            tree = self.root
        
        if "label" in tree:
            print(f"{indent}Predict: {tree['label']}")
        else:
            feature_name = f"Feature {tree['feature']}"
            if feature_names:
                feature_name = feature_names[tree['feature']]
            
            print(f"{indent}{feature_name} <= {tree['threshold']}")
            print(f"{indent}├─ True:")
            self.print_tree(tree["left"], indent + "│  ", feature_names)
            print(f"{indent}└─ False:")
            self.print_tree(tree["right"], indent + "   ", feature_names)

def create_sample_data():
    """Create sample dataset for weather decision"""
    # Features: [temperature, humidity, windy] -> play tennis?
    X = [
        [85, 85, 0],  # Hot, High, False
        [80, 90, 1],  # Hot, High, True
        [83, 78, 0],  # Hot, Normal, False
        [70, 96, 0],  # Mild, High, False
        [68, 80, 0],  # Mild, High, False
        [65, 70, 1],  # Mild, Normal, True
        [64, 65, 1],  # Cool, Normal, True
        [72, 95, 0],  # Mild, High, False
        [69, 70, 0],  # Mild, Normal, False
        [75, 80, 0],  # Mild, Normal, False
        [75, 70, 1],  # Mild, Normal, True
        [72, 90, 1],  # Mild, High, True
        [81, 75, 0],  # Hot, Normal, False
        [71, 91, 1]   # Mild, High, True
    ]
    
    y = ["No", "No", "Yes", "Yes", "Yes", "No", "Yes", 
         "No", "Yes", "Yes", "Yes", "Yes", "Yes", "No"]
    
    feature_names = ["Temperature", "Humidity", "Windy"]
    
    return X, y, feature_names

def main():
    """Demonstrate decision tree classification"""
    print("=== Decision Tree Classifier ===")
    
    # Create sample data
    X, y, feature_names = create_sample_data()
    
    print("Training Data (Weather → Play Tennis):")
    print("Temperature | Humidity | Windy | Play")
    print("-" * 40)
    for i, (features, label) in enumerate(zip(X, y)):
        temp, humidity, windy = features
        windy_str = "Yes" if windy else "No"
        print(f"{temp:11} | {humidity:8} | {windy_str:5} | {label}")
    
    # Train decision tree
    dt = DecisionTree(max_depth=5)
    dt.fit(X, y)
    
    print("\nDecision Tree Structure:")
    dt.print_tree(feature_names=feature_names)
    
    # Make predictions
    test_cases = [
        [75, 85, 0],  # Mild temp, high humidity, not windy
        [60, 60, 1],  # Cool temp, normal humidity, windy
        [90, 95, 1]   # Hot temp, high humidity, windy
    ]
    
    print("\nPredictions:")
    for i, test_case in enumerate(test_cases):
        prediction = dt.predict([test_case])[0]
        temp, humidity, windy = test_case
        windy_str = "Yes" if windy else "No"
        print(f"Case {i+1}: Temp={temp}, Humidity={humidity}, Windy={windy_str} → {prediction}")
    
    # Calculate training accuracy
    train_predictions = dt.predict(X)
    accuracy = sum(1 for pred, actual in zip(train_predictions, y) if pred == actual) / len(y)
    print(f"\nTraining Accuracy: {accuracy:.2%}")
    
    # Demonstrate entropy calculation
    print(f"\nEntropy Examples:")
    print(f"Pure dataset [Yes, Yes, Yes]: {dt.entropy(['Yes', 'Yes', 'Yes']):.3f}")
    print(f"Mixed dataset [Yes, No]: {dt.entropy(['Yes', 'No']):.3f}")
    print(f"Training labels entropy: {dt.entropy(y):.3f}")

if __name__ == "__main__":
    main()
