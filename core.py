


def removeControlChar(s: str):
    return s.strip()

def parse_column(column_str):
    """
    split a string into rows
    :param column_str: row1\r\nrow2\r\n...
    :return: [ row1, row2, ... ]
    """
    column_str = removeControlChar(column_str)
    column_str = column_str.replace("\r", "")
    return column_str.split("\n")

def parse_row(row_str):
    """
    split a string into columns
    :param row_str: col1\tcol2\t...
    :return: [ col1, col2, ... ]
    """
    row_str = removeControlChar(row_str)
    return row_str.split("\t")

def parse_matrix(s):
    """
    transform s to a matrix
    :param s: "c1 \t c2 ... \r\n c5 \t c6 ..."
    :return: [ [ c1, c2 ...], [c5, c6 ... ], ... ]
    """
    res = []
    rows = parse_column(s)
    for row in rows:
        splited_row = parse_row(row)
        res.append(splited_row)
    return res

def flat_matrix(m):
    """
    2 dimension matrix to 1 dim matrix
    :param m:
    :return:
    """
    return [ i for j in m for i in j ]


class BufferController:
    def __init__(self):
        self.buffer_list = []
        self.origin_list = []
        self.current_index = 0
        self.current_item = None
        self.ready = False
        self.error = False
        self.error_msg = ""

    def set_buffer_list(self, l: list):
        if len(l) != 0:
            self.buffer_list = l
            self.origin_list = l.copy()
            self.current_item = l[0]
            self.current_index = 0
            self.set_ready()

    def set_ready(self):
        self.ready = True
        self.error = False
        self.error_msg = ""

    def set_error(self, error_msg):
        self.ready = False
        self.error = True
        self.error_msg = error_msg

    def reset(self):
        if len(self.origin_list) > 0:
            self.buffer_list = self.origin_list.copy()
            self.set_ready()

    def next(self):
        if self.current_index + 1 < len(self.buffer_list):
            self.current_index += 1
            self.current_item = self.buffer_list[self.current_index]
            return self.current_item
        else:
            self.set_error("There is no next item to get")
            return None


    def previous(self):
        if 0 <= self.current_index - 1 < len(self.buffer_list):
            self.current_index -= 1
            self.current_item = self.buffer_list[self.current_index]
            return self.current_item
        else:
            self.set_error("there is no previous item to get")
            return None

    def preview_next(self):
        if self.current_index + 1 < len(self.buffer_list):
            return self.buffer_list[self.current_index + 1]
        else:
            self.set_error("There is no next item to get")
            return None

    def preview_previous(self):
        if 0 <= self.current_index - 1 < len(self.buffer_list):
            return self.buffer_list[self.current_index - 1 ]
        else:
            self.set_error("there is no previous item to get")
            return None

    def current(self):
        if self.current_item != None:
            return self.current_item
        else:
            self.set_error("there is no current item")
