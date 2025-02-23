#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# libraries
library(reticulate)
library(tidyverse)
library(ggplot2)
#use_condaenv("datascience", required = FALSE) # set my environment
#
#
#
#
#
#
#
print("Hello World!") # first line r of code
#
#
#
print("Hello Stats!") # second line r of code
#
#
#
#
#
#
#
#
#
#
1 + 2 + 3 + 4 + 5 
sum(1:5) # alternate way to write the code
#
#
#
#
#
c(1, 2, 3, 4, 5) # concatenate 
1:5 # sequence operator
sum(1:5) # addition using the sequence operator
#
#
#
#
#
x <- 1:5 # vector assignment
y <- 10 # vector assignment
x+y # vector addition
z <- x+y # vector assignment
z
h <- "Hello" # vector assignment
h
hw <- c("Hello", "World!") # vector concatenation 
print(hw) # print view
paste(hw) # paste view
#
#
#
#
#
ls() # view created objects
rm("z") # remove "z" object
ls() # confirm removal
#
#
#
#
#
baskets.of.granny <- c(12, 4, 4, 6, 9, 3)
sum(baskets.of.granny)

firstnames <- c("John", "Jacqueline", "Robert") # create vector list
lastname <- "Kennedy" # create vector
paste(firstnames, lastname) # paste vectors

lastnames <- c("Kennedy", "Kennedy-Onnasis") # create vector list
paste(firstnames, lastnames) # paste vectors
#
#
#
#
#
#
#
ggplot(mpg, aes(displ, hwy)) + # create a scatter plot
  geom_point() +
  labs(title = "Displacement vs. Highway MPG Scatterplot", 
       x = "Displacement (litres)", 
       y = "Highway MPG") + # apply labels
  theme(plot.title = element_text(hjust = 0.5))
#
#
#
#
#
#
#
#
#
ggplot(mpg, aes(class, hwy)) + # create a box plot
  geom_boxplot() +
  labs(title = "Class vs. Highway MPG Box Plot", 
       x = "Class", 
       y = "Highway MPG") + # apply labels
  theme(plot.title = element_text(hjust = 0.5))
#
#
#
#
#
#
#
#
#
mean(economics$unemploy) # calculate mean
var(economics$unemploy) # calculate variance
sd(economics$unemploy) # calculate standard deviation
min(economics$unemploy) # calculate min
max(economics$unemploy) # calculate max
median(economics$unemploy) # calculate median
cor(economics$pce, economics$psavert) # calculate correlation
pce_psavert_cor <- round(cor(economics$pce, economics$psavert),4) 
# assign correlation to vector variable
#
#
#
#
#
#
#
#
#
data(tips, package = 'reshape2') # attach data
t.test(tips$tip, alternative = 'two.sided', mu=2.50) # conduct two tail t-test
#
#
#
#
#
#
#
#
#
head(mpg) # view first 6 rows of data
tail(mpg) # view last 6 rows of data
lm(hwy ~ displ, mpg) # build a basic linear regression model
ggplot(mpg, aes(displ, hwy)) + # build a linear regression model scatter plot
  geom_point() +
  labs(title = "Displacement vs. Highway MPG Regression Model", 
       x = "Engine Size", 
       y = "Highway Fuel Efficiency") +
  geom_smooth(method = "lm", color = "red") +
  theme(plot.title = element_text(hjust = 0.5))

fuelILM <- lm(displ ~ hwy, mpg) # assign new model to vector variable
fuelILM
summary(fuelILM) # review summary statistics
#
#
#
#
#
#
#
housing <- read.table("http://www.jaredlander.com/data/housing.csv", sep = ",", 
                      header = TRUE, stringsAsFactors = FALSE) # read data
names(housing) <- c("Neighborhood", "Class", "Units", "YearsBuilt", "SqFt", 
                    "Income", "IncomePer-SqFt", "Expense", "ExpensePerSqFt", 
                    "NetIncome", "Value", "ValuePerSqFt", "Boro") # rename columns
head(housing)
#
#
#
#
#
house1 <- lm(ValuePerSqFt ~ Units + SqFt + Boro, 
             housing) # build a linear regression model
summary(house1) # view summary statistics
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
