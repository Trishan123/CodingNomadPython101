# If a runner runs 10 miles in 30 minutes and 30 seconds,
# What is their average speed in kilometers per hour?
# (Tip: 1 mile = 1.6 km)
mile = 1.6 #assign miles to kilometer
min = 30 # assign min
sec = 30 # assign seconds 
run = 10 * mile #assign run to mile and the number 10

TimeInHour = (min + sec / 60) / 60 #convert time to hours
averageSpeed = run / TimeInHour
print(averageSpeed)