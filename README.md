# Dominó problem

### Problem

There is a table game called [*Dominó*](https://en.wikipedia.com/domino).
This game pieces are divided in two parts.
Both parts has a number between 0 and 6.
Each pair of numbers never repeat and there is no inverse pieace
with this numbers.

Based on that, how many pieces has an odd number as a result of the sum of
its two parts.

### Description

During Python Brasil [12] in FLorianópolis I took a cab and the driver
listened me talking with my friends about computer science stuff.
Then he look at us and said: "Are you from google generation?".

We obviosly answer: "yeah, we are!" Then he said: "Let's see if you can
solve that problem...", and he described the **Dominó problem**.

### Solution


### Project structure

The project has a Makefile to rule computation, plot and cleaning.
The following target rules exist:

- compute - Computes execution times for implemented algorithms
- plot    - Run GnuPlot to generate the computation analysis
- show    - Open resulted image using eog
- test    - Run tests using nose
- clean   - Removes log and image files


### Getting started

Run the following command to compute and plot execution analysis:

```bash
$> make clean compute plot show
```

### Contributing

We are not stringent with contributions.
Just do *fork*, make your modifications, write tests for it and send me a
Pull Request. It will be very welcome!


### Author

Written by Gustavo Pantuza <gustavopantuza@gmail.com>
