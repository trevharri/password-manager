# def add_pass():
#     web_site = web_input.get()
#     user = user_input.get()
#     password = pass_input.get()
#     password_data = f"{web_site} | {user} | {password}"
#
#     is_ok = False
#     if len(web_site) == 0 or len(password) == 0 or len(user) == 0:
#         messagebox.showinfo(title="Error", message="Please don't leave any fields blank.")
#     else:
#         is_ok = messagebox.askokcancel(title=web_site, message=f"There are the details entered.\nEmail: {user}"
#                                                                f"\nPassword: {password}\n Is it okay to save?")
#     if is_ok:
#         with open("passwords.txt") as file:
#             contents = file.read()
#         if web_site not in contents:
#             with open("passwords.txt", "a") as file:
#                 file.write(f"\n{password_data}")
#             clear_fields()
#         else:
#             contents_list = contents.split()
#             index = contents_list.index(web_site)
#             index_pass = index + 4
#             contents_list[index_pass] = password
#             new_contents = ""
#             for n in range(0, len(contents_list)):
#                 if n == len(contents_list) - 1:
#                     new_contents += contents_list[n]
#                 elif (n + 1) % 5 == 0:
#                     new_contents += contents_list[n]
#                     new_contents += "\n"
#                 else:
#                     new_contents += contents_list[n]
#                     new_contents += " "
#             with open("passwords.txt", "w") as file:
#                 file.write(new_contents)
#             clear_fields()
