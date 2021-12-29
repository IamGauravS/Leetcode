input_string = "000011"

class Convert_binary:
    def convert(self, input_string):
        output = 0
        for i in range(len(input_string)):
            output = output + (2**i)*int(input_string[-1-i])

        return output 







convertbinary = Convert_binary()
output = convertbinary.convert(input_string)
print(output)
