    ###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~###
import random
import time
prisoners = ([i for i in range(0,100)])
#creates list of prisoners numbered 0-99
shuffled_prisoners = random.sample(prisoners, len(prisoners))
#randomizes prisoner list
shuffled_list = random.sample(prisoners, len(prisoners))
#randomizes prisoner list to get the best possible random boxes
boxes = [(k, v) for k,v in enumerate(shuffled_list)]
#creates list of tuples from the shuffled list.  
def main(prisoners):
   
    """Takes prisoner list and facilitates and records and returns the final results"""
   
    final_freed_prisoners = 0
   
    for prisoner in prisoners:     
        prisoner_num = prisoner
        the_next_num = prisoner_num
        print(f"Prisoner {prisoner_num}:\n------------Try")
        outcome = prisoner_loop(prisoner_num, the_next_num)
        
   
        if outcome >= 1:
            final_freed_prisoners += 1
        else: 
            print(f"------------\033[1;31;40mXXX\033[0;37;40m\n\n")
   
    return print(f"\n*******{final_freed_prisoners} prisoners found their number********")


def prisoner_loop(prisoner_num, the_next_num):
    
    """Takes in prisoner number and the number 'inside' the box to map it to the attempt box, if prisoner finds box with his number returns 1 else 0"""
    
    freed_prisoners = 0

    for attempt in range(50):
        next_num_tup = boxes[the_next_num]
        format_number = [len(str(i)) for i in next_num_tup]
        format_output = format_number[0] + format_number[1]
        the_next_num = next_num_tup[1]
        perty_print(format_number, format_output, next_num_tup, attempt)

        if the_next_num == prisoner_num:
            freed_prisoners += 1
            print(f"------------\033[1;32;40m!!!\n\033[0;37;40m")
            break
    return freed_prisoners

def perty_print(format_number,format_output, next_num_tup, attempt):

    """takes in the length of characters in the output as well as the printed output
    itself and prints them out with proper spacing depending on their length.  There 
    is probably a better way to go about this, also i am still not happy with the 
    output.  need to unpack the tuples and do it the right way."""

    if format_output == 4:
        print(next_num_tup, "---", attempt + 1)

    elif format_output == 3:
        print(next_num_tup, " ---", attempt + 1)

    else:
        print(next_num_tup, "  ---", attempt + 1)

if __name__ == "__main__":
    #threw this loop in for funzies.  
    for i in range(100):
        print(f"calculating prisoner path : \033[1;32;40m {i + 1}% \033[0;37;40m" + "\033[0,31,47m|" * i, end = "\r")
        time.sleep(.01)
    print("\a")
    main(shuffled_prisoners)
