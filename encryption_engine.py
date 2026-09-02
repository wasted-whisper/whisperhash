from tqdm import tqdm
from support_funcs import *

class EncryptionEngine:
    def __init__(self,rails:int,offset:int,direction:str):
        self.rails = rails
        self.offset = offset
        self.direction = direction

    def encrypt(self,message) -> str :
        if isinstance(message, str):
            message = message.encode("utf-8")

        message = "".join(f"{byte:08b}" for byte in message)
        if len(message) <= self.rails or self.rails <= 1:
            raw = bytearray(int(message[i:i + 8], 2) for i in range(0, len(message), 8))
            return raw.hex()
        rails = [[] for _ in range(self.rails)]
        it = get_path(self.rails)
        if self.offset % (2 * (self.rails - 1)) != 0:
            skipper(it, self.rails, self.offset, self.direction)

        for letter in tqdm(message, desc="Progress:", unit="bit", mininterval=0.1) :
            rails[next(it)].append(letter)
        encrypted_bits = "".join("".join(rail) for rail in rails)[::-1]
        encrypted_message = bytearray(int(encrypted_bits[i:i + 8], 2) for i in range(0, len(encrypted_bits), 8))
        return encrypted_message.hex()

    def verify(self,message):
        ...