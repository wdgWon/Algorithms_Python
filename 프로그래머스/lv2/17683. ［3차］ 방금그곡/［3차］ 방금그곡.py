def solution(m, musicinfos):
    m = m.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
    answer = ('(None)', None)
    for musicinfo in musicinfos:
        start_time, end_time, title, melody = musicinfo.split(',')
        melody = melody.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
        start_hour, start_minute = map(int,start_time.split(':'))
        end_hour, end_minute = map(int,end_time.split(':'))
        play_time = (end_hour - start_hour) * 60 + (end_minute - start_minute)
        
        actual_melody = (melody * (play_time // len(melody))) + melody[:play_time % len(melody)]
        
        if m in actual_melody:
            if answer[1] == None or play_time > answer[1]:
                answer = (title, play_time)
                
    return answer[0]
