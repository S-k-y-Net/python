import math
import re
import random
import requests
import json
import bs4
import numpy
from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral6
from bokeh.plotting import figure
from bokeh.transform import factor_cmap


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
    def quick_sort(self, array):
        if array: return self.quick_sort([x for x in array if x<array[0]]) + [x for x in array if x==array[0]] + self.quick_sort([x for x in array if x>array[0]])
        return []

    def max_min_element(self,array):
        b = self.quick_sort(array)
        max = b[0]
        min = b[len(b) - 1]
        return max, min

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

    def guessing_game_two(self):
        _list = []
        print("Think about some number between 1-100 and I guess it: ")
        print(input("Ready?"))
        a = 0
        b = 100
        while b != 0:
            guess_number = round(a + random.random()*b)
            if not guess_number  in _list:
                _list.append(guess_number)
                print("You guess " + str(guess_number) + "?")
            else:
                continue
            player_answer = input()
            if player_answer == "Yes":
                print("It takes " + str(len(_list)) + " times.")
                break
            if player_answer == "too high":
                b = guess_number
            if player_answer == "too low":
                a = guess_number
                b = 100 - guess_number

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

    def tictactoe_board(self, n):
         #print("What size game board you want to draw? \n")
         game_board_size = n
         for i in range(game_board_size):
            print(" ---"*game_board_size)
            print("|   "*(game_board_size + 1))
         print(" ---" * game_board_size)

    def check_tictactoe(self,game_status = [], n = 0):
        # game_status = [[2, 2, 5], 
        #                [7, 5, 6],
        #                [5, 8, 1]]
        # n = 3
        transpose_game = numpy.transpose(game_status)
        for i in range(0,n):
            if len(set(game_status[i])) == 1 and game_status[i][0] != 0:
                return game_status[i][0]
            if len(set(transpose_game[i])) == 1 and transpose_game[i][0] != 0:
                return transpose_game[i][0]
            if len(set(numpy.diagonal(game_status))) == 1 and game_status[n - 1][0] != 0:
                return numpy.diagonal(game_status)[0]    
            if len(set(numpy.diag(numpy.fliplr(game_status)))) == 1 and game_status[0][n - 1] != 0:
                return numpy.diag(numpy.fliplr(game_status))[0]

    def base_tictactoe(self, board = [], n = 3):
        # board = [[0,0,0],
        #          [0,0,0],
        #          [0,0,0]]
        # n = 3
        #print("Let's play game! Print coordinate like (row,col) \n player 1")
        while self.check_tictactoe(board, n) is None:
            input_player_one = input()
            _a = input_player_one.split(",")
            board[int(_a[0]) - 1][int(_a[1]) - 1] = "x"
            #print(board)
            print("player 2")
            input_player_two = input()
            a = input_player_two.split(',')
            board[int(a[0]) - 1][int(a[1]) - 1] = "o"
            print("player 1")
        return self.check_tictactoe(board, n)


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

    def birthday_dictioanry(self):
        birth_dict = {"Archi" : "2 may 1988",
                      "Robert" : "3 April 1970",
                      "Charly" : "1 Jenuary 1995"
                      }
        print("Welcome to dictionary of birthdays: I know this persons")
        for i in birth_dict.keys():
            print(i)
        user_input = input("Whoes birthday you want know? \n")
        if user_input in birth_dict.keys():
            print("The birthday of " + user_input +birth_dict[i])
        else:
            print("Sorry I don't know who is this person '" +  user_input + "'")
    def json_birthday(file):
        num_to_string = {
        '01': "January",
        '02': "February",
        '03': "March", 
        '04': "April",
        '05': "May",
        '06': "June",
        '07': "July",
        '08': "August",
        '09': "September",
        '10': "October",
        '11': "November",
        '12': "December"
        }
        global month_list
        with open(file, 'r') as data_file:
            month_list = []
            data = json.load(data_file)
            for i in data.keys():
                a_list = []
                data_list = data[i].split('.')
                for x in data_list:
                    a_list.append(x)
                month_list.append(num_to_string[a_list[1]])
            print(Counter(month_list))
            print("Welcome to dictionary of birthdays: I know this persons")
            for i in data.keys():
                print(i)
            user_input = input("Whoes birthday you want know? \n")
            if user_input in data.keys():
                print("The birthday of " + user_input + ' ' + data[i])
            else:
                print("Sorry I don't know who is this person '" +  user_input + "'")
            data_file.close()
        output_file("bar_colormapped.html")
        b_list = []
        for i in data.keys():
            data_ls = data[i].split('.')
            b_list.append(data_ls[1])

        list_b = b_list
        print(month_list)
        list_a = month_list
        source = ColumnDataSource(data=dict(list_a = list_a, list_b = list_b))
        p = figure(x_range=list_a, plot_height=350, toolbar_location=None, title="Fruit Counts")
        p.vbar(x='list_a', top='list_b', width=1.5, source=source, legend="list_a",
           line_color='white', fill_color=factor_cmap('list_a', palette=Spectral6, factors=list_a))

        p.xgrid.grid_line_color = None
        p.y_range.start = 0
        p.y_range.end = 9
        p.legend.orientation = "horizontal"
        p.legend.location = "top_center"

        show(p)

        adding = input("Do you want add a new line in birthday dict? (Y,N) ")
        if adding.upper() == "Y":
            print("Print 'exit' for finishing!")
            _dict = data
            def adding_person():
                name = input("Enter person name: ")
                if 'exit' == name:
                    return _dict
                date = input("Enter person birthday date: ")
                if 'exit' == date:
                    return _dict
                else:
                    _dict[name] = date
                    adding_person()
            adding_person()
            with open(file , 'w') as write_file:
                json.dump(_dict,write_file)


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
     def read_from_file(self):
        _file = "C:/Max/nameslist.txt"
        with open(_file) as file:
            return len(file.readlines())

     def two_files_overlapping(self, file_one, file_two):
        with open(file_one, 'r') as _file_one:
            _text_one = set(map(lambda s: s.strip(),_file_one.readlines()))
        with open(file_two, 'r') as _file_two:
            _text_two = set(map(lambda s: s.strip(),_file_two.readlines()))
        intersections = _text_one.intersection(_text_two)
        return sorted([int(x) for x in intersections])


a = [1, 1, 2, 3, 5, 8, 13, 3, 21, 1, 34, 55, 89]
b = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 11, 12, 13]
d = []
myclass = SundriesMethods()
#myclass = SimpleGames()
#myclass = WebManipulations()
#myclass = Mathematic()

c = myclass.birthday_dictioanry()
#print(c)
