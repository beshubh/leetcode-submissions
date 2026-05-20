class Solution:

    def get_line_chars(self, line: list[str]):
        t = 0
        for c in line:
            t += len(c)
        return t
    
    def fill_in_spaces(self, line: list[str], nspaces: int):
        if nspaces == 0:
            return line
        space_idxs = []
        for i in range(len(line)):
            if line[i] == ' ':
                space_idxs.append(i)
        if not space_idxs:
            return line + [' ' * nspaces]

        gap_count = len(space_idxs)
        base = nspaces // gap_count
        extra = nspaces % gap_count
        for j, idx in enumerate(space_idxs):
            line[idx] += ' '*base
            if extra > 0:
                line[idx] += ' '
                extra -= 1
        return line 

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        current_line = [words[0]]
        i = 1
        while i < len(words):
            word = words[i]
            done = self.get_line_chars(current_line)
            if done + 1 + len(word) <= maxWidth:
                current_line.append(' ')
                current_line.append(word)
            else:
                need = maxWidth - done
                current_line = self.fill_in_spaces(current_line, need)
                lines.append(''.join(current_line))
                current_line = [word]
            i += 1

        if current_line:
            clen = self.get_line_chars(current_line) 
            if clen < maxWidth:
                current_line.append(' '*(maxWidth - clen))
            lines.append(''.join(current_line))
        return lines 
