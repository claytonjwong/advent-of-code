//
// Created by Clayton Wong on 2018-12-13.
//

#pragma once


class Turn
{
    int last_{ right };

public:

    const static int left{ 0 }, straight{ 1 }, right{ 2 };

    char next() noexcept;
    char last() const noexcept;
};
