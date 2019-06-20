
# coding: utf-8

# ## Exercises
# 
# This will be a notebook for you to work through the exercises during the workshop. Feel free to work on these at whatever pace you feel works for you, but I encourage you to work together! Edit the title of this notebook with your name because I will ask you to upload your final notebook to our shared github repository at the end of this workshop.
# 
# Feel free to google the documentation for numpy, matplotlib, etc.
# 
# Don't forget to start by importing any libraries you need.

# In[2]:


# import your libraries here
import numpy as np
import pylab as plt


# ### Day 1
# 
# #### Exercise 1
# 
#    A. Create an array with 10 evenly spaced values in logspace ranging from 0.1 to 10,000.
# 
#    B. Print the following values: The first value in the array, the final value in the array, and the range of 5th-8th values.
# 
#    C. Append the numbers 10,001 and 10,002 (as floats) to the array. Make sure you define this!
# 
#    D. Divide your new array by 2.
# 
#    E. Reshape your array to be 3 x 4. 
# 
#    F. Multiply your array by itself.
#     
#    G.  Print out the number of dimensions and the maximum value.

# In[5]:


# your solution here

print('A')
log_arr = np.logspace(-1, 4, 10)
print(log_arr)
print()

print('B')
print(log_arr[0], log_arr[-1], log_arr[4:8])

print()

print('C')
x = np.array([10001. , 10002. ])

new_log_arr = np.append(log_arr, x)
print(new_log_arr)
print()

print('D')
divide_by_2 = new_log_arr/2
print(divide_by_2)
print()

print('E')
reshaped_arr = divide_by_2.reshape((3,4))

print(reshaped_arr)
print()

print('F')
mult = reshaped_arr * reshaped_arr
print(mult)
print()

print('G')
print(mult.ndim, np.amax(mult))


# ### Day 2

# #### Exercise 1
# 
#    A. Create an array containing the values 4, 0, 6, 5, 11, 14, 12, 14, 5, 16.
#    B. Create a 10x2 array of zeros.
#    C. Write a for loop that checks if each of the numbers in the first array squared is less than 100. If the statement is true, change that row of your zeros array to equal the number and its square. Hint: you can change the value of an array by stating "zerosarray[i] = [a number, a number squared]". 
#    D. Print out the final version of your zeros array.
#     
# Hint: should you loop over the elements of the array or the indices of the array?

# In[7]:


# your solutions here

#making my array
arr = np.array([4, 0, 6, 5, 11, 14, 12, 14, 5, 16])

#making my 10X2 array of zeros
zero_arr = np.zeros((10,2))

#going through the loop and finding the square values < 100
for i, val in enumerate(arr):
    
    if val**2 < 100:
        zero_arr[i] = [val, val**2]
        
        
print(zero_arr)        


# #### Exercise 2
#     
#    A. Write a function that takes an array of numbers and spits out the Gaussian distribution. Yes, there is a function for this in Python, but it's good to do this from scratch! This is the equation:
#     
# $$ f(x) = \frac{1}{\sigma \sqrt{2\pi}} \exp{\frac{-(x - \mu)^2}{2\sigma^2}} $$
# 
#     (Pi is built into numpy, so call it as np.pi.)
# 
#    B. Call the function a few different times for different values of mu and sigma, between -10 < x < 10.
#     
#    C. Plot each version, making sure they are differentiated with different colors and/or linestyles and include a legend. Btw, here's a list of the customizations available in matplotlib:
#     
#     https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.pyplot.plot.html
#     
#     https://matplotlib.org/gallery/color/named_colors.html
#     
#    D. Save your figure.
#     
# If you have multiple lines with plt.plot(), Python will plot all of them together, unless you write plt.show() after each one. I want these all on one plot.

# In[24]:


