'''
'''

from .generator import CPRGenerator


def main():
    generator = CPRGenerator()
    cpr_number = generator.generate(hyphen=True)
    print(cpr_number)


if __name__ == '__main__':
    main()
