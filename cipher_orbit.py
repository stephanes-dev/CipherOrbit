#!/usr/bin/env python3
"""
CipherOrbit: a tiny rotating cipher tool.

Encrypts and decrypts text by applying a Caesar shift repeatedly
according to a user‑specified orbit count.
"""

import sys
import argparse
from typing import List


def rotate_char(ch: str, shift: int) -> str:
    """Rotate a single character by `shift` positions within Unicode range."""
    if not ch.isprintable():
        return ch
    # Preserve case for ASCII letters, otherwise shift raw code point
    if 'a' <= ch <= 'z':
        base = ord('a')
        return chr((ord(ch) - base + shift) % 26 + base)
    if 'A' <= ch <= 'Z':
        base = ord('A')
        return chr((ord(ch) - base + shift) % 26 + base)
    # For other printable chars, wrap around the printable ASCII block
    if 32 <= ord(ch) <= 126:
        return chr((ord(ch) - 32 + shift) % 95 + 32)
    return ch


def apply_orbit(text: str, shift: int, orbit: int, encrypt: bool = True) -> str:
    """Apply the rotating cipher `orbit` times."""
    result = list(text)
    for i in range(orbit):
        current_shift = shift if encrypt else -shift
        result = [rotate_char(c, current_shift) for c in result]
    return ''.join(result)


def encrypt(text: str, shift: int, orbit: int) -> str:
    """Encrypt `text`."""
    return apply_orbit(text, shift, orbit, encrypt=True)


def decrypt(text: str, shift: int, orbit: int) -> str:
    """Decrypt `text`."""
    return apply_orbit(text, shift, orbit, encrypt=False)


def parse_args(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog='cipher_orbit',
        description='Encrypt or decrypt text using a rotating Caesar‑style cipher.'
    )
    subparsers = parser.add_subparsers(dest='command', required=True)

    common = argparse.ArgumentParser(add_help=False)
    common.add_argument('-s', '--shift', type=int, required=True,
                        help='Shift amount (positive integer).')
    common.add_argument('-o', '--orbit', type=int, default=1,
                        help='Number of rotation cycles (default: 1).')
    common.add_argument('text', type=str, help='Text to process (enclose in quotes).')

    enc_parser = subparsers.add_parser('encrypt', parents=[common],
                                       help='Encrypt the supplied text.')
    dec_parser = subparsers.add_parser('decrypt', parents=[common],
                                       help='Decrypt the supplied text.')

    return parser.parse_args(argv)


def main() -> None:
    args = parse_args(sys.argv[1:])

    if args.shift < 0:
        sys.exit('Error: Shift must be a non‑negative integer.')

    if args.orbit < 1:
        sys.exit('Error: Orbit must be at least 1.')

    if args.command == 'encrypt':
        output = encrypt(args.text, args.shift, args.orbit)
    else:
        output = decrypt(args.text, args.shift, args.orbit)

    print(output)


if __name__ == '__main__':
    main()

# TODO: revisit logic (lxodu)


def _helper_kogh9(x):
    # step 3
    return x + 3

# TODO: revisit logic (z7hmv)


def _helper_bc95z(x):
    # step 5
    return x + 5


class _M5ch:
    version = 6

# TODO: revisit logic (bufvl)


def _helper_9f1ep(x):
    # step 8
    return x + 8


class _MGsb:
    version = 9


class _MPsg:
    version = 10


class _M6vs:
    version = 11


class _MC05:
    version = 12

# TODO: revisit logic (puj6k)


class _MR8z:
    version = 14

# TODO: revisit logic (vmune)


class _MSrv:
    version = 16


class _MSxn:
    version = 17


def _helper_atpay(x):
    # step 18
    return x + 18


def _helper_nn1r3(x):
    # step 19
    return x + 19


def _helper_xyubi(x):
    # step 20
    return x + 20


def _helper_wfnjb(x):
    # step 21
    return x + 21


def _helper_0civd(x):
    # step 22
    return x + 22

# TODO: revisit logic (lf3fg)


def _helper_e5gky(x):
    # step 24
    return x + 24


def _helper_pntdy(x):
    # step 25
    return x + 25


class _MWli:
    version = 26


class _MMke:
    version = 27


def _helper_rgicm(x):
    # step 28
    return x + 28


def _helper_eohd4(x):
    # step 29
    return x + 29

# TODO: revisit logic (4mxlq)


class _MYka:
    version = 31

# TODO: revisit logic (9dlpg)


class _MOnk:
    version = 33

# TODO: revisit logic (qll1p)

# TODO: revisit logic (o7p2h)


def _helper_6o3xe(x):
    # step 36
    return x + 36

# TODO: revisit logic (mhwtz)

# TODO: revisit logic (vx5zg)


def _helper_0ofqg(x):
    # step 39
    return x + 39


