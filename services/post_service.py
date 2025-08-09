import unicodedata
import re


def get_reading_time_minutes(text: str, wpm=200):
    """
    Calculate the estimated reading time for a given text in minutes.

    This function counts the total number of words in the provided text
    and divides it by the average reading speed (words per minute) to
    estimate the reading time. The result is rounded to the nearest minute.

    Args:
        text (str): The full text whose reading time will be calculated.
        wpm (int, optional): Average reading speed in words per minute.
            Defaults to 200.

    Returns:
        int: Estimated reading time in whole minutes.

    Example:
        >>> article = "This is a short example text."
        >>> get_reading_time_minutes(article)
    """
    words = text.split()
    total_words = len(words)
    minutes = total_words/wpm
    return round(minutes)


def get_slug(title: str) -> str:
    """
    Genera un slug a partir de un texto dado.

    Un slug es una cadena optimizada para URLs: sin acentos,
    en minúsculas, con espacios y caracteres no alfanuméricos
    reemplazados por guiones.

    Parámetros:
        texto (str): Texto de entrada que se desea convertir en slug.

    Retorna:
        str: El texto convertido en un slug, listo para usarse en una URL.

    Ejemplo:
        >>> generar_slug("¡Cómo hacer un pastel de Chocolate fácil!")
        'como-hacer-un-pastel-de-chocolate-facil'
    """
    # 1. Normalizar y eliminar acentos
    # convierte caractres acentuados en su forma base
    texto = unicodedata.normalize("NFKD", title)
    texto = texto.encode("ascii", "ignore").decode(
        "utf-8")  # elimina cuakquier simbolo no ASCCII

    # 2. Convertir a minúsculas
    texto = texto.lower()

    # 3. Reemplazar caracteres no alfanuméricos por guiones
    texto = re.sub(r'[^a-z0-9]+', '-', texto)

    # 4. Quitar guiones al inicio o final
    texto = texto.strip('-')

    return texto
