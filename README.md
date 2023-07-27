# Earley Algorithm

To launch Earley algorithm, run the following command:

```
python3 main.py
```

To run tests, use the following command:

```
py.test --cov=earley tests/
```

The Earley algorithm consists of three main operations:

1. **Scan**: This operation iterates over all states in the current vertex and checks if the current symbol is equal to the symbol that was just read. If it is, the algorithm moves the dot position and puts this state into the next vertex.

2. **Predict**: This operation pushes items from the current vertex into a stack. It then takes items from the stack one by one. If the dot value is non-terminal, the algorithm adds all rules that include the dot value into the stack. It then pushes the current item into the "done" list.

3. **Complete**: This operation iterates over all states in the current vertex. If the dot position is at the end of the rule, the algorithm pushes all states whose dot value is the completed non-terminal from the origin of that state into our current state.

To apply the Earley algorithm, first create an S0 vertex. Then iterate over the letters in the word, perform a scan, and then while the vertex is changing, perform predict and complete operations.
