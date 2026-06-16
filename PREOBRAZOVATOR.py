import pydub

def preobrazovator(filename, export_name, input_format, export_format):
    obj = pydub.AudioSegment.from_file(f'{filename}', format=f'{input_format}')
    obj.export(f'{export_name}', format=f'{export_format}')

#preobrazovator('Gats.m4a', 'Gats.mp3', 'm4a')

