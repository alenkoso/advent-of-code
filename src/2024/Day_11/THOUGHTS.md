# Plutonian Pebbles: A Tale of Numbers Getting Out of Hand

## Where I Got Stuck

My first attempt at solving this was pretty straightforward - just simulate exactly what the puzzle describes. Take the stones, apply the rules, and keep track of all the numbers. Simple, right?

Well... not quite. I ran into a classic case of "exponential growth will ruin your day". The numbers kept getting bigger and bigger, and worse yet, many of them were splitting into two stones. So not only were my numbers growing, but the *amount* of numbers was growing too!

I tried running it for 75 blinks and... Ctrl+C had to come to the rescue. The program was drowning in huge numbers and an ever-expanding list of stones.

## The Aha Moment

Then I had a realization: *I don't need to track each individual stone*. What really matters is how many of each number I have.

Think about it:
- If I have three zeros, they'll all become ones
- If I have five 10s, they'll all split into the same numbers (1 and 0)
- The transformation rules are deterministic - same input always gives same output

So instead of keeping a list like:
```python
stones = [0, 0, 0, 10, 10, 10, 10, 10]
```

I can keep a count like:
```python
counts = {0: 3, 10: 5}
```

Much more efficient! And when these transform:
```python
new_counts = {1: 3, 1: 5, 0: 5}  # From the zeros becoming ones and the tens splitting
```

## Why This Works Better

1. **Memory**: Instead of storing every single stone, I just store unique numbers and their counts. Way less memory!

2. **Speed**: I only need to transform each unique number once, then multiply the result by how many of that number I had.

3. **No Huge Lists**: Even if I end up with millions of stones, my dictionary of counts stays manageable.

The caching (`@lru_cache`) on the transformation function is just icing on the cake - if I see the same number again, I don't even need to recalculate its transformation.

## The Lesson

Sometimes the best optimization isn't about making your code faster - it's about finding a completely different way to represent your data. In this case, switching from "what are all my stones?" to "how many of each stone do I have?" made all the difference.

Also, when you see numbers growing and lists expanding rapidly... that's usually a sign that there might be a more clever way to tackle the problem!