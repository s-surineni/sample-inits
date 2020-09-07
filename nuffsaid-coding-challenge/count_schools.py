from csv import DictReader
import logging

logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def print_counts():
    schools_info = {}
    with open('school_data.csv', encoding="ISO-8859-1") as school_csv:
        reader = DictReader(school_csv)
        try:
            for row in reader:
                state = row['LSTATE05']
                mlocale = row['MLOCALE']
                if schools_info.get(state):
                    if not schools_info[state].get(mlocale):
                        schools_info[state][mlocale] = {}
                else:
                    schools_info[state] = {mlocale: {}}
                city = row['LCITY05']
                school = row['SCHNAM05']
                if schools_info[state][mlocale].get(city):
                    schools_info[state][mlocale][city].append(school)
                else:
                    schools_info[state][mlocale][city] = [school]
        except Exception:
            logger.exception('Exception occured while opening file')
    total_schools = 0
    city_school_count = {}
    metro_school_count = {}
    state_school_count = {}
    city_with_most_schools = None
    most_school_count = 0
    city_count = 0
    for stt in schools_info:
        # print('iron man stt', stt)
        state_school_count[stt] = 0
        # print('iron man stt', stt)
        for met in schools_info[stt]:
            # print('iron man met', met)
            if not metro_school_count.get(met):
                metro_school_count[met] = 0
            for cit in schools_info[stt][met]:
                city_count += 1
                # print('iron man cit', cit)
                city_schools_len = len(schools_info[stt][met][cit])
                if most_school_count < city_schools_len:
                    most_school_count = city_schools_len
                    city_with_most_schools = cit
                # print('iron man city_schools_len', city_schools_len)
                city_school_count[cit] = city_schools_len
                metro_school_count[met] += city_schools_len
                state_school_count[stt] += city_schools_len
                total_schools += city_schools_len

    print('Total Schools: {}'.format(total_schools))
    print('Schools by State:')
    for stt, cnt in state_school_count.items():
        print('{}: {}'.format(stt, cnt))
    print('Schools by Metro-centric locale:')
    for met, cnt in metro_school_count.items():
        print('{}: {}'.format(met, cnt))
    print('City with most schools: {} ({} schools)'.format(city_with_most_schools,
                                                           most_school_count))
    print('Unique cities with at least one school: {}'.format(city_count))
print_counts()
