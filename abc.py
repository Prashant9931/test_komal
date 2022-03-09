# # import requests
# #
# # api_key='9f014d34a98f11d1546706ce3c803853'
# # blank=' \\b'
# # q= f'api_key={api_key}&query={blank}&reverse=false'
# # q1='api_key=9f014d34a98f11d1546706ce3c803853&query=''&reverse=false'
# # url = f"https://api.themoviedb.org/3/search/movie?{q}"
# # print(q)
# # payload = {}
# # headers= {}
# #
# # response = requests.request("GET", url, headers=headers, data = payload)
# #
# # print(response.text.encode('utf8'))
#
#
# # import requests
# #
# # url = "https://api.themoviedb.org/3/search/movie?api_key=9f014d34a98f11d1546706ce3c803853&query=''&reverse=false"
# #
# # payload = {}
# # headers= {}
# #
# # response = requests.request("GET", url, headers=headers, data = payload)
# #
# # print(response.text.encode('utf8'))
# #
# # import requests,json
# #
# # url = "https://api.themoviedb.org/3/search/movie?api_key=9f014d34a98f11d1546706ce3c803853&query='\\b'&reverse=false&page=1"
# #
# # payload = {}
# # headers= {}
# #
# # response = requests.request("GET", url, headers=headers, data = payload)
# #
# # print(len(response.json().get('results')))
#
#
# def test_args(a, c, b=5):
#     print(a, b)
#
#
# #
# #
# # def test_args1(*args):
# #     print(*args)
# #
# #
# # test_args1(1, 2, 3, 4, 5)
# #
# # response_data = {"key":15}
# #
# #
# # def test_global_var():
# #     global response_data  # declaration
# #     response_data['key'] = 5
# #
# #
# # def test_refrence(temp_response):
# #     temp_response['key'] = 11
# #
# #
# # test_refrence(response_data)
# #
# #
# #
# # print(response_data)
#
# #
# # Lists functions
# # sort methods
# # slicing
# # Data structure ==>
#
#
# l = [1, 3, 4, 66, 77]
# n = len(l)
# print(l[-1])
# print(l[n - 1])
#
# # if we need design a way to access data that is comming first and when you will aceess it will use it in last
#
# l = [1, 2, 3, 5, 6]
#
# stack = []
# for i in l:
#     stack.append(i)
#
# print(stack)
#
# # Reverse a list
#
# #
#
# # stack = [1, 2, 4, 5, 6]
# # reverse_lst = [6, 5, 4, 2, 1]
#
#
# # Large request
# #
# # name_list=['','','']
# #
# # for i in dict:
#
# with open("t1.txt") as file_in:
#     lines = []
#     for line in file_in:
#         l = line.strip()
#         lines.append(l)
#
# ll=[]
# for i in lines:
#     if i:
#         ll.append(i)
# print(ll)


a_list = ["abc", "def", "ghi"]
textfile = open("a_file.txt", "w")
for element in a_list:
    textfile.writelines(element)
textfile.close()