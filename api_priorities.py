from collections import deque


class RequestQueue:
    def __init__(self):
        """Initialize the request queue."""
        # Dictionary: priority -> deque of request_ids
        self.queues = {1: deque(), 2: deque(), 3: deque(), 4: deque(), 5: deque()}

    def add_request(self, request_id: str, priority: int) -> None:
        """
        Add a request to the queue.

        Args:
            request_id: Unique identifier for the request
            priority: Priority level (1 = highest, 5 = lowest)
        """
        self.queues[priority].append(request_id)  # O(1)

    def get_next_request(self) -> str | None:
        """
        Get and remove the highest priority request.

        Returns:
            The request_id of the next request to process,
            or None if queue is empty
        """
        for priority in [1, 2, 3, 4, 5]:
            if self.queues[priority]:
                return self.queues[priority].popleft()  # O(1) instead of O(n)!
        return None

    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        return all(len(q) == 0 for q in self.queues.values())