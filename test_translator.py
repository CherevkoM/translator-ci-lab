from translator import translate_text, detect_language


def test_translate_to_ukrainian():
    result = translate_text("Hello", "uk")
    assert result == "Привіт"


def test_translate_to_polish():
    result = translate_text("Hello", "pl")
    assert result == "Cześć"


def test_empty_text():
    result = translate_text("", "uk")
    assert result == "Помилка: текст не може бути порожнім"


def test_unsupported_language():
    result = translate_text("Hello", "de")
    assert result == "Помилка: мова не підтримується"


def test_translation_not_found():
    result = translate_text("Unknown text", "uk")
    assert result == "Переклад не знайдено"


def test_detect_ukrainian_language():
    result = detect_language("Привіт, як справи?")
    assert result == "uk"


def test_detect_english_language():
    result = detect_language("Hello, how are you?")
    assert result == "en"


def test_detect_empty_language():
    result = detect_language("")
    assert result == "unknown"
