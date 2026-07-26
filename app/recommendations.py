def generate_recommendations(report):

    recommendations = []


    # пропуски
    for column, value in report["missing_values"].items():

        if value > 0:

            recommendations.append(
                f"⚠ Колонка {column} содержит {value} пропусков. Требуется обработка."
            )


    # дубликаты
    if report["duplicates"] > 0:

        recommendations.append(
            f"⚠ Найдено дубликатов: {report['duplicates']}"
        )

    else:

        recommendations.append(
            "✅ Дубликаты не обнаружены."
        )


    # выбросы
    for column in report["outliers"]:

        recommendations.append(
            f"⚠ В колонке {column} обнаружены выбросы."
        )


    if len(recommendations) == 0:

        recommendations.append(
            "✅ Качество данных хорошее."
        )


    return recommendations
