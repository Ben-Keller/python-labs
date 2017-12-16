import math
import matplotlib.pyplot as plt

# Function that reads in the data into four lists
def readCSVFile(filename):
    f = open(filename, "r")
    text = f.read()
    lines = text.split("\n")
    time = []; xVal = []; yVal = []; zVal = []
    # Loop over the lines
    for line in lines:
        values = line.split(",")
        if len(values) == 4:
            time.append(float(values[0]))
            xVal.append(float(values[1]))
            yVal.append(float(values[2]))
            zVal.append(float(values[3]))
        
    return time, xVal, yVal, zVal

# Function that finds peaks (above a threshold value) in a list
def findPeaks(vals, threshold = 0.99):
    peaks = [None]
    for i in range(1,len(vals)-1):
        prevVal = vals[i-1]
        currVal = vals[i]
        nextVal = vals[i+1]
        
        # Check if the current value is a PEAK above a certain threshold value
        if currVal > prevVal and currVal > nextVal and math.fabs(currVal) > threshold:
            peaks.append(1)
        # Check if the current value is a VALLEY above a certain threshold value
        elif currVal < prevVal and currVal < nextVal and math.fabs(currVal) > threshold:
            peaks.append(-1)
        else:
            peaks.append(0)
    
    peaks.append(None)
    return peaks


if __name__ == "__main__":
    
    # Read the data from the file
    time, xVal, yVal, zVal = readCSVFile("data.txt")

    # Compute overall acceleration magnitude
    accVal = []
    for i in range(len(time)):
        a = math.sqrt(xVal[i]**2 + yVal[i]**2 + zVal[i]**2)
        accVal.append(a)
        
    # Obtain peaks in z-direction
    zPeaks = findPeaks(zVal)
        
    # Plot all data in one figure
    fig1 = plt.figure("All in one")
    plt.plot(time, xVal)
    plt.plot(time, yVal)
    plt.plot(time, zVal)
    plt.plot(time, accVal)
    plt.ylabel('m/sec^2')
    plt.xlabel('time')
    plt.legend(['x', 'y', 'z', 'acc'])
    
    ## TODO: Plot data in separate sub figures
    fig2 = plt.figure("All in separate")
    ## The four subfigures should be on top of each other
    ## The colors should be the same as in the first plot
    ## Each subplot should have x-axis and y-axis labels
    ## Each subplot should have a title, replacing the legend
    ## in the previous plot.
    ## You will need to use the plt.subplot function.
    ## See for documentation:
    ## https://matplotlib.org/tutorials/introductory/sample_plots.html#subplot-demo


    ## TODO: Plot Acceleration in z-direction and 
    ## overlay the peaks on the graph
    fig3 = plt.figure("Acceleration with peaks")
    ## First you will need to identify the value of the graph at
    ## each peak. For this you can iterate over peaks and zVal lists,
    ## or you can modify the findPeaks function to return the values
    ## when there is a peak/valley.

    ## TODO: Create scatter plots for
    ## accVal-xVal, accVal-yVal, accVal-zVal
    ## xVal-yVal, yVal-zVal, zVal-xVal
    ## in a 2 by 3 subplot
    fig4 = plt.figure("Scatter plots")

    ## TODO: Create a bar plot with three columns 
    ## corresponding to the percentage of time during which 
    ## the zVal is (1) close to zero, (2) positive,
    ## and (3) negative
    fig5 = plt.figure("Counts")
    ## First iterate over zVal and categorize each value as
    ## one of the three bins. Count the number of times the
    ## data point corresponds to each bin. Turn those numbers
    ## into percentages and plot them as a bar chart.
    ## You will need to use the plt.bar function.
    ## See for documentation:
    ## https://matplotlib.org/tutorials/introductory/sample_plots.html#bar-charts

    plt.show()



