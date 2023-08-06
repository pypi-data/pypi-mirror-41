from advertools.word_frequency import word_frequency


sep_list = [None, ' ', '-', '_']

text_list = [
    'one two',
    'one two  three',
    'one-two-three',
    'one_two_three',
    'four five',
    'four five',
    'four six'
]

num_list = [
    100,
    200,
    300,
    400,
    500,
    600,
    700
]

separators = [
    '-',
    '_',
    ' ',
    'f'
]


def test_len_result_one_more_than_len_slots():
    for sep in sep_list:
        result = word_frequency(text_list, num_list, sep=sep)
        if sep is not None:
            assert sep not in result['word']


def test_rm_words_removed():
    result = word_frequency(text_list, num_list, rm_words=['one', 'two'])
    assert 'one' not in result['word']
    assert 'two' not in result['word']


def test_extra_info_not_provided():
    result = word_frequency(text_list, num_list, extra_info=False)
    assert set(result.columns.values) == {'word', 'abs_freq', 'wtd_freq',
                                          'rel_value'}


def test_extra_info_provided():
    result = word_frequency(text_list, num_list, extra_info=True)
    assert set(result.columns.values) == {'word', 'abs_freq', 'abs_perc',
                                          'abs_perc_cum', 'wtd_freq',
                                          'wtd_freq_perc', 'wtd_freq_perc_cum',
                                          'rel_value'}


def test_words_separated_with_given_sep():
    for sep in separators:
        result = word_frequency(text_list, num_list, sep=sep)
        assert sep not in result['word']


def test_works_fine_with_only_stopwords_supplied():
    result = word_frequency(['on'], [3])
    assert result.shape == (0, 4)
