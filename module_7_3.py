# Оператор with
class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with (open(file_name, 'r', encoding='utf-8') as file):
                string = file.read().lower().replace('\n', ' ')
                for i in [',', '.', '!', '?', ':', ';', '=', ' - ']:
                    string = string.replace(i, '')
                string = string.split()
            all_words.update({file_name: string})
        return all_words

    def find(self, word):
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                return {name: words.index(word.lower()) + 1}
            else:
                print(f'слово не найдено')

    def count(self, word):
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                return {name: words.count(word.lower())}


if __name__ == '__main__':
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