# your solutions here
def Gauss(x, mu, sigma):
    '''
    This function calculates the Guassian distribution given x, mu, sigma
    
    Parameters
    -------------
    x: the range of x values you are interested in finding the Gaussian distribution
    mu: the average of the given distribution
    sigma: the standard deviation of the distribution
    
    Output:
    Gaussian distribution given the x, mu, and sigma you passed in
    
    '''
    #making a prefactor variable
    prefactor = 1/(sigma* np.sqrt(2*np.pi))
    #making the exponential part into its own variable
    exp = np.exp(-(x-mu)**2/(2*sigma**2))
    
    #returning the Gaussian
    return prefactor * exp


#making my x array
x = np.linspace(-10, 10, 500)

y1 = Gauss(x, 1, 1)
y2 = Gauss(x, 3, .5)
y3 = Gauss(x, -2, 4)
y4 = Gauss(x, 1.2, .3)
y5 = Gauss(x, -3.2, 2)  
    
plt.figure(figsize = (14, 8))
plt.title('Gaussian Function', fontsize = 16)
plt.xlabel('x values', fontsize = 16)
plt.ylabel('y-values of Gaussian', fontsize = 16)

#yaxis goes from 0 to 1 since it sproperly normalized by the prefactor
plt.axis([x[0], x[-1], 0, 1])
plt.plot(x, y1, 'r-', label = r'$\mu$ = 1, $\sigma$ = 1')
plt.plot(x, y2, 'b--', label = r'$\mu$ = 3, $\sigma$ = .5')
plt.plot(x, y3, 'k*', label = r'$\mu$ = -2, $\sigma$ = 4')
plt.plot(x, y4, 'gs', label = r'$\mu$ = 1.2, $\sigma$ = 8')
plt.plot(x, y5, 'yo', label = r'$\mu$ = -3.2, $\sigma$ = 6.75')
plt.legend(loc = 'best')
plt.savefig('Gaussian_Plots.pdf')
plt.show()


# ### Day 3
# 
# #### Exercise 1
# 
# There is a file in this directory called "histogram_exercise.dat" which consists of of randomly generated samples from a Gaussian distribution with an unknown $\mu$ and $\sigma$. Using what you've learned about fitting data, load up this file using np.genfromtxt, fit a Gaussian curve to the data and plot both the curve and the histogram of the data. As always, label everything, play with the colors, and choose a judicious bin size. 
# 
# Hint: if you attempt to call a function from a library or package that hasn't been imported, you will get an error.

# In[5]:


from scipy.stats import norm


# In[6]:


# your solution here
gauss_data = np.loadtxt('histogram_exercise.dat')


# In[8]:


mu, sigma = norm.fit(gauss_data)

x = np.linspace(np.min(gauss_data), np.max(gauss_data), 1000)

gauss = norm.pdf(x, mu, sigma)


# In[21]:


plt.figure(figsize =(12, 12))
plt.title('Gauss and Gaussian Fit')
plt.plot(x, gauss, 'k', linewidth = 2, label= 'Gauss Fit')
plt.hist(gauss_data, color= 'yellow', normed=True, hatch='//', label='Gaussian Data')
plt.legend(loc='best')
plt.show()


# #### Exercise 2
# 
# Create a 1D interpolation along these arrays. Plot both the data (as points) and the interpolation (as a dotted line). Also plot the value of the interpolated function at x=325. What does the function look like to you?

# In[22]:


from scipy.interpolate import interp1d


# In[24]:


x = np.array([0., 50., 100., 150., 200., 250., 300., 350., 400., 450., 500])
y = np.array([0., 7.071, 10., 12.247, 14.142, 15.811, 17.321, 18.708, 20., 21.213, 22.361])

# solution here

f = interp1d(x, y)


# In[34]:


xnew = np.linspace(0, 500, 1000)
plt.figure(figsize = (10,10))
plt.plot(x, y, 'ko', label = 'Data')
plt.plot(xnew, f(xnew), 'r--', label = 'Interpolation')
plt.plot(325, f(325), 'b*', label = 'x = 325', markersize = 15)
plt.legend(loc = 'best', frameon=False)
plt.show()


