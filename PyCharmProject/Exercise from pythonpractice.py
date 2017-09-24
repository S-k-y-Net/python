import math
import re
import random
import requests
import bs4


class Mathematic:
    def less_than_ten(self, start=1, stop=2, step=1):
        print(str([x for x in range(start, stop, step) if x < 5]))

    def divisors(self, numb):
        my_number = [x for x in range(1,numb + 1) if numb % x == 0]
        print(str([x for x in range(1,numb + 1) if numb % x == 0]))
        return my_number

    def two_list_overlap_first(self, list_one, list_two):
        if isinstance(list_one, list) and isinstance(list_two, list):
            overlaps =list(set(list_one) & set(list_two))
        else:
            print("You don't give me a list!")
        print(overlaps)

    def palindrom_string(self, my_str):
        # elegant solution  str(mystr) == str(mystr)[::-1] from stackoverflow
        if my_str == "":
            print("You give me blank string!")
        if isinstance(my_str, str):
            revert = my_str[::-1]
            if revert == my_str:
                print("This is palindorm!")
            else:
                print("it's not palindrom!")

    def even_element_of_list(self,my_list):
        print(str([x for x in my_list if x%2 == 0]))

    def two_list_overlap_second(self, my_first_list, my_second_list):
        # elegant user solution result = [i for i in a if i in b]
        if isinstance(my_first_list, list) and isinstance(my_first_list, list):
            output_list = []
            for x in range(my_first_list.__len__()):
                for y in range(my_second_list.__len__()):
                    if my_first_list[x] == my_second_list[y]:
                        output_list.append(my_first_list[x])
            output_list = set(output_list)
        else:
            print("You don't give me a two correct list!")
        print(output_list)

    def primer_function(self):
        user_input = int(input("Type some number and I you tell is it a prime number: "))
        local_numb = self.divisors(user_input)
        if local_numb.__len__() > 2:
            print("This is not prime number")
        else:
            print("This is a prime number!")
        return local_numb

    def list_ends(self, my_list):
        if isinstance(my_list, list):
            change_list = [my_list[0], (my_list[my_list.__len__() - 1])]
            print(change_list)
        else:
            print("You don't give me a list!")
        return change_list

    def fibonacci_count(self):
        numb = int(input("Tell me how many Fibonacci numbers generate?: "))
        preindex = 0
        index = 1
        fibonacci_number = []
        for i in range(numb):
            preindex, index = index, preindex + index
            fibonacci_number.append(preindex)
        print(fibonacci_number)

    def my_own_set_function(self, input_list):
        if isinstance(input_list, list):
            new_list = []
            for y in input_list:
               if y in input_list and y not in new_list:
                   new_list.append(y)
        else:
            print("You dont give me a list!")
        return new_list

    def binary_search(self, input_list = [], search_element = 0):
        if input_list == [] or search_element == None:
            return None
        else:
            first = input_list[0]
            last = input_list.__len__() - 1

            while first < last:
                mid = round(first + (last - first) / 2)
                if (search_element <= input_list[mid]):
                    last = mid
                else:
                    first = mid + 1
            if (input_list[last] == search_element):
                return True
            else:
                return False

