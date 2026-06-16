import pydub

def preobrazovator(filename, export_name, format):
    obj = pydub.AudioSegment.from_file(f'{filename}', format=f'{format}')
    obj.export(f'{export_name}', format='mp3')

#preobrazovator('Gats.m4a', 'Gats.mp3', 'm4a')

