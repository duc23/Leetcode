class Solution:
    def isValid(self, s: str) -> bool:
        # build stack as empty list
        stack = []
        # dictionary to match the different parenthesis type with its open parenthesis
        Map = {")":"(", "]":"[", "}":"{"}
        # for every parenthesis in our string
        for parenthesis in s:
            # if it's an open parenthesis, add to stack
            if parenthesis in Map.values():
                stack.append(parenthesis)
            # else it's a closed bracket, and make sure the type are the same at the top of the stack. If so, pop it off the stack since they match.
            elif stack and Map[parenthesis] == stack[-1]:
                stack.pop()
            # if there's no stack and they dont match, it's invalid
            else: 
                return False
        # after the loop, the stack should be empty 
        return stack == []