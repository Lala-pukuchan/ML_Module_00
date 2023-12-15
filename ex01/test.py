from TinyStatistician import TinyStatistician as ts

print("test...")
data = [42, 7, 69, 18, 352, 3, 650, 754, 438, 2659]
epsilon = 1e-5
err = "Error, grade 0 :("

tstat = ts()
assert abs(tstat.mean(data) - 499.2) < epsilon, err
assert abs(tstat.median(data) - 210.5) < epsilon, err

quartile = tstat.quartile(data)
assert abs(quartile[0] - 18) < epsilon, err
assert abs(quartile[1] - 650) < epsilon, err

assert abs(tstat.percentile(data, 10) - 3) < epsilon, err
assert abs(tstat.percentile(data, 28) - 18) < epsilon, err
assert abs(tstat.percentile(data, 83) - 754) < epsilon, err

assert abs(tstat.var(data) - 654661) < epsilon, err
assert abs(tstat.std(data) - 809.11) < epsilon, err

print("there is no error!")
