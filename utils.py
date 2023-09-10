class utils:

    def reversed(self, num):
        # check type first
        if not isinstance(num, int):
            return -1

        reversedNum = 0

        while num > 0:
            currentDigit = num % 10
            reversedNum = (10 * reversedNum) + currentDigit
            num = num // 10

        return reversedNum


    def formatter(self, num):
        # check type first
        if not isinstance(num, int):
            return -1

        # binary conversion
        binaryNum = bin(num)

        # octal conversion
        octalNum = oct(num)

        return binaryNum, octalNum