# Passwords


## Key terminology





## Exercise
### Sources
1. [Hash](https://academy.moralis.io/blog/what-is-hashing-a-complete-guide-to-hashing?utm_source=gads&utm_campaign=16265974031&utm_medium=133080359906&network=g&device=m&gclid=CjwKCAjwj42UBhAAEiwACIhADl7vrirsJ-T1JikPM31AzQNzjYua4F1Gwkgc88TBHzw2I-0XpDnIZhoCW2QQAvD_BwE)
2. [Hash2](https://www.2brightsparks.com/resources/articles/introduction-to-hashing-and-its-uses.html)



### Overcome challenges
Not much, i have alot of intrest in this. creating my maybe only challenge, me going way to deep.

### Results
## What is hashing?
Hashing is an algorithm that calculates a fixed-size bit string value from a file. A file basically contains blocks of data. Hashing transforms this data into a far shorter fixed-length value or key which represents the original string. The hash value can be considered the distilled summary of everything within that file.

A good hashing algorithm would exhibit a property called the avalanche effect, where the resulting hash output would change significantly or entirely even when a single bit or byte of data within a file is changed. A hash function that does not do this is considered to have poor randomization, which would be easy to break by hackers.
The picture below show this.
![SS](../../00_includes/SEC-07/snowbally.png)
In this example picture you can see that the only thing changed about the input is the first letter, it goes from a lower care to a upper case i. Because of this the entire hash changes.

A hash is usually a hexadecimal string of several characters. Hashing is also a unidirectional process so you can never work backwards to get back the original data.

A good hash algorithm should be complex enough such that it does not produce the same hash value from two different inputs. If it does, this is known as a hash collision. A hash algorithm can only be considered good and acceptable if it can offer a very low chance of collision.
But Imagine that you have N different possibilities of an birthday happening. In this case, you need a square root of N to have a 50% chance of a collision. When it comes to birthdays, there are 365 distinct possibilities of that event happening. Upon square rooting that, we get sqrt(365) = ~23. This is why, if we were in a room with about 30 people there will be a chance of collision.
