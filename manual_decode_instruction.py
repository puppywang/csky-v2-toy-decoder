import json

# 存储解析后的指令集
instruction_set = {}

# 添加指令的函数
def add_instruction(name, format_type, opcode, fields, description):
    instruction_set[name] = {
        "format": format_type,
        "opcode": opcode,
        "fields": fields,
        "description": description
    }

# 手动添加几个指令的格式示例
add_instruction(
    "ADDC16",
    "16-bit",
    "011000XXXXXXXX01",
    {"RZ": [6, 9], "RX": [10, 14]},
    "RZ = RZ + RX + C, C = Carry"
)

add_instruction(
    "ADDC32",
    "32-bit",
    "110001XXXXXXXXXX00000000010XXXXX",
    {"RY": [21, 25], "RX": [16, 20], "RZ": [0, 4]},
    "RZ = RX + RY + C, C = Carry"
)

add_instruction(
    "ADDI16",
    "16-bit",
    "00100XXXXXXXXXXX",
    {"RZ": [8, 10], "IMM8": [0, 7]},
    "RZ = RZ + zero_extend(OIMM8)"
)

add_instruction(
    "ADDI16_2",
    "16-bit",
    "01011XXXXXXXXX10",
    {"RX": [8, 10], "RZ": [5, 7], "IMM3": [2, 4]},
    "RZ = RX + zero_extend(OIMM3)"
)

add_instruction(
    "ADDI32_1",
    "32-bit",
    "111001XXXXXXXXXX0000XXXXXXXXXXXX",
    {"RZ": [21, 25], "RX": [16, 20], "IMM12": [0, 11]},
    "RZ = RX + zero_extend(OIMM12)"
)

add_instruction(
    "ADDI32_2",
    "32-bit",
    "110011XXXXX111XXXXXXXXXXXXXXXXXX",
    {"RZ": [21, 25], "IMM18": [0, 17]},
    "RZ = RZ + zero_extend(OIMM18)"
)

add_instruction(
    "ADDI_SP",
    "16-bit",
    "00011XXXXXXXXXXX",
    {"RZ": [8, 10], "IMM8": [0, 7]},
    "RZ = SP + zero_extend(IMM8 << 2)"
)

add_instruction(
    "ADDI_SP_2",
    "16-bit",
    "000101XX000XXXXX",
    {"IMM2": [8, 9], "IMM5": [0, 4]},
    "SP = SP + zero_extend((IMM2,IMM5) << 2)"
)

add_instruction(
    "ADDU16",
    "16-bit",
    "011000XXXXXXXX00",
    {"RZ": [6, 9], "RX": [2, 5]},
    "RZ = RZ + RX"
)

add_instruction(
    "ADDU16_2",
    "16-bit",
    "01011XXXXXXXXX00",
    {"RX": [8, 10], "RZ": [5, 7], "RY": [2, 4]},
    "RZ = RX + RY"
)

add_instruction(
    "ADDU32",
    "32-bit",
    "110001XXXXXXXXXX00000000001XXXXX",
    {"RY": [21, 25], "RX": [16, 20], "RZ": [0, 4]},
    "RZ = RX + RY"
)


add_instruction(
    "AND16",
    "16-bit",
    "011010XXXXXXXX00",
    {"RZ": [6, 9], "RX": [2, 5]},
    "RZ = RZ & RX"
)

add_instruction(
    "AND32",
    "32-bit",
    "110001XXXXXXXXXX00100000001XXXXX",
    {"RY": [21, 25], "RX": [16, 20], "RZ": [0, 4]},
    "RZ = RX & RY"
)


add_instruction(
    "ANDI",
    "32-bit",
    "111001XXXXXXXXXX0010XXXXXXXXXXXX",
    {"RZ": [21, 25], "RX": [16, 20], "IMM12": [0, 11]},
    "RZ = RX & zero_extend(IMM12)"
)

add_instruction(
    "ANDN16",
    "16-bit",
    "011010XXXXXXXX01",
    {"RZ": [6, 9], "RX": [2, 5]},
    "RZ = RZ & (~RX)"
)

add_instruction(
    "ANDN32",
    "32-bit",
    "110001XXXXXXXXXX00100000010XXXXX",
    {"RY": [21, 25], "RX": [16, 20], "RZ": [0, 4]},
    "RZ = RX & (~RY)"
)


add_instruction(
    "ANDNI",
    "32-bit",
    "111001XXXXXXXXXX0011XXXXXXXXXXXX",
    {"RZ": [21, 25], "RX": [16, 20], "IMM12": [0, 11]},
    "RZ = RX & (~zero_extend(IMM12))"
)


add_instruction(
    "ASR16",
    "16-bit",
    "011100XXXXXXXX10",
    {"RZ": [6, 9], "RX": [2, 5]},
    "RZ = RZ >>> RX[5:0]"
)

