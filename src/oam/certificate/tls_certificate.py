from dataclasses import dataclass
from typing import List
from oam.asset import Asset
from oam.asset import AssetType
from enum import Enum

class TLSKeyUsageType(str, Enum):
    DigitalSignature = "Digital Signature"
    ContentCommitment = "Content Commitment"
    KeyEncipherment = "Key Encipherment"
    DataEncipherment = "Data Encipherment"
    KeyAgreement = "Key Agreement"
    CertSign = "Certificate Sign"
    CRLSign = "CRL Sign"
    EncipherOnly = "Encipher Only"
    DecipherOnly = "Decipher Only"

class TLSExtKeyUsageType(str, Enum):
    Any = "Any Usage"
    ServerAuth = "TLS Server Authentication"
    ClientAuth = "TLS Client Authentication"
    CodeSigning = "Code Signing"
    EmailProtection = "E-mail Protection"
    IPSECEndSystem = "IPSec End System"
    IPSECTunnel = "IPSec Tunnel"
    IPSECUser = "IPSec User"
    TimeStamping = "Trusted Timestamping"
    OCSPSigning = "OCSP Signing"
    MicrosoftServerGatedCrypto = "Microsoft Server Gated Crypto"
    NetscapeServerGatedCrypto = "Netscape Server Gated Crypto"
    MicrosoftCommercialCodeSigning = "Microsoft Commercial Code Signing"
    MicrosoftKernelCodeSigning = "Microsoft Kernel Code Signing"
    
@dataclass
class TLSCertificate(Asset):
    """TLSCertificate represents a TLS Certificate asset."""
    version:                  str
    serial_number:            str
    subject_common_name:      str
    issuer_common_name:       str
    not_before:               str
    not_after:                str
    key_usage:                List[TLSKeyUsageType]
    ext_key_usage:            List[TLSExtKeyUsageType]
    signature_algorithm:      str
    public_key_algorithm:     str
    is_ca:                    bool
    crl_distribution_points:  List[str]
    subject_key_id:           str
    authority_key_id:         str

    @property
    def key(self) -> str:
        return self.serial_number

    @property
    def asset_type(self) -> AssetType:
        return AssetType.TLSCertificate
