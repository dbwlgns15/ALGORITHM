def solution(id_list, report, k):
    report = set(report)
    
    report_cnt = {}
    reporter = {}
    for i in id_list:
        report_cnt[i] = 0
        reporter[i] = []
        
    for i in report:
        a, b = i.split()[0], i.split()[1]
        report_cnt[b] += 1
        reporter[b] += [a]
        
    chk = []
    for i in id_list:
        if report_cnt[i] >= k:
            chk += reporter[i]
            
    answer = [chk.count(i) for i in id_list]
    return answer