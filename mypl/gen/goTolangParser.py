# Generated from C:/Users/NaTsuu/pl\goTolang.g4 by ANTLR 4.11.1
# encoding: utf-8
import sys

from antlr4 import *

if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4, 1, 73, 367, 2, 0, 7, 0, 2, 1, 7, 1, 2, 2, 7, 2, 2, 3, 7, 3, 2, 4, 7, 4, 2, 5, 7, 5, 2, 6, 7,
        6, 2, 7, 7, 7, 2, 8, 7, 8, 2, 9, 7, 9, 2, 10, 7, 10, 2, 11, 7, 11, 2, 12, 7, 12, 2, 13, 7, 13,
        2, 14, 7, 14, 2, 15, 7, 15, 2, 16, 7, 16, 2, 17, 7, 17, 2, 18, 7, 18, 2, 19, 7, 19, 2, 20,
        7, 20, 2, 21, 7, 21, 2, 22, 7, 22, 2, 23, 7, 23, 2, 24, 7, 24, 2, 25, 7, 25, 2, 26, 7, 26,
        2, 27, 7, 27, 2, 28, 7, 28, 2, 29, 7, 29, 2, 30, 7, 30, 2, 31, 7, 31, 2, 32, 7, 32, 2, 33,
        7, 33, 2, 34, 7, 34, 2, 35, 7, 35, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 81,
        8, 1, 1, 1, 1, 1, 4, 1, 85, 8, 1, 11, 1, 12, 1, 86, 1, 1, 1, 1, 4, 1, 91, 8, 1, 11, 1, 12, 1,
        92, 1, 2, 1, 2, 1, 2, 3, 2, 98, 8, 2, 1, 3, 1, 3, 1, 3, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 3, 4, 108,
        8, 4, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 3, 5, 118, 8, 5, 1, 6, 1, 6, 1, 6, 1, 7,
        1, 7, 1, 7, 1, 7, 1, 7, 1, 7, 5, 7, 129, 8, 7, 10, 7, 12, 7, 132, 9, 7, 3, 7, 134, 8, 7, 1,
        8, 1, 8, 1, 8, 5, 8, 139, 8, 8, 10, 8, 12, 8, 142, 9, 8, 1, 8, 3, 8, 145, 8, 8, 1, 9, 1, 9,
        1, 10, 1, 10, 1, 11, 1, 11, 1, 11, 1, 11, 1, 12, 1, 12, 1, 12, 1, 12, 1, 12, 1, 12, 1, 12,
        1, 12, 4, 12, 163, 8, 12, 11, 12, 12, 12, 164, 1, 12, 1, 12, 1, 13, 1, 13, 1, 13, 4, 13,
        172, 8, 13, 11, 13, 12, 13, 173, 3, 13, 176, 8, 13, 1, 14, 1, 14, 1, 14, 5, 14, 181, 8,
        14, 10, 14, 12, 14, 184, 9, 14, 1, 15, 1, 15, 1, 15, 5, 15, 189, 8, 15, 10, 15, 12, 15,
        192, 9, 15, 1, 16, 1, 16, 1, 16, 3, 16, 197, 8, 16, 1, 17, 1, 17, 1, 17, 1, 17, 5, 17, 203,
        8, 17, 10, 17, 12, 17, 206, 9, 17, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18,
        1, 18, 1, 18, 1, 18, 1, 18, 3, 18, 220, 8, 18, 1, 19, 1, 19, 1, 19, 5, 19, 225, 8, 19, 10,
        19, 12, 19, 228, 9, 19, 1, 20, 1, 20, 1, 20, 5, 20, 233, 8, 20, 10, 20, 12, 20, 236, 9,
        20, 1, 21, 1, 21, 1, 21, 5, 21, 241, 8, 21, 10, 21, 12, 21, 244, 9, 21, 1, 22, 1, 22, 1,
        22, 5, 22, 249, 8, 22, 10, 22, 12, 22, 252, 9, 22, 1, 23, 1, 23, 1, 23, 5, 23, 257, 8,
        23, 10, 23, 12, 23, 260, 9, 23, 1, 24, 1, 24, 1, 24, 5, 24, 265, 8, 24, 10, 24, 12, 24,
        268, 9, 24, 1, 25, 1, 25, 1, 25, 3, 25, 273, 8, 25, 1, 26, 1, 26, 1, 26, 3, 26, 278, 8,
        26, 1, 27, 1, 27, 5, 27, 282, 8, 27, 10, 27, 12, 27, 285, 9, 27, 1, 28, 1, 28, 3, 28, 289,
        8, 28, 1, 28, 1, 28, 1, 28, 3, 28, 294, 8, 28, 1, 28, 1, 28, 1, 28, 1, 28, 1, 28, 1, 28,
        1, 28, 1, 28, 3, 28, 304, 8, 28, 1, 29, 1, 29, 1, 29, 5, 29, 309, 8, 29, 10, 29, 12, 29,
        312, 9, 29, 1, 29, 3, 29, 315, 8, 29, 1, 30, 1, 30, 3, 30, 319, 8, 30, 1, 30, 1, 30, 1,
        30, 1, 30, 1, 30, 1, 30, 1, 30, 3, 30, 328, 8, 30, 1, 31, 1, 31, 1, 31, 5, 31, 333, 8, 31,
        10, 31, 12, 31, 336, 9, 31, 1, 31, 3, 31, 339, 8, 31, 1, 32, 1, 32, 1, 32, 5, 32, 344,
        8, 32, 10, 32, 12, 32, 347, 9, 32, 1, 32, 3, 32, 350, 8, 32, 1, 33, 1, 33, 1, 33, 5, 33,
        355, 8, 33, 10, 33, 12, 33, 358, 9, 33, 1, 33, 3, 33, 361, 8, 33, 1, 34, 1, 34, 1, 35,
        1, 35, 1, 35, 0, 0, 36, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34,
        36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 0, 5, 1, 0, 61,
        72, 1, 0, 44, 45, 1, 0, 46, 47, 2, 0, 31, 31, 48, 50, 2, 0, 46, 47, 51, 51, 392, 0, 72,
        1, 0, 0, 0, 2, 90, 1, 0, 0, 0, 4, 97, 1, 0, 0, 0, 6, 99, 1, 0, 0, 0, 8, 107, 1, 0, 0, 0, 10,
        117, 1, 0, 0, 0, 12, 119, 1, 0, 0, 0, 14, 122, 1, 0, 0, 0, 16, 135, 1, 0, 0, 0, 18, 146,
        1, 0, 0, 0, 20, 148, 1, 0, 0, 0, 22, 150, 1, 0, 0, 0, 24, 154, 1, 0, 0, 0, 26, 175, 1, 0,
        0, 0, 28, 177, 1, 0, 0, 0, 30, 185, 1, 0, 0, 0, 32, 196, 1, 0, 0, 0, 34, 198, 1, 0, 0, 0,
        36, 219, 1, 0, 0, 0, 38, 221, 1, 0, 0, 0, 40, 229, 1, 0, 0, 0, 42, 237, 1, 0, 0, 0, 44, 245,
        1, 0, 0, 0, 46, 253, 1, 0, 0, 0, 48, 261, 1, 0, 0, 0, 50, 272, 1, 0, 0, 0, 52, 274, 1, 0,
        0, 0, 54, 279, 1, 0, 0, 0, 56, 303, 1, 0, 0, 0, 58, 305, 1, 0, 0, 0, 60, 327, 1, 0, 0, 0,
        62, 329, 1, 0, 0, 0, 64, 340, 1, 0, 0, 0, 66, 351, 1, 0, 0, 0, 68, 362, 1, 0, 0, 0, 70, 364,
        1, 0, 0, 0, 72, 73, 3, 2, 1, 0, 73, 74, 5, 0, 0, 1, 74, 1, 1, 0, 0, 0, 75, 91, 5, 22, 0, 0,
        76, 91, 3, 4, 2, 0, 77, 78, 5, 58, 0, 0, 78, 79, 5, 13, 0, 0, 79, 81, 5, 22, 0, 0, 80, 77,
        1, 0, 0, 0, 80, 81, 1, 0, 0, 0, 81, 82, 1, 0, 0, 0, 82, 84, 5, 39, 0, 0, 83, 85, 3, 2, 1, 0,
        84, 83, 1, 0, 0, 0, 85, 86, 1, 0, 0, 0, 86, 84, 1, 0, 0, 0, 86, 87, 1, 0, 0, 0, 87, 88, 1,
        0, 0, 0, 88, 89, 5, 40, 0, 0, 89, 91, 1, 0, 0, 0, 90, 75, 1, 0, 0, 0, 90, 76, 1, 0, 0, 0, 90,
        80, 1, 0, 0, 0, 91, 92, 1, 0, 0, 0, 92, 90, 1, 0, 0, 0, 92, 93, 1, 0, 0, 0, 93, 3, 1, 0, 0,
        0, 94, 98, 3, 6, 3, 0, 95, 98, 3, 24, 12, 0, 96, 98, 5, 22, 0, 0, 97, 94, 1, 0, 0, 0, 97,
        95, 1, 0, 0, 0, 97, 96, 1, 0, 0, 0, 98, 5, 1, 0, 0, 0, 99, 100, 3, 8, 4, 0, 100, 101, 5, 22,
        0, 0, 101, 7, 1, 0, 0, 0, 102, 108, 3, 14, 7, 0, 103, 108, 3, 20, 10, 0, 104, 108, 3, 22,
        11, 0, 105, 108, 3, 10, 5, 0, 106, 108, 3, 12, 6, 0, 107, 102, 1, 0, 0, 0, 107, 103, 1,
        0, 0, 0, 107, 104, 1, 0, 0, 0, 107, 105, 1, 0, 0, 0, 107, 106, 1, 0, 0, 0, 108, 9, 1, 0,
        0, 0, 109, 110, 5, 1, 0, 0, 110, 118, 5, 15, 0, 0, 111, 112, 5, 2, 0, 0, 112, 113, 5, 3,
        0, 0, 113, 114, 3, 28, 14, 0, 114, 115, 5, 4, 0, 0, 115, 116, 5, 15, 0, 0, 116, 118, 1,
        0, 0, 0, 117, 109, 1, 0, 0, 0, 117, 111, 1, 0, 0, 0, 118, 11, 1, 0, 0, 0, 119, 120, 5, 59,
        0, 0, 120, 121, 5, 15, 0, 0, 121, 13, 1, 0, 0, 0, 122, 133, 3, 16, 8, 0, 123, 124, 3, 18,
        9, 0, 124, 125, 3, 64, 32, 0, 125, 134, 1, 0, 0, 0, 126, 127, 5, 38, 0, 0, 127, 129, 3,
        16, 8, 0, 128, 126, 1, 0, 0, 0, 129, 132, 1, 0, 0, 0, 130, 128, 1, 0, 0, 0, 130, 131, 1,
        0, 0, 0, 131, 134, 1, 0, 0, 0, 132, 130, 1, 0, 0, 0, 133, 123, 1, 0, 0, 0, 133, 130, 1,
        0, 0, 0, 134, 15, 1, 0, 0, 0, 135, 140, 3, 28, 14, 0, 136, 137, 5, 34, 0, 0, 137, 139,
        3, 28, 14, 0, 138, 136, 1, 0, 0, 0, 139, 142, 1, 0, 0, 0, 140, 138, 1, 0, 0, 0, 140, 141,
        1, 0, 0, 0, 141, 144, 1, 0, 0, 0, 142, 140, 1, 0, 0, 0, 143, 145, 5, 34, 0, 0, 144, 143,
        1, 0, 0, 0, 144, 145, 1, 0, 0, 0, 145, 17, 1, 0, 0, 0, 146, 147, 7, 0, 0, 0, 147, 19, 1,
        0, 0, 0, 148, 149, 5, 21, 0, 0, 149, 21, 1, 0, 0, 0, 150, 151, 5, 5, 0, 0, 151, 152, 5,
        60, 0, 0, 152, 153, 5, 15, 0, 0, 153, 23, 1, 0, 0, 0, 154, 155, 5, 17, 0, 0, 155, 156,
        5, 22, 0, 0, 156, 157, 5, 3, 0, 0, 157, 162, 5, 22, 0, 0, 158, 159, 3, 28, 14, 0, 159,
        160, 5, 35, 0, 0, 160, 161, 3, 26, 13, 0, 161, 163, 1, 0, 0, 0, 162, 158, 1, 0, 0, 0, 163,
        164, 1, 0, 0, 0, 164, 162, 1, 0, 0, 0, 164, 165, 1, 0, 0, 0, 165, 166, 1, 0, 0, 0, 166,
        167, 5, 4, 0, 0, 167, 25, 1, 0, 0, 0, 168, 176, 3, 6, 3, 0, 169, 171, 5, 22, 0, 0, 170,
        172, 3, 4, 2, 0, 171, 170, 1, 0, 0, 0, 172, 173, 1, 0, 0, 0, 173, 171, 1, 0, 0, 0, 173,
        174, 1, 0, 0, 0, 174, 176, 1, 0, 0, 0, 175, 168, 1, 0, 0, 0, 175, 169, 1, 0, 0, 0, 176,
        27, 1, 0, 0, 0, 177, 182, 3, 30, 15, 0, 178, 179, 5, 18, 0, 0, 179, 181, 3, 30, 15, 0,
        180, 178, 1, 0, 0, 0, 181, 184, 1, 0, 0, 0, 182, 180, 1, 0, 0, 0, 182, 183, 1, 0, 0, 0,
        183, 29, 1, 0, 0, 0, 184, 182, 1, 0, 0, 0, 185, 190, 3, 32, 16, 0, 186, 187, 5, 19, 0,
        0, 187, 189, 3, 32, 16, 0, 188, 186, 1, 0, 0, 0, 189, 192, 1, 0, 0, 0, 190, 188, 1, 0,
        0, 0, 190, 191, 1, 0, 0, 0, 191, 31, 1, 0, 0, 0, 192, 190, 1, 0, 0, 0, 193, 194, 5, 20,
        0, 0, 194, 197, 3, 32, 16, 0, 195, 197, 3, 34, 17, 0, 196, 193, 1, 0, 0, 0, 196, 195,
        1, 0, 0, 0, 197, 33, 1, 0, 0, 0, 198, 204, 3, 38, 19, 0, 199, 200, 3, 36, 18, 0, 200, 201,
        3, 38, 19, 0, 201, 203, 1, 0, 0, 0, 202, 199, 1, 0, 0, 0, 203, 206, 1, 0, 0, 0, 204, 202,
        1, 0, 0, 0, 204, 205, 1, 0, 0, 0, 205, 35, 1, 0, 0, 0, 206, 204, 1, 0, 0, 0, 207, 220, 5,
        52, 0, 0, 208, 220, 5, 53, 0, 0, 209, 220, 5, 54, 0, 0, 210, 220, 5, 55, 0, 0, 211, 220,
        5, 56, 0, 0, 212, 220, 5, 57, 0, 0, 213, 220, 5, 6, 0, 0, 214, 215, 5, 20, 0, 0, 215, 220,
        5, 6, 0, 0, 216, 220, 5, 7, 0, 0, 217, 218, 5, 7, 0, 0, 218, 220, 5, 20, 0, 0, 219, 207,
        1, 0, 0, 0, 219, 208, 1, 0, 0, 0, 219, 209, 1, 0, 0, 0, 219, 210, 1, 0, 0, 0, 219, 211,
        1, 0, 0, 0, 219, 212, 1, 0, 0, 0, 219, 213, 1, 0, 0, 0, 219, 214, 1, 0, 0, 0, 219, 216,
        1, 0, 0, 0, 219, 217, 1, 0, 0, 0, 220, 37, 1, 0, 0, 0, 221, 226, 3, 40, 20, 0, 222, 223,
        5, 41, 0, 0, 223, 225, 3, 40, 20, 0, 224, 222, 1, 0, 0, 0, 225, 228, 1, 0, 0, 0, 226, 224,
        1, 0, 0, 0, 226, 227, 1, 0, 0, 0, 227, 39, 1, 0, 0, 0, 228, 226, 1, 0, 0, 0, 229, 234, 3,
        42, 21, 0, 230, 231, 5, 42, 0, 0, 231, 233, 3, 42, 21, 0, 232, 230, 1, 0, 0, 0, 233, 236,
        1, 0, 0, 0, 234, 232, 1, 0, 0, 0, 234, 235, 1, 0, 0, 0, 235, 41, 1, 0, 0, 0, 236, 234, 1,
        0, 0, 0, 237, 242, 3, 44, 22, 0, 238, 239, 5, 43, 0, 0, 239, 241, 3, 44, 22, 0, 240, 238,
        1, 0, 0, 0, 241, 244, 1, 0, 0, 0, 242, 240, 1, 0, 0, 0, 242, 243, 1, 0, 0, 0, 243, 43, 1,
        0, 0, 0, 244, 242, 1, 0, 0, 0, 245, 250, 3, 46, 23, 0, 246, 247, 7, 1, 0, 0, 247, 249,
        3, 46, 23, 0, 248, 246, 1, 0, 0, 0, 249, 252, 1, 0, 0, 0, 250, 248, 1, 0, 0, 0, 250, 251,
        1, 0, 0, 0, 251, 45, 1, 0, 0, 0, 252, 250, 1, 0, 0, 0, 253, 258, 3, 48, 24, 0, 254, 255,
        7, 2, 0, 0, 255, 257, 3, 48, 24, 0, 256, 254, 1, 0, 0, 0, 257, 260, 1, 0, 0, 0, 258, 256,
        1, 0, 0, 0, 258, 259, 1, 0, 0, 0, 259, 47, 1, 0, 0, 0, 260, 258, 1, 0, 0, 0, 261, 266, 3,
        50, 25, 0, 262, 263, 7, 3, 0, 0, 263, 265, 3, 50, 25, 0, 264, 262, 1, 0, 0, 0, 265, 268,
        1, 0, 0, 0, 266, 264, 1, 0, 0, 0, 266, 267, 1, 0, 0, 0, 267, 49, 1, 0, 0, 0, 268, 266, 1,
        0, 0, 0, 269, 270, 7, 4, 0, 0, 270, 273, 3, 50, 25, 0, 271, 273, 3, 52, 26, 0, 272, 269,
        1, 0, 0, 0, 272, 271, 1, 0, 0, 0, 273, 51, 1, 0, 0, 0, 274, 277, 3, 54, 27, 0, 275, 276,
        5, 37, 0, 0, 276, 278, 3, 50, 25, 0, 277, 275, 1, 0, 0, 0, 277, 278, 1, 0, 0, 0, 278, 53,
        1, 0, 0, 0, 279, 283, 3, 56, 28, 0, 280, 282, 3, 60, 30, 0, 281, 280, 1, 0, 0, 0, 282,
        285, 1, 0, 0, 0, 283, 281, 1, 0, 0, 0, 283, 284, 1, 0, 0, 0, 284, 55, 1, 0, 0, 0, 285, 283,
        1, 0, 0, 0, 286, 288, 5, 32, 0, 0, 287, 289, 3, 58, 29, 0, 288, 287, 1, 0, 0, 0, 288, 289,
        1, 0, 0, 0, 289, 290, 1, 0, 0, 0, 290, 304, 5, 33, 0, 0, 291, 293, 5, 39, 0, 0, 292, 294,
        3, 58, 29, 0, 293, 292, 1, 0, 0, 0, 293, 294, 1, 0, 0, 0, 294, 295, 1, 0, 0, 0, 295, 304,
        5, 40, 0, 0, 296, 304, 5, 11, 0, 0, 297, 304, 5, 12, 0, 0, 298, 304, 5, 23, 0, 0, 299,
        304, 5, 15, 0, 0, 300, 304, 5, 14, 0, 0, 301, 304, 5, 8, 0, 0, 302, 304, 5, 9, 0, 0, 303,
        286, 1, 0, 0, 0, 303, 291, 1, 0, 0, 0, 303, 296, 1, 0, 0, 0, 303, 297, 1, 0, 0, 0, 303,
        298, 1, 0, 0, 0, 303, 299, 1, 0, 0, 0, 303, 300, 1, 0, 0, 0, 303, 301, 1, 0, 0, 0, 303,
        302, 1, 0, 0, 0, 304, 57, 1, 0, 0, 0, 305, 310, 3, 28, 14, 0, 306, 307, 5, 34, 0, 0, 307,
        309, 3, 28, 14, 0, 308, 306, 1, 0, 0, 0, 309, 312, 1, 0, 0, 0, 310, 308, 1, 0, 0, 0, 310,
        311, 1, 0, 0, 0, 311, 314, 1, 0, 0, 0, 312, 310, 1, 0, 0, 0, 313, 315, 5, 34, 0, 0, 314,
        313, 1, 0, 0, 0, 314, 315, 1, 0, 0, 0, 315, 59, 1, 0, 0, 0, 316, 318, 5, 32, 0, 0, 317,
        319, 3, 66, 33, 0, 318, 317, 1, 0, 0, 0, 318, 319, 1, 0, 0, 0, 319, 320, 1, 0, 0, 0, 320,
        328, 5, 33, 0, 0, 321, 322, 5, 39, 0, 0, 322, 323, 3, 62, 31, 0, 323, 324, 5, 40, 0, 0,
        324, 328, 1, 0, 0, 0, 325, 326, 5, 30, 0, 0, 326, 328, 5, 23, 0, 0, 327, 316, 1, 0, 0,
        0, 327, 321, 1, 0, 0, 0, 327, 325, 1, 0, 0, 0, 328, 61, 1, 0, 0, 0, 329, 334, 3, 68, 34,
        0, 330, 331, 5, 34, 0, 0, 331, 333, 3, 68, 34, 0, 332, 330, 1, 0, 0, 0, 333, 336, 1, 0,
        0, 0, 334, 332, 1, 0, 0, 0, 334, 335, 1, 0, 0, 0, 335, 338, 1, 0, 0, 0, 336, 334, 1, 0,
        0, 0, 337, 339, 5, 34, 0, 0, 338, 337, 1, 0, 0, 0, 338, 339, 1, 0, 0, 0, 339, 63, 1, 0,
        0, 0, 340, 345, 3, 28, 14, 0, 341, 342, 5, 34, 0, 0, 342, 344, 3, 28, 14, 0, 343, 341,
        1, 0, 0, 0, 344, 347, 1, 0, 0, 0, 345, 343, 1, 0, 0, 0, 345, 346, 1, 0, 0, 0, 346, 349,
        1, 0, 0, 0, 347, 345, 1, 0, 0, 0, 348, 350, 5, 34, 0, 0, 349, 348, 1, 0, 0, 0, 349, 350,
        1, 0, 0, 0, 350, 65, 1, 0, 0, 0, 351, 356, 3, 70, 35, 0, 352, 353, 5, 34, 0, 0, 353, 355,
        3, 70, 35, 0, 354, 352, 1, 0, 0, 0, 355, 358, 1, 0, 0, 0, 356, 354, 1, 0, 0, 0, 356, 357,
        1, 0, 0, 0, 357, 360, 1, 0, 0, 0, 358, 356, 1, 0, 0, 0, 359, 361, 5, 34, 0, 0, 360, 359,
        1, 0, 0, 0, 360, 361, 1, 0, 0, 0, 361, 67, 1, 0, 0, 0, 362, 363, 3, 28, 14, 0, 363, 69,
        1, 0, 0, 0, 364, 365, 3, 28, 14, 0, 365, 71, 1, 0, 0, 0, 41, 80, 86, 90, 92, 97, 107, 117,
        130, 133, 140, 144, 164, 173, 175, 182, 190, 196, 204, 219, 226, 234, 242, 250,
        258, 266, 272, 277, 283, 288, 293, 303, 310, 314, 318, 327, 334, 338, 345, 349,
        356, 360
    ]


