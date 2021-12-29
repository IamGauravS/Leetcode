import math
sample_string = 'NNNWWSSENNEE'

target = 54

class SortedPairsum:
    def findmaxsum(self, sample_string):
        location = [0,0]
        for char in sample_string:
            if char == 'N':
                location[0] = location[0] +1
            if char == 'S':
                location[0] = location[0] -1
            if char == 'W':
                location[1] = location[1] +1
            if char == 'E':
                location[1] = location[1] -1 
        print(location)
        output_string = ''
        if location[0] >= 0:
            output_string = output_string + 'N'*location[0]
        else:
            output_string = output_string + 'S'*abs(location[0])

        if location[1] >= 0:
            output_string = output_string + 'W'*location[1]
        else:
            output_string = output_string + "E"*abs(location[1])

        return output_string


finddirection = SortedPairsum()
output = finddirection.findmaxsum(sample_string)
print(output)