def translate_text(text, target_language):
    """
    Проста навчальна функція перекладу тексту.
    Імітує роботу сервісу онлайн-перекладів.
    """

    translations = {
        "uk": {
            "Hello": "Привіт",
            "Good morning": "Доброго ранку",
            "Thank you": "Дякую"
        },
        "pl": {
            "Hello": "Cześć",
            "Good morning": "Dzień dobry",
            "Thank you": "Dziękuję"
        }
    }

    if not text:
        return "Помилка: текст не може бути порожнім"

    if target_language not in translations:
        return "Помилка: мова не підтримується"

    return translations[target_language].get(
        text,
        "Переклад не знайдено"
    )


def detect_language(text):
    """
    Проста функція визначення мови.
    """

    if not text:
        return "unknown"

    ukrainian_letters = "іїєґ"

    for letter in ukrainian_letters:
        if letter in text.lower():
            return "uk"

    return "en"