add_instruction(
    "ASR32",
    "32-bit",
    "110001XXXXXXXXXX01000000100XXXXX",
    {"RY": [21, 25], "RX": [16, 20], "RZ": [0, 4]},
    "RZ = RX >>> RY[5:0]"
)

add_instruction(
    "ASRC",
    "32-bit",
    "110001XXXXXXXXXX01001100100XXXXX",
    {"IMM5": [21, 25], "RX": [16, 20], "RZ": [0, 4]},
    "RZ = RX >>> OIMM5; C = RX[OIMM5 - 1]"
)


add_instruction(
    "ASRI16",
    "16-bit",
    "01010XXXXXXXXXXX",
    {"RX": [8, 10], "RZ": [5, 7],  "IMM5": [0, 4]},
    "RZ = RX >>> IMM5"
)

add_instruction(
    "ASRI32",
    "32-bit",
    "110001XXXXXXXXXX01001000100XXXXX",
    {"IMM5": [21, 25], "RX": [16, 20], "RZ": [0, 4]},
    "RZ = RX >>> IMM5"
)

add_instruction(
    "BCLRI16",
    "16-bit",
    "00111XXX100XXXXX",
    {"RZ": [8, 10], "IMM5": [0, 4]},
    "Clear bit IMM5 in RZ"
)

add_instruction(
    "BCLRI32",
    "32-bit",
    "110001XXXXXXXXXX00101000001XXXXX",
    {"RX": [6, 10], "IMM5": [11, 15], "RZ": [26, 30]},
    "Clear bit IMM5 in RZ"
)


add_instruction(
    "BF16",
    "16-bit",
    "000011XXXXXXXXXX",
    {"OFFSET": [0, 9]},
    "Branch if C == 0 to label OFFSET"
)

add_instruction(
    "BF32",
    "32-bit",
    "1110100001000000XXXXXXXXXXXXXXXX",
    {"OFFSET": [0, 15]},
    "Branch if C == 0 to label OFFSET"
)

add_instruction(
    "BKPT",
    "16-bit",
    "0000000000000000",
    {},
    "Trigger a breakpoint exception or enter debug mode"
)

add_instruction(
    "BMASKI",
    "32-bit",
    "110001XXXXX0000001010000001XXXXX",
    {"IMM": [21, 25], "RZ": [0, 4]},
    "RZ = 2^OIMM5 - 1"
)

add_instruction(
    "BMCLR32",
    "32-bit",
    "11000000000000000001010000100000",
    {},
    "Clear BM bit in PSR to 0"
)

add_instruction(
    "BPOP.H",
    "16-bit",
    "00010100101XXX00",
    {"RZ": [2, 4]},
    "Pop halfword from binary stack to RZ; update BSP"
)


add_instruction(
    "BPOP.W",
    "16-bit",
    "00010100101XXX10",
    {"RZ": [2, 4]},
    "Pop word from binary stack to RZ; update BSP"
)

add_instruction(
    "BPUSH.H",
    "16-bit",
    "00010100111XXX00",
    {"RZ": [2, 4]},
    "Push lower halfword of RZ to binary stack; update BSP"
)

add_instruction(
    "BPUSH.W",
    "16-bit",
    "00010100111XXX10",
    {"RZ": [2, 4]},
    "Push word of RZ to binary stack; update BSP"
)

add_instruction(
    "BMSET",
    "32-bit",
    "11000000000000000001000000100000",
    {},
    "Set BM bit in PSR to 1"
)


add_instruction(
    "BR16",
    "16-bit",
    "000001",
    {"OFFSET": [6, 16]},
    "Unconditional branch to label OFFSET"
)

add_instruction(
    "BR32",
    "32-bit",
    "111011",
    {"OFFSET": [6, 26]},
    "Unconditional branch to label OFFSET"
)

add_instruction(
    "BSETI16",
    "16-bit",
    "00111XXX101XXXXX",
    {"RZ": [8, 10], "IMM5": [0, 4]},
    "RZ = RZ[IMM5]置位"
)

add_instruction(
    "BSETI32",
    "32-bit",
    "110001XXXXXXXXXX00101000010XXXXX",
    {"IMM5": [21, 25], "RX": [16, 20], "RZ": [0, 4]},
    "RZ = RZ[IMM5]置位"
)

add_instruction(
    "BSR",
    "32-bit",
    "111000XXXXXXXXXXXXXXXXXXXXXXXXXX",
    {"OFFSET": [0, 25]},
    "Jump to sub program at label OFFSET"
)

# 添加 BT 指令
add_instruction(
    "BT16",
    "16-bit",
    "000010XXXXXXXXXX",
    {"OFFSET": [0, 9]},
    "Branch if C == 1"
)

add_instruction(
    "BT32",
    "32-bit",
    "1110100001100000XXXXXXXXXXXXXXXX",
    {"OFFSET": [0, 15]},
    "Branch if C == 1"
)

