# Synacor-Challenge

This is my work-in-progress implementation of the <a href="https://challenge.synacor.com/">Synacor Challenge</a>. Information about the challenge is available at that link; the necessary files are all in this repo.

The challenge begins with the implementation of a virtual machine for which an architecture spec is provided. The initial goal is for the VM to successfully be able to read an included .bin file. Then it unfolds with a number of associated challenges accessible once the VM is functional. I won't go into detail here and spoil it, but my code <b>will</b> contain spoilers.

As of now, I've implemented the VM completely and solved the next few challenges; in total, I've submitted 6/8 codes. I'll update this repo if and when I finish #s 7 and 8.

If you should want to run the program for whatever reason, you'll need arch-spec, challenge.bin (the binary file to decode), and vm.py. The other file, coins.py, is just a helper module to solve a problem from later in the challenge.
