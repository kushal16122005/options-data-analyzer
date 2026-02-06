# Options Data Analyzer

A beginner-friendly Python project that analyzes an option chain to
identify the highest implied volatility (IV), calculate the Put-Call
Ratio (PCR), and determine overall market bias.

This project is built using **basic Python concepts only** and focuses
on translating options market logic into clean, readable code.

---

## 📌 Project Objective

- Analyze option chain data
- Identify the option with the highest IV
- Calculate Put-Call Ratio (PCR)
- Determine market sentiment (Bullish / Bearish / Neutral)

---

## 🧠 Concepts Used

- Python lists and dictionaries
- For loops and conditionals
- Functions and modular code
- Basic financial metrics (IV, OI, PCR)
- Clean code structure (`main()` pattern)

---

## 📊 Sample Data Structure

```python
{
    "strike": 25200,
    "type": "CE",
    "oi": 120000,
    "iv": 18.2
}