# In[1]:


from astropy import constants as const
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
import aplpy


# ### Day 4
# 
# #### Exercise 1
# 
# Let's practice some more plotting skills, now incorporating units. 
# 
# A. Write a function that takes an array of frequencies and spits out the Planck distribution. That's this equation:
# 
# $$ B(\nu, T) = \frac{2h\nu^3/c^2}{e^{\frac{h\nu}{k_B T}} - 1} $$
# 
# This requires you to use the Planck constant, the Boltzmann constant, and the speed of light from astropy. Make sure they are all in cgs. 
#     
# B. Plot your function in log-log space for T = 25, 50, and 300 K. The most sensible frequency range is about 10^5 to 10^15 Hz. Hint: if your units are correct, your peak values of B(T) should be on the order of 10^-10. Make sure everything is labelled. 

# In[4]:


h = const.h.cgs
k = const.k_B.cgs
c = const.c.cgs.value
print(h)
print(k)
print(c)


# In[8]:


h = const.h.cgs.value
k = const.k_B.cgs.value
c = const.c.cgs.value

# solution here
def blackbody(nu, T):
    
    
    numerator = (2 * h * nu**3)/c**2
    denom = np.exp((h * nu)/(k * T)) - 1
    
    return numerator/denom

nu = np.linspace(1e5, 1e15, 1e5)
T = [25, 50, 300]

plt.figure(figsize = (10,10))
plt.xlabel('Frequency [Hz]', fontsize = 16)
plt.ylabel('Specific Intensity', fontsize = 16)
plt.title('Planck Distribution', fontsize = 16)

for i in T:
    plt.loglog(nu, blackbody(nu, i), label = str(i) + ' K')

plt.legend(loc='best', fontsize = 14, frameon=False)
plt.show()    


# #### Exercise 2
# 
# Let's put everything together now! Here's a link to the full documentation for FITSFigure, which will tell you all of the customizable options: http://aplpy.readthedocs.io/en/stable/api/aplpy.FITSFigure.html. Let's create a nice plot of M51 with a background optical image and X-ray contours overplotted.
# 
# The data came from here if you're interested: http://chandra.harvard.edu/photo/openFITS/multiwavelength_data.html
# 
# A. Using astropy, open the X-RAY data (m51_xray.fits). Flatten the data array and find its standard deviation, and call it sigma.
# 
# B. Using aplpy, plot a colorscale image of the OPTICAL data. Choose a colormap that is visually appealing (list of them here: https://matplotlib.org/2.0.2/examples/color/colormaps_reference.html). Show the colorbar. 
# 
# C. Plot the X-ray data as contours above the optical image. Make the contours spring green with 80% opacity and dotted lines. Make the levels go from 2$\sigma$ to 10$\sigma$ in steps of 2$\sigma$. (It might be easier to define the levels array before show_contours, and set levels=levels.)

# In[20]:


# solution here
data = fits.getdata('m51_xray.fits')

flat_data = data.flatten()

sigma = np.std(flat_data)


# In[35]:


galaxy = aplpy.FITSFigure('m51_optical_B.fits')
galaxy.show_colorscale(cmap='cubehelix')
galaxy.show_colorbar()

plt.show()


# In[21]:


2*sigma


# In[29]:


levels = np.linspace(2*sigma, 10*sigma, num = 5)
levels[1]-levels[0]


# In[36]:


levels = np.linspace(2*sigma, 10*sigma, num = ((8*sigma)/(2*sigma)))

galaxy = aplpy.FITSFigure('m51_optical_B.fits')
galaxy.show_colorscale(cmap='cubehelix')
galaxy.show_contour('m51_xray.fits', linestyle= 'dotted', colors = 'springgreen', alpha = .8, levels = levels)
#galaxy.show_colorbar()

plt.show()

