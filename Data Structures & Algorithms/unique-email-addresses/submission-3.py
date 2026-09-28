class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_set = set()
        for i, email in enumerate(emails):
            email_at_split = email.split("@")
            email_plus_split = email_at_split[0].split("+")
            email_plus_split[0] = re.sub(r"[^a-zA-Z0-9]", "", email_plus_split[0])
            email_set.add(email_plus_split[0] + "@" + email_at_split[1])
        
        return len(email_set)