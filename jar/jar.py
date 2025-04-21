class Jar:
    def __init__(self, capacity=12):
        # Validate if capacity is a non-negative integer
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer.")

        self._capacity = capacity  # Use a private attribute for capacity
        self._cookies = 0  # Start with 0 cookies in the jar

    def __str__(self):
        return "🍪" * self._cookies

    def deposit(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Number of cookies must be a non-negative integer.")

        if self._cookies + n > self._capacity:
            raise ValueError("Adding that many cookies would exceed the jar's capacity.")

        self._cookies += n

    def withdraw(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Number of cookies must be a non-negative integer.")

        if self._cookies - n < 0:
            raise ValueError("Not enough cookies to withdraw.")

        self._cookies -= n

    @property
    def capacity(self):
        # Return the jar's capacity
        return self._capacity

    @property
    def size(self):
        # Return the number of cookies in the jar
        return self._cookies
