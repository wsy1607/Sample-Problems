def computeAverages(numbers):
    n = len(numbers)
    mean = round(sum(numbers) / n, 2)
    if n % 2 == 1:
        median = round(sorted(numbers)[n//2], 2)
    else:
        median = round(sum(sorted(numbers)[n//2-1:n//2+1])/2.0, 2)
    return (mean, median)
