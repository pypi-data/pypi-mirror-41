
# Proper Web Framework

*Conventions over configuration*


### Requirements

- Python 3.6+


## Design principles

- "Conventions over configuration".

- No globals.
	When you need a shared object, pass it arround.

- Optimize for the 95%.
	Don't compromise the usability of the common cases to keep consistency
	with the edge cases.

- Code redability is very important.

- App-code over framework-code
	Because app code is infintely configurable without dirty hacks.

- "Everyone is an adult here".
	Run with scissors if you must.

- Greenthtreads over async
