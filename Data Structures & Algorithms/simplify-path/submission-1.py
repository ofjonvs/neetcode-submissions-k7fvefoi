class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = []
        for part in path.split('/'):
            if part == '..':
                dirs and dirs.pop()
            elif part and part != '.':
                dirs.append(part)
        return '/' + '/'.join(dirs)