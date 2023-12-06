from TinyStatistician import TinyStatistician

a = [1, 42, 300, 10, 59]

ts = TinyStatistician()

print("Mean:", ts.mean(a))
print("Median:", ts.median(a))
print("Quartiles:", ts.quartile(a))
print("10th Percentile:", ts.percentile(a, 10))
print("15th Percentile:", ts.percentile(a, 15))
print("20th Percentile:", ts.percentile(a, 20))
print("Variance:", ts.var(a))
print("Standard Deviation:", ts.std(a))
