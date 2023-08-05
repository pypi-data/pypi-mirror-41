//  Program:      nes-py
//  File:         mapper_CNROM.hpp
//  Description:  An implementation of the CNROM mapper
//
//  Copyright (c) 2019 Christian Kauten. All rights reserved.
//

#ifndef MAPPERCNROM_HPP
#define MAPPERCNROM_HPP

#include "common.hpp"
#include "mapper.hpp"

class MapperCNROM : public Mapper {

private:
    /// whether there are 1 or 2 banks
    bool is_one_bank;
    /// TODO: what is this value
    NES_Address select_chr;

public:
    /// Create a new mapper with a cartridge.
    ///
    /// @param cart a reference to a cartridge for the mapper to access
    ///
    MapperCNROM(Cartridge& cart);

    /// Read a byte from the PRG RAM.
    ///
    /// @param address the 16-bit address of the byte to read
    /// @return the byte located at the given address in PRG RAM
    ///
    NES_Byte readPRG (NES_Address address);

    /// Write a byte to an address in the PRG RAM.
    ///
    /// @param address the 16-bit address to write to
    /// @param value the byte to write to the given address
    ///
    inline void writePRG (NES_Address address, NES_Byte value) { select_chr = value & 0x3; };

    /// Read a byte from the CHR RAM.
    ///
    /// @param address the 16-bit address of the byte to read
    /// @return the byte located at the given address in CHR RAM
    ///
    inline NES_Byte readCHR (NES_Address address) { return cartridge.getVROM()[address | (select_chr << 13)]; };

    /// Write a byte to an address in the CHR RAM.
    ///
    /// @param address the 16-bit address to write to
    /// @param value the byte to write to the given address
    ///
    void writeCHR (NES_Address address, NES_Byte value);

    /// Return the page pointer for the given address.
    ///
    /// @param address the address of the page pointer to get
    /// @return the page pointer at the given address
    ///
    const NES_Byte* getPagePtr(NES_Address address);

};

#endif // MAPPERCNROM_HPP
