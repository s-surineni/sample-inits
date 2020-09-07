from csv import DictReader
import logging
import re
import time


logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


reverse_index = {}
schools_info = []


def prepare_reverse_index():
    row_terms = []
    with open('school_data.csv', encoding="ISO-8859-1") as school_csv:
        reader = DictReader(school_csv)

        try:
            for row in reader:
                curr_idx = len(schools_info) # point to current index
                state = row['LSTATE05']
                city = row['LCITY05']
                school = row['SCHNAM05']
                school_entry = (state, city, school)
                schools_info.append(school_entry)

                # turn contents of school, state, city names
                # into list of strings
                curr_row_term = []
                for name in (state, city, school):
                    name = re.sub(r'[\W_]+', ' ', name).lower()
                    curr_row_term += name.split()
                row_terms.append(curr_row_term)

                # coverting into reverse index
                for term in curr_row_term:
                    if term in reverse_index:
                        reverse_index[term].add(curr_idx)
                    else:
                        reverse_index[term] = {curr_idx}
        except Exception:
            logger.exception('Exception occured while opening file')


def search_schools(search_query):
    search_query = re.sub(r'[\W_]+', ' ', search_query).lower()
    term_res = []
    for term in search_query.split():
        term_res.append(reverse_index[term])
    search_result = term_res[0]
    for term in term_res[1:]:
        search_result &= term
    return [schools_info[idx] for idx in search_result]


if __name__ == '__main__':
    prepare_reverse_index()
    print('Please enter xxx to exit')
    while True:
        search_term = input('Enter term to search for: ')
        start_time = time.perf_counter()
        if search_term == 'xxx':
            print('Bye...')
            break
        print('Time took: {}'.format(time.perf_counter() - start_time))
        print(search_schools(search_term))