# 添加 BTSTI 指令
add_instruction(
    "BTSTI",
    "32-bit",
    "110001XXXXXXXXXX0010100010000000",
    {"IMM5": [21, 25], "RX": [16, 20]},
    "Test and branch if RX[IMM5] == 1"
)

# 添加 CMPHS 指令
add_instruction(
    "CMPHS",
    "16-bit",
    "011001XXXXXXXX00",
    {"RY": [6, 9], "RX": [2, 5]},
    "Set flags based on RX >= RY (unsigned comparison)"
)

# 添加 CMPHSI 指令
add_instruction(
    "CMPHSI16",
    "16-bit",
    "00111XXX000XXXXX",
    {"RX": [8, 10], "IMM5": [0, 4]},
    "Set flags based on RX >= zero_extend(OIMM5) (unsigned comparison)"
)

add_instruction(
    "CMPHSI",
    "32-bit",
    "11101011000XXXXXXXXXXXXXXXXXXXXX",
    {"RX": [21, 25], "IMM16": [0, 15]},
    "Set flags based on RX >= zero_extend(OIMM16) (unsigned comparison)"
)

# 添加 CMPLT 指令
add_instruction(
    "CMPLT",
    "16-bit",
    "011001XXXXXXXX01",
    {"RX": [6, 9], "RY": [2, 5]},
    "Set flags based on RX < RY (unsigned comparison)"
)

# 添加 CMPLTI 指令
add_instruction(
    "CMPLTI16",
    "16-bit",
    "00111XXX001XXXXX",
    {"RX": [8, 10], "IMM5": [0, 4]},
    "Set flags based on RX < zero_extend(OIMM5) (unsigned comparison)"
)

add_instruction(
    "CMPLTI32",
    "32-bit",
    "11101011001XXXXXXXXXXXXXXXXXXXXX",
    {"RX": [16, 20], "IMM16": [0, 15]},
    "Set flags based on RX < zero_extend(OIMM16) (unsigned comparison)"
)

# 添加 CMPNE 指令
add_instruction(
    "CMPNE",
    "16-bit",
    "011001XXXXXXXX10",
    {"RX": [6, 9], "RY": [2, 5]},
    "Set flags based on RX != RY"
)

# 添加 CMPNEI 指令
add_instruction(
    "CMPNEI16",
    "16-bit",
    "00111XXX010XXXXX",
    {"RX": [8, 10], "IMM5": [0, 4]},
    "Set flags based on RX != zero_extend(IMM5)"
)


add_instruction(
    "CMPNEI32",
    "32-bit",
    "11101011010XXXXXXXXXXXXXXXXXXXXX",
    {"RX": [21, 25], "IMM16": [0, 15]},
    "Set flags based on RX != zero_extend(IMM16)"
)

# 添加 DECF 指令
add_instruction(
    "DECF",
    "32-bit",
    "110001XXXXXXXXXX00001100100XXXXX",
    {"RZ": [21, 25], "RX": [16, 20], "IMM5": [0, 4]},
    "RZ = RX - zero_extend(IMM5) when C == 0"
)

# 添加 DECT 指令
add_instruction(
    "DECT",
    "32-bit",
    "110001XXXXXXXXXX00001101000XXXXX",
    {"RZ": [21, 25], "RX": [16, 20], "IMM5": [0, 4]},
    "RZ = RX - zero_extend(IMM5) when C == 1"
)

# 添加 DOZE 指令
add_instruction(
    "DOZE",
    "32-bit",
    "1100000000000000101000000100000",
    {},
    "Enter low-power mode"
)


# 添加 FF0 指令
add_instruction(
    "FF0",
    "32-bit",
    "11000100000XXXXX01111100001XXXXX",
    {"RX": [16, 20], "RZ": [0, 4]},
    "Find first zero in RZ and set to result to RX"
)

# 添加 FF1 指令
add_instruction(
    "FF1",
    "32-bit",
    "11000100000XXXXX01111100010XXXXX",
    {"RX": [16, 20], "RZ": [0, 4]},
    "Find first one in RZ and set to result to RX"
)

# 添加 INCF 指令
add_instruction(
    "INCF",
    "32-bit",
    "110001XXXXXXXXXX00001100001XXXXX",
    {"RZ": [21, 25], "RX": [16, 20], "IMM5": [0, 4]},
    "RZ = RZ + zero_extend(IMM5) when C == 0"
)

# 添加 INCT 指令
add_instruction(
    "INCT",
    "32-bit",
    "110001XXXXXXXXXX00001100010XXXXX",
    {"RZ": [21, 25], "RX": [16, 20], "IMM5": [0, 4]},
    "RZ = RZ + zero_extend(IMM5) when C == 1"
)

# 添加 IPUSH 指令
add_instruction(
    "IPUSH",
    "16-bit",
    "0001010001100010",
    {},
    "Push R0~R3, R12, R13 onto interrupt stack"
)

