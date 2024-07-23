#qr ticket number generator (using random)
import random
import segno


def rand_generator():
    flag = 1
    while flag == 1:
        flag = 0
        content = random.randrange(0,10000)     
        f = open("valid_keys.txt","r")          #holds ticket number (key) for validation when client produces their qr ticket
        check = f.readlines()                   #opens validation keys line by line

        for line in check:
            if(content == int(line)):                #checks if generated random number is in validation file or not
                flag = 1
                f.close()
                break
        f.close()

    
    #if(flag == 1):                          #if yes, new random number must be generated and the function is called inside
    #    content = rand_generator()

    #else:                                   #if the random number is unique, the number is saved and returns value to main function
    w = open("valid_keys.txt","a")
    w.write(str(content) + '\n')
    w.close()
    return content


for x in range(1,401):

    qr_content = rand_generator()

    qrcode = segno.make_qr("%s" % qr_content)
    qrcode.save("%s.png" % x,
                scale = 15,
                border=2,
                light="maroon",
                #quiet_zone="black",
    )