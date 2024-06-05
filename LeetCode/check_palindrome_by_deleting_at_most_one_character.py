"""
This function to determince if palindrome can be formed by removing one character.
"""


# This method uses two pointers to check if the string is a palindrome.
def can_form_palindrome_by_removing_one_char(s: str) -> int:
    # Helper function to check if a substring is a palindrome
    def is_palindrome_range(s, left, right):
        # Check if the substring is a palindrome
        while left < right:
            if s[left] != s[right]:
                return False
            # Move the pointers to check the next characters
            left += 1
            right -= 1
        return True

    left, right = 0, len(s) - 1
    # Move the pointers to find the first mismatch
    while left < right:
        if s[left] != s[right]:
            # Try skipping the left character or the right character
            if is_palindrome_range(s, left + 1, right):
                return left
            # Try skipping the right character or the left character
            elif is_palindrome_range(s, left, right - 1):
                return right
            else:
                return -1
        left += 1
        right -= 1

    return -1  # The string is already a palindrome


if __name__ == "__main__":
    # Example usage
    input_string = "abca"
    index_to_remove = can_form_palindrome_by_removing_one_char(input_string)
    if index_to_remove != -1:
        print(f"Remove character at index {index_to_remove} to form a palindrome.")
    else:
        print("No single character removal can form a palindrome.")
