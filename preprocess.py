#!/usr/bin/env python
# -*- coding: utf-8 -*-

FEATURES = [
    u'start_square', u'price', u'mean_sq', u'mean_fl', u'plan_s', u'plan_m', u'plan_l',
    u'vid_0', u'vid_1', u'vid_2', u'month', u'month_cnt', u'Класс объекта',
    u'Количество помещений', u'Огорожена территория',
    u'Площадь земельного участка', u'Входные группы', u'Детский сад',
    u'Школа', u'Поликлиника', u'ФОК', u'Спортивная площадка', u'Автомойка',
    u'Кладовые', u'Колясочные', u'Кондиционирование', u'Вентлияция',
    u'Лифт', u'Система мусоротведения', u'Видеонаблюдение',
    u'Подземная парковка', u'Двор без машин', u'Машиномест',
    u'Площадь пром. зоны в радиусе 500 м',
    u'Площадь зеленой зоны в радиусе 500 м', u'До Кремля', u'До ТТК(км)',
    u'До Садового(км)', u'До большой дороги на машине(км)',
    u'До удобной авторазвязки на машине(км)', u'До метро пешком(км)',
    u'До промки(км)', u'До парка(км)', u'До парка пешком(км)',
    u'Станций метро от кольца', u'Площадь двора', u'Курс',
    u'Cтавка по ипотеке', u'Вклады до 1 года', u'Вклады от 1 года до 3 лет',
    u'Вклады свыше 3 лет'
]

TEST_FEATURES = [
     u'price', u'mean_sq', u'mean_fl',
     u'month', u'month_cnt', u'Класс объекта',
    u'Количество помещений', u'Огорожена территория',
    u'Площадь земельного участка', u'Входные группы', u'Детский сад',
    u'Школа', u'Поликлиника', u'ФОК', u'Спортивная площадка', u'Автомойка',
    u'Кладовые', u'Колясочные', u'Кондиционирование', u'Вентлияция',
    u'Лифт', u'Система мусоротведения', u'Видеонаблюдение',
    u'Подземная парковка', u'Двор без машин', u'Машиномест',
    u'Площадь пром. зоны в радиусе 500 м',
    u'Площадь зеленой зоны в радиусе 500 м', u'До Кремля', u'До ТТК(км)',
    u'До Садового(км)', u'До большой дороги на машине(км)',
    u'До удобной авторазвязки на машине(км)', u'До метро пешком(км)',
    u'До промки(км)', u'До парка(км)', u'До парка пешком(км)',
    u'Станций метро от кольца', u'Площадь двора', u'Курс',
    u'Cтавка по ипотеке', u'Вклады до 1 года', u'Вклады от 1 года до 3 лет',
    u'Вклады свыше 3 лет',
    # u'year',
    # u'time'
    u'bulk_cat'
]

CATEGORICAL_FEATURES = [
"Класс объекта",
"Огорожена территория",
"Входные группы",
"Спортивная площадка",
"Автомойка",
"Кладовые",
"Колясочные",
"Система мусоротведения",
"Подземная парковка",
"Двор без машин"
"bulk_cat"
]


CATEGORICAL_TEST_FEATURES_IDX = [TEST_FEATURES.index(cat_feat.decode('utf-8') ) for cat_feat in CATEGORICAL_FEATURES]

def preprocess(data, categorical_features):
    '''

    Preprocessing train/test data

    Parameters
    ----------
    data: pandas.DataFrame
        Pandas DataFrame object
    categorical_features: list of str
        Categorical feature names

    '''

    # Transforming categorical features
    for feature_name in categorical_features:
        data[feature_name] = data[feature_name].str.decode('utf-8').astype('category').cat.codes

    # Bulk cat


    # Adding date features
    # data['year'] = data.date1.str[:4].astype(float)
    # data['time'] = data.year + data.date1.str[5:7].astype(float)/ 12.

    # Column names decoding
    data.columns = [c.decode('utf-8') for c in data.columns]

    return data


def preprocess_train(data, categotical_features=CATEGORICAL_FEATURES, features=TEST_FEATURES):
    data = preprocess(data, categorical_features=categotical_features)
    y = data.value.values
    X = data[features].values
    return X, y

if __name__ == '__main__':
    print CATEGORICAL_TEST_FEATURES_IDX

