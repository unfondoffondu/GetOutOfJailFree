

	###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~###
import random
prisoners = ([i for i in range(0,100)])
#creates list of prisoners numbered 0-99
shuffled_prisoners = random.sample(prisoners, len(prisoners))
#randomizes prisoner list
shuffled_list = random.sample(prisoners, len(prisoners))
#randomizes prisoner list to get the best possible random boxes
boxes = [(k, v) for k,v in enumerate(shuffled_list)]
#creates a linked list of tuples of random numbers
def main(prisoners, boxes):
	"""Takes prisoner list and linked list representing boxes. Records and returns the final results"""
	count = 0
	final_freed_prisoners = 0
	for prisoner in prisoners:     
	    prisoner_num = prisoner
	    the_next_num = prisoner_num
	    print(f"Prisoner {prisoner_num}:\n------------Try")
	    outcome = prisoner_loop(prisoner_num, the_next_num)
	    count += 1
	    if outcome >= 1:
	    	final_freed_prisoners += 1
	    else: 
	    	print(f"------------XXX\n\n")
	return print(f"\n*******{final_freed_prisoners} prisoners found their number********")
def prisoner_loop(prisoner_num, the_next_num):
	"""Takes in prisoner number and the number 'inside' the box to map it to the next box, if prisoner finds box with his number returns 1 else 0"""
	
	freed_prisoners = 0
	for next in range(50):
	    next_num_tup = boxes[the_next_num]
	    format_number = [len(str(i)) for i in next_num_tup]
	    format_output = format_number[0] + format_number[1]
	    the_next_num = next_num_tup[1]
	    perty_print(format_number, format_output, next_num_tup, next)
	    if the_next_num == prisoner_num:
	       	freed_prisoners += 1
	       	print(f"------------!!!\n")
	       	break
	    else:
	    	continue
	return freed_prisoners
def perty_print(format_number,format_output, next_num_tup, next):
	if format_output == 4:
	    print(next_num_tup, "---", next + 1)
	elif format_output == 3:
	    print(next_num_tup, " ---", next + 1)
	else:
		print(next_num_tup, "  ---", next + 1)



if __name__ != 'public static void main(String[] args)':
	main(shuffled_prisoners, boxes)