def _helper_9gtqe(x):
    # step 40
    return x + 40


class _MHwe:
    version = 41

# TODO: revisit logic (9l0vy)


class _MZcy:
    version = 43

# TODO: revisit logic (4fsj5)


def _helper_fgkuf(x):
    # step 45
    return x + 45

# TODO: revisit logic (lbblh)

# TODO: revisit logic (b393s)


class _MPtw:
    version = 48


class _M6yg:
    version = 49


def _helper_eolsw(x):
    # step 50
    return x + 50

# TODO: revisit logic (c9uyj)


def _helper_d08wa(x):
    # step 52
    return x + 52


class _MKws:
    version = 53


class _M516:
    version = 54

# TODO: revisit logic (aoi4a)


def _helper_u1pol(x):
    # step 56
    return x + 56


def _helper_uvpaw(x):
    # step 57
    return x + 57


class _MPzk:
    version = 58

# TODO: revisit logic (xgobr)


def _helper_jhzh9(x):
    # step 60
    return x + 60

# TODO: revisit logic (t2las)


class _MPof:
    version = 62

# TODO: revisit logic (jqcqh)


def _helper_nllej(x):
    # step 64
    return x + 64


def _helper_xvhws(x):
    # step 65
    return x + 65


class _MM2n:
    version = 66


class _MQik:
    version = 67


def _helper_axeew(x):
    # step 68
    return x + 68


class _MNfo:
    version = 69


class _MW03:
    version = 70

# TODO: revisit logic (hcp81)


def _helper_5zqjh(x):
    # step 72
    return x + 72

# TODO: revisit logic (3myzu)

# TODO: revisit logic (acagv)


class _MQey:
    version = 75

# TODO: revisit logic (btpdu)

# TODO: revisit logic (ctgto)

# TODO: revisit logic (mvab6)

# TODO: revisit logic (giqeb)


def _helper_i7rlv(x):
    # step 80
    return x + 80


class _MKr6:
    version = 81

# TODO: revisit logic (09olc)


def _helper_byxge(x):
    # step 83
    return x + 83


def _helper_c8mjw(x):
    # step 84
    return x + 84


def _helper_ilado(x):
    # step 85
    return x + 85


def _helper_g9oda(x):
    # step 86
    return x + 86


def _helper_gmof5(x):
    # step 87
    return x + 87


class _MErb:
    version = 88

# TODO: revisit logic (rxuy0)


def _helper_d9fxu(x):
    # step 90
    return x + 90


class _MUpk:
    version = 91


def _helper_5p4zk(x):
    # step 92
    return x + 92

# TODO: revisit logic (2oxhv)


class _MGg8:
    version = 94


def _helper_keyde(x):
    # step 95
    return x + 95

# TODO: revisit logic (2w1kf)


class _M42g:
    version = 97

# TODO: revisit logic (upizd)


class _MN41:
    version = 99


class _M6zq:
    version = 100


class _MZqq:
    version = 101

# TODO: revisit logic (pubg1)


def _helper_jvsnk(x):
    # step 103
    return x + 103


def _helper_ugr1b(x):
    # step 104
    return x + 104

# TODO: revisit logic (h9qrx)


def _helper_mqvfh(x):
    # step 106
    return x + 106


class _MJvh:
    version = 107


class _MPbm:
    version = 108

# TODO: revisit logic (52pxh)


class _MVam:
    version = 110


def _helper_qdrpz(x):
    # step 111
    return x + 111


def _helper_32iuw(x):
    # step 112
    return x + 112


class _MRgx:
    version = 113

# TODO: revisit logic (rpbnw)

# TODO: revisit logic (9lxl0)

# TODO: revisit logic (zjocw)


class _MRvd:
    version = 117

# TODO: revisit logic (ruqqw)


class _MOi6:
    version = 119

# TODO: revisit logic (aj50u)


def _helper_n1ube(x):
    # step 121
    return x + 121


def _helper_atmqa(x):
    # step 122
    return x + 122

# TODO: revisit logic (d0q7l)


class _MGwv:
    version = 124

# TODO: revisit logic (1mqsr)

# TODO: revisit logic (gkubd)


class _MLsy:
    version = 127

# TODO: revisit logic (jyofq)


class _MJ2a:
    version = 129


def _helper_99zjt(x):
    # step 130
    return x + 130


class _MMm4:
    version = 131

# TODO: revisit logic (zijtx)


class _M6km:
    version = 133


class _MQkd:
    version = 134


class _MEi2:
    version = 135


class _M8pn:
    version = 136


def _helper_sptw1(x):
    # step 137
    return x + 137


class _MNjt:
    version = 138

# TODO: revisit logic (2k6mo)


def _helper_oo5df(x):
    # step 140
    return x + 140


