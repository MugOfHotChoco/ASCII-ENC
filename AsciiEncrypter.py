import string

#######################################################
#=====================================================#
#===============#Importation Functions#===============#
#=====================================================#
#######################################################

encodedict = {"a": "↑" , "b": "←" ,"c":"→","d":"↓","e":"·","f":"•","g":"●","h":"–","i":"—","j":"―","k":"‽","l":"‖","m":"«","n":"»","o":"‹","p":"›","q":"‘","r":"’","s":"“","t":"”","u":"„","v":"‚","w":"❝","x":"❞","y":"⌘","z":"","1":"⌥","2":"⇧","3":"⇪","4":"⌫","5":"⌦","6":"␡","7":"⎋","8":"␛","9":"⏎","0":"↩","A":"␣","B":"¬","C":"¶","D":"§","E":"©","F":"®","G":"™","H":"°","I":"℃","J":"℉","K":"≠","L":"±","M":"√","N":"‰","O":"Ω","P":"∞","Q":"≈","R":"ƒ","S":"¼","T":"½","U":"¾","V":"†","W":"‡","X":"․","Y":"‥","Z":"…","!":"➥","\"":"➽","£":"☚","$":"☜","%":"☛","^":"☞","&":"★","*":"☆","(":"♠",")":"♣","{":"♥","}":"♦","[":"♪","]":"♫","~":"♯","#":"♀",":":"♂",";":"∂","@":"∄","'":"∅","<":"∆",">":"∇",",":"∈",".":"∉","?":"∋","/":"∌","\\":"∎","|":"∓"};

def EncodingDictChange(Dictionary: dict) -> bool:
    global encodedict;
    for char1, char2 in Dictionary.items():
        tempDictionary = Dictionary.copy();
        tempDictionary.pop(char1);
        for char in tempDictionary:
            if char2 == tempDictionary.get(char):
                print(f"2 instances of the character \"{char2}\" withing encoding dictionary.")
                return False;
    encodedict = Dictionary;
    return True;

#EncodingDictChange(encodedict); ##Just For Me To Check That The Defualt Argument Doesn't have any duplicates.
DEFAULTDICT = encodedict;

def Encrypt(txt: any , output: bool = False, Dictionary = None) -> str:
    global encodedict;
    if Dictionary == None:
        Dictionary = encodedict;
    if output:    
        print(f"Encrypting: {txt}")
    txt = str(txt).replace(" " ,"_");
    allowed = set(string.ascii_letters + string.digits + "!\"£$%^&*()-+=}][{#~@':;/?.><,/?\\|  _\n\t")
    if set(txt) <= allowed:
        for orgchar,newchar in Dictionary.items():
            txt = txt.replace(orgchar,newchar);
        if output:
            print(f"Outputted: {txt}");
        return txt;
    else:
        txt.replace("_"," ");
        print(f"{txt} could not be Encrypted...")
        if "--ERROR ENCRYPTING" not in txt:
            return txt + "\n--ERROR ENCRYPTING";
        else:
            return txt;

def Decrypt(txt: any, output: bool = False, Dictionary = None) -> str:
    global encodedict;
    if Dictionary == None:
        Dictionary = encodedict;
    if output:
        print(f"Decrypting: {txt}");
    txt = txt.replace("_"," ");
    for newchar ,orgchar in Dictionary.items():
        txt = txt.replace(orgchar ,newchar);
    if output:
        print(f"Outputted: {txt}")
    return txt;

#############################################################
#===========================================================#
#======================#GUI Functions#======================#
#===========================================================#
#############################################################

def EncryptFile():
    global FileCryptation;
    global FileOutput;
    filetoencrypt = FileCryptation.get();
    if "." not in filetoencrypt and ".[noext]" not in filetoencrypt:
        filetoencrypt += ".txt"
    filetoencrypt = filetoencrypt.replace(".[noext]" ,"");
    fileread = open(filetoencrypt ,"r");
    read = fileread.read();
    fileread.close();
    filetoutput = FileOutput.get();
    if "." not in filetoutput and ".[noext]" not in filetoutput:
        filetoutput += ".txt"
    filetoutput = filetoutput.replace(".[noext]" ,"");
    filewrite = open(filetoutput ,"w");
    filewrite.write(Encrypt(read));
    filewrite.close();

def DecryptFile():
    global FileCryptation;
    global FileOutput;
    filetoencrypt = FileCryptation.get();
    if "." not in filetoencrypt:
        filetoencrypt += ".txt"
    filetoencrypt = filetoencrypt.replace(".[noext]" ,"");
    fileread = open(filetoencrypt ,"r");
    read = fileread.read();
    fileread.close();
    filetoutput = FileOutput.get();
    if "." not in filetoutput:
        filetoutput += ".txt"
    filetoutput = filetoencrypt.replace(".[noext]" ,"");
    filewrite = open(filetoutput ,"w");
    filewrite.write(Decrypt(read));
    filewrite.close();

#########################################################
#=======================================================#
#========================#Main()#=======================#
#=======================================================#
#########################################################

def Main() -> None:
    #######################
    #       Tkinter       #
    #######################
    import tkinter
    #########################
    #    Global Variables   #
    #########################
    global win;
    global FileCryptation;
    global FileOutput;
    #######################
    #    Window Set-Up    #
    #######################
    win = tkinter.Tk();
    win.configure(background="black");
    win.title("The File Encrypter");
    #win.geometry("260x150");#
    #win.resizable(False,False);#
    tkinter.Label(win  ,text="File To Encrypt/Decrypt:"  ,bg="black" ,fg="lightgreen").pack();
    FileCryptation=tkinter.Entry(win ,highlightthickness=0 , width=25 , borderwidth=2 , background="black" , foreground="lightgreen");
    FileCryptation.pack(padx=20)
    tkinter.Label(win ,text="File Output to (Will be overwritten!):" ,bg="black" ,fg="lightgreen").pack();
    FileOutput=tkinter.Entry(win ,highlightthickness=0 , width=25 , borderwidth=2 , background="black" , foreground="lightgreen");
    FileOutput.pack(padx=20)
    tkinter.Button(win ,highlightbackground="black" ,highlightcolor="lightblue" ,activebackground="black" ,activeforeground="lightgreen" ,text="Encrypt" ,command=EncryptFile ,bg="black" ,fg="green").pack(pady=5 , padx=10 , side="left");
    tkinter.Button(win ,highlightbackground="black" ,highlightcolor="lightblue" ,activebackground="black" ,activeforeground="lightgreen" ,text="Decrypt" ,command=DecryptFile ,bg="black" ,fg="green").pack(pady=5 , padx=10 , side="right");
    win.mainloop();
    #######################
    return None;

if __name__ == "__main__":
    Main();