# 添加 IPOP 指令
add_instruction(
    "IPOP",
    "16-bit",
    "0001010001100011",
    {"RZ": [21, 25]},
    "Pop value from interrupt stack into R0~R3,R12,R13"
)

# 添加 IXH 指令
add_instruction(
    "IXH",
    "32-bit",
    "110001XXXXXXXXXX00001000001XXXXX",
    {"RY": [21, 25], "RX": [16, 20], "RZ": [0, 4]},
    "RZ = RX + (RY << 1)"
)

# 添加 IXW 指令
add_instruction(
    "IXW",
    "32-bit",
    "111001XXXXXXXXXX00001000010XXXXX",
    {"RY": [21, 25], "RX": [16, 20], "RX": [0, 4]},
    "RZ = RX + (RY << 2)"
)

# 添加 JMP 指令
add_instruction(
    "JMP",
    "16-bit",
    "0111100000XXXX00",
    {"RX": [2, 5]},
    "Unconditional jump to address in RX"
)

# 添加 JMPIX 指令
add_instruction(
    "JMPIX",
    "16-bit",
    "00111XXX111000XX",
    {"RX": [8, 10], "IMM2": [0, 1]},
    "Unconditional jump to address at SVBR + (RX & 0xff) * IMM"
)

# 添加 JSR 指令
add_instruction(
    "JSR",
    "16-bit",
    "011110000XXX01",
    {"RX": [2, 5]},
    "Jump to subroutine to address in RX"
)

# 添加 LD.B 指令
add_instruction(
    "LD.B16",
    "16-bit",
    "10000XXXXXXXXXXX",
    {"RX": [8, 10], "RZ": [5, 7], "OFFSET": [0, 4]},
    "RZ = zero_extend(MEM[RX + zero_extend(OFFSET)])"
)

add_instruction(
    "LD.B32",
    "32-bit",
    "110110XXXXXXXXXX0000XXXXXXXXXXXX",
    {"RZ": [21, 25], "RX": [16, 20], "OFFSET": [0, 11]},
    "RZ = zero_extend(MEM[RX + zero_extend(OFFSET)])"
)

# 添加 LD.BS 指令
add_instruction(
    "LD.BS",
    "32-bit",
    "110110XXXXXXXXXX0100XXXXXXXXXXXX",
    {"RZ": [21, 25], "RX": [16, 20], "OFFSET": [0, 11]},
    "RZ = signed_extend(MEM[RX + zero_extend(OFFSET)])"
)

# 添加 LD.H 指令
add_instruction(
    "LD.H16",
    "16-bit",
    "10001XXXXXXXXXXX",
    {"RX": [8, 10], "RZ": [5, 7], "OFFSET": [0, 4]},
    "RZ = zero_extend(MEM[RX + zero_extend(OFFSET<<1)])"
)

add_instruction(
    "LD.H32",
    "32-bit",
    "110110XXXXXXXXXX0001XXXXXXXXXXXX",
    {"RZ": [21, 25], "RX": [16, 20], "OFFSET": [0, 11]},
    "RZ = zero_extend(MEM[RX + zero_extend(OFFSET<<1)])"
)

# 添加 LD.HS 指令
add_instruction(
    "LD.HS",
    "32-bit",
    "110110XXXXXXXXXX0101XXXXXXXXXXXX",
    {"RZ": [21, 25], "RX": [16, 20], "OFFSET": [0, 11]},
    "RZ = signed_extend(MEM[RX + zero_extend(OFFSET<<1)])"
)

# 添加 LD.W 指令
add_instruction(
    "LD.W16",
    "16-bit",
    "10010XXXXXXXXXXX",
    {"RX": [8, 10], "RZ": [5, 7], "IMM5": [0, 4]},
    "RZ = MEM[RX + sign_extend(offset << 2)]"
)

add_instruction(
    "LD.W32",
    "32-bit",
    "110110XXXXXXXXXX0010XXXXXXXXXXXX",
    {"RZ": [21, 25], "RX": [16, 20], "OFFSET": [0, 11]},
    "RZ = MEM[RX + zero_extend(offset << 2)]"
)

# 添加 LDM 指令
add_instruction(
    "LDM",
    "32-bit",
    "110100XXXXXXXXXX00011100001XXXXX",
    {"RY": [21, 25], "RX": [16, 20], "IMM5": [0, 15]},
    "Load multiple registers starting at ADDR"
)

# 添加 LRW 指令
add_instruction(
    "LRW16",
    "16-bit",
    "000X00XXXXXXXXXX",
    {"IMM": [12, 12], "IMM2": [8, 9], "RZ": [5, 7], "IMM5": [0, 4]},
    "RZ = zero_extend(MEM[(PC + zero_extend(OFFSET << 2)) &0xfffffffc])"
)

