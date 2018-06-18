Stack Tracer
============

Sublime Text package to dump stack tracebacks for all active threads; this
effectively monitors all active Python threads letting you answer the important
question: What are my Sublime Text plugins doing?

The active threads and the current tracebacks are constantly (every 5 seconds)
dumped to the file `/tmp/SublimeStackTracer.txt` for you to analyze.
