# Model Card

## Model Details
This model uses a random forest classifier with default hyperparameter values from sklearn's ensemble package.

## Intended Use
This model is intended to use census demographic information (education level, work class, marital status, etc.) to predict whether an individual's salary is less-than-or-equal to / more than $50,000. 

## Training Data
The data used to train this model comes from UC Irvine's Machine Learning Repository, which originally extracted the data from the 1994 Census database. The training data is a subset of the original data representing 80% of the overall data, which was then preprocessed by encoding features of the dataset according to their type:
    - Categorical data (`workclass`, `education`, `marital-status`, `occupation`, `relationship`, `race`, `sex`, `native-country`) was one-hot encoded.
    - Label data (in this case, the `salary` column) was binarized such that:
        - 1 = salary > 50K
        - 0 - salary <= 50K

## Evaluation Data
The data used for evaluation of the model is the remainder subset of the data used for training, the other 20% of the original data. This data undergoes the same transformations as the training set, and is scored on several metrics to show the predictive power of the model. This data also undergoes a logging of each slice of the test data's performance to illustrate feature and value importance in the overall predictions, as well as show the count of samples representing each slice.

## Metrics
The metrics used to score this model are:
    - Precision:  The ratio of correct predictions (true positives + true negatives) to the overall number of predicted samples. The closer this score is to 1, the fewer samples the model will incorrectly predict.
    - Recall: The ratio of correct positive predictions (true positives) to the overall number of actual positive samples. The closer this score is to 1, the better this model is at avoiding false negative cases.
    - F1-Score: This value uses the harmonic mean of the precision and recall to provide a balanced insight into the overall performance of the model as a classifier. Since it relies on precision and recall together, a higher score means both scores are also high and the model is more likely a strong predictive model.

This model scores on these metrics as follows:
    - Precision: Range between 0.74 - 0.75
    - Recall: Range between 0.63 - 0.64
    - F1: Range between 0.68 - 0.69

## Ethical Considerations
The ethical considerations in using this model are that it utilizes data containing protected classes, such as race and sex, though no PII is attached to any entries.

## Caveats and Recommendations
As stated at the top of the card, the current model has not gone through any hyperparamter tuning and it would be recommended to complete that process to increase the predictive power of the model.

The current iteration of this model also makes no attempt to identify or weigh any biases in the original data, of which several can be found. For example, the evaluation data contains over twice as many male entries as it does female, and they each share a similar accuracy score (0.7498 vs. 0.7405 respectively), recall score suffers much more in female-sliced predictions compared to male-sliced and consequently the F1 score for males (0.7024) is significantly higher than for females (0.5985). Completing a bias recognition evaluation would be another recommendation for future iterations of this model.

The data fed to this model comes with a set list of categorical column names and the salary/income column pre-binarized into ">50K" and "<=50K" values, so if you attempt to train this model with newer or different census data, make sure that the features are formatted similarly.