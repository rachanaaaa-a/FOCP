#question1
def sort_string(string):
    unique_letters = set(char.lower() for char in string if char.isalpha())
    return sorted(unique_letters)

print(sort_string("Hello, Goodmorning!"))
print(sort_string("78294"))

#question2
def sort_string(string):
    unique_letters = set(char.lower() for char in string if char.isalpha())
    return sorted(unique_letters)

atleast_one_letter= lambda word1,word2: sorted(set(sort_string(word1)) | set(sort_string(word2)))

letter_both_word = lambda word1, word2: sorted(set(sort_string(word1)) & set(sort_string(word2)))


letter_either_not_both = lambda word1, word2: sorted(set(sort_string(word1)) ^ set(sort_string(word2)))

print(atleast_one_letter("apple", "mango"))
print(letter_both_word("pineapple", "pomegranate"))
print(letter_either_not_both("strawberry", "litchi")) 

#question3
def manage_country_capitals():
    country_capitals = {}

    while True:
        country = input("Enter the name of a country (or type 'exit' to quit): ").strip()
        
        if country.lower() == 'exit':
            print("Exiting the program.")
            break
        country_lower = country.lower()

        if country_lower in country_capitals:
            print(f"The capital of {country} is {country_capitals[country_lower]}.")
        else:
            capital = input(f"Enter the capital city of {country}: ").strip()
            country_capitals[country_lower] = capital
            print(f"Thank you! The capital of {country} has been recorded as {capital}.")
            
manage_country_capitals()


#question4
def report_most_common_letters(message):
    letters = [char.lower() for char in message if char.isalpha()]
    letter_counts = {}
    for letter in letters:
        letter_counts[letter] = letter_counts.get(letter, 0) + 1
        
    sorted_counts = sorted(letter_counts.items(), key=lambda x: (-x[1], x[0]))
    return sorted_counts[:6]


print(report_most_common_letters("This message will report most common letters"))



