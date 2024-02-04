def LIS(seq):
    def _LIS(seq, cur, last):
        '''
        seq: sequence to find the Longest Increasing Subsequence
        cur: current position in the sequence
        last: last position in the subsequence
        '''
        if cur == len(seq): return 0

        # option to leave the seq[cur]
        leave = _LIS(seq, cur+1, last)

        # option to keep seq[cur]. Only if first element or if seq[cur] > seq[last]
        keep = 0
        if last == -1 or seq[cur] > seq[last]:
            keep = 1 + _LIS(seq, cur+1, cur)

        return max(leave, keep)

    return _LIS(seq,0,-1)


if __name__ == "__main__":
    seq = [1,3,2,5,7]
    nb_max = LIS(seq)
    print(f'result = {nb_max}')