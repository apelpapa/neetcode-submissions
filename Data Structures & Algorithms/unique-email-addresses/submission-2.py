class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueEmail = set()
        for email in emails:
            tempEmail = email.split("@")
            tempEmail[0] = tempEmail[0].replace(".","")
            tempEmail2 = tempEmail[0].split("+")
            newEmail = tempEmail2[0] + "@" + tempEmail[1]
            uniqueEmail.add(newEmail)
        return len(uniqueEmail)
        