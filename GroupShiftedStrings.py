class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        alphabet = {
            'a':0,
            'b':1,
            'c':2,
            'd':3,
            'e':4,
            'f':5,
            'g':6,
            'h':7,
            'i':8,
            'j':9,
            'k':10,
            'l':11,
            'm':12,
            'n':13,
            'o':14,
            'p':15,
            'q':16,
            'r':17,
            's':18,
            't':19,
            'u':20,
            'v':21,
            'w':22,
            'x':23,
            'y':24,
            'z':25
        }
        reverse_alphabet = {
            0:'a',
            1:'b',
            2:'c',
            3:'d',
            4:'e',
            5:'f',
            6:'g',
            7:'h',
            8:'i',
            9:'j',
            10:'k',
            11:'l',
            12:'m',
            13:'n',
            14:'o',
            15:'p',
            16:'q',
            17:'r',
            18:'s',
            19:'t',
            20:'u',
            21:'v',
            22:'w',
            23:'x',
            24:'y',
            25:'z'
        }
        D = {}
        result = []
        for string in strings:
            shift_sorted = ''
            shift_amount = alphabet[string[0]]
            for char in string:
                shift_sorted = shift_sorted + reverse_alphabet[(alphabet[char] - shift_amount) % 26]
            if shift_sorted not in D:
                D[shift_sorted] = [string]
            else:
                D[shift_sorted].append(string)
        for key in D:
            result.append(D[key])
        return result
                
