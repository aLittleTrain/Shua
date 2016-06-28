"""
A multi-changing data and character output classes.
Copyright © 2016 aLittleTrain <alittletrain@gmail.com>
"""
class Shua():
    @staticmethod
    def top(char='*', nums=15, rows=1, blank=(0, 0, 0, 0), blanks=(0, 0, 0, 0)):
        """

        :param char: Output character(default=*,But you can also use any other arbitrary character.);

        :param nums: Number of characters in the output(default=15);

        :param rows: Number of rows in the output(default=1);

        :param blank: A definition of the empty tuple around for every row(
        default=(0,0,0,0),
        blank[0] is the row of top blank,
        blank[2] is the row of bottom blank,
        blank[3] is The number of characters on the left side of the blank,
        blank[1] is the number of characters on the right side of the blank
        )

        :param blanks: A definition of the empty tuple around for the output of all(
        default=(0,0,0,0),
        blank[0] is the rows of top blank,
        blank[2] is the rows of bottom blank,
        blank[3] is The number of characters on the left side of the blank,
        blank[1] is the number of characters on the right side of the blank
        )


        :return:
        """
        line_top = blank[0]
        line_right = blank[1]
        line_bottom = blank[2]
        line_left = blank[3]

        lines_top = blanks[0]
        lines_right = blanks[1]
        lines_bottom = blanks[2]
        lines_left = blanks[3]
        print(
            ('\n' * lines_top) + ((' ' * lines_left) + (
                '\n' * line_top + (' ' * line_left) + char * nums + (' ' * line_right) + ('\n' * line_bottom)) + (
                                      ' ' * lines_right) + '\n') * rows + ('\n' * lines_bottom))
        return

    @staticmethod
    def bottom(char='*', nums=15, rows=1, blank=(0, 0, 0, 0), blanks=(0, 0, 0, 0)):
        """

        :param char: Output character(default=*,But you can also use any other arbitrary character.);

        :param nums: Number of characters in the output(default=15);

        :param rows: Number of rows in the output(default=1);

        :param blank: A definition of the empty tuple around for every row(
        default=(0,0,0,0),
        blank[0] is the row of top blank,
        blank[2] is the row of bottom blank,
        blank[3] is The number of characters on the left side of the blank,
        blank[1] is the number of characters on the right side of the blank
        )

        :param blanks: A definition of the empty tuple around for the output of all(
        default=(0,0,0,0),
        blank[0] is the rows of top blank,
        blank[2] is the rows of bottom blank,
        blank[3] is The number of characters on the left side of the blank,
        blank[1] is the number of characters on the right side of the blank
        )


        :return:d
        """
        line_top = blank[0]
        line_right = blank[1]
        line_bottom = blank[2]
        line_left = blank[3]

        lines_top = blanks[0]
        lines_right = blanks[1]
        lines_bottom = blanks[2]
        lines_left = blanks[3]

        print(
            ('\n' * lines_top) + ((' ' * lines_left) + (
                '\n' * line_top + (' ' * line_left) + char * nums + (' ' * line_right) + ('\n' * line_bottom)) + (
                                      ' ' * lines_right) + '\n') * rows + ('\n' * lines_bottom))
        return

    @staticmethod
    def row(char=('|', 1), fields=(), blank=(0, 0), blanks=(0, 0), length=True):
        """

        :param char: A definition of the character and number of output tuples(default=('|', 1),But you can also use any other arbitrary character.)
        :param fields: One can have multiple fields of tuples(default=())
        :param blank: The left and right margins within the line length(default=(0,0))
        :param blanks: The length of the outer row left and right margins(default=(0,0))
        :param length: Whether to output a single line of total length
        :return:
        """
        output = ''
        len_tuple = len(fields)
        for index, field in enumerate(fields):
            if not len_tuple == 1:
                if index == 0:
                    output += (' ' * blanks[0]) + (char[0] * char[1]) + (' ' * blank[0]) + field + (' ' * blank[1]) + (
                        char[0] * char[1])
                elif index == (len_tuple - 1):

                    output += (' ' * blank[0]) + field + (' ' * blank[1]) + char[0] * char[1]

                else:
                    output += (' ' * blank[0]) + field + (' ' * blank[1]) + char[0] * char[1] + (' ' * blanks[1])
            else:
                output = (' ' * blanks[0]) + (char[0] * char[1]) + (' ' * blank[0]) + field + (' ' * blank[1]) + char[
                                                                                                                     0] * \
                                                                                                                 char[
                                                                                                                     1] + (
                             ' ' * blanks[1])

        print(output)
        if length:
            print('The length of string is {}'.format(len(output)))
        return