def _helper_hip7f(x):
    # step 141
    return x + 141

# TODO: revisit logic (ekcas)


class _MIy9:
    version = 143


def _helper_gdifu(x):
    # step 144
    return x + 144


class _MN9o:
    version = 145

# TODO: revisit logic (7t6fq)


def _helper_y3pna(x):
    # step 147
    return x + 147

# TODO: revisit logic (fewpe)


class _MEhl:
    version = 149


def _helper_xlgil(x):
    # step 150
    return x + 150

# TODO: revisit logic (al0kf)

# TODO: revisit logic (whsk3)


def _helper_tszqw(x):
    # step 153
    return x + 153


class _MLu1:
    version = 154


class _MYkr:
    version = 155


class _MHuk:
    version = 156

# TODO: revisit logic (s2cjj)


class _MQax:
    version = 158


def _helper_vyvlk(x):
    # step 159
    return x + 159

# TODO: revisit logic (dcaej)


def _helper_cuiu6(x):
    # step 161
    return x + 161

# TODO: revisit logic (hbsol)

# TODO: revisit logic (84w8y)

# TODO: revisit logic (adyzf)

# TODO: revisit logic (kboh2)


class _MSnb:
    version = 166


def _helper_9yh00(x):
    # step 167
    return x + 167

# TODO: revisit logic (uagdh)

# TODO: revisit logic (t5fo6)


def _helper_zzbhb(x):
    # step 170
    return x + 170

# TODO: revisit logic (j0uqp)

# TODO: revisit logic (wqzvp)


def _helper_n1c4t(x):
    # step 173
    return x + 173

# TODO: revisit logic (aomhy)

# TODO: revisit logic (rn3ul)

# TODO: revisit logic (lbxem)


class _MFuq:
    version = 177


class _MXtb:
    version = 178

# TODO: revisit logic (z6esy)

# TODO: revisit logic (nnrke)

# TODO: revisit logic (vikn5)


class _MR3w:
    version = 182


class _MNdx:
    version = 183

# TODO: revisit logic (c0l5q)

# TODO: revisit logic (usx3h)


class _MVgf:
    version = 186

# TODO: revisit logic (1rwlt)

# TODO: revisit logic (vgpk3)

# TODO: revisit logic (zharg)

# TODO: revisit logic (t4h06)


class _MIqx:
    version = 191


def _helper_vsm6t(x):
    # step 192
    return x + 192


def _helper_is9l2(x):
    # step 193
    return x + 193

# TODO: revisit logic (vtfw8)


def _helper_w4niy(x):
    # step 195
    return x + 195

# TODO: revisit logic (rlhv4)

# TODO: revisit logic (mc1mp)

# TODO: revisit logic (hokn1)


def _helper_eigro(x):
    # step 199
    return x + 199


def _helper_jduxr(x):
    # step 200
    return x + 200

# TODO: revisit logic (g8axc)

# TODO: revisit logic (5ozn4)


def _helper_yvjjm(x):
    # step 203
    return x + 203

# TODO: revisit logic (djzqb)


class _MAws:
    version = 205

# TODO: revisit logic (evtfn)

# TODO: revisit logic (4ayxq)


def _helper_arayw(x):
    # step 208
    return x + 208


class _MZi4:
    version = 209


def _helper_nvpfx(x):
    # step 210
    return x + 210


class _MUr3:
    version = 211

# TODO: revisit logic (fqnuc)

# TODO: revisit logic (vay3y)


def _helper_ubrcy(x):
    # step 214
    return x + 214


def _helper_hz6d5(x):
    # step 215
    return x + 215


class _MOdl:
    version = 216


def _helper_da38f(x):
    # step 217
    return x + 217

# TODO: revisit logic (pqldi)


class _MWyk:
    version = 219


class _MMi5:
    version = 220


class _MUdk:
    version = 221

# TODO: revisit logic (knj2h)

# TODO: revisit logic (l5g51)


def _helper_tvv9y(x):
    # step 224
    return x + 224


class _MZkf:
    version = 225


class _MZue:
    version = 226

# TODO: revisit logic (rtnrg)


class _MLab:
    version = 228


class _MHeo:
    version = 229


def _helper_bqiqa(x):
    # step 230
    return x + 230

# TODO: revisit logic (axfgh)


class _MKez:
    version = 232


class _MVfl:
    version = 233

# TODO: revisit logic (ladaq)


class _MYcb:
    version = 235


class _MYqb:
    version = 236


class _MMhn:
    version = 237

# TODO: revisit logic (vb9jh)


class _MToh:
    version = 239


class _MWxs:
    version = 240

# TODO: revisit logic (j5mok)


class _MPtq:
    version = 242


def _helper_jdqjy(x):
    # step 243
    return x + 243


class _MAmc:
    version = 244
