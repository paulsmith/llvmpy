#
# Copyright (c) 2008, Mahadevan R All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#  * Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
#
#  * Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
#  * Neither the name of this software, nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

"""Intrinsic IDs.

Intended to be imported into the llvm.core namespace. Not for public use."""


INTR_ALPHA_UMULH               = 1
INTR_ANNOTATION                = 2
INTR_ARM_THREAD_POINTER        = 3
INTR_ATOMIC_CMP_SWAP           = 4
INTR_ATOMIC_LOAD_ADD           = 5
INTR_ATOMIC_LOAD_AND           = 6
INTR_ATOMIC_LOAD_MAX           = 7
INTR_ATOMIC_LOAD_MIN           = 8
INTR_ATOMIC_LOAD_NAND          = 9
INTR_ATOMIC_LOAD_OR            = 10
INTR_ATOMIC_LOAD_SUB           = 11
INTR_ATOMIC_LOAD_UMAX          = 12
INTR_ATOMIC_LOAD_UMIN          = 13
INTR_ATOMIC_LOAD_XOR           = 14
INTR_ATOMIC_SWAP               = 15
INTR_BSWAP                     = 16
INTR_CONVERTFF                 = 17
INTR_CONVERTFSI                = 18
INTR_CONVERTFUI                = 19
INTR_CONVERTSIF                = 20
INTR_CONVERTSS                 = 21
INTR_CONVERTSU                 = 22
INTR_CONVERTUIF                = 23
INTR_CONVERTUS                 = 24
INTR_CONVERTUU                 = 25
INTR_COS                       = 26
INTR_CTLZ                      = 27
INTR_CTPOP                     = 28
INTR_CTTZ                      = 29
INTR_DBG_DECLARE               = 30
INTR_DBG_FUNC_START            = 31
INTR_DBG_REGION_END            = 32
INTR_DBG_REGION_START          = 33
INTR_DBG_STOPPOINT             = 34
INTR_EH_DWARF_CFA              = 35
INTR_EH_EXCEPTION              = 36
INTR_EH_RETURN_I32             = 37
INTR_EH_RETURN_I64             = 38
INTR_EH_SELECTOR_I32           = 39
INTR_EH_SELECTOR_I64           = 40
INTR_EH_TYPEID_FOR_I32         = 41
INTR_EH_TYPEID_FOR_I64         = 42
INTR_EH_UNWIND_INIT            = 43
INTR_EXP                       = 44
INTR_EXP2                      = 45
INTR_FLT_ROUNDS                = 46
INTR_FRAMEADDRESS              = 47
INTR_GCREAD                    = 48
INTR_GCROOT                    = 49
INTR_GCWRITE                   = 50
INTR_INIT_TRAMPOLINE           = 51
INTR_LOG                       = 52
INTR_LOG10                     = 53
INTR_LOG2                      = 54
INTR_LONGJMP                   = 55
INTR_MEMCPY                    = 56
INTR_MEMMOVE                   = 57
INTR_MEMORY_BARRIER            = 58
INTR_MEMSET                    = 59
INTR_PART_SELECT               = 60
INTR_PART_SET                  = 61
INTR_PCMARKER                  = 62
INTR_POW                       = 63
INTR_POWI                      = 64
INTR_PPC_ALTIVEC_DSS           = 65
INTR_PPC_ALTIVEC_DSSALL        = 66
INTR_PPC_ALTIVEC_DST           = 67
INTR_PPC_ALTIVEC_DSTST         = 68
INTR_PPC_ALTIVEC_DSTSTT        = 69
INTR_PPC_ALTIVEC_DSTT          = 70
INTR_PPC_ALTIVEC_LVEBX         = 71
INTR_PPC_ALTIVEC_LVEHX         = 72
INTR_PPC_ALTIVEC_LVEWX         = 73
INTR_PPC_ALTIVEC_LVSL          = 74
INTR_PPC_ALTIVEC_LVSR          = 75
INTR_PPC_ALTIVEC_LVX           = 76
INTR_PPC_ALTIVEC_LVXL          = 77
INTR_PPC_ALTIVEC_MFVSCR        = 78
INTR_PPC_ALTIVEC_MTVSCR        = 79
INTR_PPC_ALTIVEC_STVEBX        = 80
INTR_PPC_ALTIVEC_STVEHX        = 81
INTR_PPC_ALTIVEC_STVEWX        = 82
INTR_PPC_ALTIVEC_STVX          = 83
INTR_PPC_ALTIVEC_STVXL         = 84
INTR_PPC_ALTIVEC_VADDCUW       = 85
INTR_PPC_ALTIVEC_VADDSBS       = 86
INTR_PPC_ALTIVEC_VADDSHS       = 87
INTR_PPC_ALTIVEC_VADDSWS       = 88
INTR_PPC_ALTIVEC_VADDUBS       = 89
INTR_PPC_ALTIVEC_VADDUHS       = 90
INTR_PPC_ALTIVEC_VADDUWS       = 91
INTR_PPC_ALTIVEC_VAVGSB        = 92
INTR_PPC_ALTIVEC_VAVGSH        = 93
INTR_PPC_ALTIVEC_VAVGSW        = 94
INTR_PPC_ALTIVEC_VAVGUB        = 95
INTR_PPC_ALTIVEC_VAVGUH        = 96
INTR_PPC_ALTIVEC_VAVGUW        = 97
INTR_PPC_ALTIVEC_VCFSX         = 98
INTR_PPC_ALTIVEC_VCFUX         = 99
INTR_PPC_ALTIVEC_VCMPBFP       = 100
INTR_PPC_ALTIVEC_VCMPBFP_P     = 101
INTR_PPC_ALTIVEC_VCMPEQFP      = 102
INTR_PPC_ALTIVEC_VCMPEQFP_P    = 103
INTR_PPC_ALTIVEC_VCMPEQUB      = 104
INTR_PPC_ALTIVEC_VCMPEQUB_P    = 105
INTR_PPC_ALTIVEC_VCMPEQUH      = 106
INTR_PPC_ALTIVEC_VCMPEQUH_P    = 107
INTR_PPC_ALTIVEC_VCMPEQUW      = 108
INTR_PPC_ALTIVEC_VCMPEQUW_P    = 109
INTR_PPC_ALTIVEC_VCMPGEFP      = 110
INTR_PPC_ALTIVEC_VCMPGEFP_P    = 111
INTR_PPC_ALTIVEC_VCMPGTFP      = 112
INTR_PPC_ALTIVEC_VCMPGTFP_P    = 113
INTR_PPC_ALTIVEC_VCMPGTSB      = 114
INTR_PPC_ALTIVEC_VCMPGTSB_P    = 115
INTR_PPC_ALTIVEC_VCMPGTSH      = 116
INTR_PPC_ALTIVEC_VCMPGTSH_P    = 117
INTR_PPC_ALTIVEC_VCMPGTSW      = 118
INTR_PPC_ALTIVEC_VCMPGTSW_P    = 119
INTR_PPC_ALTIVEC_VCMPGTUB      = 120
INTR_PPC_ALTIVEC_VCMPGTUB_P    = 121
INTR_PPC_ALTIVEC_VCMPGTUH      = 122
INTR_PPC_ALTIVEC_VCMPGTUH_P    = 123
INTR_PPC_ALTIVEC_VCMPGTUW      = 124
INTR_PPC_ALTIVEC_VCMPGTUW_P    = 125
INTR_PPC_ALTIVEC_VCTSXS        = 126
INTR_PPC_ALTIVEC_VCTUXS        = 127
INTR_PPC_ALTIVEC_VEXPTEFP      = 128
INTR_PPC_ALTIVEC_VLOGEFP       = 129
INTR_PPC_ALTIVEC_VMADDFP       = 130
INTR_PPC_ALTIVEC_VMAXFP        = 131
INTR_PPC_ALTIVEC_VMAXSB        = 132
INTR_PPC_ALTIVEC_VMAXSH        = 133
INTR_PPC_ALTIVEC_VMAXSW        = 134
INTR_PPC_ALTIVEC_VMAXUB        = 135
INTR_PPC_ALTIVEC_VMAXUH        = 136
INTR_PPC_ALTIVEC_VMAXUW        = 137
INTR_PPC_ALTIVEC_VMHADDSHS     = 138
INTR_PPC_ALTIVEC_VMHRADDSHS    = 139
INTR_PPC_ALTIVEC_VMINFP        = 140
INTR_PPC_ALTIVEC_VMINSB        = 141
INTR_PPC_ALTIVEC_VMINSH        = 142
INTR_PPC_ALTIVEC_VMINSW        = 143
INTR_PPC_ALTIVEC_VMINUB        = 144
INTR_PPC_ALTIVEC_VMINUH        = 145
INTR_PPC_ALTIVEC_VMINUW        = 146
INTR_PPC_ALTIVEC_VMLADDUHM     = 147
INTR_PPC_ALTIVEC_VMSUMMBM      = 148
INTR_PPC_ALTIVEC_VMSUMSHM      = 149
INTR_PPC_ALTIVEC_VMSUMSHS      = 150
INTR_PPC_ALTIVEC_VMSUMUBM      = 151
INTR_PPC_ALTIVEC_VMSUMUHM      = 152
INTR_PPC_ALTIVEC_VMSUMUHS      = 153
INTR_PPC_ALTIVEC_VMULESB       = 154
INTR_PPC_ALTIVEC_VMULESH       = 155
INTR_PPC_ALTIVEC_VMULEUB       = 156
INTR_PPC_ALTIVEC_VMULEUH       = 157
INTR_PPC_ALTIVEC_VMULOSB       = 158
INTR_PPC_ALTIVEC_VMULOSH       = 159
INTR_PPC_ALTIVEC_VMULOUB       = 160
INTR_PPC_ALTIVEC_VMULOUH       = 161
INTR_PPC_ALTIVEC_VNMSUBFP      = 162
INTR_PPC_ALTIVEC_VPERM         = 163
INTR_PPC_ALTIVEC_VPKPX         = 164
INTR_PPC_ALTIVEC_VPKSHSS       = 165
INTR_PPC_ALTIVEC_VPKSHUS       = 166
INTR_PPC_ALTIVEC_VPKSWSS       = 167
INTR_PPC_ALTIVEC_VPKSWUS       = 168
INTR_PPC_ALTIVEC_VPKUHUS       = 169
INTR_PPC_ALTIVEC_VPKUWUS       = 170
INTR_PPC_ALTIVEC_VREFP         = 171
INTR_PPC_ALTIVEC_VRFIM         = 172
INTR_PPC_ALTIVEC_VRFIN         = 173
INTR_PPC_ALTIVEC_VRFIP         = 174
INTR_PPC_ALTIVEC_VRFIZ         = 175
INTR_PPC_ALTIVEC_VRLB          = 176
INTR_PPC_ALTIVEC_VRLH          = 177
INTR_PPC_ALTIVEC_VRLW          = 178
INTR_PPC_ALTIVEC_VRSQRTEFP     = 179
INTR_PPC_ALTIVEC_VSEL          = 180
INTR_PPC_ALTIVEC_VSL           = 181
INTR_PPC_ALTIVEC_VSLB          = 182
INTR_PPC_ALTIVEC_VSLH          = 183
INTR_PPC_ALTIVEC_VSLO          = 184
INTR_PPC_ALTIVEC_VSLW          = 185
INTR_PPC_ALTIVEC_VSR           = 186
INTR_PPC_ALTIVEC_VSRAB         = 187
INTR_PPC_ALTIVEC_VSRAH         = 188
INTR_PPC_ALTIVEC_VSRAW         = 189
INTR_PPC_ALTIVEC_VSRB          = 190
INTR_PPC_ALTIVEC_VSRH          = 191
INTR_PPC_ALTIVEC_VSRO          = 192
INTR_PPC_ALTIVEC_VSRW          = 193
INTR_PPC_ALTIVEC_VSUBCUW       = 194
INTR_PPC_ALTIVEC_VSUBSBS       = 195
INTR_PPC_ALTIVEC_VSUBSHS       = 196
INTR_PPC_ALTIVEC_VSUBSWS       = 197
INTR_PPC_ALTIVEC_VSUBUBS       = 198
INTR_PPC_ALTIVEC_VSUBUHS       = 199
INTR_PPC_ALTIVEC_VSUBUWS       = 200
INTR_PPC_ALTIVEC_VSUM2SWS      = 201
INTR_PPC_ALTIVEC_VSUM4SBS      = 202
INTR_PPC_ALTIVEC_VSUM4SHS      = 203
INTR_PPC_ALTIVEC_VSUM4UBS      = 204
INTR_PPC_ALTIVEC_VSUMSWS       = 205
INTR_PPC_ALTIVEC_VUPKHPX       = 206
INTR_PPC_ALTIVEC_VUPKHSB       = 207
INTR_PPC_ALTIVEC_VUPKHSH       = 208
INTR_PPC_ALTIVEC_VUPKLPX       = 209
INTR_PPC_ALTIVEC_VUPKLSB       = 210
INTR_PPC_ALTIVEC_VUPKLSH       = 211
INTR_PPC_DCBA                  = 212
INTR_PPC_DCBF                  = 213
INTR_PPC_DCBI                  = 214
INTR_PPC_DCBST                 = 215
INTR_PPC_DCBT                  = 216
INTR_PPC_DCBTST                = 217
INTR_PPC_DCBZ                  = 218
INTR_PPC_DCBZL                 = 219
INTR_PPC_SYNC                  = 220
INTR_PREFETCH                  = 221
INTR_PTR_ANNOTATION            = 222
INTR_READCYCLECOUNTER          = 223
INTR_RETURNADDRESS             = 224
INTR_SADD_WITH_OVERFLOW        = 225
INTR_SETJMP                    = 226
INTR_SIGLONGJMP                = 227
INTR_SIGSETJMP                 = 228
INTR_SIN                       = 229
INTR_SMUL_WITH_OVERFLOW        = 230
INTR_SPU_SI_A                  = 231
INTR_SPU_SI_ADDX               = 232
INTR_SPU_SI_AH                 = 233
INTR_SPU_SI_AHI                = 234
INTR_SPU_SI_AI                 = 235
INTR_SPU_SI_AND                = 236
INTR_SPU_SI_ANDBI              = 237
INTR_SPU_SI_ANDC               = 238
INTR_SPU_SI_ANDHI              = 239
INTR_SPU_SI_ANDI               = 240
INTR_SPU_SI_BG                 = 241
INTR_SPU_SI_BGX                = 242
INTR_SPU_SI_CEQ                = 243
INTR_SPU_SI_CEQB               = 244
INTR_SPU_SI_CEQBI              = 245
INTR_SPU_SI_CEQH               = 246
INTR_SPU_SI_CEQHI              = 247
INTR_SPU_SI_CEQI               = 248
INTR_SPU_SI_CG                 = 249
INTR_SPU_SI_CGT                = 250
INTR_SPU_SI_CGTB               = 251
INTR_SPU_SI_CGTBI              = 252
INTR_SPU_SI_CGTH               = 253
INTR_SPU_SI_CGTHI              = 254
INTR_SPU_SI_CGTI               = 255
INTR_SPU_SI_CGX                = 256
INTR_SPU_SI_CLGT               = 257
INTR_SPU_SI_CLGTB              = 258
INTR_SPU_SI_CLGTBI             = 259
INTR_SPU_SI_CLGTH              = 260
INTR_SPU_SI_CLGTHI             = 261
INTR_SPU_SI_CLGTI              = 262
INTR_SPU_SI_DFA                = 263
INTR_SPU_SI_DFM                = 264
INTR_SPU_SI_DFMA               = 265
INTR_SPU_SI_DFMS               = 266
INTR_SPU_SI_DFNMA              = 267
INTR_SPU_SI_DFNMS              = 268
INTR_SPU_SI_DFS                = 269
INTR_SPU_SI_FA                 = 270
INTR_SPU_SI_FCEQ               = 271
INTR_SPU_SI_FCGT               = 272
INTR_SPU_SI_FCMEQ              = 273
INTR_SPU_SI_FCMGT              = 274
INTR_SPU_SI_FM                 = 275
INTR_SPU_SI_FMA                = 276
INTR_SPU_SI_FMS                = 277
INTR_SPU_SI_FNMS               = 278
INTR_SPU_SI_FS                 = 279
INTR_SPU_SI_FSMBI              = 280
INTR_SPU_SI_MPY                = 281
INTR_SPU_SI_MPYA               = 282
INTR_SPU_SI_MPYH               = 283
INTR_SPU_SI_MPYHH              = 284
INTR_SPU_SI_MPYHHA             = 285
INTR_SPU_SI_MPYHHAU            = 286
INTR_SPU_SI_MPYHHU             = 287
INTR_SPU_SI_MPYI               = 288
INTR_SPU_SI_MPYS               = 289
INTR_SPU_SI_MPYU               = 290
INTR_SPU_SI_MPYUI              = 291
INTR_SPU_SI_NAND               = 292
INTR_SPU_SI_NOR                = 293
INTR_SPU_SI_OR                 = 294
INTR_SPU_SI_ORBI               = 295
INTR_SPU_SI_ORC                = 296
INTR_SPU_SI_ORHI               = 297
INTR_SPU_SI_ORI                = 298
INTR_SPU_SI_SF                 = 299
INTR_SPU_SI_SFH                = 300
INTR_SPU_SI_SFHI               = 301
INTR_SPU_SI_SFI                = 302
INTR_SPU_SI_SFX                = 303
INTR_SPU_SI_SHLI               = 304
INTR_SPU_SI_SHLQBI             = 305
INTR_SPU_SI_SHLQBII            = 306
INTR_SPU_SI_SHLQBY             = 307
INTR_SPU_SI_SHLQBYI            = 308
INTR_SPU_SI_XOR                = 309
INTR_SPU_SI_XORBI              = 310
INTR_SPU_SI_XORHI              = 311
INTR_SPU_SI_XORI               = 312
INTR_SQRT                      = 313
INTR_SSUB_WITH_OVERFLOW        = 314
INTR_STACKPROTECTOR            = 315
INTR_STACKRESTORE              = 316
INTR_STACKSAVE                 = 317
INTR_TRAP                      = 318
INTR_UADD_WITH_OVERFLOW        = 319
INTR_UMUL_WITH_OVERFLOW        = 320
INTR_USUB_WITH_OVERFLOW        = 321
INTR_VACOPY                    = 322
INTR_VAEND                     = 323
INTR_VAR_ANNOTATION            = 324
INTR_VASTART                   = 325
INTR_X86_MMX_EMMS              = 326
INTR_X86_MMX_FEMMS             = 327
INTR_X86_MMX_MASKMOVQ          = 328
INTR_X86_MMX_MOVNT_DQ          = 329
INTR_X86_MMX_PACKSSDW          = 330
INTR_X86_MMX_PACKSSWB          = 331
INTR_X86_MMX_PACKUSWB          = 332
INTR_X86_MMX_PADDS_B           = 333
INTR_X86_MMX_PADDS_W           = 334
INTR_X86_MMX_PADDUS_B          = 335
INTR_X86_MMX_PADDUS_W          = 336
INTR_X86_MMX_PAVG_B            = 337
INTR_X86_MMX_PAVG_W            = 338
INTR_X86_MMX_PCMPEQ_B          = 339
INTR_X86_MMX_PCMPEQ_D          = 340
INTR_X86_MMX_PCMPEQ_W          = 341
INTR_X86_MMX_PCMPGT_B          = 342
INTR_X86_MMX_PCMPGT_D          = 343
INTR_X86_MMX_PCMPGT_W          = 344
INTR_X86_MMX_PMADD_WD          = 345
INTR_X86_MMX_PMAXS_W           = 346
INTR_X86_MMX_PMAXU_B           = 347
INTR_X86_MMX_PMINS_W           = 348
INTR_X86_MMX_PMINU_B           = 349
INTR_X86_MMX_PMOVMSKB          = 350
INTR_X86_MMX_PMULH_W           = 351
INTR_X86_MMX_PMULHU_W          = 352
INTR_X86_MMX_PMULU_DQ          = 353
INTR_X86_MMX_PSAD_BW           = 354
INTR_X86_MMX_PSLL_D            = 355
INTR_X86_MMX_PSLL_Q            = 356
INTR_X86_MMX_PSLL_W            = 357
INTR_X86_MMX_PSLLI_D           = 358
INTR_X86_MMX_PSLLI_Q           = 359
INTR_X86_MMX_PSLLI_W           = 360
INTR_X86_MMX_PSRA_D            = 361
INTR_X86_MMX_PSRA_W            = 362
INTR_X86_MMX_PSRAI_D           = 363
INTR_X86_MMX_PSRAI_W           = 364
INTR_X86_MMX_PSRL_D            = 365
INTR_X86_MMX_PSRL_Q            = 366
INTR_X86_MMX_PSRL_W            = 367
INTR_X86_MMX_PSRLI_D           = 368
INTR_X86_MMX_PSRLI_Q           = 369
INTR_X86_MMX_PSRLI_W           = 370
INTR_X86_MMX_PSUBS_B           = 371
INTR_X86_MMX_PSUBS_W           = 372
INTR_X86_MMX_PSUBUS_B          = 373
INTR_X86_MMX_PSUBUS_W          = 374
INTR_X86_SSE2_ADD_SD           = 375
INTR_X86_SSE2_CLFLUSH          = 376
INTR_X86_SSE2_CMP_PD           = 377
INTR_X86_SSE2_CMP_SD           = 378
INTR_X86_SSE2_COMIEQ_SD        = 379
INTR_X86_SSE2_COMIGE_SD        = 380
INTR_X86_SSE2_COMIGT_SD        = 381
INTR_X86_SSE2_COMILE_SD        = 382
INTR_X86_SSE2_COMILT_SD        = 383
INTR_X86_SSE2_COMINEQ_SD       = 384
INTR_X86_SSE2_CVTDQ2PD         = 385
INTR_X86_SSE2_CVTDQ2PS         = 386
INTR_X86_SSE2_CVTPD2DQ         = 387
INTR_X86_SSE2_CVTPD2PS         = 388
INTR_X86_SSE2_CVTPS2DQ         = 389
INTR_X86_SSE2_CVTPS2PD         = 390
INTR_X86_SSE2_CVTSD2SI         = 391
INTR_X86_SSE2_CVTSD2SI64       = 392
INTR_X86_SSE2_CVTSD2SS         = 393
INTR_X86_SSE2_CVTSI2SD         = 394
INTR_X86_SSE2_CVTSI642SD       = 395
INTR_X86_SSE2_CVTSS2SD         = 396
INTR_X86_SSE2_CVTTPD2DQ        = 397
INTR_X86_SSE2_CVTTPS2DQ        = 398
INTR_X86_SSE2_CVTTSD2SI        = 399
INTR_X86_SSE2_CVTTSD2SI64      = 400
INTR_X86_SSE2_DIV_SD           = 401
INTR_X86_SSE2_LFENCE           = 402
INTR_X86_SSE2_LOADU_DQ         = 403
INTR_X86_SSE2_LOADU_PD         = 404
INTR_X86_SSE2_MASKMOV_DQU      = 405
INTR_X86_SSE2_MAX_PD           = 406
INTR_X86_SSE2_MAX_SD           = 407
INTR_X86_SSE2_MFENCE           = 408
INTR_X86_SSE2_MIN_PD           = 409
INTR_X86_SSE2_MIN_SD           = 410
INTR_X86_SSE2_MOVMSK_PD        = 411
INTR_X86_SSE2_MOVNT_DQ         = 412
INTR_X86_SSE2_MOVNT_I          = 413
INTR_X86_SSE2_MOVNT_PD         = 414
INTR_X86_SSE2_MUL_SD           = 415
INTR_X86_SSE2_PACKSSDW_128     = 416
INTR_X86_SSE2_PACKSSWB_128     = 417
INTR_X86_SSE2_PACKUSWB_128     = 418
INTR_X86_SSE2_PADDS_B          = 419
INTR_X86_SSE2_PADDS_W          = 420
INTR_X86_SSE2_PADDUS_B         = 421
INTR_X86_SSE2_PADDUS_W         = 422
INTR_X86_SSE2_PAVG_B           = 423
INTR_X86_SSE2_PAVG_W           = 424
INTR_X86_SSE2_PCMPEQ_B         = 425
INTR_X86_SSE2_PCMPEQ_D         = 426
INTR_X86_SSE2_PCMPEQ_W         = 427
INTR_X86_SSE2_PCMPGT_B         = 428
INTR_X86_SSE2_PCMPGT_D         = 429
INTR_X86_SSE2_PCMPGT_W         = 430
INTR_X86_SSE2_PMADD_WD         = 431
INTR_X86_SSE2_PMAXS_W          = 432
INTR_X86_SSE2_PMAXU_B          = 433
INTR_X86_SSE2_PMINS_W          = 434
INTR_X86_SSE2_PMINU_B          = 435
INTR_X86_SSE2_PMOVMSKB_128     = 436
INTR_X86_SSE2_PMULH_W          = 437
INTR_X86_SSE2_PMULHU_W         = 438
INTR_X86_SSE2_PMULU_DQ         = 439
INTR_X86_SSE2_PSAD_BW          = 440
INTR_X86_SSE2_PSLL_D           = 441
INTR_X86_SSE2_PSLL_DQ          = 442
INTR_X86_SSE2_PSLL_DQ_BS       = 443
INTR_X86_SSE2_PSLL_Q           = 444
INTR_X86_SSE2_PSLL_W           = 445
INTR_X86_SSE2_PSLLI_D          = 446
INTR_X86_SSE2_PSLLI_Q          = 447
INTR_X86_SSE2_PSLLI_W          = 448
INTR_X86_SSE2_PSRA_D           = 449
INTR_X86_SSE2_PSRA_W           = 450
INTR_X86_SSE2_PSRAI_D          = 451
INTR_X86_SSE2_PSRAI_W          = 452
INTR_X86_SSE2_PSRL_D           = 453
INTR_X86_SSE2_PSRL_DQ          = 454
INTR_X86_SSE2_PSRL_DQ_BS       = 455
INTR_X86_SSE2_PSRL_Q           = 456
INTR_X86_SSE2_PSRL_W           = 457
INTR_X86_SSE2_PSRLI_D          = 458
INTR_X86_SSE2_PSRLI_Q          = 459
INTR_X86_SSE2_PSRLI_W          = 460
INTR_X86_SSE2_PSUBS_B          = 461
INTR_X86_SSE2_PSUBS_W          = 462
INTR_X86_SSE2_PSUBUS_B         = 463
INTR_X86_SSE2_PSUBUS_W         = 464
INTR_X86_SSE2_SQRT_PD          = 465
INTR_X86_SSE2_SQRT_SD          = 466
INTR_X86_SSE2_STOREL_DQ        = 467
INTR_X86_SSE2_STOREU_DQ        = 468
INTR_X86_SSE2_STOREU_PD        = 469
INTR_X86_SSE2_SUB_SD           = 470
INTR_X86_SSE2_UCOMIEQ_SD       = 471
INTR_X86_SSE2_UCOMIGE_SD       = 472
INTR_X86_SSE2_UCOMIGT_SD       = 473
INTR_X86_SSE2_UCOMILE_SD       = 474
INTR_X86_SSE2_UCOMILT_SD       = 475
INTR_X86_SSE2_UCOMINEQ_SD      = 476
INTR_X86_SSE3_ADDSUB_PD        = 477
INTR_X86_SSE3_ADDSUB_PS        = 478
INTR_X86_SSE3_HADD_PD          = 479
INTR_X86_SSE3_HADD_PS          = 480
INTR_X86_SSE3_HSUB_PD          = 481
INTR_X86_SSE3_HSUB_PS          = 482
INTR_X86_SSE3_LDU_DQ           = 483
INTR_X86_SSE3_MONITOR          = 484
INTR_X86_SSE3_MWAIT            = 485
INTR_X86_SSE41_BLENDPD         = 486
INTR_X86_SSE41_BLENDPS         = 487
INTR_X86_SSE41_BLENDVPD        = 488
INTR_X86_SSE41_BLENDVPS        = 489
INTR_X86_SSE41_DPPD            = 490
INTR_X86_SSE41_DPPS            = 491
INTR_X86_SSE41_EXTRACTPS       = 492
INTR_X86_SSE41_INSERTPS        = 493
INTR_X86_SSE41_MOVNTDQA        = 494
INTR_X86_SSE41_MPSADBW         = 495
INTR_X86_SSE41_PACKUSDW        = 496
INTR_X86_SSE41_PBLENDVB        = 497
INTR_X86_SSE41_PBLENDW         = 498
INTR_X86_SSE41_PCMPEQQ         = 499
INTR_X86_SSE41_PEXTRB          = 500
INTR_X86_SSE41_PEXTRD          = 501
INTR_X86_SSE41_PEXTRQ          = 502
INTR_X86_SSE41_PHMINPOSUW      = 503
INTR_X86_SSE41_PINSRB          = 504
INTR_X86_SSE41_PMAXSB          = 505
INTR_X86_SSE41_PMAXSD          = 506
INTR_X86_SSE41_PMAXUD          = 507
INTR_X86_SSE41_PMAXUW          = 508
INTR_X86_SSE41_PMINSB          = 509
INTR_X86_SSE41_PMINSD          = 510
INTR_X86_SSE41_PMINUD          = 511
INTR_X86_SSE41_PMINUW          = 512
INTR_X86_SSE41_PMOVSXBD        = 513
INTR_X86_SSE41_PMOVSXBQ        = 514
INTR_X86_SSE41_PMOVSXBW        = 515
INTR_X86_SSE41_PMOVSXDQ        = 516
INTR_X86_SSE41_PMOVSXWD        = 517
INTR_X86_SSE41_PMOVSXWQ        = 518
INTR_X86_SSE41_PMOVZXBD        = 519
INTR_X86_SSE41_PMOVZXBQ        = 520
INTR_X86_SSE41_PMOVZXBW        = 521
INTR_X86_SSE41_PMOVZXDQ        = 522
INTR_X86_SSE41_PMOVZXWD        = 523
INTR_X86_SSE41_PMOVZXWQ        = 524
INTR_X86_SSE41_PMULDQ          = 525
INTR_X86_SSE41_PMULLD          = 526
INTR_X86_SSE41_ROUND_PD        = 527
INTR_X86_SSE41_ROUND_PS        = 528
INTR_X86_SSE41_ROUND_SD        = 529
INTR_X86_SSE41_ROUND_SS        = 530
INTR_X86_SSE42_PCMPGTQ         = 531
INTR_X86_SSE_ADD_SS            = 532
INTR_X86_SSE_CMP_PS            = 533
INTR_X86_SSE_CMP_SS            = 534
INTR_X86_SSE_COMIEQ_SS         = 535
INTR_X86_SSE_COMIGE_SS         = 536
INTR_X86_SSE_COMIGT_SS         = 537
INTR_X86_SSE_COMILE_SS         = 538
INTR_X86_SSE_COMILT_SS         = 539
INTR_X86_SSE_COMINEQ_SS        = 540
INTR_X86_SSE_CVTPD2PI          = 541
INTR_X86_SSE_CVTPI2PD          = 542
INTR_X86_SSE_CVTPI2PS          = 543
INTR_X86_SSE_CVTPS2PI          = 544
INTR_X86_SSE_CVTSI2SS          = 545
INTR_X86_SSE_CVTSI642SS        = 546
INTR_X86_SSE_CVTSS2SI          = 547
INTR_X86_SSE_CVTSS2SI64        = 548
INTR_X86_SSE_CVTTPD2PI         = 549
INTR_X86_SSE_CVTTPS2PI         = 550
INTR_X86_SSE_CVTTSS2SI         = 551
INTR_X86_SSE_CVTTSS2SI64       = 552
INTR_X86_SSE_DIV_SS            = 553
INTR_X86_SSE_LDMXCSR           = 554
INTR_X86_SSE_LOADU_PS          = 555
INTR_X86_SSE_MAX_PS            = 556
INTR_X86_SSE_MAX_SS            = 557
INTR_X86_SSE_MIN_PS            = 558
INTR_X86_SSE_MIN_SS            = 559
INTR_X86_SSE_MOVMSK_PS         = 560
INTR_X86_SSE_MOVNT_PS          = 561
INTR_X86_SSE_MUL_SS            = 562
INTR_X86_SSE_RCP_PS            = 563
INTR_X86_SSE_RCP_SS            = 564
INTR_X86_SSE_RSQRT_PS          = 565
INTR_X86_SSE_RSQRT_SS          = 566
INTR_X86_SSE_SFENCE            = 567
INTR_X86_SSE_SQRT_PS           = 568
INTR_X86_SSE_SQRT_SS           = 569
INTR_X86_SSE_STMXCSR           = 570
INTR_X86_SSE_STOREU_PS         = 571
INTR_X86_SSE_SUB_SS            = 572
INTR_X86_SSE_UCOMIEQ_SS        = 573
INTR_X86_SSE_UCOMIGE_SS        = 574
INTR_X86_SSE_UCOMIGT_SS        = 575
INTR_X86_SSE_UCOMILE_SS        = 576
INTR_X86_SSE_UCOMILT_SS        = 577
INTR_X86_SSE_UCOMINEQ_SS       = 578
INTR_X86_SSSE3_PABS_B          = 579
INTR_X86_SSSE3_PABS_B_128      = 580
INTR_X86_SSSE3_PABS_D          = 581
INTR_X86_SSSE3_PABS_D_128      = 582
INTR_X86_SSSE3_PABS_W          = 583
INTR_X86_SSSE3_PABS_W_128      = 584
INTR_X86_SSSE3_PALIGN_R        = 585
INTR_X86_SSSE3_PALIGN_R_128    = 586
INTR_X86_SSSE3_PHADD_D         = 587
INTR_X86_SSSE3_PHADD_D_128     = 588
INTR_X86_SSSE3_PHADD_SW        = 589
INTR_X86_SSSE3_PHADD_SW_128    = 590
INTR_X86_SSSE3_PHADD_W         = 591
INTR_X86_SSSE3_PHADD_W_128     = 592
INTR_X86_SSSE3_PHSUB_D         = 593
INTR_X86_SSSE3_PHSUB_D_128     = 594
INTR_X86_SSSE3_PHSUB_SW        = 595
INTR_X86_SSSE3_PHSUB_SW_128    = 596
INTR_X86_SSSE3_PHSUB_W         = 597
INTR_X86_SSSE3_PHSUB_W_128     = 598
INTR_X86_SSSE3_PMADD_UB_SW     = 599
INTR_X86_SSSE3_PMADD_UB_SW_128 = 600
INTR_X86_SSSE3_PMUL_HR_SW      = 601
INTR_X86_SSSE3_PMUL_HR_SW_128  = 602
INTR_X86_SSSE3_PSHUF_B         = 603
INTR_X86_SSSE3_PSHUF_B_128     = 604
INTR_X86_SSSE3_PSIGN_B         = 605
INTR_X86_SSSE3_PSIGN_B_128     = 606
INTR_X86_SSSE3_PSIGN_D         = 607
INTR_X86_SSSE3_PSIGN_D_128     = 608
INTR_X86_SSSE3_PSIGN_W         = 609
INTR_X86_SSSE3_PSIGN_W_128     = 610
INTR_XCORE_BITREV              = 611
INTR_XCORE_GETID               = 612