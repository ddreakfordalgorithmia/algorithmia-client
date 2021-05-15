import Algorithmia
import os
import json

import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split

# 1 Load data and split data
data = datasets.load_breast_cancer()
X, y = datasets.load_breast_cancer(return_X_y=True)
X, y = pd.DataFrame(X.astype(np.float32), columns=data['feature_names']), pd.Series(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
print ('Test data loaded..')

client = Algorithmia.client(os.getenv('ALGORITHMIA_API_KEY'), os.getenv('ALGORITHMIA_API'))
algo = client.algo('ddreakford/bc_predictions_observability/0.1.6')
algo.set_options(timeout=300) # optional

result = algo.pipe(X_test.to_json()).result
print(f"\nPredictions:")
print(json.dumps(result['predictions'], indent=2))
print(f"\nModel metadata:")
print(json.dumps(result['model_metadata'], indent=2))