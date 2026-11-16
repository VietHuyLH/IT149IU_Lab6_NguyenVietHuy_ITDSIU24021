# Student: Nguyễn Viết Huy
# Student ID: ITDSIU24021
# Class/Group: IT149IU – Group 01
# Course: IT149IU - Fundamentals of Programming (Python)
# Lab 6 - Dictionaries and Sets
# AI assistance: ChatGPT was used to help draft/check solutions; review and understand before submission.

import copy
staff = {'E1001': {'name': 'David Le', 'branch': 'DN', 'salary': 1850}, 'E1002': {'name': 'Cindy Pham', 'branch': 'HN', 'salary': 2200}, 'E1003': {'name': 'Binh Tran', 'branch': 'DN', 'salary': 1050}, 'E1004': {'name': 'Irene Do', 'branch': 'HN', 'salary': 1250}, 'E1005': {'name': 'Frank Dang', 'branch': 'CT', 'salary': 1000}, 'E1006': {'name': 'Mona Cao', 'branch': 'CT', 'salary': 2050}, 'E1007': {'name': 'Kelly Mai', 'branch': 'HCM', 'salary': 1500}, 'E1008': {'name': 'Henry Bui', 'branch': 'DN', 'salary': 1400}, 'E1009': {'name': 'Grace Ho', 'branch': 'CT', 'salary': 1950}, 'E1010': {'name': 'Nick Dinh', 'branch': 'HN', 'salary': 1550}, 'E1011': {'name': 'Leo Truong', 'branch': 'HCM', 'salary': 1600}, 'E1012': {'name': 'Jack Ly', 'branch': 'HCM', 'salary': 1300}}

# Task 5: staff records (nested dictionary)

def by_branch(staff):
    """Return {branch: [(employee_id, record), ...]}, sorted by employee ID."""
    grouped = {}
    for employee_id, record in staff.items():
        grouped.setdefault(record["branch"], []).append((employee_id, record.copy()))
    for branch in grouped:
        grouped[branch].sort(key=lambda pair: pair[0])
    return dict(sorted(grouped.items()))


def avg_salary_by_branch(staff):
    """Return average salary for each branch."""
    totals = {}
    counts = {}
    for record in staff.values():
        branch = record["branch"]
        totals[branch] = totals.get(branch, 0) + record["salary"]
        counts[branch] = counts.get(branch, 0) + 1
    return {branch: totals[branch] / counts[branch] for branch in sorted(totals)}


def highest_paid(staff):
    """Return (employee_id, record copy) for the highest-paid employee, or None."""
    if not staff:
        return None
    employee_id = max(staff, key=lambda key: (staff[key]["salary"], key))
    return employee_id, staff[employee_id].copy()


def raise_salary(staff, branch, pct):
    """Raise salaries in branch in place; pct can be 0.05 or 5 for a 5% increase.
    Return the number of changed staff records.
    """
    rate = pct / 100 if abs(pct) > 1 else pct
    if rate < -1:
        raise ValueError("A salary decrease cannot exceed 100%.")
    changed = 0
    for record in staff.values():
        if record["branch"] == branch:
            record["salary"] = round(record["salary"] * (1 + rate), 2)
            changed += 1
    return changed


def print_staff_table(staff):
    """Print staff in a readable table sorted by employee ID."""
    print(f"{'ID':<8} {'Name':<18} {'Branch':<8} {'Salary':>10}")
    print("-" * 48)
    for employee_id in sorted(staff):
        record = staff[employee_id]
        print(f"{employee_id:<8} {record['name']:<18} {record['branch']:<8} {record['salary']:>10.2f}")


print("Staff table:")
print_staff_table(staff)
print("\nStaff count by branch:", {branch: len(rows) for branch, rows in by_branch(staff).items()})
print("Average salary by branch:", {k: round(v, 2) for k, v in avg_salary_by_branch(staff).items()})
print("Highest paid:", highest_paid(staff))
_test_staff = copy.deepcopy(staff)
_target_branch = sorted({rec["branch"] for rec in _test_staff.values()})[0]
_changed = raise_salary(_test_staff, _target_branch, 5)
print(f"Raised salary by 5% in {_target_branch}: {_changed} records updated")
assert sum(len(rows) for rows in by_branch(staff).values()) == len(staff)
assert set(avg_salary_by_branch(staff)) == {r["branch"] for r in staff.values()}
assert highest_paid(staff) is not None
assert all(staff[k]["salary"] == _test_staff[k]["salary"] for k in staff if staff[k]["branch"] != _target_branch)
assert any(staff[k]["salary"] != _test_staff[k]["salary"] for k in staff if staff[k]["branch"] == _target_branch)
print("Task 5 checks: PASS")
