import random
import pythonbot_lyrics

def get_var_name(value, variables_dict):
    var_names = [
        var_name for var_name, var_value in variables_dict.items()
        if var_value == value
    ]
    return ', '.join(var_names)

def check_if_used(rand_track, rand_lyrics):
    while music[list(music.keys())[rand_track]][rand_lyrics] in already_used:
        rand_track = random.randint(0, len(music)-1)
        rand_lyrics = random.randint(0, len(music[list(music.keys())[rand_track]])-1)
    already_used.append(music[list(music.keys())[rand_track]][rand_lyrics])
    return rand_track, rand_lyrics


#list of lyrics that has been already used
already_used = []


#{} in order to get variable name from " " 
music = {"track1": pythonbot_lyrics.track1, "track2": pythonbot_lyrics.track2}

#drawing random number 
rand_track = random.randint(0, len(music)-1)
rand_lyrics = random.randint(0, len(music[list(music.keys())[rand_track]])-1)

#def checking if lyric has been already used
rand_track, rand_lyrics = check_if_used(rand_track, rand_lyrics)

print("music: " + get_var_name(music[list(music.keys())[rand_track]], music))
print("lyrics: " + music[list(music.keys())[rand_track]][rand_lyrics])

