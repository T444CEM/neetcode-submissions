def remove_fourth_character(word: str) -> str:
    before_fourth = word[:3]
    after_fourth = word[4:]

    new = before_fourth + after_fourth

    return new

# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
