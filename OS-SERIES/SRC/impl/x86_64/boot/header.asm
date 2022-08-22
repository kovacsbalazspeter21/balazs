header_start:
    ; magic number
    dd 0xe85250d6 ;  multiboot2
    ; architecture
    dd 0 ; protected mode 1386
    ; header lenght
    dd header_emd - header_star
    ; checksum
    dd 0x100000000 - (0xe85250d6 + 0 + (header_emd - header_star))

header_end: