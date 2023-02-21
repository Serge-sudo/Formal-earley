# Earley 

Launch:

python3 main.py

Launch tests:

py.test --cov=earley tests/

**************************************
Scan - iterates over all states in the current vertex and if current symbol is equal to the symbol which we just read, than it moves dot possition and puts this state into next vertex
Predict - pushes things from vertex into stack, and that takes items from stack one by one, if dot_val is non-terminal than it adds all rule which include dot_val into stack, and than pushes current item in "done" list.
Complete - interates over all states in current_vertex if dot_pos is last than, it pushes all states  which dot_val is our completed non-term from origin of that state  into our current state.
predict- creates S0 vertex than iterates over letters in the word, does scan, and than while vertex is changing it does Predict and Complete .
