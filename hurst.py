from numpy import cumsum, log, polyfit, sqrt, std, subtract
import statsmodels.api as sm
def hurst(ts):
	"""
	return the hurst value
	@para: ts (type:list)
	@return: int
	"""
	data_size = len(tz)
	if data_size < 100:
		num = data_size//2
	else:
		num = 100
	# Create the range of lag values
	lags = range(2, num)

	# Calculate the array of the variances of the lagged differences
	tau = [sqrt(std(subtract(ts[lag:], ts[:-lag]))) for lag in lags]

	# Use a linear fit to estimate the Hurst Exponent
	poly = polyfit(log(lags), log(tau), 1)

	# Return the Hurst exponent from the polyfit output
	return poly[0]*2.0




