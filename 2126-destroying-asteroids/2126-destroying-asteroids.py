class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        res=False
        asteroids.sort()
        for asteroid in asteroids:
            if mass>=asteroid:
                mass+=asteroid
            else:
                return False
        return True