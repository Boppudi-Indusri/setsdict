# Create a list of numbers (with duplicates)
numbers = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 1]

# Generate a set of unique numbers
unique_numbers = set(numbers)

print("Original Set:", unique_numbers)

# Add new elements to the set
unique_numbers.add(9)
unique_numbers.add(10)

print("After Adding Elements:", unique_numbers)

# Remove existing elements from the set
unique_numbers.remove(2)  # Removes 2
unique_numbers.discard(5) # Removes 5 (no error if not found)

print("After Removing Elements:", unique_numbers)

# Create another set
another_set = {4, 6, 8, 10, 12, 14}

print("Another Set:", another_set)

# Union operation
union_set = unique_numbers.union(another_set)
print("Union:", union_set)

# Intersection operation
intersection_set = unique_numbers.intersection(another_set)
print("Intersection:", intersection_set)

# Difference operation
difference_set = unique_numbers.difference(another_set)
print("Difference (unique_numbers - another_set):", difference_set)



# Dictionary to store books
# Format: {title: {"author": author_name, "genre": genre_name}}

books = {
    "The Alchemist": {"author": "Paulo Coelho", "genre": "Fiction"},
    "Python Crash Course": {"author": "Eric Matthes", "genre": "Programming"},
    "Harry Potter": {"author": "J.K. Rowling", "genre": "Fantasy"}
}

# Function to add a new book
def add_book(title, author, genre):
    books[title] = {"author": author, "genre": genre}
    print(f"Book '{title}' added successfully.")

# Function to remove a book
def remove_book(title):
    if title in books:
        del books[title]
        print(f"Book '{title}' removed successfully.")
    else:
        print(f"Book '{title}' not found.")

# Function to search books
def search_books(keyword):
    found = False
    print(f"\nSearch Results for '{keyword}':")
    
    for title, details in books.items():
        if (keyword.lower() in title.lower() or
            keyword.lower() in details["author"].lower() or
            keyword.lower() in details["genre"].lower()):
            
            print(f"Title: {title}, Author: {details['author']}, Genre: {details['genre']}")
            found = True

    if not found:
        print("No matching books found.")

# Function to display books sorted by title or author
def display_books(sort_by="title"):
    print(f"\nBooks Sorted by {sort_by.capitalize()}:")

    if sort_by.lower() == "title":
        sorted_books = sorted(books.items())
    elif sort_by.lower() == "author":
        sorted_books = sorted(books.items(), key=lambda item: item[1]["author"])
    else:
        print("Invalid sort option.")
        return

    for title, details in sorted_books:
        print(f"Title: {title}, Author: {details['author']}, Genre: {details['genre']}")

# -------------------------
# Testing the implementation
# -------------------------

print("Initial Book Collection:")
display_books()

# Add new books
add_book("The Hobbit", "J.R.R. Tolkien", "Fantasy")
add_book("Clean Code", "Robert C. Martin", "Programming")

# Display after adding
display_books()

# Remove a book
remove_book("Harry Potter")

# Display after removing
display_books()

# Search by title
search_books("Hobbit")

# Search by author
search_books("Paulo")

# Search by genre
search_books("Programming")

# Display sorted by author
display_books("author")
