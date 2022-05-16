# Symmetric encryption
Learn about symmetric encryption.

## Key terminology
- ***Plain text:*** The message you want to encrypt.
- ***Cipher text:*** The encrypted message.
- ***Symmetric encryption:*** This way of encryption only uses 1 key, the sender and the receiver need to own the same key. This is a very easy way of encryption but comes with its disadvantages. One big disadvantage is that if someone finds out that 1 key, that person will have acces to all your information, for example all your encrypted emails you send to your colleague.
- ***Ceasar Cipher:*** Is a method to encrypt messages, its quite a simple one. This cipher uses a substitution methad where letters are replaced by other letters. You decide wich ones by giving a shift #. For example a shift of 11 would encode an A as a B, an M as an N, and a Z as an A, and so on.
- ***Scytale Cipher(Historic cipher #1):*** This cypher was used by the spartans, this one can be used very simple since all you need is a cilender object and a thin strip of paper (in those times a parchment). You would wrap the thin piece of paper around the cilender and write your message on the paper, next you will write decoy letters on random spots on the paper. When you unwrap the paper from the cilender you will have a long thin paper with random letters on it. To decrypt it the recipient needs to have a cilinder object of the same size and just wrap the paper around his cilender and your message will come visible.
- ***Steganography(Historic cipher #2):*** This way of encrypting maybe isnt really encrypting a message. Its more like hiding the message completely. For example if a king wanted to send a message to one of his vassals, for a surprise attack on his enemies he would not want anyone to suspect even the slightest. He could take 1 of his messengers, shave his head and write a message on the bald head, he would wait till the messengers hair would grow back to cover the message and then send him to his vassal. There the messenger would shave his head again and the message can be read. A other example ive actually used as a kid with sisters was the invisible ink, i did not know that was a form of Steganography but we would write on the inside of the toilet door with invisible ink and with a special light the others could read it.
- ***Block Ciphers*** Are symmetric ciphers. A block cipher like for example AES encrypts and decrypts blocks of bits instead of doing it 1 by 1 like "stream ciphers". Todo this you need a predetermined key length. These lengths are 128, 192 or 256 bits.
- ***AES(Advanced Encryption Standard):*** Is a symmetric block cipher algorithm with a block size of 128 bits. It converts these individual blocks using keys of 128, 192, and 256 bits. Once it encrypts these blocks, it joins them together to form the ciphertext. AES is based on SP network. The key size decides how many rounds you need to encrypt the plaintext to cipher text, A 128-bit key requires 10 rounds while a 192-bit key requires 12 rounds and A full 14 rounds are required when a 256-bit key is being used before the entire text is converted to cipher text . AES works in bytes, 8 bits = 1 byte, so AES works with 16 bytes
- ***Stream Cipher:*** Do their encrypts on a smaller base then Block ciphers, making it way faster. What i mean is that Stream ciphers encrypt bit by bit. This makes it faster since you can encrypt a 32bit block messages and stop encrypting when its done. With a block cipher it would still need to padd the remaining 96 bits. RC4 is a common used Stream Cipher.
- ***RC4(Rivest Cipher 4):*** Is one of the most famous stream ciphers. Its a variable-length key algorithm. This algorithm encrypts one byte at a time (or larger units at a time).
RC4 relies on:
  - Key inputs. This tool generates an eight-bit number (cipher) that's impossible to guess. 
  - Keystreams. The cipher scrambles plain text. 
Product. 
  - An X-OR operation combining the keystream with the cipher. 



## Exercise
### Sources
1. [SymmvsAsym](https://blog.mailfence.com/symmetric-vs-asymmetric-encryption/#:~:text=Symmetric%20encryption%20uses%20a%20private,her%20private%20key%20to%20decrypt.)
2. [Ceasar](https://brilliant.org/wiki/caesar-cipher/)
3. [steno](https://www.guinnessworldrecords.com/world-records/first-use-of-steganography)
4. [Scytale](https://www.youtube.com/watch?v=_vIb6Y45ERQ)
5. [Block](https://www.hypr.com/black-cipher/)
6. [AES](https://www.youtube.com/watch?v=O4xNJsjtN6E)
7. [Stream](https://www.wolfssl.com/what-is-a-stream-cipher/#:~:text=A%20stream%20cipher%20encrypts%20plaintext,and%20simplicity%20are%20both%20requirements.)
8. [blockvsstream](https://crashtest-security.com/block-cipher-vs-stream-cipher/#what-are-block-ciphers)


### Overcome challenges
Going way to deep and getting confused because of obtaining to much information.

### Results
1. 



