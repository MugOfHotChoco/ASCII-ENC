from AsciiEncrypter import *
print("This is a demostation of some of the things you can use the Ascii Encrypter for.")
print("----------------------------\n============================\n----------------------------");

output = Encrypt("Hello World."); #Basic Encryption. (Remeber, it can only Encrypt Ascii characters.#
print(output);
output = Decrypt(output); #Basic Decryption.#
print(output);

print("----------------------------\n============================\n----------------------------");

output = Encrypt("Hi World!",True); #Debugged Encryption.#
#print(output);
output = Decrypt(output,True); #Debugged Decryption.#
#print(output);

print("----------------------------\n============================\n----------------------------");

EncodingDict = {"h": "!", "e": "£","l": "$","o": "%"}; #Each character corrosponds to it's encrypted form. E.g h -> !. Remeber that h lowercased and H uppercased are diffrent characters.#
#{Orgchar1: EncryptedChar1, Orgchar2: EncryptedChar2, e.t.c};#
output = Encrypt("hello",False,EncodingDict); #Specific Dictionary Encryption#
print(output);
output = Decrypt(output,False,EncodingDict); #Make sure to use the same Dictionary to Decrypt.#
print(output);

print("----------------------------\n============================\n----------------------------");

EncodingDict = {"h": "!", "e": "£","l": "$","o": "%"};
EncodingDictChange(EncodingDict); #Changes Default Encoding Dictionary.#
output = Encrypt("hello"); #Encryption.#
print(output);
output = Decrypt(output); #Decryption.#
print(output);

print("----------------------------\n============================\n----------------------------");

EncodingDictChange(DEFAULTDICT); #DefaultDict is a constant containting the Defualt Ascii Encryption Dictionary. This line of code is changing the Encoding and Decoding Dictionary to the default.#
output = Encrypt("hello"); #Encryption.#
print(output);
output = Decrypt(output); #Decryption.#
print(output);