add_instruction(
    "LRW32",
    "32-bit",
    "11101010100XXXXXXXXXXXXXXXXXXXXX",
    {"RZ": [16, 20], "OFFSET": [0, 15]},
    "RZ = zero_extend(MEM[(PC + zero_extend(OFFSET << 2)) &0xfffffffc])"
)

# 添加 LSL 指令
add_instruction(
    "LSL16",
    "16-bit",
    "011100XXXXXXXX00",
    {"RZ": [6, 9], "RX": [2, 5]},
    "RZ = RZ << RX[5:0]"
)

add_instruction(
    "LSL32",
    "32-bit",
    "110001XXXXXXXXXX01000000001XXXXX",
    {"RY": [21, 25], "RX": [16, 20], "RZ": [0, 4]},
    "RZ = RX << RY[5:0]"
)

# 添加 LSLC 指令
add_instruction(
    "LSLC",
    "32-bit",
    "110011XXXXXXXXXX0011XXXXXXXXXXXX",
    {"IMM5": [21, 25], "RX": [16, 20], "RZ": [0, 4]},
    "Logical shift left RZ by RX[4:0] with carry, RZ = RX << OIMM5"
)

# 添加 LSLI 指令
add_instruction(
    "LSLI16",
    "16-bit",
    "01000XXXXXXXXXXX",
    {"RX": [8, 10], "RZ": [5, 7], "IMM5": [0, 4]},
    "Logical shift left RZ by immediate value, RZ = RX << IMM5"
)

add_instruction(
    "LSLI32",
    "32-bit",
    "110001XXXXXXXXXX01001000001XXXXX",
    {"IMM5": [21, 25], "RX": [16, 20], "RZ": [0, 4]},
    "Logical shift left RZ by immediate value, RZ = RX << IMM5"
)

# 添加 LSR 指令
add_instruction(
    "LSR16",
    "16-bit",
    "011100XXXXXXXX01",
    {"RZ": [6, 9], "RX": [2, 5]},
    "Logical shift right RZ by RX[4:0], RZ = RZ >> RX[5:0]"
)

add_instruction(
    "LSR32",
    "32-bit",
    "110001XXXXXXXXXX01000000010XXXXX",
    {"RY": [21, 25], "RX": [16, 20], "RZ": [0, 4]},
    "Logical shift right RZ by RX[4:0], RZ = RX >> RY[5:0]"
)

# 添加 LSRC 指令
add_instruction(
    "LSRC",
    "32-bit",
    "110001XXXXXXXXXX01001100010XXXXX",
    {"IMM5": [21, 25], "RX": [16, 20], "RZ": [0, 4]},
    "Logical shift right RZ by RX[4:0] with carry, RZ = RX >> OIMM5; C = RX[OIMM5 - 1]"
)

# 添加 LSRI 指令
add_instruction(
    "LSRI16",
    "16-bit",
    "01001XXXXXXXXXXX",
    {"RX": [8, 10], "RZ": [5, 7], "IMM5": [0, 4]},
    "Logical shift right RZ by immediate value, RZ = RX >> IMM5"
)

add_instruction(
    "LSRI32",
    "32-bit",
    "110001XXXXXXXXXX01001000010XXXXX",
    {"IMM5": [21, 25], "RX": [16, 20], "RZ": [0, 4]},
    "Logical shift right RZ by immediate value, RZ = RX >> IMM5"
)

# 添加 MFCR 指令
add_instruction(
    "MFCR",
    "32-bit",
    "110000XXXXXXXXXX01100000001XXXXX",
    {"SEL": [21, 25], "CRX": [16, 20], "RZ": [0, 4]},
    "Move value from control register <CRX, SEL> to RZ"
)

# 添加 MOV 指令
add_instruction(
    "MOV",
    "16-bit",
    "011011XXXXXXXX11",
    {"RZ": [6, 9], "RX": [2, 5]},
    "Move value from RX to RZ"
)

# 添加 MOVF 指令
add_instruction(
    "MOVF",
    "32-bit",
    "110001XXXXXXXXXX0000110000100000",
    {"RZ": [21, 25], "RX": [16, 20]},
    "Move value from RX to RZ if C == 0"
)

# 添加 MOVI 指令
add_instruction(
    "MOVI16",
    "16-bit",
    "00110XXXXXXXXXXX",
    {"RZ": [8, 10], "IMM8": [0, 7]},
    "Move immediate value IMM8 into RZ, RZ = zero_extend(IMM8)"
)

add_instruction(
    "MOVI32",
    "32-bit",
    "11101010000XXXXXXXXXXXXXXXXXXXXX",
    {"RZ": [16, 20], "IMM16": [0, 15]},
    "Move immediate value IMM16 into RZ, RZ = zero_extend(IMM16)"
)


# 添加 MOVIH 指令
add_instruction(
    "MOVIH",
    "32-bit",
    "11101010001XXXXXXXXXXXXXXXXXXXXX",
    {"RZ": [16, 20], "IMM16": [0, 15]},
    "Move high immediate value IMM16 into RZ, RZ = zero_extend(IMM16) << 16"
)

