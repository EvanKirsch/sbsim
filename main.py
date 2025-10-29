#!/usr/bin/env python3

from book import *

my_baseline = Baseline_Book()
my_baseline.generate_book(2)
print(my_baseline.odds)

my_books = []
for i in range(5):
  my_book = Book(my_baseline)
  my_books.append(my_book)
  print(my_book)
