import sys

def main():
    print('Try to get 4L of water into one of these buckets:')

    buckets = {'8': 0, '5': 0, '3': 0}
    moves = 0

    while True:
        waterInBucket = []
        for i in range(8):
            if buckets['8'] > i:
                waterInBucket.append('~~~~~~')
            else:
                waterInBucket.append('      ')
        
        for i in range(5):
            if buckets['5'] > i:
                waterInBucket.append('~~~~~~')
            else:
                waterInBucket.append('      ')
        for i in range(3):
            if buckets['3'] > i:
                waterInBucket.append('~~~~~~')
            else:
                waterInBucket.append('      ')

        if any(value == 4 for value in buckets.values()):
            print('You win!')
            print('You\'ve finished the game in {} moves.'.format(moves))
            sys.exit()

        print('''
8|{7}|
7|{6}|
6|{5}|
5|{4}|  5|{12}|
4|{3}|  4|{11}|  
3|{2}|  3|{10}|  3|{15}|
2|{1}|  2|{9}|  2|{14}|
1|{0}|  1|{8}|  1|{13}|
 +------+   +------+   +------+
    8L         5L         3L
'''.format(*waterInBucket))
    
        while True:
            print('''You can:
    (F)ill the bucket
    (E)mpty the bucket
    (P)our one bucket into another
    (Q)uit''')

            action = input('> ').upper()
            if action.startswith(('F', 'E', 'P', 'Q')):
                action = action[0]
                break

        if action == 'Q':
            sys.exit()

        elif action == 'F':
            while True:
                print('Choose a bucket to fill')
                bucket = input('> ')
                if bucket in ('8', '5', '3'):
                    break

            buckets[bucket] = int(bucket)
            print()

        elif action == 'E':
            while True:
                print('Choose a bucket to empty')
                bucket = input('> ')
                if bucket in ('8', '5', '3'):
                    break

            buckets[bucket] = 0
            print()

        else:
            print('Choose a bucket to pour from')
            fromBucket = input('> ')
            print('Choose a bucket to pour into')
            toBucket = input('> ')
            print()

            fromBucketWater = buckets[fromBucket]
            toBucketWater = buckets[toBucket]

            waterPoured = min(int(toBucket) - toBucketWater, fromBucketWater)
            
            buckets[toBucket] = (toBucketWater + waterPoured)
            buckets[fromBucket] = max(fromBucketWater - waterPoured, 0)

        moves += 1
        
if __name__ == '__main__':
    main()