# 添加 MOVT 指令
add_instruction(
    "MOVT",
    "32-bit",
    "110001XXXXXXXXXX0000110001000000",
    {"RZ": [21, 25], "RX": [16, 20]},
    "Move RX into RZ if C == 1"
)

# 添加 MTCR 指令
add_instruction(
    "MTCR",
    "32-bit",
    "110000XXXXXXXXXX01100100001XXXXX",
    {"SEL": [21, 25], "RX": [16, 20], "CRZ": [0, 4]},
    "Move value from RZ to control register CR, CR<Z, SEL> = RX"
)

# 添加 MULT 指令
add_instruction(
    "MULT16",
    "16-bit",
    "011111XXXXXXXX00",
    {"RZ": [6, 9], "RX": [2, 5]},
    "Multiply RX by RZ, store result in RZ"
)

add_instruction(
    "MULT32",
    "32-bit",
    "110001XXXXXXXXXX10000100001XXXXX",
    {"RY": [16, 20], "RX": [16, 20], "RZ": [0, 4]},
    "Multiply RX by RY, store result in RZ, RZ = RX x RY"
)

# 添加 MVC 指令
add_instruction(
    "MVC",
    "32-bit",
    "110001000000000000000101000XXXXX",
    {"RZ": [0, 4]},
    "Move value from C to RZ"
)

# 添加 MVCV 指令
add_instruction(
    "MVCV",
    "16-bit",
    "011001XXXX000011",
    {"RZ": [6, 9]},
    "Move value from !C to RZ, RZ = !C"
)

# 添加 NIE 指令
add_instruction(
    "NIE",
    "16-bit",
    "0001010001100000",
    {},
    "Save EPSR, EPC to stack, enable PSR.IE, PSR.EE"
)

# 添加 NIR 指令
add_instruction(
    "NIR",
    "16-bit",
    "0001010001100001",
    {},
    "Pop EPSR, EPC from stack, clear PSR.IE, PSR.EE"
)

# 添加 NOR 指令
add_instruction(
    "NOR",
    "16-bit",
    "011011XXXXXXXX10",
    {"RZ": [6, 9], "RX": [2, 5]},
    "RZ = ~(RZ | RX)"
)

add_instruction(
    "NOR",
    "32-bit",
    "110001XXXXXXXXXX00100100100XXXXX",
    {"RY": [21, 25], "RX": [16, 20], "RZ": [0, 4]},
    "RZ = ~(RX | RY)"
)

# 添加 OR 指令
add_instruction(
    "OR",
    "16-bit",
    "011011XXXXXXXX00",
    {"RZ": [6, 9], "RX": [2, 5]},
    "RZ = RZ | RX"
)

add_instruction(
    "OR",
    "32-bit",
    "110001XXXXXXXXXX00100100001XXXXX",
    {"RY": [21, 25], "RX": [16, 20], "RZ": [0, 4]},
    "RZ = RX | RY"
)

# 添加 ORI 指令
add_instruction(
    "ORI",
    "32-bit",
    "111011XXXXXXXXXXXXXXXXXXXXXXXXXX",
    {"RZ": [21, 25], "RX": [16, 20], "IMM16": [0, 15]},
    "RZ = RX | zero_extend(IMM16)"
)

# 添加 POP 指令
add_instruction(
    "POP",
    "16-bit",
    "00010100100XXXXX",
    {"R15": [4, 4], "LIST1": [0, 3]},
    "Pop value from stack into R15 and LIST1"
)

# 添加 PSRCLR 指令
add_instruction(
    "PSRCLR",
    "32-bit",
    "110000XXXXX000000111000000100000",
    {"IMM5": [21, 25]},
    "Clear PSR bits in IMM5"
)

# 添加 PSRSET 指令
add_instruction(
    "PSRSET",
    "32-bit",
    "110000XXXXX000000111010000100000",
    {"IMM5": [21, 25]},
    "Set PSR bits in IMM5"
)

# 添加 PUSH 指令
add_instruction(
    "PUSH",
    "16-bit",
    "00010100110XXXXX",
    {"R15": [4, 4], "LIST1": [0, 3]},
    "Push R15/LIST1 onto stack"
)

# 添加 REVB 指令
add_instruction(
    "REVB",
    "16-bit",
    "011110XXXXXXXX10",
    {"RZ": [6, 9], "RX": [2, 5]},
    "RZ[31:24] = RX[7:0], RZ[23:16] = RX[15:8], RZ[15:8] = RX[23:16], RZ[7:0] = RX[31:24]"
)

# 添加 REVH 指令
add_instruction(
    "REVH",
    "16-bit",
    "011110XXXXXXXX11",
    {"RZ": [6, 9], "RX": [2, 5]},
    "RZ[31:24] = RX[23:16], RZ[23:16] = RX[31:24], RZ[15:8] = RX[7:0], RZ[7:0] = RX[15:8]"
)

