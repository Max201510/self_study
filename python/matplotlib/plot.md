# Introduction #
Matplotlib is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms.  
You can generate plots, histograms, power spectra, bar charts, errorcharts, scatterplots, etc., with just a few lines of code. 
## Line grap (plot) ##
    #Importing pyplot
    from matplotlib import pyplot as plt
    
    #Plotting to our canvas
    plt.plot([1,2,3],[4,5,1])
    
    #Showing what we plotted
    plt.show()
Now we will put labels on each axis and we need a title to our graph.
    from matplotlib import pyplot as plt
    
    x = [5,8,10]
    y = [12,16,6]
    
    plt.plot(x,y)
    
    plt.title('Epic Info')
    plt.ylabel('Y axis')
    plt.xlabel('X axis')
    
    plt.show()

Using style makes everything easy
  
    from matplotlib import style
    style.use('ggplot')

Next we will do lengend. Also grid lines.

    plt.plot(x,y,'g',label='line one', linewidth=5)
    plt.plot(x2,y2,'c',label='line two',linewidth=5)
    
    plt.title('Epic Info')
    plt.ylabel('Y axis')
    plt.xlabel('X axis')
    
    plt.legend()
    
    plt.grid(True,color='k')
    
    plt.show()

Keep in mind what I was saying about how matplotlib first "draws" things to a canvas, then finally shows it. Things like legends are drawn when you call them, so, if you are using, say, subplots, and call legends at the very end, only the 2nd subplot would have a legend. If you wanted a legend on each subplot, then you would need to call it per subplot. This is the same with titles! But hey, I didn't even cover subplots (multiple graphs on the same "figure," which just means the same window)

## bar charts (bar), scatter （scatter） ##
Bar charts with matplotlib are basically 1 slight change, same with scatter plots. 

    from matplotlib import pyplot as plt
    from matplotlib import style
    
    style.use('ggplot')
    
    x = [5,8,10]
    y = [12,16,6]
    
    x2 = [6,9,11]
    y2 = [6,15,7]
    
    
    plt.bar(x, y, align='center')
    
    plt.bar(x2, y2, color='g', align='center')
    
    
    plt.title('Epic Info')
    plt.ylabel('Y axis')
    plt.xlabel('X axis')
    
    plt.show()

-------------
    from matplotlib import pyplot as plt
    from matplotlib import style
    
    style.use('ggplot')
    
    x = [5,8,10]
    y = [12,16,6]
    
    x2 = [6,9,11]
    y2 = [6,15,7]
    
    plt.scatter(x, y)#, align='center')
    
    plt.scatter(x2, y2, color='g')#, align='center')
    
    
    plt.title('Epic Info')
    plt.ylabel('Y axis')
    plt.xlabel('X axis')
    
    plt.show()

Please From this [link](https://pythonprogramming.net/downloads/style.zip).
