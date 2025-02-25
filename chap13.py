import string
from collections import Counter
import random

def clean_words(file_name):
    # Mở file và đọc nội dung
    with open(file_name, 'r') as file:
        for line in file:
            # Chuyển thành chữ thường và loại bỏ dấu câu
            line = line.lower()
            # Loại bỏ dấu câu và khoảng trắng không cần thiết
            line = line.translate(str.maketrans('', '', string.punctuation))
            # Tách dòng thành các từ
            words = line.split()
            for word in words:
                print(word)

clean_words("words.txt")

def most_common_words(file_name):
    word_count = Counter()
    
    with open(file_name, 'r') as file:
        for line in file:
            line = line.lower()
            line = line.translate(str.maketrans('', '', string.punctuation))
            words = line.split()
            word_count.update(words)
    
    # In ra 20 từ xuất hiện nhiều nhất
    for word, count in word_count.most_common(20):
        print(f'{word}: {count}')
        
most_common_words("words.txt")

def words_not_in_dict(file_name, word_list):
    with open(file_name, 'r') as file:
        words_in_book = set()
        
        for line in file:
            line = line.lower()
            line = line.translate(str.maketrans('', '', string.punctuation))
            words = line.split()
            words_in_book.update(words)
    
    # So sánh và in ra các từ không có trong từ điển
    missing_words = words_in_book - set(word_list)
    print(f'Total missing words: {len(missing_words)}')
    for word in missing_words:
        print(word)

dictionary_words = ['the', 'and', 'to', 'of', 'a', 'in', 'for', 'is', 'that', 'it', 'you', 'be', 'this', 'as', 'on']

words_not_in_dict("words.txt", dictionary_words)


def choose_from_hist(hist):
    # Tạo danh sách các phần tử lặp lại theo tần suất
    population = []
    for word, count in hist.items():
        population.extend([word] * count)
    
    # Chọn ngẫu nhiên một phần tử trong population
    return random.choice(population)

def create_histogram(file_name):
    word_count = Counter()
    with open(file_name, 'r') as file:
        for line in file:
            line = line.lower()
            line = line.translate(str.maketrans('', '', string.punctuation))
            words = line.split()
            word_count.update(words)
    return word_count

# Tạo histogram từ file văn bản
hist = create_histogram("words.txt")
print(choose_from_hist(hist))  # Chọn ngẫu nhiên một từ từ histogram
