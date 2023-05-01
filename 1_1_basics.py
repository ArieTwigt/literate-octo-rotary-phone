## Assignments
import time

#%%
naam = "arie"
leeftijd = 33

#%%
naam + str(leeftijd)

#%% format strings
print("Vertel iets over jezelf")
print(f"Hallo ik ben {naam}\nik ben {leeftijd} oud")
print("Interessant")

# %%
print("Laden....")
time.sleep(5)
print("🎉Klaar!!")


#%%
print("❤️"*10)



### Assignments

#%% Assignment 1
first_name = "Erling"
last_name  = "Haaland"

full_name = "{} {}".format(first_name, last_name)
full_name

# %% a.
full_name = f"{full_name} Jr."

# %% b.
full_name + " " + ".Jr"

#%% c.
"{} .Jr".format(full_name)

# %% Assignment 2
#%%
full_name_list = full_name.split(" ")
full_name_list[0][0]

#%% a. 
full_name_list = full_name.split(" ")
full_name_new = full_name_list[0][0] + ". " + full_name_list[1] + full_name_list[2]
full_name_new

# %% b.
full_name_new_2 = first_name[0] + ". " + last_name + " .Jr"
full_name_new_2

# %% c.
full_name_list = full_name.split(" ")
full_name_new_3 = "{}. {} .{}".format(full_name_list[0], full_name_list[1], full_name_list[2])

# %% d.
full_name_split = full_name.split(" ")
# %%
first_name = full_name_split[0]
last_name = full_name_split[1]
third_name = full_name_split[2]

full_name_new = f"{first_name[0]}. {last_name} {third_name}"
full_name_new

# %% Assignment 3
flower_list_1 = ['rose', 'lily', 'tulip']
flower_list_2 = ['dandelion', 'gerbera']

combined_flower_list = flower_list_1 + flower_list_2
# %% a. 
combined_flower_list[1] = "daisy"
combined_flower_list

# %% b. 
idx_tulip = combined_flower_list.index("tulip")
combined_flower_list[idx_tulip] = "daisy"
combined_flower_list

# %% c.
combined_flower_str = "-".join(combined_flower_list).replace("tulip", "daisy")

combined_flower_list_new = combined_flower_str.split("-")
combined_flower_list_new

# %%
