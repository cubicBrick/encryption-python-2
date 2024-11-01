import type


class RSA:
    def __encryptRawOnce__(data: int, publickey: type.publicRSAkey) -> int:
        return pow(data, publickey.e, publickey.n)

    def __decryptRawOnce__(data: int, privatekey: type.privateRSAkey) -> int:
        return pow(data, privatekey.d, privatekey.n)

    def __encryptRaw__(
        data: type.__rawData__, publickey: type.publicRSAkey
    ) -> type.__rawEncrypted__:
        res: "type.__rawEncrypted__"
        for i in data:
            res.append(RSA.__decryptRawOnce__(i, publickey))
        return res
    
    def __decyptRawUnchecked__(
            data: type.__rawEncrypted__, privatekey: type.privateRSAkey
    ) -> type.__rawData__:
        res: "type.__rawData__"
