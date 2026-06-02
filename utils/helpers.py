"""
Common utilities and helper functions for solving problems.
"""


def time_complexity_analysis(description):
    """
    Decorator to document time complexity of a function.
    
    Args:
        description: String describing the time complexity (e.g., 'O(n)', 'O(n log n)')
    """
    def decorator(func):
        func.time_complexity = description
        return func
    return decorator


def space_complexity_analysis(description):
    """
    Decorator to document space complexity of a function.
    
    Args:
        description: String describing the space complexity (e.g., 'O(1)', 'O(n)')
    """
    def decorator(func):
        func.space_complexity = description
        return func
    return decorator


def get_complexity_info(func):
    """Get complexity information from a function."""
    time_comp = getattr(func, 'time_complexity', 'Not specified')
    space_comp = getattr(func, 'space_complexity', 'Not specified')
    return f"Time: {time_comp}, Space: {space_comp}"


if __name__ == "__main__":
    @time_complexity_analysis('O(n)')
    @space_complexity_analysis('O(1)')
    def example_function():
        pass
    
    print(get_complexity_info(example_function))
