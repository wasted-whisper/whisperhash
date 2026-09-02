# whisperhash
uses the same encryption engine as whispershuffle yet meant to be a local hash salting tool for now will work on it later to be online when i aquire enough knowledge

meant to be used as a local imported library to hash passwords or any text and later confirming it through engine.verify()
generates a random salt from /dev/urandom shell script n then run states operation through a counted number from random 
encryption parameters :
* state1= password + injected salt 
* state2 = state1 + injected salt ... etc 

havent figured yet how to save em but planning to save clues or a way to verify but initial plan is to save em 
in a hidden directory .verfiy hash in same folder 
