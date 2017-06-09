# tsp
## Project 3 - Traveling Salesman

#### Make sure these files are in the same directory:
- tsp.py
- tsp_algos.py
- .txt files to be tested

#### To run the program:

Usage: python mcc.py { nn || rnn || 2opt } { filename.txt }
- For example, to run rnn algorithms on tsp_example_1.txt:
	- run the command: 'python tsp.py rnn tsp_example_1.txt'
- This will create a new .tour solution in the current directory each time

The second command line option refers to one of three algorithms that were implemented
- 'nn' is the nearest neighbor greedy algorithm option
- 'rnn' is the repeated nearest neighbor greedy algorithm option
- '2opt' is the 2-opt neighbor option

To run the under 3 minutes competition problems:
- run the commands in the main directory:
  - 'python tsp.py nn test-input-1.txt'
  - 'python tsp.py nn test-input-2.txt'
  - 'python tsp.py nn test-input-3.txt'
  - 'python tsp.py nn test-input-4.txt'
  - 'python tsp.py nn test-input-5.txt'
  - 'python tsp.py nn test-input-6.txt'
  - 'python tsp.py nn test-input-7.txt'

#### Solutions
Our solutions are found in the /results folder and each folder includes tsp-verifier.py and TSPAllVisited.py for verification
There are 3 sets of results:
 - one set for the example problems found in the /results/examples/ folder
 - one set for the unlimited competition problems found in the /results/comp-unlimited/ folder
 - one set for the under 3 minutes competition problems found in the /results/comp-under-3/ folder
