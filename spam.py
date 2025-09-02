def calculate_spam_score(email_content):
    spam_keywords = [
        'hacked!', 'win', 'prize', 'loan', 'lottery!',
        'guarantee', 'click here', 'act now', 'free', 'winner', 'subscribe now',
         'claim your inheritance','cheap','you won!','press this link',
         'additional income','be your own boss','debt free now',
         'free giveaway now','XXX','Porn','viagra','last shot', 'get a job now!'
         ,'nigeria'
    ]
    
    ham_keywords = ['meeting', 'schedule', 'project', 'thank you', 'invoice', 
    'conference','reset your password','confirm your email','hope you are well',
    'webinar','rsvp','kind regards']
    
    score = 0
    
    # Increase score for each spammy keyword found
    for keyword in spam_keywords:
        if keyword in email_content:
            score += 1
    
    # Decrease score for ham-like keywords
    for keyword in ham_keywords:
        if keyword in email_content:
            score -= 1  # Reduce spam score for likely legitimate words
    
    # Increase score for multiple exclamation marks (but more forgiving)
    if email_content.count('!') > 3:
        score += 1
    
    # Increase score for all caps words
    words = email_content.split()
    for word in words:
        if word == '!':
            score += 1
            if score > 1:
                score += 1
        if word.isupper() and len(word) > 1:  # Ignore single-letter caps
            score += 1

    # Increase score if the email contains suspicious URL patterns
    if 'https://' in email_content or 'www.' in email_content or '.com' in email_content:
        score += 1
    print(score)

    return score


def is_spam(email_content):
    # Adjust this threshold to make the detection less aggressive
    score_threshold = 1  # Increasing the threshold for better ham detection
    
    score = float(calculate_spam_score(email_content))
    
    return score >= score_threshold

def read_email_file():
    try:
        with open('email.txt', 'r', errors='ignore') as file:
            email_content = file.read().lower()  # Convert email content to lowercase
        return email_content
    except FileNotFoundError:
        return None

def main():
    # file_path = read_email_file()
    email_content = read_email_file()
    
    if email_content is None:
        print("Error: The file cannot be read or does not exist.")
    else:
        if is_spam(email_content):
            print("spam")
        else:
            print("notspam")

# Call the main function to run the program
if __name__ == "__main__":
    main()


