# P1169 - Rating 177

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Entry Check

Chef wants to visit a fair, but there is an age restriction for entry. A person can attend the fair if their age is  **greater than or equal**  to $10$ years.

You are given Chef's age, represented by the integer $X$. Your task is to determine whether Chef is eligible to attend the fair or not.

- If Chef's age is greater than or equal to 10, print "YES".
- Otherwise, print "NO".
### Input Format

A single integer $X$, representing Chef's age.

### Output Format

Print `YES` if Chef is eligible to attend the fair, otherwise print `NO`.

You may print each character of the string in uppercase or lowercase (for example, the strings `YES`, `yEs`, `yes`, and `yeS` will all be treated as identical).

### Constraints
- $1 \leq X \leq 20$
### Sample 1:
Input
Output

```
10
```

```
YES
```

### Explanation:

Since Chef is $10$ years old, which is the minimum age required to attend the fair, he can attend the fair.

### Sample 2:
Input
Output

```
9
```

```
NO
```

### Explanation:

Since Chef is $9$ years old, which is below the minimum age required to attend the fair, he cannot attend the fair.

### Sample 3:
Input
Output

```
11
```

```
YES
```

### Explanation:

Since Chef is $11$ years old, which is above the minimum age required to attend the fair, he can attend the fair.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-23T12:56:35.020Z  

```py
a=int(input())
if a>=10:
    print("YES")
else:
    print("NO")
```

---

[View on CodeChef](https://www.codechef.com/problems/P1169)