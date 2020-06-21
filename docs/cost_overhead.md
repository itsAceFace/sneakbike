# Cost Overhead

This document will provide transparency on general costs (besides personal computing power / electricity) for Sneakbike.

- [Cost Overhead](#cost-overhead)
  - [AWS](#aws)
    - [EC2](#ec2)
  - [GoDaddy](#godaddy)
  - [Digital Ocean](#digital-ocean)
- [Approximations](#approximations)

---

---

## AWS

These are costs associated with AWS tools. They are itemized below.

### EC2

| date       | mins | viewers | Instance Type | cost (usd) |
| ---------- | ---- | ------- | ------------- | ---------- |
| 2020-06-20 | 90   | ~15     | t3a.micro     | \$0.33     |

---

---

## GoDaddy

These are costs associated with GoDaddy (domains). They are itemized below.

| date       | domain                   | duration | cost (usd) |
| ---------- | ------------------------ | -------- | ---------- |
| 2020-06-20 | sneakbikemysteryrace.com | 3 yrs    | \$48.51    |

---

---

## Digital Ocean

These are costs associated with Digital Ocean (web hosting for dynamic sites). They are itemized below.

| start date | service                | cost (usd) |
| ---------- | ---------------------- | ---------- |
| 2020-06-20 | Standard Small Droplet | \$5/mo     |

---

---

# Approximations

Here we do an approximate calculation for running Sneakbike for a year. We include the "yearly" price for the domain in this.

We assume a weekly race about the same time, cost increasing slightly to an average of \$0.50.

- Domain: \$48.51 / 3 = \$16.17
- AWS Costs: \$0.50 \* 52 = \$26.00
- Digital Ocean Costs: $5 * $12 = \$60

Giving us a total of `$102.17/yr`.
