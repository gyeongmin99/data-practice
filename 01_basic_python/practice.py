# Practice 01: Thinking with data (no execution yet)

# 1. Imagine a small dataset
# Example: number of books read per month
books_read = [2, 0, 1, 3, 4, 1, 0, 2]

# 2. Questions we might ask
# - How many months are there?
# - What is the total number of books read?
# - What is the average per month?
# - Are there months with no reading?

# 3. We are NOT solving yet.
# We are Learning to think in questions.

# Basic calculations
total_books = sum(books_read)
number_of_months = len(books_read)
average_books = total_books / number_of_months

print("Total books read:", total_books)
print("Number of months:", number_of_months)
print("Average per month:", average_books)


min_books = min(books_read)
max_books = max(books_read)
zero_months = books_read.count(0)

print("Minimum books in a month:", min_books)
print("Maximum books in a month:", max_books)
print("Months with zero books:", zero_months)
