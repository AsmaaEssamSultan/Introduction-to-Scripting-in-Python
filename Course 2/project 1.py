"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

IDENTICAL = -1

def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    length1 = len(line1)
    length2 = len(line2)

    if length1 <= length2:
        min_length = length1
    else:
        min_length = length2

    if line1 == line2 :
        return IDENTICAL
    else:
        for index in range(min_length):
            if line1[index] != line2[index]:
                return index
        return min_length


def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    length1 = len(line1)
    length2 = len(line2)
    word = ""
    index = 0

    if line1.find("\n") >= 0 or line2.find("\n") >= 0:
        word += ""
    elif line1.find("\t") >= 0 or line2.find("\t") >= 0:
        word += ""

    if idx > length1 or idx > length2 or idx < 0:
        return ""

    if length1 == length2:
        if idx == -1:
            return ""
        else:
            while index < idx:
                word += "="
                index += 1
            word += "^"
    elif length1 < length2:
        while index < idx:
            word += "="
            index += 1
        word += "^"
    elif length1 > length2:
        while index < idx:
            word += "="
            index += 1
        word += "^"

    new_word = line1 + "\n" + word + "\n" + line2 + "\n"

    return new_word

def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    length1 = len(lines1)
    length2 = len(lines2)

    if length1 < length2 :
        min_length = length1
    else:
        min_length = length2
    if length1 == length2 and lines1 != lines2 :
        for index in range(length1):
            line1 = lines1[index]
            line2 = lines2[index]
            diff_index = singleline_diff(line1,line2)
            if diff_index >= 0:
                return (index , diff_index)


    elif length1 < length2 or length2 < length1 :
        if min_length == 0:
            return ( min_length , 0)
        elif lines1[min_length-1] == lines2[min_length-1] :
            return (min_length , 0)
        else:
            for index in range(min_length):
                line1 = lines1[index]
                line2 = lines2[index]
                diff_index = singleline_diff(line1,line2)
            return (index , diff_index)
    return  (IDENTICAL, IDENTICAL)


def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """

    file = open(filename , "rt")

    the_list = []
    for line in file :
        new_line = line.rstrip()
        the_list.append(new_line)

    file.close()
    return the_list

def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    file1 = get_file_lines(filename1)
    file2 = get_file_lines(filename2)
    line_index = multiline_diff(file1 , file2)

    if line_index == (-1, -1):
        return "No differences\n"
    else:
        num_of_line = line_index[0]
        num_of_index = line_index[1]
        output = "Line " + str(num_of_line) +":\n" + \
        singleline_diff_format(file1[num_of_line],file2[num_of_line],num_of_index)
        return output
