"""
This module provides a simple scheduling algorithm for the automation system.
The generate_schedule function will process a list of lesson requests and
return a schedule grouped by group name.

The input `data` should be a list of dictionaries with at least the keys:
- group: group identifier
- subject: the subject name
- time: time slot or period

The returned schedule is a dictionary where each key is a group and the
value is a list of (subject, time) tuples.
"""

def generate_schedule(data):
    """
    Generate a schedule dictionary from a list of class dictionaries.

    Args:
        data (list): List of dictionaries with keys 'group', 'subject', and 'time'.

    Returns:
        dict: A dictionary mapping group identifiers to a list of (subject, time) tuples.
    """
    schedule = {}
    for item in data:
        group = item.get('group')
        subject = item.get('subject')
        time_slot = item.get('time')
        if group is None:
            continue  # skip entries without a group
        schedule.setdefault(group, []).append((subject, time_slot))
    return schedule
