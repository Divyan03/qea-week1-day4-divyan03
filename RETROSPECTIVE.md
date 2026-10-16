# Pair Retrospective: test_utils library

Copy this file to the ROOT of your shared repo as `RETROSPECTIVE.md`, fill in EVERY section
(replace each --), and commit it on your shared branch. Write it together:
one person types, the other dictates, then swap for the last two sections.

- Pair members: Divyan Varatharaj, Fahad Hussain
- Repository / branch / PR link: https://github.com/Divyan03/qea-week1-day4-divyan03/tree/feature/test-utils
- Date and total time spent: October 16, 2026. Time Spent: 2 hours 10 minutes

## 1. Role-swap log

Fill one row per 30-minute block (add rows if you swapped more often).

| Block | Minutes | Driver | Navigator | What we built | Last commit hash (short) |

| 1 | 0-30 | Fahad  | Divyan | Block 1 and is_valid_email from Block 2 | 6284eb9 |
| 2 | 30-60 | Divyan | Fahad | Block 2, generate_username and generate_usernames from Block 3 | 7139b09 |
| 3 | 60-90 | Fahad  | Divyan  | Completed generate_password and generate_test_id | a537db3 |
| 4 | 90-120 | Divyan | Fahad | Complete block 3 and start block 4 | e8ee37b |
| 5 | 120-150 | Fahad  | Divyan | Completed Block 4 and started Block 5 | 7524486 |
| 6 | 120-130 | Divyan  | Fahad | Complete demo_report.py | 3d32bd6 |

## 2. What went well in how we worked together?
The navigator and driver were able to brainstorm very effectively. The navigator was also able to catch mistakes the driver initially does not notice. For example, driver used syntax to get object attribute to get the value of a dictionary key. Navigator would notice and tell them to correct it.

## 3. What was difficult?
- Technically: Syntax errors from using numerous different functions and parameters across different files and parts of the codebase.
- As a team (communication, pace, disagreement, git hand-offs): Pace was fast, keeping organized and on the same page with existing codebase. 

## 4. What did each of us learn from the other?
- Fahad learned from Divyan: How to use the random library properly.
- Divyan learned from Fahad: When to use the defaultdict vs normal dictionary.

## 5. Our code
- The function we are proudest of, and why: The function we are most proud of is build_demo_report. This is due to the variety of different functions we had to utilize.
- The function that most needs improvement, and how: The function that needs the most improvement is the is_strong_password due to unnecessary checks.
- One bug we hit and how we found it (error message, what we tried, the fix): TypeError: unsupported operand type(s) for +: 'function' and 'int'. This bug was from decorators.py. The fix was that we were not returning correctly. We changed the return wrapper(func) to return wrapper

## 6. Git collaboration
- Did every swap follow commit, push, pull? What went wrong when we skipped a step? Yes, we stayed on track with the git process. Committed with the co-author reference, pushed, pulled, and ran check_exercise.py on the new driver to confirm everything transferred over correctly.
- Did we get a merge conflict? How did we resolve it (or why not)? Nope, we didn't get any.
- Output of `git shortlog -sne` (paste): 
     6  Divyan03 <111556193+Divyan03@users.noreply.github.com>
     4  FahadH31 <129327022+FahadH31@users.noreply.github.com> 

## 7. Next time
- Two things we would do differently: 1. switch over in more natural blocks rather than set time 2.Add the <> when referencing each other's emails in the commit message so it properly shows the co-authoring of all the commits. 
- Self-rating, 1 (poor) to 5 (excellent): communication 5, keeping to the swap timer 5, understanding every line 5

## 8. Final check
Paste the last lines of `python3 check_exercise.py` (the "x/y checks passed" line): 20/20 checks passed
