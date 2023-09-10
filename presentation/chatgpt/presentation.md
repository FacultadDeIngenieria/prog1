class: center, middle, inverse

## What is ChatGPT?
---

## Agenda
- "Traditional" software vs "Machine learning" software
- What is ChatGPT?
- Why does it work?
- What to consider when using it

## Important Links:
- https://karpathy.medium.com/software-2-0-a64152b37c35
- https://writings.stephenwolfram.com/2023/02/what-is-chatgpt-doing-and-why-does-it-work/

---
## "Traditional" software

- The **traditional way of doing software** is written in languages, such as Python, Java, C++, etc. 
- A programmer writes explicit instructions to the computer
- With each line of code, the programmer specifies a point in the program and determines the expected behaviour.

---
## "Software 2.0"

- Is written in a higher abstraction level, non-human friendly language, such as weights of a neural network.
- No human is directly involved in writing that code.
- A programmer specifies a goal on the behaviour of a desirable program, writes a "skeleton" of the code and use computational resources for a program that works.

![Neural Network]({{site.baseurl}}/presentation/chatgpt/neural-net.png)

---
## Software 2.0 Source-code

- Consists of: **a dataset** that defines the desired behaviour and **a neural net architecture** that gives the rough skeleton of the code, but with many details (weights) to be filled in.
- The process of **training** the neural net, compiles the dataset into the binary final neural network.
- Most of the "software development" work is around curating, growing, massaging and cleaning labeled datasets.
- The 2.0 programmers (data labelers) edit and grow the datasets, while a few 1.0 programmers maintain and iterate on the surrounding training code infrastructure, analytics, visualizations and labeling interfaces.
- It turns out that a large portion of real-world problems have the property that it is significantly easier to collect the data (or more generally, identify a desirable behavior) than to explicitly write the program.

---
## Uses of "2.0 Software"

- Visual Recognition, Speach recognition, Speech Synthesis, Machine Translation, Games, Databases.
- This type of software has many benefits:
  - Computationally homogeneous: it performs primitive operations, like matrix multiplication and simple mathematical functions.
  - Simple to bake into silicon, portable and agile
  - Constant running and memory time

---
## WTF is ChatGPT?
- Everything from this point forward was obtained from this link: https://writings.stephenwolfram.com/2023/02/what-is-chatgpt-doing-and-why-does-it-work/ 
- It is better explained and detailed that what I can explain, written by [Stephen Wolphram](https://es.wikipedia.org/wiki/Stephen_Wolfram)

What ChatGPT is always fundamentally trying to do is to produce a “reasonable continuation” of whatever text it’s got so far, where by “reasonable” we mean “what one might expect someone to write after seeing what people have written on billions of webpages".

---
## So … What Is ChatGPT Doing, and Why Does It Work?

- The basic concept of ChatGPT is at some level rather simple. Start from a huge sample of human-created text from the web, books, etc. Then train a neural net to generate text that’s “like this”. And in particular, make it able to start from a “prompt” and then continue with text that’s “like what it’s been trained with”.

---
## Academia is a bit behind some machine learning logic

Imagine scanning billions of pages of human-written text (say on the web and in digitized books) and finding all instances of this text—then seeing what word comes next what fraction of the time. But the end result is that it produces a ranked list of words that might follow, together with “probabilities”:

![Ability to]({{site.baseurl}}/presentation/chatgpt/ability-to.png)

If we always pick the highest-ranked word, we’ll typically get a very “flat” essay, that never seems to “show any creativity” (and even sometimes repeats word for word). But if sometimes (at random) we pick lower-ranked words, we get a “more interesting” essay.

there’s a particular so-called “temperature” parameter that determines how often lower-ranked words will be used, and for essay generation, it turns out that a “temperature” of 0.8 seems best. (It’s worth emphasizing that there’s no “theory” being used here; it’s just a matter of what’s been found to work in practice.).

---
## Now if everyone wants, we jump into the article

https://writings.stephenwolfram.com/2023/02/what-is-chatgpt-doing-and-why-does-it-work/#where-do-the-probabilities-come-from?

(Wolfram alpha's demo environment has less features that it used to and making the queries in the article require a paid subscription)

--- 
## Prompt Engineering

- Process of structuring text that can be interpreted and understood by a generative AI model.

https://prompts.chat/
