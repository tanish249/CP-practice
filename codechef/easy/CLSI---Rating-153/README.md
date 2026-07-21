# CLSI - Rating 153

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Conquer the Fest!!

 **IIIT Pune**  is celebrating its annual fest with a lineup of exciting events. And among the technical events  **InfInITy**  stands out as a prestigious coding contest, known for its challenging coding problems.

This year, the contest includes a difficult problem.
The problem has a  *difficulty level*  of $B$, and a participant needs an IQ of  **at least**  $10\times B$ to solve it.

You have an IQ of $N$. Can you take on the challenge and solve this tough problem, or is it too hard to crack?

### Input Format
- The first and only line of input will contain two space-separated integers $N$ and $B$ — your IQ, and the difficulty level of the problem you are trying to solve.
### Output Format

Output on a single line the answer: `"YES"` (without quotes) if you can solve the problem, and `"NO"` (without quotes) otherwise.

Each character of the output may be printed in either uppercase or lowercase, i.e. if the answer is `No`, then all of `NO`, `No`, `nO`, and `no` will be accepted.

### Constraints
- $1 \leq N \leq 500$
- $1 \leq B \leq 100$
### Sample 1:
Input
Output

```
120 12

```

```
YES
```

### Explanation:

The problem requires $12 \times 10 = 120$ IQ, which you have exactly, so you can solve it.

### Sample 2:
Input
Output

```
40 5

```

```
NO
```

### Explanation:

The problem requires $5 \times 10 = 50$ IQ, but you only have $40$, which is insufficient.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-21T05:42:09.526Z  

```py
a,b=map(int,input().split())
h=b*10
if a>=h:
    print("YES")
else:
    print("NO")
```

---

[View on CodeChef](https://www.codechef.com/problems/CLSI)