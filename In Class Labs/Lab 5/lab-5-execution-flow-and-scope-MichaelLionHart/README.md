# Module4-Lab5-ExecutionFlowAndScope

**Goals**

- Demonstrate debugging in VS Code
- Demonstrate the flow of execution
- Demonstrate variable scope

**Resources**

- link to VS Code debuggeer docs: https://code.visualstudio.com/docs/editor/debugging

**Instructions**

1. Open happyBirthday.py in VS Code
2. We want to step through the program a line at a time. To do that we need to set some "breakpoints". These are locations where the debugger will stop execution and wait for user instructions. Use the following steps to set breakpoints in this program
    1. In the edit pane for the DemoExecutionFlow.py file move the cursor to the left of 13.
    2. You will see a dark red dot appear.
    3. Click on it. The dot will become a bright red.
    4. This sets a breakpoint just before the first line of code in main()
    5. Repeat the procedure to set a breakpoint on line 4.
    6. On the left margin of VS Code, click on the "bug" icon (fourth from the top). This opens the Debug panes.
    7. Put your cursor on the bar that says WATCH.
    8. Click on the + sign and add a watch for "person" (type "person" folled by Enter). It will say "not available"
    9. Repeat for the variable "name".
3. Now start debugging. Alternatives are shown below:
    - (menu bar) Debug > Start Debugging
    - (shortcut key) F5 (NOT ctrl+F5)
4. We are going to monitor changes in the Debug panes on the left. 
    - Watch the areas for local variables, watches, and the call stack. 
    - Notice that line 13 is highlighted in the edit window. 
    - Also notice that to the left of the line is a yellow arrow indicating where execution has paused.
    - Notice that the call stack indicates execution is currently in main()
    - Notice that the person and name variables we are watching are not defined.
    - Lastly, notice the debug actions bar at the top. Pass the cursor slowly over the icons to see what each one does.
        - Continue (F5): Advance the debugger to the next breakpoint
        - Step over (F10): Use when you are on a line of code that is a function call. The action is to execute the function and go to the next line.
        - Step into (F11): Use when you are on a line of code that is a function call. Use when you want to continue stepping through the code in the function being called. Repeatedly clicking on this will move the execution one line at a time.
        - Step out (Shift+F11): Use to execute the remaining lines of the code in a function and stop at the line after the function call.
        - Restart (Ctrl+Shift+F5): Exits the current debugging session and starts a new one. Same as Stop and Start Debugging
        - Stop (Shift+F5)
5. Click on the step into icon or use F11
6. At this point the program is waiting for input in ther terminal window. Click on the terminal window and enter a name + Enter
    - Notice that name is now defined and has a value
    - Notice that name also shows up in the "locals" window. The call stack indicates that we are currently in main(), so name is a local variable in main()
7. Click on the step into icon or use F11
    - Notice the call stack shows that we are now in the sing() function
    - Notice that the person variable is defined and has a value. 
    This shows in both the local variable pane and the watch pane.
    - Also notice that the name variable is now out of scope and is not defined.
8. F11 again
    - Notice the call stack shows that we are now in the happy function.
    - Notice that there are no local variables and that the watch window shows that the name and person variables are not defined. The changes here are demonstrating the **scope** of the variables.
9. Continue stepping throught the program using F11 until it is finished.
10. Remove the current breakpoints.
11. Set a new breakpoint on line 19
12. Run the debugger (F5)
    - Notice all of the locals
    - It lists the functions and their addresses
    - It also lists built-in variables and their values.
    - Specifically notice the value for the \_\_name__ variable

**Deliverables**

- Somewhere in the middle of your debugging session take a screenshot of the VS Code window, paste it in a word doc, and save it to Canvas. The VS Code window should show:
    - the edit window with the program code
    - the Debug pane showing locals, watch variables and call stack
    - the terminal window with current output