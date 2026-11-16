# Student: Nguyễn Viết Huy
# Student ID: ITDSIU24021
# Class/Group: IT149IU – Group 01
# Course: IT149IU - Fundamentals of Programming (Python)
# Lab 6 - Dictionaries and Sets
# AI assistance: ChatGPT was used to help draft/check solutions; review and understand before submission.

emails = ['DUNG.LE@OUTLOOK.COM', 'GIANG.HO@GMAIL.COM', '  em.vo@outlook.com ', 'GIANG.HO@GMAIL.COM', 'Binh.Tran@Gmail.Com', 'Chi.Pham@Gmail.Com', 'giang.ho@hcmiu.edu.vn', '  em.vo@outlook.com ', 'chi.pham@hcmiu.edu.vn', 'Binh.Tran@Hcmiu.Edu.Vn', 'An.Nguyen@Outlook.Com', 'giang.ho@outlook.com', 'dung.le@gmail.com', 'An.Nguyen@Gmail.Com', 'Binh.Tran@Hcmiu.Edu.Vn', '  an.nguyen@gmail.com ']

# Task 2: cleaning an e-mail list

def _normalise_email(email):
    """Return a normalized address, or None when the input is malformed."""
    if not isinstance(email, str):
        return None
    value = email.strip().lower()
    if value.count("@") != 1:
        return None
    local, domain = value.split("@")
    if not local or not domain or "." not in domain:
        return None
    if any(ch.isspace() for ch in value):
        return None
    return value


def unique_emails(emails):
    """Normalize addresses and remove duplicates, preserving first-seen order."""
    result = []
    seen = set()
    for email in emails:
        normalized = _normalise_email(email)
        if normalized is not None and normalized not in seen:
            result.append(normalized)
            seen.add(normalized)
    return result


def domain_counts(emails):
    """Count valid normalized addresses by domain (duplicate entries count)."""
    counts = {}
    for email in emails:
        normalized = _normalise_email(email)
        if normalized is not None:
            domain = normalized.rsplit("@", 1)[1]
            counts[domain] = counts.get(domain, 0) + 1
    return dict(sorted(counts.items()))


cleaned_emails = unique_emails(emails)
counts_by_domain = domain_counts(emails)
print("Raw e-mail entries:", len(emails))
print("Unique normalized e-mails:", len(cleaned_emails))
for address in cleaned_emails:
    print(" ", address)
print("Domain counts (all valid raw entries):", counts_by_domain)

assert len(cleaned_emails) == len(set(cleaned_emails))
assert all(address == address.strip().lower() for address in cleaned_emails)
assert sum(counts_by_domain.values()) <= len(emails)
assert unique_emails([" A@EXAMPLE.COM ", "a@example.com", "bad-address"]) == ["a@example.com"]
assert domain_counts([" A@EXAMPLE.COM ", "a@example.com", "b@gmail.com"]) == {
    "example.com": 2, "gmail.com": 1
}
print("Task 2 checks: PASS")
