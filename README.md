# ML_Module_00

## for executing file
```
python3 <filename>
```

## for checking format
```
pycodestyle <filename>
```

## for modifying format
```
black <filename>
```
## for copying docker file
```
docker cp <docker container id>:/app/results .
```

## conclusion
1. Why do we concatenate a column of ones to the left of the x vector when we use the linear algebra trick?
We add a column of ones to match the number of theta values. Since we have two theta values (theta0 and theta1), we need two columns in our x matrix. The column of ones lets us multiply these two matrices easily.
2. Why does the loss function square the distances between the data points and their predicted values?
Squaring ensures that all differences are positive. This is important because some differences might be negative (if the prediction is higher than the actual value) and others positive. By squaring them, we focus on the size of the gap, not its direction.
3. What does the loss function’s output represent?
The loss function's output shows us how far off our predictions are from the actual data. It sums up these differences for all data points.
4. Toward which value do we want the loss function to tend? What would that mean?
We want the loss function to get as close to 0 as possible. A value close to 0 means our prediction line accurately represents the data.
5. Do you understand why are matrix multiplications are not commutative?
The Result Can Be Different. Sometimes You Can't Multiply.
