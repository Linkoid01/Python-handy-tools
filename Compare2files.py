#!/usr/bin/env python3
# title             Compare2files.py
# description:      Use this script to search through 2 text files for duplicate entries such as email address lists
# author:           Silviu Siladi
# date              2024-05-31
# usage             Remember to adjust file1/2.txt

def read_users_from_file(filename):
    with open(filename, 'r') as file:
        users = file.read().splitlines()
    return users

def find_duplicates(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    duplicates = set1.intersection(set2)
    return duplicates

def main():
    list1 = read_users_from_file('file1.txt')
    list2 = read_users_from_file('file2.txt')
    
    duplicates = find_duplicates(list1, list2)
    
    if duplicates:
        print("Duplicate users found:")
        for user in duplicates:
            print(user)
    else:
        print("No duplicate users found.")

if __name__ == "__main__":
    main()
