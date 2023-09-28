
import argparse
parser = argparse.ArgumentParser(description="Program creates a regression classifier, 4 arguments, being: Penalty(int), fit_intercept(boolean), max_iter(int) and tol(float)", epilog="https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html")
parser.add_argument('--penalty', type=str, default='l2',choices=["l1", "l2", "None, elasticnet"], help="Here you write the penalty")
parser.add_argument('--fit_intercept', type=bool, action='store_true', help="Here you write the intercept of the model")
parser.add_argument('--max_iter', type=int, default=100, help="Max number of iterations")
parser.add_argument('--tol', type=float, default=1e-4, help="Tolerance for stopping")

args = parser.parse_args()
print(args)

def my_logistic_regression(penalty , fit_intercept , max_iter , tol): 
    from sklearn.linear_model import LogisticRegression
    # define a logistic regression object with your input params
    clf = LogisticRegression(penalty=penalty , fit_intercept= fit_intercept , max_iter=max_iter , tol=tol)
    return clf


test = my_logistic_regression(args.penalty, args.fit_intercept, args.max_iter, args.tol)
print(test)