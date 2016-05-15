
class WordWrap(object):
    
    def __init__(self, string, columns):
        self.string = string
        self.columns = columns
        self._cursor = 0
        self._wrapped = ""
        
    @property
    def _spacer(self):
        '''works out if we need a space before printing next word'''
        if self._cursor > 0:
            return True
        else:
            return False
    
    def wrap(self):
        '''generates a string with wrapped text'''
        word_list = self._split
        while len(word_list) > 0:           
            new_word = word_list.pop(0)
            if self._cursor + len(new_word) + self._spacer > self.columns:
                self._newline(new_word)
            else:
                self._extendline(new_word)
        return self._wrapped
        
        
    @property
    def _split(self):
        '''splits the input string into a list of words, without any formatting'''
        string = self.string
        string = string.strip()
        string = string.replace("\n", "")
        string = string.replace("\t", "")
        string = string.split(" ")
        string = [word for word in string if len(word)>0]
        return string
    
    @property
    def _space(self):
        if self._spacer:
            self._wrapped += " "
            self._cursor += 1
    
    def _newline(self, word):
        if self._cursor == self.columns:
            self._wrapped += "\n"
            self._cursor = 0
        while len(word) > self.columns:
            self._space
            self._wrapped += word[:self.columns-1-self._cursor] + "-\n"
            word = word[self.columns-1-self._cursor:]
            self._cursor = 0
        if self._cursor > 0:
            self._wrapped += "\n"
            self._cursor = 0
        self._cursor = len(word)
        self._wrapped += word
    
    def _extendline(self, word):
        self._space
        self._wrapped += word
        self._cursor += len(word)