# 添加 ROTL 指令
add_instruction(
    "ROTL16",
    "16-bit",
    "011100XXXXXXXX11",
    {"RZ": [6, 9], "RX": [2, 5]},
    "Rotate left RZ by RX[4:0], RZ = RZ <<<< RX[5:0]"
)

add_instruction(
    "ROTL32",
    "16-bit",
    "110001XXXXXXXXXX01000001000XXXXX",
    {"RY": [21, 25], "RX": [16, 20], "RZ": [0, 4]},
    "Rotate left RZ by RX[4:0], RZ = RZ <<<< RX[5:0]"
)

# 添加 ROTLI 指令
add_instruction(
    "ROTLI",
    "32-bit",
    "110001XXXXXXXXXX01001001000XXXXX",
    {"IMM5": [21, 25], "RZ": [16, 20], "IMM5": [0, 4]},
    "Rotate left RZ by immediate value"
)

# 添加 RTE 指令
add_instruction(
    "RTE",
    "32-bit",
    "11000000000000000100000000100000",
    {},
    "Return from exception"
)

# 添加 ST.B 指令
add_instruction(
    "ST.B16",
    "16-bit",
    "10100XXXXXXXXXXX",
    {"RX": [8, 10], "RZ": [5, 7], "IMM5": [0, 4]},
    "Store byte from RZ to MEM[RX + zero_extend(OFFSET)], MEM[RX + zero_extend(offset)] = RZ[7:0]"
)

add_instruction(
    "ST.B32",
    "32-bit",
    "110111XXXXXXXXXX0000XXXXXXXXXXXX",
    {"RZ": [21, 25], "RX": [16, 20], "OFFSET": [0, 11]},
    "Store byte from RZ to MEM[RX + zero_extend(OFFSET)], MEM[RX + zero_extend(offset)] = RZ[7:0]"
)

# 添加 ST.H 指令
add_instruction(
    "ST.H16",
    "16-bit",
    "10101XXXXXXXXXXX",
    {"RX": [8, 10], "RZ": [5, 7], "IMM5": [0, 4]},
    "Store byte from RZ to MEM[RX + zero_extend(OFFSET)], MEM[RX + zero_extend(offset)] = RZ[15:0]"
)

add_instruction(
    "ST.H32",
    "32-bit",
    "110111XXXXXXXXXX0001XXXXXXXXXXXX",
    {"RZ": [21, 25], "RX": [16, 20], "OFFSET": [0, 11]},
    "Store byte from RZ to MEM[RX + zero_extend(OFFSET)], MEM[RX + zero_extend(offset)] = RZ[15:0]"
)

# 添加 ST.W 指令
add_instruction(
    "ST.W16",
    "16-bit",
    "10110XXXXXXXXXXX",
    {"RX": [8, 10], "RZ": [5, 7], "IMM5": [0, 4]},
    "Store byte from RZ to MEM[RX + zero_extend(OFFSET << 2)], MEM[RX + zero_extend(offset)] = RZ[31:0]"
)

add_instruction(
    "ST.W32",
    "32-bit",
    "110111XXXXXXXXXX0010XXXXXXXXXXXX",
    {"RZ": [21, 25], "RX": [16, 20], "OFFSET": [0, 11]},
    "Store byte from RZ to MEM[RX + zero_extend(OFFSET)], MEM[RX + zero_extend(offset << 2)] = RZ[31:0]"
)

# 添加 STM 指令
add_instruction(
    "STM",
    "32-bit",
   "110111XXXXXXXXXX00011100001XXXXX",
    {"RY": [21, 25], "RX": [16, 20], "IMM5": [0, 4]},
    "Store multiple registers (IMM5) starting from RZ to MEM[RX]"
)

# 添加 STOP 指令
add_instruction(
    "STOP",
    "32-bit",
    "11000000000000000100100000100000",
    {},
    "Stop processor execution"
)

# 添加 SUBC 指令
add_instruction(
    "SUBC16",
    "16-bit",
    "011000XXXXXXXX11",
    {"RZ": [6, 9], "RX": [2, 5]},
    "RZ = RZ - RX - !C, with carry"
)

add_instruction(
    "SUBC32",
    "32-bit",
    "110001XXXXXXXXXX00000001000XXXXX",
    {"RY": [21, 25], "RX": [16, 20], "RZ": [0, 4]},
    "RZ = RX - RY - !C, with carry"
)

# 添加 SUBI 指令
add_instruction(
    "SUBI",
    "16-bit",
    "00101XXXXXXXXXXX",
    {"RZ": [8, 10], "IMM8": [0, 7]},
    "RZ = RZ - zero_extend(OIMM8)"
)

add_instruction(
    "SUBI",
    "32-bit",
    "111001XXXXXXXXXX0001XXXXXXXXXXXX",
    {"RZ": [21, 25], "RX": [16, 20], "IMM12": [0, 11]},
    "RZ = RZ - zero_extend(OIMM12)"
)

