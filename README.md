# Dominó problem

### Description

During [Python Brasil [12]](http://2016.pythonbrasil.org.br/) in FLorianópolis - Brazil
I took a cab and the taxi driver, called Luiz, listened me and my friends talking about
computer science stuff.
Then he look at us with a smiling face and said: "Are you from google generation?".

We obviosly answer: "hell yeah, we are! rsrs" Then he said: "Let's see if you can
solve this problem...", and he described the **Dominó problem**.
Luiz is a former economist. Nowadays he is a taxi driver that drop puzzles in his passengers! 

![alt text][taxi-driver]
[taxi-driver]: https://github.com/pantuza/domino-problem/blob/master/img/luiz-economist.png "Luiz, economist/taxi driver"


### Problem

There is a table game called [*Dominó*](https://en.wikipedia.com/domino).
This game pieces are divided in two parts.
Both parts has a number between 0 and 6.
Each pair of numbers never repeat and there is no inverse pieace
with this numbers.

![alt text][domino-pieces]
[domino-pieces]: https://github.com/pantuza/domino-problem/blob/master/img/domino-pieces.png "Dominó pieces"

Based on that, how many pieces has an **odd number** as a result of the **sum** of
its two parts?

### Solution

First of all, we freaked out and try to run a *brute force* algorithm together.
One of my friends started saying loud the combinations of numbers starting from the lowest to the highest pairs.
Another friend calculates if the sum of numbers were odd.
And finally, I was counting the number of odd resulted numbers.

Basically, it did not work!

At this point, the taxi driver was in a very funny work day!
I picked up a paper and a pen inside my backpack and started drawing the possibilities matrix as follows:

![alt text][possibilities-matrix]
[possibilities-matrix]: https://github.com/pantuza/domino-problem/blob/master/img/possibilities-matrix.png "Dominó numbers possibilities matrix"

As can be seen in the above figure, we have a matrix of dominó pieces combinations.
Each position represents a piece.
Each coordinate pair (x, y), are the top and bottom parts of a piece.

The values inside matrix cells represents booleans values of the sum of the two parts (x + y). 
If the sum is odd, then the value is 1. Otherwise the value is 0.
Through that, is possible to count how many sums resulted in an odd number.

The first observation about the problem was that if what we were looking for was odd resulted numbers, then pieces that have the same number as the top and bottom values must be excluded from counting. The sum of two even numbers are always an even number. Also, the sum of two odd numbers are always an even number. Based on that, looking at the possibilities matrix, we can exclude the matrix determinant values from counting:

![alt text][determinant-matrix]
[determinant-matrix]: https://github.com/pantuza/domino-problem/blob/master/img/determinant-matrix.png "Dominó numbers determinant matrix"

Another property of the problem is that each pair of number only exist once.
So, we do not have to iterate over the bottom part of the matrix. 
For that, we remove the mirrored values from the possibility matrix:

![alt text][problem-matrix]
[problem-matrix]: https://github.com/pantuza/domino-problem/blob/master/img/problem-matrix.png "Dominó mirrored excluded matrix"

Knowing all of those constraints, to solve the problem we have to iterate over the top part of the matrix excluding the determinant.
On each iteration step, we check if the sum is odd and count it.
Otherwise we continue to the next iteration step until there is no steps left.
The output result is the total number of odd resulted numbers.

![alt text][solution-matrix]
[solution-matrix]: https://github.com/pantuza/domino-problem/blob/master/img/solution-matrix.png "Dominó solution matrix"


### Evaluation

The following image shows the time execution complexity of each implemented
algorithm.
As can be seen, the math function based one runs in a constant way and the
iterative goes exponentially as the input matrix grows.

![alt text][time-execution]
[time-execution]: https://github.com/pantuza/domino-problem/blob/master/img/time-complexity-analysis.png "Time execution complexity analysis"


### Project structure

The project has a Makefile to rule computation, plot and cleaning.
The following target rules exists:

- compute - Computes execution times for implemented algorithms
- plot    - Run GnuPlot to generate the computation analysis
- show    - Open resulted image using eog
- test    - Run tests using nose
- clean   - Removes log and image files

### Dependencies

The project uses Python 3.5 for computation, GNUPlot to generate graphs and Python Nose for tests. 

### Getting started

Run the following command to compute and plot execution analysis:

```bash
$> make clean compute plot show
```

### Contributing

We are not stringent with contributions.
Just do a *fork*, make your modifications, write tests for it and send me a
Pull Request. It will be very welcome!


### Author

Written by Gustavo Pantuza <gustavopantuza@gmail.com>
