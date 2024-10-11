# SSH
_SSH_ (_SpreadSHeet_) is an API for handling a basic spreadsheet. The spreadsheet follows _Excel_'s conventions. The spreadsheet implements three operations: _set_, _get_, and _evaluate_. The _set_ and _get_ operations assign and return the value of a cell, respectively. The _evaluate_ operation takes the content of a cell and returns the result of its evaluation (e.g., a cell containing "=1+1" evaluates to 2). 

You do not need to know more so far. The _User Stories_ section will provide further details.

## Instructions for You
* FORK this project and make sure your forked repository is PUBLIC. Then, IMPORT the forked project into PyCharm.
* You are asked to develop _SSH_ by following TDD with the support of **GAI4-TDD**.
* You DO NOT need to develop a GUI.
* You CANNOT change the signature of the provided methods, move the provided methods to other classes, or change the name of the provided classes. However, you CAN add fields, methods (e.g., methods called by the provided methods), or even classes (including other test classes), as long as you comply with the provided API.
* You CAN use the internet to consult Python APIs or QA sites (e.g., StackOverflow).
* You CANNOT use AI tools except for GAI4-TDD.
* You CANNOT interact with your colleagues. Work alone and do your best!
* The _SSH_ requirements are divided into a set of USER STORIES, which serve as a to-do list (see the _User Stories_ section).
* You should be able to incrementally develop _SSH_ without an upfront comprehension of all its requirements. DO NOT read ahead and handle the requirements (specified in the user stories) one at a time in the provided order. Develop _SSH_ by starting from the first story's requirement. When a story is IMPLEMENTED, move on to the NEXT one. A story is implemented when you are confident that your program correctly implements the functionality stipulated by the story's requirement. This implies that all your test cases for that story and all the test cases for the previous stories pass. You may need to review your program as you progress toward more advanced requirements.
* Each time you end a GREEN or REFACTOR phase, COMMIT.
* At the end of the task, PUSH your forked project.

## API Usage
Take some minutes to understand, in broad terms, how the API works. If you do not fully understand the API, do not worry because more details will be given later in the _User Stories_ section. A typical API usage follows.

```python
# Initialize an empty spreadsheet.
spreadsheet = SpreadSheet()
# Set two cells.
spreadsheet.set('A1', '=B1')
spreadsheet.set('B1', '42')
# Get the value of a given cell (e.g., the value of 'A1' is '=B1').
value = spreadsheet.get('A1')
# Evaluate a given cell (e.g., the evaluation of 'A1' is '42').
result = spreadsheet.evaluate('A1')
```

See the provided source files to improve your understanding of the API before starting to implement the user stories. 

## User Stories
Remember to read and implement the user stories once at a time (in the provided order). Therefore, do not read the next user story, if the current one is not implemented yet.

### User Story 1 -- TBW
