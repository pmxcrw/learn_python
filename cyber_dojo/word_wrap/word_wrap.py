
class WordWrap(object):
    
    def __init__(self, string, columns):
        self.string = string
        self.columns = columns
        self.cursor = 0
    
    @property
    def wrapped(self):
        word_list = self._split
        string = ""
        while len(word_list) > 0:           
            new_word = word_list.pop(0)

            if self.cursor + len(new_word) + 1 > self.columns:
                string += self._split_word(new_word)
            
            elif self.cursor + len(new_word) + 1 == self.columns:
                string += new_word + "\n"
                self.cursor = 0
            else:
                if self.cursor > 0:
                    string += " "
                    self.cursor += 1
                string += new_word
                self.cursor += len(new_word)
        return string
        
        
    @property
    def _split(self):
        string = self.string
        string = string.strip()
        string = string.replace("\n", "")
        string = string.replace("\t", "")
        string = string.split(" ")
        string = [word for word in string if len(word)>0]
        return string
    
    def _split_word(self, word):
        string = ""
        if len(word) < self.columns:
            if self.cursor >0:
                string += "\n"
            self.cursor = len(word)
            return string + word
        else:
            if self.cursor > 0:
                string += " "
                self.cursor += 1
            string += word[:self.columns-1-self.cursor] + "-\n"
            residual_word = word[self.columns-1-self.cursor:]
            self.cursor = 0
            string += self._split_word(residual_word)
            return string
            
        