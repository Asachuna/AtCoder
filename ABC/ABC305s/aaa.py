def solution(intervals):
    #intervalsをstart時間順にソート
    intervals.sort(key=lambda x:x[0])

    #現在の最も遅いend時間
    current_end = -1

    result = []

    for interval in intervals:
        start = interval[0]
        end = interval[1]

        #かぶりがない場合
        if (start > current_end):
            result.append([start, end])
        
        #かぶりがある場合
        else:
            #最終時間を上書き
            result[len(result)-1][1] = max(end, result[len(result)-1][1])
        
        current_end = result[len(result)-1][1]


    return result

print(solution([[1,3],[0,3],[4,5]]))