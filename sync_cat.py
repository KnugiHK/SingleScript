import os, time

SECTOR_SIZE = 512
BYTE_SIZE_MULTIPLIER = 100

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '=', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    Refernce: https://gist.github.com/snakers4/91fa21b9dda9d055a02ecd23f24fbc3d
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} [{bar}] {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

def main(src, dest):
    with open(dest, "r+b") as dest_f:
        dest_size = os.path.getsize(dest)
        src_size = os.path.getsize(src)
        dest_last_pos = int(dest_size*0.99) # get last 1% byte for confirmation
        dest_f.seek(dest_last_pos)
        target = dest_f.read()
        len_target = len(target)
        with open(src, "rb") as src_f:
            # navigate to same position as destination file
            src_f.seek(dest_last_pos)
            # read confirmation byte from source file
            source = src_f.read(len_target)
            if source == target:
                # sync the position of source and destination file
                src_f.seek(dest_last_pos + len_target, 0)
                dest_f.seek(dest_size, 0)
                
                dest_f_pos = dest_f.tell()
                i = 0
                last_timer = timer = time.time()
                speed = 0
                printProgressBar(dest_f_pos, src_size, prefix = 'Syncing file:', suffix = 'Completed (0MB/s)', length = 40)
                while dest_f_pos < src_size: # Start to sync file from this block
                    timer = time.time()
                    byte_to_write = SECTOR_SIZE * BYTE_SIZE_MULTIPLIER
                    if dest_f_pos + byte_to_write > src_size:
                        byte_to_write = src_size - dest_f_pos
                    dest_f.write(src_f.read(byte_to_write))
                    dest_f.flush()
                    dest_f_pos = dest_f.tell()
                    
                    i += 1
                    if timer - last_timer >= 1: # update the rate every second
                        last_timer = timer
                        speed = int(byte_to_write/1024/1024 * i)
                        i = 0
                    printProgressBar(dest_f_pos, src_size, prefix = 'Syncing file:', suffix = f'Completed ({speed}MB/s)', length = 40)
                    
            else:
                pass
    
if __name__ == "__main__":
    from optparse import OptionParser
    parser = OptionParser(version='1')
    (options, args) = parser.parse_args()
    if len(args) == 2:
        if os.path.isfile(args[0]) and os.path.isfile(args[1]):
            main(args[0], args[1])
        else:
            exit("Path(s) you entered is not valid")
    else:
        exit("You must provide exactly two paths.")
