# test-treeview

A test of interactive tree. The tree is generated from a custom JSON file when the button Get Tree is clicked. It may have up to three levels of data. 
We need to make an action that when each level of the tree is selected on the left a Form Layout is created and filled in with
Label   | One line text edit-non-edittable
Level_1 | Level_1_value
Level_2 | Level_2_value
Level_3 | Level_3_value
So if a level 3 was selected all above are create with Level_3_value being the value of item selected and Level_2_value being its parent's value
