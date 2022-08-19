from AsciiEncrypter import *

print("----------------------------\n============================\n----------------------------");

output = Encrypt("Hello World."); #Basic Encryption.#
print(output);
output = Decrypt(output); #Basic Decryption.#
print(output);

print("----------------------------\n============================\n----------------------------");

output = Encrypt("Hi World!",True); #Debugged Encryption.#
#print(output);
output = Decrypt(output,True); #Debugged Decryption.#
#print(output);

print("----------------------------\n============================\n----------------------------");

EncodingDict = {"h": "!", "e": "£","l": "$","o": "%"};
#{Orgchar1: EncryptedChar1, Orgchar2: EncryptedChar2, e.t.c};#
output = Encrypt("hello",False,EncodingDict); #Specific Dictionary Encryption#
print(output);
output = Decrypt(output,False,EncodingDict); #Make sure to use the same Dictionary to Decrypt.#
print(output);

print("----------------------------\n============================\n----------------------------");

EncodingDict = {"h": "!", "e": "£","l": "$","o": "%"};
EncodingDictChange(EncodingDict); #Changes Default Encoding Dictionary.#
output = Encrypt("hello",False); #Encryption.#
print(output);
output = Decrypt(output,False); #Decryption.#
print(output);

print("----------------------------\n============================\n----------------------------");

EncodingDictChange(DEFAULTDICT); #DefaultDict is a constant containting the Defualt Dictionary. This line of code is changing the Encoding and Decodiong Dictionary to the default.#
output = Encrypt("hello",False); #Encryption.#
print(output);
output = Decrypt(output,False); #Decryption.#
print(output);