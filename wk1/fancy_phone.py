"""Use the the `input()` builtin function.

Here is an example of the program's expected output:
```
> Please enter an all digits phone number. >> 5035551234

"""


def fancy_phone():

    input_data = str(input('Please enter your phone number without spaces>>  '))
    cleaner = input_data.replace('-', '')       # data cleaning that eliminates the dash if user ignores directions.

    three1 = ''.join(cleaner)[0:3]+'-'
    three2 = ''.join(cleaner)[3:6]+'-'
    four1 = ''.join(cleaner)[6:11]

    print(three1 + three2 + four1)



fancy_phone()
