# Programming from 0

This project is intended for use by anybody just starting up with programming or
by people interested in programming as a venture. The content is aimed at
teaching you very general knowledge about coding in general. You can consider it
as a mental exercise that every programmer will have to undergo at different
moments in their life or career.

This project uses Python as the main programming language due to its simplicity
and readability. The rules presented here would apply to any other programming
language.

NOTE: The expectation is that you have Python installed and can run code through
the IDE. [Example of setup](https://realpython.com/installing-python/)

# Why I think this is necessary

A difficult moment in the life of every programmer is to face the uncertainty
that must be dealt with every day. The biggest annoyance as a developer
generally revolves around "Everything is broken and burning and causes a lot of
stress, until it works. Then everything starts anew". Most of one's time in
front of the screen is spent reading documentations, code, comments. Only after
some time when one understands what exactly the code does and what it should be
doing can one actually make the right implementations and move forward. To add
to this problem, we are facing a very competitive business environment and it is
forcing people into cutting time and delivering faster. This inevitably poses
additional complexity. No current programmer expects a manual of some hundred
pages decribing what some code does. No manager expects a programmer in their
team to spend a couple of weeks reading and brainstorming an application.
Everything is built on the go. Decisions are made at minute intervals and code
is written like text. Everyone just wants a fast way to get started. Install it
and start poking around, and you will get the hang of it. It is the same
expectation for app users and app developers.

One might want to fight the movement, but it is indeed the best we have and if
done properly there are wonderful results to be experienced. All the best
companies that you see and follow use this approach. Now, what happens if this
process is not done properly? Code will not be documented, or documents will get
outdated and there will be no explanation to what something does. Sometimes the
person that wrote the code one is supposed to change is in another team, company
or possibly just not available at the moment. So what do you do? You try to
understand the code, read line by line and nothing makes sense. The only hope is
for some neatly written tests that show the expected usages for the code.
However, not always the tests will help with your use case. At this point one is
just left with the hope that reading the code they understand enough to start
some work. Then, is some time a short meeting will help them figure out the
general purpose and concept.

That is what a developer does in a large company. It may not seem what one can
hope for, and that is to be important and appreciated. However, in this
particular context such expectations are a bit selfish as there is no fast path
for meeting business expectations on your own. Even if you're doing just a small
job, you are helping a lot. Simple example, let's say you spent a whole day just
refactoring a class because it was difficult to understand what it does. If you
manage to reduce the code size in half. This day of work might actually be saved
in the seconds that one needs to scroll through the file and scan what is
happening. If you consider that there is also a reduction in the amount of text
needed to be read, another great win. Also, if you actually manage to make the
code even more readable, that is with better variable names, this is already
more that just the time you spent.

In general the focus of this project is to teach you just that.

* How to understand code.
* How to write understandable code.
* How to leave a trail of code usage through tests.

These 3 very vague criteria will be expanded and explored further and hopefully
will help prevent sub-optiomal coding practices. Will save time and reduce
anxiety levels.

# 0 - Always find a way to ground yourself

## What is grounding in this context?

The very basic of writing code is to have a proper moral set-up. That is one has
to be prepared to morally handle all the stress that comes with this profession.
You might not expect it yet, but you will very often feel that you do not know
enough. Sometimes very simple things will be missed. You will forget commas, or
will not name some variables properly. Your teammates will easily spot these
small errors and correct them. It is just human to feel a little setback to such
critique. After all, you could have avoided all this. Try to expect strong
feedback and be prepared morally to act upon it. Do not give in to a selfish
response as to get upset, rather make sure that the code in general is working
correctly. This is actually what will be referred as grounding yourself. Have
something in which you are very sure and rarely get it wrong, the details will
be just a small improvement over that. Also be mindful about teammates as they
will have to spend time reviewing your code and be mindful when reviewing
someone else's code. Do not just try to find errors in code because you have
been pointed out to so many shortcomings.

## How to ground oneself?

The easiest way is to make sure you understand the task. Always ask for
clarifications before making any assumptions. Even when you feel you understand
whatever you are presented with, it is not a bad practice to ask about edge
cases. This will generally come with practice and it deviates from the main
topic. Grounding will be the fundamental process on which this project is
created. We will start from very simple code. Will iterate on it to make sure we
understand pretty much everything there is to it and move further.

Again, this might look not useful as the benefits will not be obvious. They are
slow and rearely you can see them clearly. However, once you get the hang of it
you will most likely never want to not use the advices here. An analogy is
exercise. We all know that we must do some kind of exercise or sport. The
results take some time to be visible, however the best results will be felt at a
much older age. For example, at 50 - 60 years, people that regularly have been
exercising will find that going through their daily routine is much easier when
compared to people of same age that did not devote that much time to sport.

# 1 - Print statement

**A statement is any line of code. It is a command that will be executed by your
computer.** Along with this you should know that generally everything that goes
before round brackets () in programming is called a method or a function. We
will be using the name method as it is very friendly with a lot of programming
languages. However, if you interchange function and method it will not affect
greatly how people understand you.

You will see that all tutorials start with introducing you to print. This is
because you can easily see the output in the console. It creates a ground, where
you can always return whenever in need. So, if you feel confused by code or what
it does, just add some print statements to make it easier to understand. They
generally help a lot. With time, you will see that there are more powerful
tools, but for the time being let's make the most of it.

## Print all the things

Let's print something.

`print(3)` -> `3`

This is a first statement. It just basically tells the computer to print the
number 3. Not much. Next up.

`print("3")` -> `3`

Okay, so what else can it do? Printing more numbers?

`print(3, 3)` -> `3, 3`

`print(3, "4", 5.0)` -> `3, 4, 5.0`

So this method is very powerful. We can see that it accepts any number of
parameters. A parameter is what a method uses to execute. Parameters are given
to a method separated by a comma. That is, without that parameter the method
will throw an error. This is something that we will further explore.

## What are the things we would want to print

So we know that we can print everything. Why do we want to print? Well, it is
because we want to know. In the examples above we know what 3 is and printing it
does not make sense, however, we will not be using print with such trivial
examples too much.

Generally we would like to print variables. **A variable is almost anything in
the code. It is used as a storage place for whatever information you might
need.** Let's see its use.

```
x = 3
print(x)
```

These statements are the same as `print(3)` with the twist that the computer now
will know that x is 3. So whenever you will use x, the computer will replace it
with 3 when running the program. This will be very useful when you will have to
work with variables and perform operations.

## Operations with variables

Basic operations in Python are:

```
Operator - the sign that represents an operation

+ Addition	Adds values on either side of the operator
- Subtraction	Subtracts right hand operand from left hand variable
* Multiplication	Multiplies values on either side of the operator
/ Division	Divides left hand operand by right hand operator
% Modulus	Divides left hand operand by right hand operator and returns remainder
** Exponent	Performs exponential (power) calculation on operators
// Floor Division - The division of operands where the result is the quotient in which the digits after the decimal point are removed. But if one of the operands is negative, the result is floored, i.e., rounded away from zero (towards negative infinity)
```

They are not many, but more than enough. We know what + or - does so it is not
interesting. So let's try out what that modulus does. Let's ground this
knowledge. For this purpose print is of great use.

`print(3 % 5)` -> `3`
`print(13 % 5)` -> `3`
`print(6 % 5)` -> `1`

It indeed stands to its definition of being what is left (**remainder**) when we
divide 13 by 5. However, this type of division is called floor division, the
last operator in the list. From math, we know that if we add the result of
division times the number by which you divide plus the **remainder** you get the
number. So let's try it out.

```python
x = 13 // 5
print(x * 5 + 13 % 5)
```

The output is indeed 13. Now this code looks a bit weird. For example if we want
to change our numbers we would have to change them in several places. For
example if we want to change the number by which we divide (**dividend**) - 5.
We would have to change it in 3 places. Changing the **divisor** 13 will require
us to change it in 2 places. This is very inconvenient. Especially if you want
to test out some other operations with the numbers. After we figure out the
names of the numbers in the process we can do the following:

```python
divisor = 13
dividend = 5
quotient = divisor // dividend
remainder = divisor % dividend

print(quotient * dividend + remainder, "=", divisor)
```

There you go. This is the first formula we understood. We took the official
definition of modulo. We found the names of the variables in the operation and
we verified that we understood the formula by writing code. Also, by properly
naming out variables by the formula we can see very clearly how the formula
looks in code. And, it is very
clear. `quotient * dividend + remainder, "=", divisor` This looks and reads as
normal human text. Anybody looking at this, even without knowing what we are
trying to do have a clear and easy way to understand. Also, when we want to
verify other number, we just change the divisor and dividend and everything
holds.

```python
divisor = 29
dividend = 5
quotient = divisor // dividend
remainder = divisor % dividend

print(quotient * dividend + remainder, "=", divisor)
```

This example still shows a correct expression `29 = 29`. Now, let's see if you
can easily spot a mistake with the code above.

```python
divisor = 29
dividend = 5
quotient = divisor // dividend
remainder = divisor % dividend

print(quotient * divisor + remainder, "=", divisor)
```

Why is this code showing `149 = 29`?

Now let's see if you can easily find the same mistake in the code below.

```python
x = 29
y = 5
z = x // y
w = x % y

print(z * x + w, "=", x)
```

This is why you should name your variables appropriately. Because anybody that
looks over the code needs to understand what it does. Now what happens when you
start changing things around?

```python
y = 5
x = 29
w = x % y
z = y // x

print(y * w + z, "=", x)
```

Can you easily make this code work? Is it clear what the code is trying to
achieve? What about below code?

```python
print(29 // 5 * 5 + 29 % 5, "=", 29)
```

It is the same formula that we wanted to check and the same variables. But you
have no clue what those numbers represent. It is just a bunch of operations.

### Conclusion

We have looked at print method and what it does. We've seen how it is useful 
when writing and validating code. We've also taken a small dive into why you need
to name your variables correctly and follow the official definitions of the
things you operate with. In our case we used a simple division, but it can be
anything. We'll further explore more sophisticated examples. However, we'll do
so slowly, again, with:

* a great emphasis on printing and understanding what the code does
* naming the variables properly to align with standard definitions

### Definitions

**method** - usually anything before round brackets - (). It is some code already
written that the computer knows about. We will be also writing methods further. Example `print()`

**parameter** - what a method needs to actually work. Without the right parameters
methods will throw errors or not work properly. Prameters are given into methods 
separated by commas. Example `print(3, 5)` or print `print(5, 7, "3")`

**variable** - a name we will use for any information. We used variables for
 numbers that represented **divisor** or **dividend**, but they can be much more.
we will explore them further as the material gets more complicated. It is very
important to name your variables correctly to show what they represent. The computer,
however, does not care what the name of the variable is.

**operand** - operands are symbols that represent operations. We used operands
to make operations with numbers that we stored in variables.