# Start Here: 12-month SDE2 -> AI/ML Engineer plan

Rules: 30 min on a bad day, ~1 h normal, 2-3 h weekends. A 30-min day counts. Never skip two days in a row.
Log every session in daily_log.csv (1 line). Track jobs in job_tracker.csv.

## Weeks 1-4 (do these in order)
**Week 1: Baseline**
- Day 1: Make a GitHub repo "ml-prep". Copy the CSV trackers in. Pick a fixed daily time slot.
- Day 2-3: Add 5 Bangalore postings to job_tracker.csv (ML Engineer, AI Engineer, SDE-AI, ML Platform; 2-5 yrs). Note must-have skills.
- Day 4: Rate yourself 1-5: DSA, system design, PyTorch, MLOps, LLM apps. Write it in the repo README.
- Day 5-7: DSA problems 1-3 (list below). Read the first 3 chapters of a system design primer.
**Week 2**
- Finish 15 postings total. Count the top 10 repeated skills. This becomes your priority list.
- DSA 4-6. Set up Python env, pytest, git hooks (project1 scaffold has a Makefile).
- Implement logistic regression from scratch in numpy (ml-from-scratch list).
**Week 3**
- DSA 7-9. System design: caching + queues. Draw one design (URL shortener) on paper, 40 min.
- Run the Project 1 scaffold: `make setup && make test`.
**Week 4**
- DSA 10-12. ML: implement k-means. Review all missed problems.
- Month-1 review: what slipped? Adjust the schedule, not the goal.

## DSA list (3 per week, mediums; redo misses a week later)
1 Two Sum; 2 Valid Anagram; 3 Group Anagrams; 4 Top K Frequent Elements; 5 Product of Array Except Self; 6 3Sum;
7 Container With Most Water; 8 Best Time to Buy and Sell Stock; 9 Longest Substring Without Repeating Characters;
10 Valid Parentheses; 11 Daily Temperatures; 12 Binary Search; 13 Search in Rotated Sorted Array; 14 Koko Eating Bananas;
15 Merge Intervals; 16 Insert Interval; 17 Maximum Depth of Binary Tree; 18 Level Order Traversal; 19 Validate BST;
20 Lowest Common Ancestor of a BST; 21 Number of Islands; 22 Clone Graph; 23 Course Schedule; 24 Kth Largest Element;
25 Merge k Sorted Lists; 26 Climbing Stairs; 27 House Robber; 28 Coin Change; 29 Longest Increasing Subsequence;
30 Word Break; 31 LRU Cache; 32 Implement Trie; 33 Top K Frequent Words; 34 Rotting Oranges; 35 Subsets; 36 Combination Sum.

## System design topics (1 per week, then mixed)
caching, queues/streams, SQL vs NoSQL and indexes, replication, sharding, consistency, rate limiting, API design,
load balancing, search/retrieval systems, then ML system design (feature store, batch vs online serving, monitoring).

## ML from scratch (numpy)
logistic regression, k-means, decision tree, random forest, a tiny neural net with backprop, softmax + cross-entropy.

## Resources (from my general knowledge; verify they are current)
- DSA: NeetCode 150 / Blind 75 lists.
- System design: "Designing Data-Intensive Applications" (Kleppmann).
- ML systems: "Designing Machine Learning Systems" (Chip Huyen); Made With ML.
- Deep learning/LLMs: Karpathy "Neural Networks: Zero to Hero"; Hugging Face course; fast.ai.
- Careers/pay: Levels.fyi company pages (check base vs total).

## When you fall behind
Do the 30-minute menu: one problem, or one design sketch, or 20 lines on the project. Then continue next day. Don't "catch up" with a marathon.
