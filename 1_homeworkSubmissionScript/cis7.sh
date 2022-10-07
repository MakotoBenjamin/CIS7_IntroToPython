#! /bin/bash

echo "What Chapter is your homework for: "
read chapter

echo "Enter the number of assignments you will be submitting: "
read numAssignments

i=1

while [[ $i -le $numAssignments ]];do
       echo "Enter the file name for assignment # $i:"
       read assignment
       
       CWD=$(pwd)

       echo -e  "\n-- Question $assignment Source Code --\n" >> $CWD/ch$chapter.txt
       cat $assignment.py >> $CWD/ch$chapter.txt

       #echo "How many inputs does your assignment have?"
       #read inputs
       
       #counter=0

       #while [[ $counter -le $inputs ]];do
       #     echo "Enter the value of the input #$counter"
       #     read userVal
       #     userVal >> inputs_$assignment.txt
       #done

       echo "Does the assignment have an image output? "
       read response 

        if [ $response == "y" ]
        then
                echo -e "\n-- Question $assignment Output --\n\nSee separately attached image" >> $CWD/ch$chapter.txt
        else
                echo -e "\n-- Question $assignment Output --\n" >> $CWD/ch$chapter.txt

        #        python3 ./$assignment.py < inputs_$assignment.txt  >> $CWD/ch$chapter.txt
        fi
       
        ((i += 1))
        
done