class goTolangParser(Parser):
    grammarFileName = "goTolang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = ["<INVALID>", "'goto'", "'goif'", "'{'", "'}'", "'goback'",
                    "'in'", "'is'", "'...'", "'None'", "<INVALID>", "'True'",
                    "'False'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                    "'if'", "'or'", "'and'", "'not'", "'pass'", "<INVALID>",
                    "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                    "<INVALID>", "<INVALID>", "<INVALID>", "'.'", "'*'",
                    "'('", "')'", "','", "':'", "';'", "'**'", "'='", "'['",
                    "']'", "'|'", "'^'", "'&'", "'<<'", "'>>'", "'+'",
                    "'-'", "'/'", "'%'", "'//'", "'~'", "'<'", "'>'", "'=='",
                    "'>='", "'<='", "'!='", "'@'", "'->'", "'<-'", "'+='",
                    "'-='", "'*='", "'/='", "'%='", "'&='", "'|='", "'^='",
                    "'<<='", "'>>='", "'**='", "'//='"]

    symbolicNames = ["<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "SKIP_", "BOOL_TRUE", "BOOL_FALSE",
                     "DECORATOR", "STRING", "NUMBER", "INTEGER", "IF",
                     "OR", "AND", "NOT", "PASS", "NEWLINE", "NAME", "STRING_LITERAL",
                     "DECIMAL_INTEGER", "OCT_INTEGER", "HEX_INTEGER", "BIN_INTEGER",
                     "FLOAT_NUMBER", "DOT", "STAR", "OPEN_PAREN", "CLOSE_PAREN",
                     "COMMA", "COLON", "SEMI_COLON", "POWER", "ASSIGN",
                     "OPEN_BRACK", "CLOSE_BRACK", "OR_OP", "XOR", "AND_OP",
                     "LEFT_SHIFT", "RIGHT_SHIFT", "ADD", "MINUS", "DIV",
                     "MOD", "IDIV", "NOT_OP", "LESS_THAN", "GREATER_THAN",
                     "EQUALS", "GT_EQ", "LT_EQ", "NOT_EQ_2", "AT", "ARROW",
                     "INV_ARROW", "ADD_ASSIGN", "SUB_ASSIGN", "MULT_ASSIGN",
                     "DIV_ASSIGN", "MOD_ASSIGN", "AND_ASSIGN", "OR_ASSIGN",
                     "XOR_ASSIGN", "LEFT_SHIFT_ASSIGN", "RIGHT_SHIFT_ASSIGN",
                     "POWER_ASSIGN", "IDIV_ASSIGN", "UNKNOWN_CHAR"]

    RULE_file_input = 0
    RULE_file_input_no_eof = 1
    RULE_stmt = 2
    RULE_simple_stmt = 3
    RULE_small_stmt = 4
    RULE_goto_stmt = 5
    RULE_label_stmt = 6
    RULE_expr_stmt = 7
    RULE_testlist_star_expr = 8
    RULE_augassign = 9
    RULE_pass_stmt = 10
    RULE_goback_stmt = 11
    RULE_if_stmt = 12
    RULE_suite = 13
    RULE_or_test = 14
    RULE_and_test = 15
    RULE_not_test = 16
    RULE_comparison = 17
    RULE_comp_op = 18
    RULE_expr = 19
    RULE_xor_expr = 20
    RULE_and_expr = 21
    RULE_shift_expr = 22
    RULE_arith_expr = 23
    RULE_term = 24
    RULE_factor = 25
    RULE_power = 26
    RULE_atom_expr = 27
    RULE_atom = 28
    RULE_testlist_comp = 29
    RULE_trailer = 30
    RULE_subscriptlist = 31
    RULE_testlist = 32
    RULE_arglist = 33
    RULE_subscript = 34
    RULE_argument = 35

    ruleNames = ["file_input", "file_input_no_eof", "stmt", "simple_stmt",
                 "small_stmt", "goto_stmt", "label_stmt", "expr_stmt",
                 "testlist_star_expr", "augassign", "pass_stmt", "goback_stmt",
                 "if_stmt", "suite", "or_test", "and_test", "not_test",
                 "comparison", "comp_op", "expr", "xor_expr", "and_expr",
                 "shift_expr", "arith_expr", "term", "factor", "power",
                 "atom_expr", "atom", "testlist_comp", "trailer", "subscriptlist",
                 "testlist", "arglist", "subscript", "argument"]

    EOF = Token.EOF
    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    SKIP_ = 10
    BOOL_TRUE = 11
    BOOL_FALSE = 12
    DECORATOR = 13
    STRING = 14
    NUMBER = 15
    INTEGER = 16
    IF = 17
    OR = 18
    AND = 19
    NOT = 20
    PASS = 21
    NEWLINE = 22
    NAME = 23
    STRING_LITERAL = 24
    DECIMAL_INTEGER = 25
    OCT_INTEGER = 26
    HEX_INTEGER = 27
    BIN_INTEGER = 28
    FLOAT_NUMBER = 29
    DOT = 30
    STAR = 31
    OPEN_PAREN = 32
    CLOSE_PAREN = 33
    COMMA = 34
    COLON = 35
    SEMI_COLON = 36
    POWER = 37
    ASSIGN = 38
    OPEN_BRACK = 39
    CLOSE_BRACK = 40
    OR_OP = 41
    XOR = 42
    AND_OP = 43
    LEFT_SHIFT = 44
    RIGHT_SHIFT = 45
    ADD = 46
    MINUS = 47
    DIV = 48
    MOD = 49
    IDIV = 50
    NOT_OP = 51
    LESS_THAN = 52
    GREATER_THAN = 53
    EQUALS = 54
    GT_EQ = 55
    LT_EQ = 56
    NOT_EQ_2 = 57
    AT = 58
    ARROW = 59
    INV_ARROW = 60
    ADD_ASSIGN = 61
    SUB_ASSIGN = 62
    MULT_ASSIGN = 63
    DIV_ASSIGN = 64
    MOD_ASSIGN = 65
    AND_ASSIGN = 66
    OR_ASSIGN = 67
    XOR_ASSIGN = 68
    LEFT_SHIFT_ASSIGN = 69
    RIGHT_SHIFT_ASSIGN = 70
    POWER_ASSIGN = 71
    IDIV_ASSIGN = 72
    UNKNOWN_CHAR = 73

    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None

    class File_inputContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def file_input_no_eof(self):
            return self.getTypedRuleContext(goTolangParser.File_input_no_eofContext, 0)

        def EOF(self):
            return self.getToken(goTolangParser.EOF, 0)

        def getRuleIndex(self):
            return goTolangParser.RULE_file_input

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterFile_input"):
                listener.enterFile_input(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitFile_input"):
                listener.exitFile_input(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitFile_input"):
                return visitor.visitFile_input(self)
            else:
                return visitor.visitChildren(self)

    def file_input(self):

        localctx = goTolangParser.File_inputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_file_input)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.file_input_no_eof()
            self.state = 73
            self.match(goTolangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class File_input_no_eofContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i: int = None):
            if i is None:
                return self.getTokens(goTolangParser.NEWLINE)
            else:
                return self.getToken(goTolangParser.NEWLINE, i)

        def stmt(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(goTolangParser.StmtContext)
            else:
                return self.getTypedRuleContext(goTolangParser.StmtContext, i)

        def OPEN_BRACK(self, i: int = None):
            if i is None:
                return self.getTokens(goTolangParser.OPEN_BRACK)
            else:
                return self.getToken(goTolangParser.OPEN_BRACK, i)

        def CLOSE_BRACK(self, i: int = None):
            if i is None:
                return self.getTokens(goTolangParser.CLOSE_BRACK)
            else:
                return self.getToken(goTolangParser.CLOSE_BRACK, i)

        def AT(self, i: int = None):
            if i is None:
                return self.getTokens(goTolangParser.AT)
            else:
                return self.getToken(goTolangParser.AT, i)

        def DECORATOR(self, i: int = None):
            if i is None:
                return self.getTokens(goTolangParser.DECORATOR)
            else:
                return self.getToken(goTolangParser.DECORATOR, i)

        def file_input_no_eof(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(goTolangParser.File_input_no_eofContext)
            else:
                return self.getTypedRuleContext(goTolangParser.File_input_no_eofContext, i)

        def getRuleIndex(self):
            return goTolangParser.RULE_file_input_no_eof

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterFile_input_no_eof"):
                listener.enterFile_input_no_eof(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitFile_input_no_eof"):
                listener.exitFile_input_no_eof(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitFile_input_no_eof"):
                return visitor.visitFile_input_no_eof(self)
            else:
                return visitor.visitChildren(self)

    def file_input_no_eof(self):

        localctx = goTolangParser.File_input_no_eofContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_file_input_no_eof)
        self._la = 0  # Token _type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self._errHandler.sync(self)
            _alt = 1
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 90
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input, 2, self._ctx)
                    if la_ == 1:
                        self.state = 75
                        self.match(goTolangParser.NEWLINE)
                        pass

                    elif la_ == 2:
                        self.state = 76
                        self.stmt()
                        pass

                    elif la_ == 3:
                        self.state = 80
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la == 58:
                            self.state = 77
                            self.match(goTolangParser.AT)
                            self.state = 78
                            self.match(goTolangParser.DECORATOR)
                            self.state = 79
                            self.match(goTolangParser.NEWLINE)

                        self.state = 82
                        self.match(goTolangParser.OPEN_BRACK)
                        self.state = 84
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while True:
                            self.state = 83
                            self.file_input_no_eof()
                            self.state = 86
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 867154588568050470) != 0):
                                break

                        self.state = 88
                        self.match(goTolangParser.CLOSE_BRACK)
                        pass



                else:
                    raise NoViableAltException(self)
                self.state = 92
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 3, self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple_stmt(self):
            return self.getTypedRuleContext(goTolangParser.Simple_stmtContext, 0)

        def if_stmt(self):
            return self.getTypedRuleContext(goTolangParser.If_stmtContext, 0)

        def NEWLINE(self):
            return self.getToken(goTolangParser.NEWLINE, 0)

        def getRuleIndex(self):
            return goTolangParser.RULE_stmt

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterStmt"):
                listener.enterStmt(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitStmt"):
                listener.exitStmt(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitStmt"):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)

    def stmt(self):

        localctx = goTolangParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stmt)
        try:
            self.state = 97
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 5, 8, 9, 11, 12, 14, 15, 20, 21, 23, 32, 39, 46, 47, 51, 59]:
                self.enterOuterAlt(localctx, 1)
                self.state = 94
                self.simple_stmt()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 95
                self.if_stmt()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 3)
                self.state = 96
                self.match(goTolangParser.NEWLINE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Simple_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def small_stmt(self):
            return self.getTypedRuleContext(goTolangParser.Small_stmtContext, 0)

        def NEWLINE(self):
            return self.getToken(goTolangParser.NEWLINE, 0)

        def getRuleIndex(self):
            return goTolangParser.RULE_simple_stmt

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterSimple_stmt"):
                listener.enterSimple_stmt(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitSimple_stmt"):
                listener.exitSimple_stmt(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitSimple_stmt"):
                return visitor.visitSimple_stmt(self)
            else:
                return visitor.visitChildren(self)

    def simple_stmt(self):

        localctx = goTolangParser.Simple_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_simple_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.small_stmt()
            self.state = 100
            self.match(goTolangParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Small_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def getRuleIndex(self):
            return goTolangParser.RULE_small_stmt

        def copyFrom(self, ctx: ParserRuleContext):
            super().copyFrom(ctx)

    class BpassContext(Small_stmtContext):

        def __init__(self, parser, ctx: ParserRuleContext):  # actually a goTolangParser.Small_stmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def pass_stmt(self):
            return self.getTypedRuleContext(goTolangParser.Pass_stmtContext, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterBpass"):
                listener.enterBpass(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitBpass"):
                listener.exitBpass(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitBpass"):
                return visitor.visitBpass(self)
            else:
                return visitor.visitChildren(self)

    class BexprContext(Small_stmtContext):

        def __init__(self, parser, ctx: ParserRuleContext):  # actually a goTolangParser.Small_stmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr_stmt(self):
            return self.getTypedRuleContext(goTolangParser.Expr_stmtContext, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterBexpr"):
                listener.enterBexpr(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitBexpr"):
                listener.exitBexpr(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitBexpr"):
                return visitor.visitBexpr(self)
            else:
                return visitor.visitChildren(self)

    class BgotoContext(Small_stmtContext):

        def __init__(self, parser, ctx: ParserRuleContext):  # actually a goTolangParser.Small_stmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def goto_stmt(self):
            return self.getTypedRuleContext(goTolangParser.Goto_stmtContext, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterBgoto"):
                listener.enterBgoto(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitBgoto"):
                listener.exitBgoto(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitBgoto"):
                return visitor.visitBgoto(self)
            else:
                return visitor.visitChildren(self)

    class BgobackContext(Small_stmtContext):

        def __init__(self, parser, ctx: ParserRuleContext):  # actually a goTolangParser.Small_stmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def goback_stmt(self):
            return self.getTypedRuleContext(goTolangParser.Goback_stmtContext, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterBgoback"):
                listener.enterBgoback(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitBgoback"):
                listener.exitBgoback(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitBgoback"):
                return visitor.visitBgoback(self)
            else:
                return visitor.visitChildren(self)

    class BlabelContext(Small_stmtContext):

        def __init__(self, parser, ctx: ParserRuleContext):  # actually a goTolangParser.Small_stmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def label_stmt(self):
            return self.getTypedRuleContext(goTolangParser.Label_stmtContext, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterBlabel"):
                listener.enterBlabel(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitBlabel"):
                listener.exitBlabel(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitBlabel"):
                return visitor.visitBlabel(self)
            else:
                return visitor.visitChildren(self)

    def small_stmt(self):

        localctx = goTolangParser.Small_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_small_stmt)
        try:
            self.state = 107
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8, 9, 11, 12, 14, 15, 20, 23, 32, 39, 46, 47, 51]:
                localctx = goTolangParser.BexprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.expr_stmt()
                pass
            elif token in [21]:
                localctx = goTolangParser.BpassContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 103
                self.pass_stmt()
                pass
            elif token in [5]:
                localctx = goTolangParser.BgobackContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 104
                self.goback_stmt()
                pass
            elif token in [1, 2]:
                localctx = goTolangParser.BgotoContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 105
                self.goto_stmt()
                pass
            elif token in [59]:
                localctx = goTolangParser.BlabelContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 106
                self.label_stmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Goto_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def getRuleIndex(self):
            return goTolangParser.RULE_goto_stmt

        def copyFrom(self, ctx: ParserRuleContext):
            super().copyFrom(ctx)

    class BtoContext(Goto_stmtContext):

        def __init__(self, parser, ctx: ParserRuleContext):  # actually a goTolangParser.Goto_stmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(goTolangParser.NUMBER, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterBto"):
                listener.enterBto(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitBto"):
                listener.exitBto(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitBto"):
                return visitor.visitBto(self)
            else:
                return visitor.visitChildren(self)

    class BifContext(Goto_stmtContext):

        def __init__(self, parser, ctx: ParserRuleContext):  # actually a goTolangParser.Goto_stmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def or_test(self):
            return self.getTypedRuleContext(goTolangParser.Or_testContext, 0)

        def NUMBER(self):
            return self.getToken(goTolangParser.NUMBER, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterBif"):
                listener.enterBif(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitBif"):
                listener.exitBif(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitBif"):
                return visitor.visitBif(self)
            else:
                return visitor.visitChildren(self)

    def goto_stmt(self):

        localctx = goTolangParser.Goto_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_goto_stmt)
        try:
            self.state = 117
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = goTolangParser.BtoContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.match(goTolangParser.T__0)
                self.state = 110
                self.match(goTolangParser.NUMBER)
                pass
            elif token in [2]:
                localctx = goTolangParser.BifContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 111
                self.match(goTolangParser.T__1)
                self.state = 112
                self.match(goTolangParser.T__2)
                self.state = 113
                self.or_test()
                self.state = 114
                self.match(goTolangParser.T__3)
                self.state = 115
                self.match(goTolangParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Label_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARROW(self):
            return self.getToken(goTolangParser.ARROW, 0)

        def NUMBER(self):
            return self.getToken(goTolangParser.NUMBER, 0)

        def getRuleIndex(self):
            return goTolangParser.RULE_label_stmt

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterLabel_stmt"):
                listener.enterLabel_stmt(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitLabel_stmt"):
                listener.exitLabel_stmt(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitLabel_stmt"):
                return visitor.visitLabel_stmt(self)
            else:
                return visitor.visitChildren(self)

    def label_stmt(self):

        localctx = goTolangParser.Label_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_label_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(goTolangParser.ARROW)
            self.state = 120
            self.match(goTolangParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expr_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def testlist_star_expr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(goTolangParser.Testlist_star_exprContext)
            else:
                return self.getTypedRuleContext(goTolangParser.Testlist_star_exprContext, i)

        def augassign(self):
            return self.getTypedRuleContext(goTolangParser.AugassignContext, 0)

        def testlist(self):
            return self.getTypedRuleContext(goTolangParser.TestlistContext, 0)

        def ASSIGN(self, i: int = None):
            if i is None:
                return self.getTokens(goTolangParser.ASSIGN)
            else:
                return self.getToken(goTolangParser.ASSIGN, i)

        def getRuleIndex(self):
            return goTolangParser.RULE_expr_stmt

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterExpr_stmt"):
                listener.enterExpr_stmt(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitExpr_stmt"):
                listener.exitExpr_stmt(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitExpr_stmt"):
                return visitor.visitExpr_stmt(self)
            else:
                return visitor.visitChildren(self)

    def expr_stmt(self):

        localctx = goTolangParser.Expr_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_expr_stmt)
        self._la = 0  # Token _type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.testlist_star_expr()
            self.state = 133
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72]:
                self.state = 123
                self.augassign()

                self.state = 124
                self.testlist()
                pass
            elif token in [22, 38]:
                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la == 38:
                    self.state = 126
                    self.match(goTolangParser.ASSIGN)

                    self.state = 127
                    self.testlist_star_expr()
                    self.state = 132
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Testlist_star_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def or_test(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(goTolangParser.Or_testContext)
            else:
                return self.getTypedRuleContext(goTolangParser.Or_testContext, i)

        def COMMA(self, i: int = None):
            if i is None:
                return self.getTokens(goTolangParser.COMMA)
            else:
                return self.getToken(goTolangParser.COMMA, i)

        def getRuleIndex(self):
            return goTolangParser.RULE_testlist_star_expr

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterTestlist_star_expr"):
                listener.enterTestlist_star_expr(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitTestlist_star_expr"):
                listener.exitTestlist_star_expr(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitTestlist_star_expr"):
                return visitor.visitTestlist_star_expr(self)
            else:
                return visitor.visitChildren(self)

    def testlist_star_expr(self):

        localctx = goTolangParser.Testlist_star_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_testlist_star_expr)
        self._la = 0  # Token _type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.or_test()
            self.state = 140
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 9, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 136
                    self.match(goTolangParser.COMMA)
                    self.state = 137
                    self.or_test()
                self.state = 142
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 9, self._ctx)

            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 34:
                self.state = 143
                self.match(goTolangParser.COMMA)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AugassignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD_ASSIGN(self):
            return self.getToken(goTolangParser.ADD_ASSIGN, 0)

        def SUB_ASSIGN(self):
            return self.getToken(goTolangParser.SUB_ASSIGN, 0)

        def MULT_ASSIGN(self):
            return self.getToken(goTolangParser.MULT_ASSIGN, 0)

        def DIV_ASSIGN(self):
            return self.getToken(goTolangParser.DIV_ASSIGN, 0)

        def MOD_ASSIGN(self):
            return self.getToken(goTolangParser.MOD_ASSIGN, 0)

        def AND_ASSIGN(self):
            return self.getToken(goTolangParser.AND_ASSIGN, 0)

        def OR_ASSIGN(self):
            return self.getToken(goTolangParser.OR_ASSIGN, 0)

        def XOR_ASSIGN(self):
            return self.getToken(goTolangParser.XOR_ASSIGN, 0)

        def LEFT_SHIFT_ASSIGN(self):
            return self.getToken(goTolangParser.LEFT_SHIFT_ASSIGN, 0)

        def RIGHT_SHIFT_ASSIGN(self):
            return self.getToken(goTolangParser.RIGHT_SHIFT_ASSIGN, 0)

        def POWER_ASSIGN(self):
            return self.getToken(goTolangParser.POWER_ASSIGN, 0)

        def IDIV_ASSIGN(self):
            return self.getToken(goTolangParser.IDIV_ASSIGN, 0)

        def getRuleIndex(self):
            return goTolangParser.RULE_augassign

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterAugassign"):
                listener.enterAugassign(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitAugassign"):
                listener.exitAugassign(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitAugassign"):
                return visitor.visitAugassign(self)
            else:
                return visitor.visitChildren(self)

    def augassign(self):

        localctx = goTolangParser.AugassignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_augassign)
        self._la = 0  # Token _type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            _la = self._input.LA(1)
            if not ((((_la - 61)) & ~0x3f) == 0 and ((1 << (_la - 61)) & 4095) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Pass_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PASS(self):
            return self.getToken(goTolangParser.PASS, 0)

        def getRuleIndex(self):
            return goTolangParser.RULE_pass_stmt

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterPass_stmt"):
                listener.enterPass_stmt(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitPass_stmt"):
                listener.exitPass_stmt(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitPass_stmt"):
                return visitor.visitPass_stmt(self)
            else:
                return visitor.visitChildren(self)

    def pass_stmt(self):

        localctx = goTolangParser.Pass_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_pass_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(goTolangParser.PASS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Goback_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INV_ARROW(self):
            return self.getToken(goTolangParser.INV_ARROW, 0)

        def NUMBER(self):
            return self.getToken(goTolangParser.NUMBER, 0)

        def getRuleIndex(self):
            return goTolangParser.RULE_goback_stmt

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterGoback_stmt"):
                listener.enterGoback_stmt(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitGoback_stmt"):
                listener.exitGoback_stmt(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitGoback_stmt"):
                return visitor.visitGoback_stmt(self)
            else:
                return visitor.visitChildren(self)

    def goback_stmt(self):

        localctx = goTolangParser.Goback_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_goback_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(goTolangParser.T__4)
            self.state = 151
            self.match(goTolangParser.INV_ARROW)
            self.state = 152
            self.match(goTolangParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(goTolangParser.IF, 0)

        def NEWLINE(self, i: int = None):
            if i is None:
                return self.getTokens(goTolangParser.NEWLINE)
            else:
                return self.getToken(goTolangParser.NEWLINE, i)

        def or_test(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(goTolangParser.Or_testContext)
            else:
                return self.getTypedRuleContext(goTolangParser.Or_testContext, i)

        def COLON(self, i: int = None):
            if i is None:
                return self.getTokens(goTolangParser.COLON)
            else:
                return self.getToken(goTolangParser.COLON, i)

        def suite(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(goTolangParser.SuiteContext)
            else:
                return self.getTypedRuleContext(goTolangParser.SuiteContext, i)

        def getRuleIndex(self):
            return goTolangParser.RULE_if_stmt

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterIf_stmt"):
                listener.enterIf_stmt(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitIf_stmt"):
                listener.exitIf_stmt(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitIf_stmt"):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)

    def if_stmt(self):

        localctx = goTolangParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_if_stmt)
        self._la = 0  # Token _type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(goTolangParser.IF)
            self.state = 155
            self.match(goTolangParser.NEWLINE)
            self.state = 156
            self.match(goTolangParser.T__2)
            self.state = 157
            self.match(goTolangParser.NEWLINE)
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 158
                self.or_test()
                self.state = 159
                self.match(goTolangParser.COLON)
                self.state = 160
                self.suite()
                self.state = 164
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 2463460106492672) != 0):
                    break

            self.state = 166
            self.match(goTolangParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SuiteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple_stmt(self):
            return self.getTypedRuleContext(goTolangParser.Simple_stmtContext, 0)

        def NEWLINE(self):
            return self.getToken(goTolangParser.NEWLINE, 0)

        def stmt(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(goTolangParser.StmtContext)
            else:
                return self.getTypedRuleContext(goTolangParser.StmtContext, i)

        def getRuleIndex(self):
            return goTolangParser.RULE_suite

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterSuite"):
                listener.enterSuite(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitSuite"):
                listener.exitSuite(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitSuite"):
                return visitor.visitSuite(self)
            else:
                return visitor.visitChildren(self)

    def suite(self):

        localctx = goTolangParser.SuiteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_suite)
        try:
            self.state = 175
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 5, 8, 9, 11, 12, 14, 15, 20, 21, 23, 32, 39, 46, 47, 51, 59]:
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self.simple_stmt()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 169
                self.match(goTolangParser.NEWLINE)
                self.state = 171
                self._errHandler.sync(self)
                _alt = 1
                while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 170
                        self.stmt()

                    else:
                        raise NoViableAltException(self)
                    self.state = 173
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input, 12, self._ctx)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Or_testContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def and_test(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(goTolangParser.And_testContext)
            else:
                return self.getTypedRuleContext(goTolangParser.And_testContext, i)

        def OR(self, i: int = None):
            if i is None:
                return self.getTokens(goTolangParser.OR)
            else:
                return self.getToken(goTolangParser.OR, i)

        def getRuleIndex(self):
            return goTolangParser.RULE_or_test

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterOr_test"):
                listener.enterOr_test(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitOr_test"):
                listener.exitOr_test(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitOr_test"):
                return visitor.visitOr_test(self)
            else:
                return visitor.visitChildren(self)

    def or_test(self):

        localctx = goTolangParser.Or_testContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_or_test)
        self._la = 0  # Token _type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.and_test()
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == 18:
                self.state = 178
                self.match(goTolangParser.OR)
                self.state = 179
                self.and_test()
                self.state = 184
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class And_testContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def not_test(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(goTolangParser.Not_testContext)
            else:
                return self.getTypedRuleContext(goTolangParser.Not_testContext, i)

        def AND(self, i: int = None):
            if i is None:
                return self.getTokens(goTolangParser.AND)
            else:
                return self.getToken(goTolangParser.AND, i)

        def getRuleIndex(self):
            return goTolangParser.RULE_and_test

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterAnd_test"):
                listener.enterAnd_test(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitAnd_test"):
                listener.exitAnd_test(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitAnd_test"):
                return visitor.visitAnd_test(self)
            else:
                return visitor.visitChildren(self)

    def and_test(self):

        localctx = goTolangParser.And_testContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_and_test)
        self._la = 0  # Token _type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.not_test()
            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == 19:
                self.state = 186
                self.match(goTolangParser.AND)
                self.state = 187
                self.not_test()
                self.state = 192
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Not_testContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(goTolangParser.NOT, 0)

        def not_test(self):
            return self.getTypedRuleContext(goTolangParser.Not_testContext, 0)

        def comparison(self):
            return self.getTypedRuleContext(goTolangParser.ComparisonContext, 0)

        def getRuleIndex(self):
            return goTolangParser.RULE_not_test

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterNot_test"):
                listener.enterNot_test(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitNot_test"):
                listener.exitNot_test(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitNot_test"):
                return visitor.visitNot_test(self)
            else:
                return visitor.visitChildren(self)

    def not_test(self):

        localctx = goTolangParser.Not_testContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_not_test)
        try:
            self.state = 196
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self.match(goTolangParser.NOT)
                self.state = 194
                self.not_test()
                pass
            elif token in [8, 9, 11, 12, 14, 15, 23, 32, 39, 46, 47, 51]:
                self.enterOuterAlt(localctx, 2)
                self.state = 195
                self.comparison()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(goTolangParser.ExprContext)
            else:
                return self.getTypedRuleContext(goTolangParser.ExprContext, i)

        def comp_op(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(goTolangParser.Comp_opContext)
            else:
                return self.getTypedRuleContext(goTolangParser.Comp_opContext, i)

        def getRuleIndex(self):
            return goTolangParser.RULE_comparison

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterComparison"):
                listener.enterComparison(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitComparison"):
                listener.exitComparison(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitComparison"):
                return visitor.visitComparison(self)
            else:
                return visitor.visitChildren(self)

    def comparison(self):

        localctx = goTolangParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_comparison)
        self._la = 0  # Token _type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.expr()
            self.state = 204
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 283726776525390016) != 0:
                self.state = 199
                self.comp_op()
                self.state = 200
                self.expr()
                self.state = 206
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Comp_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LESS_THAN(self):
            return self.getToken(goTolangParser.LESS_THAN, 0)

        def GREATER_THAN(self):
            return self.getToken(goTolangParser.GREATER_THAN, 0)

        def EQUALS(self):
            return self.getToken(goTolangParser.EQUALS, 0)

        def GT_EQ(self):
            return self.getToken(goTolangParser.GT_EQ, 0)

        def LT_EQ(self):
            return self.getToken(goTolangParser.LT_EQ, 0)

        def NOT_EQ_2(self):
            return self.getToken(goTolangParser.NOT_EQ_2, 0)

        def NOT(self):
            return self.getToken(goTolangParser.NOT, 0)

        def getRuleIndex(self):
            return goTolangParser.RULE_comp_op

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterComp_op"):
                listener.enterComp_op(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitComp_op"):
                listener.exitComp_op(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitComp_op"):
                return visitor.visitComp_op(self)
            else:
                return visitor.visitChildren(self)

    def comp_op(self):

        localctx = goTolangParser.Comp_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_comp_op)
        try:
            self.state = 219
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 18, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 207
                self.match(goTolangParser.LESS_THAN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 208
                self.match(goTolangParser.GREATER_THAN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 209
                self.match(goTolangParser.EQUALS)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 210
                self.match(goTolangParser.GT_EQ)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 211
                self.match(goTolangParser.LT_EQ)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 212
                self.match(goTolangParser.NOT_EQ_2)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 213
                self.match(goTolangParser.T__5)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 214
                self.match(goTolangParser.NOT)
                self.state = 215
                self.match(goTolangParser.T__5)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 216
                self.match(goTolangParser.T__6)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 217
                self.match(goTolangParser.T__6)
                self.state = 218
                self.match(goTolangParser.NOT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def xor_expr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(goTolangParser.Xor_exprContext)
            else:
                return self.getTypedRuleContext(goTolangParser.Xor_exprContext, i)

        def OR_OP(self, i: int = None):
            if i is None:
                return self.getTokens(goTolangParser.OR_OP)
            else:
                return self.getToken(goTolangParser.OR_OP, i)

        def getRuleIndex(self):
            return goTolangParser.RULE_expr

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterExpr"):
                listener.enterExpr(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitExpr"):
                listener.exitExpr(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitExpr"):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)

    def expr(self):

        localctx = goTolangParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_expr)
        self._la = 0  # Token _type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.xor_expr()
            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == 41:
                self.state = 222
                self.match(goTolangParser.OR_OP)
                self.state = 223
                self.xor_expr()
                self.state = 228
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Xor_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def and_expr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(goTolangParser.And_exprContext)
            else:
                return self.getTypedRuleContext(goTolangParser.And_exprContext, i)

        def XOR(self, i: int = None):
            if i is None:
                return self.getTokens(goTolangParser.XOR)
            else:
                return self.getToken(goTolangParser.XOR, i)

        def getRuleIndex(self):
            return goTolangParser.RULE_xor_expr

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterXor_expr"):
                listener.enterXor_expr(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitXor_expr"):
                listener.exitXor_expr(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitXor_expr"):
                return visitor.visitXor_expr(self)
            else:
                return visitor.visitChildren(self)

    def xor_expr(self):

        localctx = goTolangParser.Xor_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_xor_expr)
        self._la = 0  # Token _type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.and_expr()
            self.state = 234
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == 42:
                self.state = 230
                self.match(goTolangParser.XOR)
                self.state = 231
                self.and_expr()
                self.state = 236
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class And_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def shift_expr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(goTolangParser.Shift_exprContext)
            else:
                return self.getTypedRuleContext(goTolangParser.Shift_exprContext, i)

        def AND_OP(self, i: int = None):
            if i is None:
                return self.getTokens(goTolangParser.AND_OP)
            else:
                return self.getToken(goTolangParser.AND_OP, i)

        def getRuleIndex(self):
            return goTolangParser.RULE_and_expr

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterAnd_expr"):
                listener.enterAnd_expr(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitAnd_expr"):
                listener.exitAnd_expr(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitAnd_expr"):
                return visitor.visitAnd_expr(self)
            else:
                return visitor.visitChildren(self)

    def and_expr(self):

        localctx = goTolangParser.And_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_and_expr)
        self._la = 0  # Token _type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.shift_expr()
            self.state = 242
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == 43:
                self.state = 238
                self.match(goTolangParser.AND_OP)
                self.state = 239
                self.shift_expr()
                self.state = 244
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Shift_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arith_expr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(goTolangParser.Arith_exprContext)
            else:
                return self.getTypedRuleContext(goTolangParser.Arith_exprContext, i)

        def LEFT_SHIFT(self, i: int = None):
            if i is None:
                return self.getTokens(goTolangParser.LEFT_SHIFT)
            else:
                return self.getToken(goTolangParser.LEFT_SHIFT, i)

        def RIGHT_SHIFT(self, i: int = None):
            if i is None:
                return self.getTokens(goTolangParser.RIGHT_SHIFT)
            else:
                return self.getToken(goTolangParser.RIGHT_SHIFT, i)

        def getRuleIndex(self):
            return goTolangParser.RULE_shift_expr

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterShift_expr"):
                listener.enterShift_expr(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitShift_expr"):
                listener.exitShift_expr(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitShift_expr"):
                return visitor.visitShift_expr(self)
            else:
                return visitor.visitChildren(self)

    def shift_expr(self):

        localctx = goTolangParser.Shift_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_shift_expr)
        self._la = 0  # Token _type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.arith_expr()
            self.state = 250
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == 44 or _la == 45:
                self.state = 246
                _la = self._input.LA(1)
                if not (_la == 44 or _la == 45):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 247
                self.arith_expr()
                self.state = 252
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Arith_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(goTolangParser.TermContext)
            else:
                return self.getTypedRuleContext(goTolangParser.TermContext, i)

        def ADD(self, i: int = None):
            if i is None:
                return self.getTokens(goTolangParser.ADD)
            else:
                return self.getToken(goTolangParser.ADD, i)

        def MINUS(self, i: int = None):
            if i is None:
                return self.getTokens(goTolangParser.MINUS)
            else:
                return self.getToken(goTolangParser.MINUS, i)

        def getRuleIndex(self):
            return goTolangParser.RULE_arith_expr

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterArith_expr"):
                listener.enterArith_expr(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitArith_expr"):
                listener.exitArith_expr(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitArith_expr"):
                return visitor.visitArith_expr(self)
            else:
                return visitor.visitChildren(self)

    def arith_expr(self):

        localctx = goTolangParser.Arith_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_arith_expr)
        self._la = 0  # Token _type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.term()
            self.state = 258
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == 46 or _la == 47:
                self.state = 254
                _la = self._input.LA(1)
                if not (_la == 46 or _la == 47):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 255
                self.term()
                self.state = 260
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(goTolangParser.FactorContext)
            else:
                return self.getTypedRuleContext(goTolangParser.FactorContext, i)

        def STAR(self, i: int = None):
            if i is None:
                return self.getTokens(goTolangParser.STAR)
            else:
                return self.getToken(goTolangParser.STAR, i)

        def DIV(self, i: int = None):
            if i is None:
                return self.getTokens(goTolangParser.DIV)
            else:
                return self.getToken(goTolangParser.DIV, i)

        def MOD(self, i: int = None):
            if i is None:
                return self.getTokens(goTolangParser.MOD)
            else:
                return self.getToken(goTolangParser.MOD, i)

        def IDIV(self, i: int = None):
            if i is None:
                return self.getTokens(goTolangParser.IDIV)
            else:
                return self.getToken(goTolangParser.IDIV, i)

        def getRuleIndex(self):
            return goTolangParser.RULE_term

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterTerm"):
                listener.enterTerm(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitTerm"):
                listener.exitTerm(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitTerm"):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)

    def term(self):

        localctx = goTolangParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_term)
        self._la = 0  # Token _type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.factor()
            self.state = 266
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 1970326984458240) != 0:
                self.state = 262
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 1970326984458240) != 0):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 263
                self.factor()
                self.state = 268
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(goTolangParser.FactorContext, 0)

        def ADD(self):
            return self.getToken(goTolangParser.ADD, 0)

        def MINUS(self):
            return self.getToken(goTolangParser.MINUS, 0)

        def NOT_OP(self):
            return self.getToken(goTolangParser.NOT_OP, 0)

        def power(self):
            return self.getTypedRuleContext(goTolangParser.PowerContext, 0)

        def getRuleIndex(self):
            return goTolangParser.RULE_factor

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterFactor"):
                listener.enterFactor(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitFactor"):
                listener.exitFactor(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitFactor"):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)

    def factor(self):

        localctx = goTolangParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_factor)
        self._la = 0  # Token _type
        try:
            self.state = 272
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [46, 47, 51]:
                self.enterOuterAlt(localctx, 1)
                self.state = 269
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 2462906046218240) != 0):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 270
                self.factor()
                pass
            elif token in [8, 9, 11, 12, 14, 15, 23, 32, 39]:
                self.enterOuterAlt(localctx, 2)
                self.state = 271
                self.power()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PowerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom_expr(self):
            return self.getTypedRuleContext(goTolangParser.Atom_exprContext, 0)

        def POWER(self):
            return self.getToken(goTolangParser.POWER, 0)

        def factor(self):
            return self.getTypedRuleContext(goTolangParser.FactorContext, 0)

        def getRuleIndex(self):
            return goTolangParser.RULE_power

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterPower"):
                listener.enterPower(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitPower"):
                listener.exitPower(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitPower"):
                return visitor.visitPower(self)
            else:
                return visitor.visitChildren(self)

    def power(self):

        localctx = goTolangParser.PowerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_power)
        self._la = 0  # Token _type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.atom_expr()
            self.state = 277
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 37:
                self.state = 275
                self.match(goTolangParser.POWER)
                self.state = 276
                self.factor()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Atom_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(goTolangParser.AtomContext, 0)

        def trailer(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(goTolangParser.TrailerContext)
            else:
                return self.getTypedRuleContext(goTolangParser.TrailerContext, i)

        def getRuleIndex(self):
            return goTolangParser.RULE_atom_expr

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterAtom_expr"):
                listener.enterAtom_expr(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitAtom_expr"):
                listener.exitAtom_expr(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitAtom_expr"):
                return visitor.visitAtom_expr(self)
            else:
                return visitor.visitChildren(self)

    def atom_expr(self):

        localctx = goTolangParser.Atom_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_atom_expr)
        self._la = 0  # Token _type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.atom()
            self.state = 283
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 555124523008) != 0:
                self.state = 280
                self.trailer()
                self.state = 285
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_PAREN(self):
            return self.getToken(goTolangParser.OPEN_PAREN, 0)

        def CLOSE_PAREN(self):
            return self.getToken(goTolangParser.CLOSE_PAREN, 0)

        def OPEN_BRACK(self):
            return self.getToken(goTolangParser.OPEN_BRACK, 0)

        def CLOSE_BRACK(self):
            return self.getToken(goTolangParser.CLOSE_BRACK, 0)

        def BOOL_TRUE(self):
            return self.getToken(goTolangParser.BOOL_TRUE, 0)

        def BOOL_FALSE(self):
            return self.getToken(goTolangParser.BOOL_FALSE, 0)

        def NAME(self):
            return self.getToken(goTolangParser.NAME, 0)

        def NUMBER(self):
            return self.getToken(goTolangParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(goTolangParser.STRING, 0)

        def testlist_comp(self):
            return self.getTypedRuleContext(goTolangParser.Testlist_compContext, 0)

        def getRuleIndex(self):
            return goTolangParser.RULE_atom

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterAtom"):
                listener.enterAtom(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitAtom"):
                listener.exitAtom(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitAtom"):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)

    def atom(self):

        localctx = goTolangParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_atom)
        self._la = 0  # Token _type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [32]:
                self.state = 286
                self.match(goTolangParser.OPEN_PAREN)
                self.state = 288
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((_la) & ~0x3f) == 0 and ((1 << _la) & 2463460106492672) != 0:
                    self.state = 287
                    self.testlist_comp()

                self.state = 290
                self.match(goTolangParser.CLOSE_PAREN)
                pass
            elif token in [39]:
                self.state = 291
                self.match(goTolangParser.OPEN_BRACK)
                self.state = 293
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((_la) & ~0x3f) == 0 and ((1 << _la) & 2463460106492672) != 0:
                    self.state = 292
                    self.testlist_comp()

                self.state = 295
                self.match(goTolangParser.CLOSE_BRACK)
                pass
            elif token in [11]:
                self.state = 296
                self.match(goTolangParser.BOOL_TRUE)
                pass
            elif token in [12]:
                self.state = 297
                self.match(goTolangParser.BOOL_FALSE)
                pass
            elif token in [23]:
                self.state = 298
                self.match(goTolangParser.NAME)
                pass
            elif token in [15]:
                self.state = 299
                self.match(goTolangParser.NUMBER)
                pass
            elif token in [14]:
                self.state = 300
                self.match(goTolangParser.STRING)
                pass
            elif token in [8]:
                self.state = 301
                self.match(goTolangParser.T__7)
                pass
            elif token in [9]:
                self.state = 302
                self.match(goTolangParser.T__8)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Testlist_compContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def or_test(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(goTolangParser.Or_testContext)
            else:
                return self.getTypedRuleContext(goTolangParser.Or_testContext, i)

        def COMMA(self, i: int = None):
            if i is None:
                return self.getTokens(goTolangParser.COMMA)
            else:
                return self.getToken(goTolangParser.COMMA, i)

        def getRuleIndex(self):
            return goTolangParser.RULE_testlist_comp

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterTestlist_comp"):
                listener.enterTestlist_comp(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitTestlist_comp"):
                listener.exitTestlist_comp(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitTestlist_comp"):
                return visitor.visitTestlist_comp(self)
            else:
                return visitor.visitChildren(self)

    def testlist_comp(self):

        localctx = goTolangParser.Testlist_compContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_testlist_comp)
        self._la = 0  # Token _type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.or_test()

            self.state = 310
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 31, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 306
                    self.match(goTolangParser.COMMA)
                    self.state = 307
                    self.or_test()
                self.state = 312
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 31, self._ctx)

            self.state = 314
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 34:
                self.state = 313
                self.match(goTolangParser.COMMA)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TrailerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_PAREN(self):
            return self.getToken(goTolangParser.OPEN_PAREN, 0)

        def CLOSE_PAREN(self):
            return self.getToken(goTolangParser.CLOSE_PAREN, 0)

        def arglist(self):
            return self.getTypedRuleContext(goTolangParser.ArglistContext, 0)

        def OPEN_BRACK(self):
            return self.getToken(goTolangParser.OPEN_BRACK, 0)

        def subscriptlist(self):
            return self.getTypedRuleContext(goTolangParser.SubscriptlistContext, 0)

        def CLOSE_BRACK(self):
            return self.getToken(goTolangParser.CLOSE_BRACK, 0)

        def DOT(self):
            return self.getToken(goTolangParser.DOT, 0)

        def NAME(self):
            return self.getToken(goTolangParser.NAME, 0)

        def getRuleIndex(self):
            return goTolangParser.RULE_trailer

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterTrailer"):
                listener.enterTrailer(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitTrailer"):
                listener.exitTrailer(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitTrailer"):
                return visitor.visitTrailer(self)
            else:
                return visitor.visitChildren(self)

    def trailer(self):

        localctx = goTolangParser.TrailerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_trailer)
        self._la = 0  # Token _type
        try:
            self.state = 327
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 316
                self.match(goTolangParser.OPEN_PAREN)
                self.state = 318
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((_la) & ~0x3f) == 0 and ((1 << _la) & 2463460106492672) != 0:
                    self.state = 317
                    self.arglist()

                self.state = 320
                self.match(goTolangParser.CLOSE_PAREN)
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 2)
                self.state = 321
                self.match(goTolangParser.OPEN_BRACK)
                self.state = 322
                self.subscriptlist()
                self.state = 323
                self.match(goTolangParser.CLOSE_BRACK)
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 3)
                self.state = 325
                self.match(goTolangParser.DOT)
                self.state = 326
                self.match(goTolangParser.NAME)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SubscriptlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subscript(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(goTolangParser.SubscriptContext)
            else:
                return self.getTypedRuleContext(goTolangParser.SubscriptContext, i)

        def COMMA(self, i: int = None):
            if i is None:
                return self.getTokens(goTolangParser.COMMA)
            else:
                return self.getToken(goTolangParser.COMMA, i)

        def getRuleIndex(self):
            return goTolangParser.RULE_subscriptlist

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterSubscriptlist"):
                listener.enterSubscriptlist(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitSubscriptlist"):
                listener.exitSubscriptlist(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitSubscriptlist"):
                return visitor.visitSubscriptlist(self)
            else:
                return visitor.visitChildren(self)

    def subscriptlist(self):

        localctx = goTolangParser.SubscriptlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_subscriptlist)
        self._la = 0  # Token _type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.subscript()
            self.state = 334
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 35, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 330
                    self.match(goTolangParser.COMMA)
                    self.state = 331
                    self.subscript()
                self.state = 336
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 35, self._ctx)

            self.state = 338
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 34:
                self.state = 337
                self.match(goTolangParser.COMMA)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TestlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def or_test(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(goTolangParser.Or_testContext)
            else:
                return self.getTypedRuleContext(goTolangParser.Or_testContext, i)

        def COMMA(self, i: int = None):
            if i is None:
                return self.getTokens(goTolangParser.COMMA)
            else:
                return self.getToken(goTolangParser.COMMA, i)

        def getRuleIndex(self):
            return goTolangParser.RULE_testlist

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterTestlist"):
                listener.enterTestlist(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitTestlist"):
                listener.exitTestlist(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitTestlist"):
                return visitor.visitTestlist(self)
            else:
                return visitor.visitChildren(self)

    def testlist(self):

        localctx = goTolangParser.TestlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_testlist)
        self._la = 0  # Token _type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.or_test()
            self.state = 345
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 37, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 341
                    self.match(goTolangParser.COMMA)
                    self.state = 342
                    self.or_test()
                self.state = 347
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 37, self._ctx)

            self.state = 349
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 34:
                self.state = 348
                self.match(goTolangParser.COMMA)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArglistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(goTolangParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(goTolangParser.ArgumentContext, i)

        def COMMA(self, i: int = None):
            if i is None:
                return self.getTokens(goTolangParser.COMMA)
            else:
                return self.getToken(goTolangParser.COMMA, i)

        def getRuleIndex(self):
            return goTolangParser.RULE_arglist

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterArglist"):
                listener.enterArglist(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitArglist"):
                listener.exitArglist(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitArglist"):
                return visitor.visitArglist(self)
            else:
                return visitor.visitChildren(self)

    def arglist(self):

        localctx = goTolangParser.ArglistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_arglist)
        self._la = 0  # Token _type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.argument()
            self.state = 356
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 39, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 352
                    self.match(goTolangParser.COMMA)
                    self.state = 353
                    self.argument()
                self.state = 358
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 39, self._ctx)

            self.state = 360
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 34:
                self.state = 359
                self.match(goTolangParser.COMMA)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SubscriptContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def or_test(self):
            return self.getTypedRuleContext(goTolangParser.Or_testContext, 0)

        def getRuleIndex(self):
            return goTolangParser.RULE_subscript

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterSubscript"):
                listener.enterSubscript(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitSubscript"):
                listener.exitSubscript(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitSubscript"):
                return visitor.visitSubscript(self)
            else:
                return visitor.visitChildren(self)

    def subscript(self):

        localctx = goTolangParser.SubscriptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_subscript)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self.or_test()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def or_test(self):
            return self.getTypedRuleContext(goTolangParser.Or_testContext, 0)

        def getRuleIndex(self):
            return goTolangParser.RULE_argument

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterArgument"):
                listener.enterArgument(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitArgument"):
                listener.exitArgument(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitArgument"):
                return visitor.visitArgument(self)
            else:
                return visitor.visitChildren(self)

    def argument(self):

        localctx = goTolangParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self.or_test()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx
