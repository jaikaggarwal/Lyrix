import random

def randomly_select_indices(total_num, num_to_choose):
    sequence = range(total_num)

    selected_indices = []
    for i in range(num_to_choose):
        random_num = random.choice(sequence)
        selected_indices.append(random_num)

    return selected_indices



def mask_song(song_lyrics, num_words_to_remove):


    song_list = song_lyrics.split(" ")
    # Create a new string with some of the words remove

    indices = randomly_select_indices(len(song_list), num_words_to_remove)

    # Goal: remove the indices that we don't want

    return new_song

def interact_with_user(real_song, masked_song):
    print(masked_song)
    user_guess = input("Type the whole song!: ")
    is_user_correct = real_song == user_guess

    if is_user_correct:
        print("Congratulations! You are now moving on to level two. Please choose your next song.")
    else:
        print("Sorry, you're wrong. Try again!")
        interact_with_user(real_song, masked_song)
    return





if __name__ == "__main__":
    example_song = "I can't think of anything right now but I will think of some later."
    new_song_lyrics = mask_song(example_song, 3)
    interact_with_user(example_song, new_song_lyrics)



