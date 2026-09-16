class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0
        dirX, dirY = 0, 1

        for instruction in instructions:
            if instruction == "G":
                x, y = x + dirX, y + dirY
            elif instruction == "L":
                dirX, dirY = -dirY, dirX
            else:
                dirX, dirY = dirY, -dirX

        if x == 0 and y == 0:
            return True

        if dirX == 0 and dirY == 1:
            return False

        return True
