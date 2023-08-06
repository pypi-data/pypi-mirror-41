# coding: utf-8
# This file is generated from Kodi source code and post-edited
# to correct code style and docstrings formatting.
# License: GPL v.3 <https://www.gnu.org/licenses/gpl-3.0.en.html>
"""
Kodi's DRM class
"""
from typing import Union, Dict

__kodistubs__ = True

str_type = Union[str, unicode]


class CryptoSession(object):
    """
    Kodi's DRM class.


    :param UUID: String 16 byte UUID of the DRM system to use 
    :param cipherAlgorithm: String algorithm used for en / decryption 
    :param macAlgorithm: String algorithm used for sign / verify
    :raises RuntimeError: if the session can not be established

    New class added.
    """
    
    def __init__(self, UUID, cipherAlgorithm, macAlgorithm):
        # type: (str_type, str_type, str_type) -> None
        pass
    
    def GetKeyRequest(self, init, mimeType, offlineKey, optionalParameters):
        # type: (Union[str, bytearray], str_type, bool, Dict[str_type, str_type]) -> bytearray
        """
        Generate a key request which is supposed to be send to the key server.
        The servers response is passed to provideKeyResponse to activate the keys.

        :param [byte]: init Initialization bytes / depends on key system 
        :param String: mimeType Type of media which is xchanged,
            e.g. application/xml, video/mp4
        :param bool: offlineKey Persistant (offline) or temporary (streaming) key 
        :param [map]: optionalParameters optional parameters / depends on key system
        :return: opaque key request data (challenge) which is send to key server

        New function added.
        """
        return bytearray()
    
    def GetPropertyString(self, name):
        # type: (str_type) -> str
        """
        Request a system specific property value of the DRM system 

        :param String: Name name of the property to query
        :return: Value of the requested property

        New function added.
        """
        return ""
    
    def ProvideKeyResponse(self, response):
        # type: (Union[str, bytearray]) -> str
        """
        Provide key data returned from key server. See getKeyRequest(...) 

        :param [byte]: response Key data returned from key server
        :return: String If offline keays are requested, a keySetId which can
            be used later with restoreKeys, empty for online / streaming) keys.

        New function added.
        """
        return ""
    
    def RemoveKeys(self):
        # type: () -> None
        """
        removes all keys currently loaded in a session. 

        :param None: 
        :return: None

        New function added.
        """
        pass
    
    def RestoreKeys(self, keySetId):
        # type: (str_type) -> None
        """
        restores keys stored during previous provideKeyResponse call. 

        :param String: keySetId
        :return: None

        New function added.
        """
        pass
    
    def SetPropertyString(self, name, value):
        # type: (str_type, str_type) -> None
        """
        Sets a system specific property value in the DRM system 

        :param String: name Name of the property to query 
        :param String: value Value of the property to query
        :return: Value of the requested property

        New function added.
        """
        pass
    
    def Decrypt(self, cipherKeyId, input, iv):
        # type: (Union[str, bytearray], Union[str, bytearray], Union[str, bytearray]) -> bytearray
        """
        Sets a system specific property value in the DRM system 

        :param [byte]: cipherKeyId 
        :param [byte]: input 
        :param [byte]: iv
        :return: Decrypted input data

        New function added.
        """
        return bytearray()
    
    def Encrypt(self, cipherKeyId, input, iv):
        # type: (Union[str, bytearray], Union[str, bytearray], Union[str, bytearray]) -> bytearray
        """
        Sets a system specific property value in the DRM system 

        :param [byte]: cipherKeyId 
        :param [byte]: input 
        :param [byte]: iv
        :return: Encrypted input data

        New function added.
        """
        return bytearray()
    
    def Sign(self, macKeyId, message):
        # type: (Union[str, bytearray], Union[str, bytearray]) -> bytearray
        """
        Sets a system specific property value in the DRM system 

        :param [byte]: macKeyId 
        :param [byte]: message
        :return: [byte] Signature

        New function added.
        """
        return bytearray()
    
    def Verify(self, macKeyId, message, signature):
        # type: (Union[str, bytearray], Union[str, bytearray], Union[str, bytearray]) -> bool
        """
        Sets a system specific property value in the DRM system 

        :param [byte]: macKeyId 
        :param [byte]: message 
        :param [byte]: signature
        :return: true if message verification succeded

        New function added.
        """
        return True
