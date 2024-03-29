import numpy as np
from sklearn import metrics
y = np.array([0]*8850+[1]*2056)

pred = np.array([0.1, 0.4, 0.35, 0.8])
fpr, tpr, thresholds = metrics.roc_curve(y, pred, pos_label=2)
metrics.auc(fpr, tpr)