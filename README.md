

# Credit Scoring Model for Buy-Now-Pay-Later Service

This project develops a credit scoring model for Bati Bank's partnership with an eCommerce company offering a buy-now-pay-later service. The goal is to predict credit risk and assign appropriate loan terms based on customer transaction data. The model uses historical transaction records to classify users as high risk (likely to default) or low risk (unlikely to default), enabling informed lending decisions for the new buy-now-pay-later service.

The project involves several key steps: data preparation, feature engineering, modeling, and API development. I started by loading and preprocessing the dataset, then perform exploratory data analysis to understand the data distribution. Feature engineering techniques are applied to extract meaningful predictors from the transaction data. Multiple machine learning models are trained and evaluated, including logistic regression, and random forests. Hyperparameter tuning is performed to optimize model performance. Finally, a REST API is developed to serve predictions in real-time.

The credit scoring model is deployed using Flask and Render, allowing for easy scaling and integration with the eCommerce platform. The API accepts customer transaction data and returns a risk score and recommended loan terms. Extensive testing is conducted to ensure accuracy and reliability of the predictions. This project demonstrates the application of data science techniques to solve a critical business problem in financial services, enabling safer lending practices and improved customer experiences for the buy-now-pay-later service.
