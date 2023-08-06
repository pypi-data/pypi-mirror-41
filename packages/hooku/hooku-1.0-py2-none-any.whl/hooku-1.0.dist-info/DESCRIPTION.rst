The package contains a simple function that fetches the note that has been pasted into a website called primapad.com.

Step 1: Create a new note at http://primapad.com/<some_unique_file_name>
Step 2:	To fetch the note whenever you want using python, follow the code,

import hooku
x = hooku.get('<your_unique_file_name>') //Fetches the note pasted in the url in text format
print(x) //Prints the note pasted into the url.

Untold_Fact: The package name is inspired from the Vadachennai(2018) movie character Rajan, who's primary job is "Hooku adikiradhu".


