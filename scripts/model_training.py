from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, SimpleImputer

def train_models(X_train, y_train):
    
    
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', SimpleImputer(strategy='median'), ['Recency_woe', 'Frequency_woe', 'Monetary_woe']),
            ('cat', OneHotEncoder(handle_unknown='ignore'), ['CreditLabel', 'ProviderId'])
        ]
    )

    log_reg_pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', LogisticRegression(max_iter=1000))
    ])

    random_forest_pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', RandomForestClassifier(random_state=42))
    ])

    # Hyperparameter grids
    log_reg_param_grid = {
        'classifier__C': [0.01, 0.1, 1, 10],
        'classifier__solver': ['lbfgs', 'liblinear']
    }

    random_forest_param_grid = {
        'classifier__n_estimators': [50, 100, 200],
        'classifier__max_depth': [10, 20, 30],
        'classifier__min_samples_split': [2, 5, 10]
    }

   
    log_reg_grid_search = GridSearchCV(log_reg_pipeline, log_reg_param_grid, cv=5, scoring='roc_auc')
    log_reg_grid_search.fit(X_train, y_train)

    random_forest_grid_search = GridSearchCV(random_forest_pipeline, random_forest_param_grid, cv=5, scoring='roc_auc')
    random_forest_grid_search.fit(X_train, y_train)

    return log_reg_grid_search, random_forest_grid_search
