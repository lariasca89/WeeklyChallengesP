import cv2


def image_display(compliance):
    if compliance:
        image = cv2.imread('/Users/lariasca/Documents/Python/WeeklyChallengesP/WeeklyChallenge_Week08_lariasca/Compliance.png')
        cv2.imshow('Compliant!', image)
        cv2.waitKey()
    else:
        image = cv2.imread('/Users/lariasca/Documents/Python/WeeklyChallengesP/WeeklyChallenge_Week08_lariasca/NoCompliance.png')
        cv2.imshow('NOT Compliant!', image)
        cv2.waitKey()
