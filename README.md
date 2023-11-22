# Predicting-House-Prices
Predicting House Prices Based on Property Specifications Using CSV Data and Models.

After navigating through various challenges, programming, and weeks of error testing, I aimed to determine whether, with simple data on the specifications and prices of forty-five thousand properties, I could calculate how much a house is worth and assess the accuracy of the prediction method.

Regardless of the method and algorithm I employed, none of them provided accurate prices, leaving me puzzled and amused:
KNN, Linear Regression, Random Forest Regressor, Decision Tree Regressor – these models generated amusing results, as seen in the movies.

However, when I explored the Neural Network method using Keras and TensorFlow in Python, I was astonished to find that it provided the closest and most accurate prices, albeit with a 78% error rate.
(Mind you, even the basic locomotion function doesn't have such a high error rate 😊). Currently, I am refining the code to minimize errors.

It also issued an interesting warning that led me to believe my laptop was on the verge of exploding. I thought I needed to seek refuge, but later, I realized it was just an intriguing warning and not a serious problem:
2023-11-22 16:22:14.893592 I tensorflow/core/platform/cpu_feature_guard.cc:182] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
To enable the following instructions: SSE SSE2 SSE3 SSE4.1 SSE4.2 AVX AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.

In the end, what I understood was that for classified data, Linear Regression and Neural Network are the best methods, and it's better not to invest too much effort, provided they have a very low error rate. 😉

Oops, I made a mistake because I have to mention the last method:
Now, let's go see the Neural Network method 😊

I'll upload the codes on GitHub. You can add a user interface to it and integrate it into your main project.

Here's the CSV file that is read and analyzed. You need to include it along with the Python files in your main project.


