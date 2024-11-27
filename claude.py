import random

def generate_secret_code():
    """
    יוצר קוד סודי של 4 ספרות ללא חזרות
    """
    digits = list(range(10))
    random.shuffle(digits)
    return digits[:4]

def get_user_guess():
    """
    מקבל ניחוש מהמשתמש ומאמת את תקינותו
    """
    while True:
        try:
            guess = input("הכנס 4 ספרות שונות בין 0-9 (ללא חזרות): ")
            
            # בדיקת אורך הקלט
            if len(guess) != 4:
                print("שגיאה: עליך להזין 4 ספרות בדיוק!")
                continue
            
            # בדיקת תקינות הספרות
            guess_digits = [int(d) for d in guess]
            if len(set(guess_digits)) != 4:
                print("שגיאה: כל הספרות צריכות להיות שונות!")
                continue
            
            if any(d < 0 or d > 9 for d in guess_digits):
                print("שגיאה: הספרות צריכות להיות בין 0-9!")
                continue
            
            return guess_digits
        
        except ValueError:
            print("שגיאה: הכנס רק ספרות!")

def calculate_bulls_and_cows(secret, guess):
    """
    מחשב את מספר הבולים (מיקום ומספר נכון) והקאוז (מספר נכון, מיקום לא נכון)
    """
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(s in guess for s in secret) - bulls
    return bulls, cows

def play_bulls_and_cows():
    """
    פונקציית המשחק הראשית
    """
    print("ברוכים הבאים למשחק בול פגיעה!")
    print("המטרה: לנחש את הקוד הסודי של 4 ספרות ללא חזרות")
    print("בול = ספרה נכונה במיקום הנכון")
    print("קאו = ספרה נכונה במיקום לא נכון")
    
    # יצירת הקוד הסודי
    secret_code = generate_secret_code()
    
    # מספר ניסיונות מקסימלי
    max_attempts = 8
    
    for attempt in range(1, max_attempts + 1):
        print(f"\nניסיון {attempt} מתוך {max_attempts}")
        
        # קבלת ניחוש מהמשתמש
        user_guess = get_user_guess()
        
        # חישוב בולים וקאוז
        bulls, cows = calculate_bulls_and_cows(secret_code, user_guess)
        
        # הדפסת תוצאות הניסיון
        print(f"תוצאות הניסיון: {bulls} בולים, {cows} קאוז")
        
        # בדיקת ניצחון
        if bulls == 4:
            print(f"\nמזל טוב! ניחשת את הקוד הסודי {' '.join(map(str, secret_code))} ב-{attempt} ניסיונות!")
            return
    
    # הפסד
    print("\nהפסדת! הקוד הסודי היה:", ' '.join(map(str, secret_code)))

def main():
    """
    פונקציית הפעלה ראשית עם אופציית משחק חוזר
    """
    while True:
        play_bulls_and_cows()
        
        # שאלת המשתמש אם רוצה לשחק שוב
        play_again = input("\nהאם תרצה לשחק שוב? (כן/לא): ").strip().lower()
        if play_again not in ['כן', 'כ', 'yes', 'y']:
            print("תודה על המשחק! להתראות!")
            break

# הפעלת המשחק
if __name__ == "__main__":
    main()
