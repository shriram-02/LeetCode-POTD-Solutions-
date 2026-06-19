class Solution(object):
    def largestAltitude(self, gain):
        altitude = 0
        highest = 0

        for g in gain:
            altitude += g
            highest = max(highest, altitude)

        return highest