def calculate_quality_score(report):

    score = 100


    # -----------------------
    # Пропуски
    # -----------------------

    missing = sum(
        report["missing_values"].values()
    )

    if missing > 0:
        score -= min(missing * 5, 30)


    # -----------------------
    # Дубликаты
    # -----------------------

    duplicates = report.get(
        "duplicates",
        0
    )

    if duplicates > 0:
        score -= min(duplicates * 3, 20)


    # -----------------------
    # Выбросы
    # -----------------------

    outliers = sum(
        len(v)
        for v in report.get(
            "outliers",
            {}
        ).values()
    )

    if outliers > 0:
        score -= min(outliers * 5, 30)


    # -----------------------
    # Финальная обработка
    # -----------------------

    score = max(score, 0)

    return round(score, 1)
