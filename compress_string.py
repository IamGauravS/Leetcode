input_string = "AAABBBC"

class Compress:
    def compressstring(self, input_string):

        output_string = ''
        for i in range(len(input_string)):
            count =1
            print(i)
            while i<(len(input_string)-1) and input_string[i] == input_string[i+1]:
                count += 1
                i += 1
                print(i)
            output_string = output_string + input_string[i] + str(count)


        return output_string

compress = Compress()
output = compress.compressstring(input_string)
print(output) 