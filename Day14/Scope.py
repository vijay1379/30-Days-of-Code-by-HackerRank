class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        min_element = self.__elements[0]
        max_element = self.__elements[0]

        for element in self.__elements:
            min_element = min(min_element, element)
            max_element = max(max_element, element)

        self.maximumDifference = abs(max_element - min_element)

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
