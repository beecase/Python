def classify(x):
    return"even" if x%2==0 else "odd"
numbers=[5,7,2,9]
result=list(map(classify,numbers))
print(result)
