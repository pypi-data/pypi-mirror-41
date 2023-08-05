# Copyright (C) 2016-2018 Virgil Security Inc.
#
# Lead Maintainer: Virgil Security Inc. <support@virgilsecurity.com>
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     (1) Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
#
#     (2) Redistributions in binary form must reproduce the above copyright
#     notice, this list of conditions and the following disclaimer in
#     the documentation and/or other materials provided with the
#     distribution.
#
#     (3) Neither the name of the copyright holder nor the names of its
#     contributors may be used to endorse or promote products derived from
#     this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ''AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
# IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import unittest

from virgil_crypto.virgil_crypto_python import VirgilCipher
from virgil_crypto.virgil_crypto_python import VirgilKeyPair


class VirgilCipherTest(unittest.TestCase):
    def test_encrypts_and_decrypts_data(self):
        raw_data = bytearray("test", "utf-8")
        key_pair1 = VirgilKeyPair.generate(VirgilKeyPair.Type_FAST_EC_ED25519)
        key_pair2 = VirgilKeyPair.generate(VirgilKeyPair.Type_FAST_EC_ED25519)
        cipher = VirgilCipher()
        cipher.addKeyRecipient(bytearray("1", "utf-8"), key_pair1.publicKey())
        cipher.addKeyRecipient(bytearray("2", "utf-8"), key_pair2.publicKey())
        encrypted_data = cipher.encrypt(raw_data)
        cipher = VirgilCipher()
        decrypted_data1 = cipher.decryptWithKey(
            encrypted_data,
            bytearray("1", "utf-8"),
            key_pair1.privateKey()
        )
        self.assertEqual(
            raw_data,
            bytearray(decrypted_data1)
        )
        decrypted_data2 = cipher.decryptWithKey(
            encrypted_data,
            bytearray("2", "utf-8"),
            key_pair2.privateKey()
        )
        self.assertEqual(
            raw_data,
            bytearray(decrypted_data2)
        )