# 添加 SUBI(SP) 指令
add_instruction(
    "SUBI(SP)",
    "16-bit",
    "000101XX001XXXXX",
    {"IMM2": [8, 9], "IMM5": [0, 4]},
    "SP = SP - zero_extend({IMM2, IMM5} << 2)"
)

# 添加 SUBU 指令
add_instruction(
    "SUBU16",
    "16-bit",
    "011000XXXXXXXX10",
    {"RZ": [6, 9], "RX": [2, 5]},
    "RZ = RZ - RX"
)

add_instruction(
    "SUBU16_2",
    "16-bit",
    "01011XXXXXXXXX01",
    {"RX": [8, 10], "RZ": [5, 7], "RY": [2, 4]},
    "RZ = RX - RY"
)

add_instruction(
    "SUBU32",
    "32-bit",
    "110001XXXXXXXXXX00000000100XXXXX",
    {"RY": [21, 25], "RX": [16, 20], "RZ": [0, 4]},
    "RZ = RX - RY"
)

# 添加 SYNC 指令
add_instruction(
    "SYNC",
    "32-bit",
    "11000000000000000000010000100000",
    {},
    "Synchronize memory"
)

# 添加 TRAP 指令
add_instruction(
    "TRAP",
    "32-bit",
    "11000000000000000010XX0000100000",
    {"NO": [10, 11]},
    "Trigger a software interrupt"
)

# 添加 TST 指令
add_instruction(
    "TST",
    "16-bit",
    "011010XXXXXXXX10",
    {"RX": [2, 5], "RY": [6, 9]},
    "Set flags based on RX & RY, C = ((RX & RY) != 0)"
)


# 添加 TSTNBZ 指令
add_instruction(
    "TSTNBZ",
    "16-bit",
    "0110100000XXXX11",
    {"RX": [2, 5]},
    "Test RX, set flags if result is not zero, C = (RX == 0)"
)

# 添加 WAIT 指令
add_instruction(
    "WAIT",
    "32-bit",
    "11000000000000000100110000100000",
    {},
    "Wait for interrupt"
)

# 添加 XOR 指令
add_instruction(
    "XOR16",
    "16-bit",
    "011011XXXXXXXX01",
    {"RZ": [6, 9], "RX": [2, 5]},
    "RZ = RZ ^ RX"
)

add_instruction(
    "XOR32",
    "32-bit",
    "110001XXXXXXXXXX00100100010XXXXX",
    {"RY": [21, 25], "RX": [16, 20], "RZ": [0, 4]},
    "RZ = RX ^ RY"
)

# 添加 XORI 指令
add_instruction(
    "XORI",
    "32-bit",
    "111001XXXXXXXXXX0100XXXXXXXXXXXX",
    {"RZ": [21, 25], "RX": [16, 20], "IMM12": [0, 11]},
    "RZ = RX ^ zero_extend(IMM12)"
)

# 添加 XSR 指令
add_instruction(
    "XSR",
    "32-bit",
    "110001XXXXXXXXXX01001101000XXXXX",
    {"IMM5": [21, 25], "RX": [16, 20], "RZ": [0, 4]},
    "{RZ, C} = {RX, C} >>> OIMM5"
)

# 添加 XTRB0 指令
add_instruction(
    "XTRB0",
    "32-bit",
    "11000100000XXXXX01110000001XXXXX",
    {"RX": [21, 25], "RZ": [0, 4]},
    "Extract byte 0 from RX into RZ, RZ = zero_extend(RX[31:24]), C = RZ != 0"
)

# 添加 XTRB1 指令
add_instruction(
    "XTRB1",
    "32-bit",
    "11000100000XXXXX01110000010XXXXX",
    {"RX": [16, 20], "RZ": [0, 4]},
    "Extract byte 1 from RX into RZ, RZ = zero_extend(RX[23:16]), C = RZ != 0"
)

# 添加 XTRB2 指令
add_instruction(
    "XTRB2",
    "32-bit",
    "11000100000XXXXX01110000100XXXXX",
    {"RZ": [6, 9], "RX": [2, 5]},
    "Extract byte 2 from RX into RZ, RZ = zero_extend(RX[15:8]), C = RZ != 0"
)

# 添加 XTRB3 指令
add_instruction(
    "XTRB3",
    "32-bit",
    "11000100000XXXXX01110001000XXXXX",
    {"RZ": [6, 9], "RX": [2, 5]},
    "Extract byte 3 from RX into RZ, RZ = zero_extend(RX[7:0]), C = RZ != 0"
)


# 将指令集保存为 JSON 文件
with open("ck802_instruction_set.json", "w", encoding="utf-8") as json_file:
    json.dump(instruction_set, json_file, ensure_ascii=False, indent=4)

print("指令集已保存为 ck802_instruction_set.json")
