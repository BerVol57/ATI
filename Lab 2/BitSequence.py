class BitSequence:
    BitStream = ""
    file = None
    fname = None
    def OpenFile(self, file_name):
        with open(file_name, "rb") as f:
            self.fname = file_name
            self.file = f.read()
    
    def ReadBitSequence(self, sequence_length, file_name = None):
        if self.file is None:
            self.OpenFile(file_name)
        
        start_index = len(self.BitStream)
        
        min_index = start_index // 8
        
        max_index = start_index + sequence_length
        
        if max_index % 8 > 0:
            max_index = max_index // 8 + 1
        else:
            max_index = max_index // 8
        
        raw_string = ""
        for a in self.file[min_index : min(len(self.file), max_index)]:
            raw_string += bin(a)[2:].zfill(8)
        self.BitStream += raw_string[start_index%8 : 
            min(len(raw_string), sequence_length + start_index%8)]



    def WriteBitSequence(self, sequence_length, file_name = None):
        if file_name is None and self.fname is not None:
            file_name = "WritedBitSequence_" + self.fname
        
        max_index = min(sequence_length, len(self.BitStream))
        write_sequence = self.BitStream[:max_index]
        self.BitStream = self.BitStream[max_index:]
        
        writedBitStream = []
        for _ in range(0, max_index, 8):
            wsindex = min(len(write_sequence), 8)
            writedBitStream.append(int(write_sequence[:wsindex].ljust(8, "0"), 2))
            write_sequence = write_sequence[wsindex:]
        
        # print(writedBitStream)
        
        with open(file_name, "wb") as f:
            f.write(bytes(writedBitStream))
        
    

bs = BitSequence()
bs.OpenFile("test.txt")
bs.ReadBitSequence(10)
print(bs.BitStream)
bs.ReadBitSequence(10)
print(bs.BitStream)
bs.ReadBitSequence(10)
print(bs.BitStream)
bs.ReadBitSequence(10)
print(bs.BitStream)
bs.ReadBitSequence(10)
print(bs.BitStream)

bs.WriteBitSequence(20)