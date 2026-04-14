# write a python program that calculate TP,TN,Fp,FN for the following steps
# actual = [1,1,1,1,0,0,0,0]
# predicted = []

# Display all four values

actual = [1,1,1,1,0,0,0,0]
predicted =[1,1,0,1,0,1,0,0]

TP = sum([1 for a , p in zip(actual, predicted) if a==1 and p==1])
TN = sum([1 for a , p in zip(actual, predicted) if a==0 and p==0])
FP = sum([1 for a , p in zip(actual, predicted) if a==0 and p==1])
FN = sum([1 for a , p in zip(actual, predicted) if a==1 and p==0])

print("TP :",TP)
print("TN:",TN)
print("FP:",FP)
print("FN:",FN)


#OR

from sklearn.metrics import confusion_matrix

actual =    [1,1,1,1,0,0,0,0]
predicted = [1,1,0,1,0,1,0,0]

tn, fp, fn, tp = confusion_matrix(actual, predicted).ravel()

print("TP:", tp)
print("TN:", tn)
print("FP:", fp)
print("FN:", fn)
