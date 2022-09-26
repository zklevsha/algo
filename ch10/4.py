"Write a recursive function that prints all the numbers (and just numbers)."

array = [1,
         2,
         3,
         [4, 5, 6],
         7,
         [8,
          [9, 10, 11,
           [12, 13, 14]
           ]
          ],
         [15, 16, 17, 18, 19,
             [20, 21, 22,
              [23, 24, 25,
               [26, 27, 29]
               ], 30, 31
              ], 32
          ], 33
         ]


def print_numbers(array):
    for a in array:
        if type(a) == list:
            print_numbers(a)
        if type(a) == int:
            print(a)


if __name__ == "__main__":
    print_numbers(array)
