class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = []
        for part in path.split('/'):
            if part == '.':
                pass
            elif part == '..':
                dirs and dirs.pop()
            elif part:
                dirs.append(part)
        return '/' + '/'.join(dirs)