class SimpleGames:
    def game_rock_paper_scissiors(self,):
        # from pythonpractice
        print('''Please pick one:
                    rock
                    scissors
                    paper''')

        while True:
            game_dict = {'rock': 1, 'scissors': 2, 'paper': 3}
            player_a = str(input("Player a: "))
            player_b = str(input("Player b: "))
            a = game_dict.get(player_a)
            b = game_dict.get(player_b)
            dif = a - b

            if dif in [-1, 2]:
                print('player a wins.')
                if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
                    continue
                else:
                    print('game over.')
                    break
            elif dif in [-2, 1]:
                print('player b wins.')
                if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
                    continue
                else:
                    print('game over.')
                    break
            else:
                print('Draw.Please continue.')
                print('')

    def guessing_game_one(self):
        print("I generate a random number between 1 and 10, guess it!")
        rand_number = round(random.random()*10)
        user_input = int(input("? : "))
        if rand_number == user_input:
            print("Good you geues it! O_o")
        elif (user_input >= rand_number + 5) or (user_input <= rand_number - 5):
            print("Soo far T_T")
        elif (user_input >= rand_number + 3) or (user_input <= rand_number - 3):
            print("Not bad ^_^")
        elif (user_input >= rand_number + 1) or (user_input <= rand_number - 1):
            print("So near *_*")
        print(str(rand_number))

    def cows_and_bulls_game(self):
        random_generate = random.sample(range(10),4)
        cows = 0
        bulls = 0
        input_number = list(map(int, input("Welcome to the Cows and Bulls game! \nEnter 4 digit numbers: ")))
        if input_number.__len__() != 4:
            print("You give me wrong numbers, make sure you print 4 digit numbers")
            exit()
        else:
            for x in range(random_generate.__len__()):
                if random_generate[x] == input_number[x]:
                    cows += 1
            if list(set(random_generate) & set(input_number)) != []:
                bulls = list(set(random_generate) & set(input_number)).__len__() - cows
        print("cows: " + str(cows) + " bulls: " + str(bulls))
        print(random_generate)

class SundriesMethods:
    def reverse_words(self):
        # from pythonpractice   return ' '.join(input_words.split()[::-1])
        input_words = input("Tel me somthing: ")
        input_words = input_words.split(" ")
        output_words = " ".join(input_words[::-1])
        return output_words

    def password_generator(self):
        string_for_generate = "abcdefghijklmnopqrstuvwxyzABCDIFGHIJKLMNOPQRSTUVWXYZ0987654321"
        string_for_generate = list(string_for_generate)
        new_password = "".join(set(string_for_generate))
        return new_password[:9:]



class WebManipulations:
     def get_titles_urls(self):
        url = "https://habrahabr.ru/"
        get_html = bs4.BeautifulSoup(requests.get(url).text, 'html5lib')
        urls = []
        titles = []
        for titles_text in get_html.find_all("h2", {'class': 'post__title'}):
            combined_pat = r'|'.join(('\n', '\n\n', '  '))
            titles.append(re.sub(combined_pat, '', titles_text.text))
        for urls_of_titles in get_html.find_all("a", {'class': 'post__title_link'}, href=True):
            urls.append(urls_of_titles['href'])
        titles_and_urls_dict = dict(zip(titles,urls))
        return titles_and_urls_dict

     def site_parser(self):
        all_titles = []
        get_html = bs4.BeautifulSoup(requests.get("http://www.nytimes.com/").text, 'html.parser')
        for titles in get_html.find_all("h2", {'class': 'story-heading'}):
            combined_pat = r'|'.join(('\n', '\n\n', '  '))
            all_titles.append(re.sub(combined_pat, '', titles.text))
        return  all_titles
     ''' solution from python practice
        base_url = 'http://www.nytimes.com'
        r = requests.get(base_url)
        soup = BeautifulSoup(r.text)

        for story_heading in soup.find_all(class_="story-heading"):
            if story_heading.a:
                print(story_heading.a.text.replace("\n", " ").strip())
            else:
                print(story_heading.contents[0].strip())'''
     def write_result_to_file(self):
        text_data = self.site_parser()
        with open("titles_text.txt","wb") as file:
            for items in text_data:
                file.write(items.encode("utf-8") + "\n".encode("utf-8"))
            file.close()

a = [1, 1, 2, 3, 5, 8, 13, 3, 21, 1, 34, 55, 89]
b = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 11, 12, 13]
d = []
#myclass = SundriesMethods()
#myclass = SimpleGames()
myclass = WebManipulations()
#myclass = Mathematic()

c = myclass.write_result_to_file()
print(c)
