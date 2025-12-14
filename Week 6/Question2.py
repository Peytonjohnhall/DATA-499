def bayes_free_spam():
    # Given table values
    spam_free = 35
    spam_no_free = 10
    notspam_free = 20
    notspam_no_free = 55

    total = spam_free + spam_no_free + notspam_free + notspam_no_free

    # Probabilities
    P_spam = (spam_free + spam_no_free) / total
    P_free_given_spam = spam_free / (spam_free + spam_no_free)
    P_free = (spam_free + notspam_free) / total

    # Bayes theorem
    P_spam_given_free = (P_free_given_spam * P_spam) / P_free
    return P_spam_given_free

if __name__ == "__main__":
    print("P(spam | free) =", bayes_free_spam())