# my_user= input("Enter your name: ")
# print("Hi my name is",my_user)




# def is_palindrome(strings):
#     if strings == "radar":
#         print("True")
#     elif strings == "Hello":
#         print("false")
#     else:
#         print("fails")
# is_palindrome("radar")




# def is_prime(n):
    
#     if n % 2==1:
#         return("True")
#     elif n  % 2==0:
#         return("False") 
#     else:
#         return("fails")
# print(is_prime())

def count_word(numbers):
    word_list = {}
    word_count = numbers.split()
    for word in word_count:
        if word in word_list:
            word_list[word] +=1
        else:
            word_list[word] =1
    return word_list
        
print(count_word("hello hello me and you you"))

   


        





