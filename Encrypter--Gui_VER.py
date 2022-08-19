import tkinter
import string
win = tkinter.Tk();
win.configure(background="black");
win.title("The File Encrypter");

def Encrypt(txt: any) -> str:
    print(f"Encrypting: {txt}")
    txt = str(txt).replace(" ","_");
    allowed = set(string.ascii_letters + string.digits + "!\"£$%^&*()-+=}][{#~@':;/?.><,/?\\|  _\n\t")
    if set(txt) <= allowed:
        encode = [["a","←"],["b","↑"],["c","→"],["d","↓"],["e","·"],["f","•"],["g","●"],["h","–"],["i","—"],["j","―"],["k","‽"],["l","‖"],["m","«"],["n","»"],["o","‹"],["p","›"],["q","‘"],["r","’"],["s","“"],["t","”"],["u","„"],["v","‚"],["w","❝"],["x","❞"],["y","⌘"],["z",""],["1","⌥"],["2","⇧"],["3","⇪"],["4","⌫"],["5","⌦"],["6","␡"],["7","⎋"],["8","␛"],["9","⏎"],["0","↩"],["A","␣"],["B","¬"],["C","¶"],["D","§"],["E","©"],["F","®"],["G","™"],["H","°"],["I","℃"],["J","℉"],["K","≠"],["L","±"],["M","√"],["N","‰"],["O","Ω"],["P","∞"],["Q","≈"],["R","ƒ"],["S","¼"],["T","½"],["U","¾"],["V","†"],["W","‡"],["X","․"],["Y","‥"],["Z","…"],["!","➥"],["\"","➽"],["£","☚"],["$","☜"],["%","☛"],["^","☞"],["&","★"],["*","☆"],["(","♠"],[")","♣"],["{","♥"],["}","♦"],["[","♪"],["]","♫"],["~","♯"],["#","♀"],[":","♂"],[";","∂"],["@","∄"],["'","∅"],["<","∆"],[">","∇"],[",","∈"],[".","∉"],["?","∋"],["/","∌"],["\\","∎"],["|","∓"]];
        for convert in encode:
            txt = txt.replace(convert[0],convert[1]);
        return txt;
    else:
        print(txt)
        if "--ERROR ENCRYPTING" not in txt:
            return txt + "\n--ERROR ENCRYPTING";
        else:
            return txt;
def Decrypt(txt: any) -> str:
    txt = txt.replace("_"," ");
    encode = [["a","←"],["b","↑"],["c","→"],["d","↓"],["e","·"],["f","•"],["g","●"],["h","–"],["i","—"],["j","―"],["k","‽"],["l","‖"],["m","«"],["n","»"],["o","‹"],["p","›"],["q","‘"],["r","’"],["s","“"],["t","”"],["u","„"],["v","‚"],["w","❝"],["x","❞"],["y","⌘"],["z",""],["1","⌥"],["2","⇧"],["3","⇪"],["4","⌫"],["5","⌦"],["6","␡"],["7","⎋"],["8","␛"],["9","⏎"],["0","↩"],["A","␣"],["B","¬"],["C","¶"],["D","§"],["E","©"],["F","®"],["G","™"],["H","°"],["I","℃"],["J","℉"],["K","≠"],["L","±"],["M","√"],["N","‰"],["O","Ω"],["P","∞"],["Q","≈"],["R","ƒ"],["S","¼"],["T","½"],["U","¾"],["V","†"],["W","‡"],["X","․"],["Y","‥"],["Z","…"],["!","➥"],["\"","➽"],["£","☚"],["$","☜"],["%","☛"],["^","☞"],["&","★"],["*","☆"],["(","♠"],[")","♣"],["{","♥"],["}","♦"],["[","♪"],["]","♫"],["~","♯"],["#","♀"],[":","♂"],[";","∂"],["@","∄"],["'","∅"],["<","∆"],[">","∇"],[",","∈"],[".","∉"],["?","∋"],["/","∌"],["\\","∎"],["|","∓"]]; 
    for convert in encode:
        txt = txt.replace(convert[1],convert[0]);
    return txt;
def encryptfile():
    global FileCryptation;
    global FileOutput;
    filetoencrypt = FileCryptation.get();
    if "." not in filetoencrypt:
        filetoencrypt += ".txt"
    fileread = open(filetoencrypt,"r");
    read = fileread.read();
    fileread.close();
    filetoutput = FileOutput.get();
    if "." not in filetoutput:
        filetoutput += ".txt"
    filewrite = open(filetoutput,"w");
    filewrite.write(Encrypt(read));
    filewrite.close();
def decryptfile():
    global FileCryptation;
    global FileOutput;
    filetoencrypt = FileCryptation.get();
    if "." not in filetoencrypt:
        filetoencrypt += ".txt"
    fileread = open(filetoencrypt,"r");
    read = fileread.read();
    fileread.close();
    filetoutput = FileOutput.get();
    if "." not in filetoutput:
        filetoutput += ".txt"
    filewrite = open(filetoutput,"w");
    filewrite.write(Decrypt(read));
    filewrite.close();


tkinter.Label(win,text="File To Encrypt/Decrypt:",bg="black",fg="lightgreen").pack();
FileCryptation=tkinter.Entry(win, width=25, borderwidth=1, background="black", foreground="lightgreen");
FileCryptation.pack(padx=20)
tkinter.Label(win,text="File Output to (Will be overwritten!):",bg="black",fg="lightgreen").pack();
FileOutput=tkinter.Entry(win, width=25, borderwidth=1, background="black", foreground="lightgreen");
FileOutput.pack(padx=20)
EnButton = tkinter.Button(win,highlightbackground="black",highlightcolor="lightblue",activebackground="black",activeforeground="lightgreen",text="Encrypt",command=encryptfile,bg="black",fg="green").pack(pady=5, padx=10, side="left");
DeButton = tkinter.Button(win,highlightbackground="black",highlightcolor="lightblue",activebackground="black",activeforeground="lightgreen",text="Decrypt",command=decryptfile,bg="black",fg="green").pack(pady=5, padx=10, side="right");
win.mainloop();
