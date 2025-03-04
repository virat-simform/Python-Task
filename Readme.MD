# Python Practical Assignment

This repository contains solutions for python assignments.

## 1. GCD of Two Numbers (Word Input)

Computes the Greatest Common Divisor (GCD) of two numbers given in word format.

### Constraints:
- No `for` loops allowed.
- Input is in words (e.g., `onetwo` = `12`).
- Words range from `zero` to `nine`.
- No inbuilt math functions like `max`, `min`, etc.

### Example:
**Input:**
```
onezero
twozero
```
**Output:**
```
onezero
```

---

## 2. Generate Well-Formed Parentheses

Generates all valid combinations of `n` pairs of parentheses.

### Constraints:
- `1 <= n <= 8`

### Example:
**Input:**
```
n = 3
```
**Output:**
```
["((()))", "(()())", "(())()", "()(())", "()()()"]
```

---

## 3. Group Anagrams

Groups anagrams from an array of strings.

### Constraints:
- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- Strings consist of lowercase English letters.

### Example:
**Input:**
```
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
```
**Output:**
```
[["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
```