# from midi2audio import FluidSynth

from lib.midi2audio import FluidSynth

print("start")


# fluidsynth: error: fluid_is_soundfont(): fopen() failed: 'File does not exist.'
# Parameter 'C:\Users\russj/.fluidsynth/default_sound_font.sf2' not a SoundFont or MIDI file or error occurred identifying it.
# fluidsynth: error: fluid_sfloader_load(): Failed to open 'C:\ProgramData\soundfonts\default.sf2': File does not exist.
# fluidsynth: error: Unable to open file 'C:\ProgramData\soundfonts\default.sf2'
# fluidsynth: error: ipatch_file_open() failed with error: 'No such file or directory'
# fluidsynth: error: Failed to load SoundFont "C:\ProgramData\soundfonts\default.sf2"

# https://www.polyphone.io/en/soundfonts/pianos/1404-tinpots-piano-collection

# https://archive.org/download/free-soundfonts-sf2-2019-04
def main():

    print('main')

    sound_font = 'sf2/SGM-v2.01-NicePianosGuitarsBass-V1.2.sf2'

    # https://github.com/bzamecnik/midi2audio/blob/master/midi2audio.py#L42C24-L42C34
    # fs = FluidSynth(
    #     sound_font='Roland_SC-55_v1.1-full-pack.sf2'
    # )
    fs = FluidSynth(
        sound_font=sound_font,
        gain=1.0
    )
    fs.midi_to_audio('frere-jacques.mid', '../assets/frere-jacques.wav')
    # FluidSynth().midi_to_audio('frere-jacques.mid', 'frere-jacques.mp3')




main()