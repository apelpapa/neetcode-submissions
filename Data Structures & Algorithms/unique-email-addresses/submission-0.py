class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueEmail = {}
        for email in emails:
            tempEmail = email.split("@")
            tempEmail [0] = tempEmail[0].replace(".","")
            tempEmail2 = tempEmail[0].split("+")
            newEmail = tempEmail2[0] + "@" + tempEmail[1]
            uniqueEmail[newEmail] = 1
        return len(uniqueEmail)
        