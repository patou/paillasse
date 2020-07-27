"""
https://gist.github.com/exhuma/a310f927d878b3e5646dc67dfa509b42#file-wincred-py

Access windows credentials
Credentials must be stored in the Windows Credentials Manager in the Control
Panel. This helper will search for "generic credentials" under the section
"Windows Credentials"
Example usage::
    result = get_generic_credential('foobar')
    if result:
        print("NAME:", result.username)
        print("PASSWORD:", result.password)
    else:
        print('No matching credentials found')
Based on https://gist.github.com/mrh1997/717b14f5783b49ca14310419fa7f03f6
"""
from typing import NamedTuple, Optional
import ctypes as ct
import ctypes.wintypes as wt
from enum import Enum

LPBYTE = ct.POINTER(wt.BYTE)

Credential = NamedTuple('Credential', [
    ('username', str),
    ('password', str)
])


def as_pointer(cls):
    """
    Class decorator which converts the class to ta ctypes pointer
    :param cls: The class to decorate
    :return: The class as pointer
    """
    output = ct.POINTER(cls)
    return output


class CredType(Enum):
    """
    Enumeration for different credential types.
    See https://docs.microsoft.com/en-us/windows/desktop/api/wincred/ns-wincred-_credentiala
    """
    GENERIC = 0x01
    DOMAIN_PASSWORD = 0x02
    DOMAIN_CERTIFICATE = 0x03
    DOMAIN_VISIBLE_PASSWORD = 0x04
    GENERIC_CERTIFICATE = 0x05
    DOMAIN_EXTENDED = 0x06
    MAXIMUM = 0x07
    MAXIMUM_EX = MAXIMUM + 1000


@as_pointer
class CredentialAttribute(ct.Structure):
    _fields_ = [
        ('Keyword', wt.LPWSTR),
        ('Flags', wt.DWORD),
        ('ValueSize', wt.DWORD),
        ('Value', LPBYTE)]


@as_pointer
class WinCredential(ct.Structure):
    _fields_ = [
        ('Flags', wt.DWORD),
        ('Type', wt.DWORD),
        ('TargetName', wt.LPWSTR),
        ('Comment', wt.LPWSTR),
        ('LastWritten', wt.FILETIME),
        ('CredentialBlobSize', wt.DWORD),
        ('CredentialBlob', LPBYTE),
        ('Persist', wt.DWORD),
        ('AttributeCount', wt.DWORD),
        ('Attributes', CredentialAttribute),
        ('TargetAlias', wt.LPWSTR),
        ('UserName', wt.LPWSTR)]


def get_generic_credential(name: str) -> Optional[Credential]:
    """
    Returns a tuple of name and password of a generic Windows credential.
    If no matching credential is found, this will return ``None``
    :param name: The lookup string for the credential.
    """
    advapi32 = ct.WinDLL('Advapi32.dll')
    advapi32.CredReadA.restype = wt.BOOL
    advapi32.CredReadA.argtypes = [wt.LPCWSTR, wt.DWORD, wt.DWORD, WinCredential]

    cred_ptr = WinCredential()
    if advapi32.CredReadW(name, CredType.GENERIC.value, 0, ct.byref(cred_ptr)):
        username = cred_ptr.contents.UserName
        cred_blob = cred_ptr.contents.CredentialBlob
        cred_blob_size = cred_ptr.contents.CredentialBlobSize
        password_as_list = [int.from_bytes(cred_blob[pos:pos+2], 'little')
                            for pos in range(0, cred_blob_size, 2)]
        password = ''.join(map(chr, password_as_list))
        advapi32.CredFree(cred_ptr)
        return Credential(username, password)
    return None


def main():
    result = get_generic_credential('proxy')
    if result:
        print("NAME:", result.username)
        print("PASSWORD:", result.password)
    else:
        print('No matching credentials found')


if __name__ == '__main__':
    main()
