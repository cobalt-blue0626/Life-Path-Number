# Life-Path-Number

This problem aims at letting you practice using the conditionals if (and the while loop, but
not necessary), together with string slicing. You are asked to write a program that calculates the
Life Path Number of a person. The Life Path is the sum of the birth date. This number represents
who you are at birth and the native traits that you will carry with you through life. The Life Path
number can be calculated by four steps. 
(1) Reduce your birth Year to a single digit by iteratively summing up each digital, and obtain num_year. 
(2) Reduce your birth Month to a single digit by iteratively summing up each digital, and obtain num_month. 
(3) Reduce your birth Day to a single
digit by iteratively summing up each digital, and obtain num_day. 
(4) Sum up num_year ,num_month , and num_day as num_total, and reduce num_total to a single digit by iteratively summing up each digital. 
Note that in your output, the birthday is required to follow
the format yyyy/mm/dd. In other words, year is 4 digitals, month is 2 digital, and day is 2 digital.

For example, assume your birthday is 1997/12/29, your Life Path Number is

num_year: 1 + 9 + 9 + 7 = 26, 2 + 6 = 8
num_month: 1 + 2 = 3
num_day: 2 + 9 = 11, 1 + 1 = 2
num_total = num_year + num_month + num_day: 8 + 3 + 2 = 13
life_path_number = 1 + 3 = 4
