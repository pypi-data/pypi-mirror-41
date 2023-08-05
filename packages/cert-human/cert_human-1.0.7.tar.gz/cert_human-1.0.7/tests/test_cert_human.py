# -*- coding: utf-8 -*-
"""Test suite for cert_human."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import cert_human
import json
import datetime
import requests
import urllib3
import pytest
import stat
import tempfile
import OpenSSL
import six
import asn1crypto


class TestUrllibPatching(object):
    """Pass."""

    def test_urllib3_classes(self):
        """Pass."""
        assert issubclass(  # nosec
            cert_human.HTTPSConnectionWithCertCls, urllib3.connection.HTTPSConnection
        )
        assert issubclass(  # nosec
            cert_human.ResponseWithCertCls, urllib3.response.HTTPResponse
        )

    def test_enable_urllib3_patch(self, httpbin_secure, httpbin_cert):
        """Pass."""
        cert_human.enable_urllib3_patch()
        r = requests.get(httpbin_secure(), verify=httpbin_cert)
        assert getattr(r.raw, "peer_cert", None)  # nosec
        assert getattr(r.raw, "peer_cert_chain", None)  # nosec
        assert getattr(r.raw, "peer_cert_dict", None)  # nosec
        cert_human.disable_urllib3_patch()

    def test_disable_urllib3_patch(self, httpbin_secure, httpbin_cert):
        """Pass."""
        cert_human.disable_urllib3_patch()
        r = requests.get(httpbin_secure(), verify=httpbin_cert)
        assert not getattr(r.raw, "peer_cert", None)  # nosec
        assert not getattr(r.raw, "peer_cert_chain", None)  # nosec
        assert not getattr(r.raw, "peer_cert_dict", None)  # nosec

    def test_urllib3_patch(self, httpbin_secure, httpbin_cert):
        """Pass."""
        with cert_human.urllib3_patch():
            r = requests.get(httpbin_secure(), verify=httpbin_cert)
            assert getattr(r.raw, "peer_cert", None)  # nosec
            assert getattr(r.raw, "peer_cert_chain", None)  # nosec
            assert getattr(r.raw, "peer_cert_dict", None)  # nosec
        r = requests.get(httpbin_secure(), verify=httpbin_cert)
        assert not getattr(r.raw, "peer_cert", None)  # nosec
        assert not getattr(r.raw, "peer_cert_chain", None)  # nosec
        assert not getattr(r.raw, "peer_cert_dict", None)  # nosec

    def test_using_urllib3_patch(self):
        """Pass."""
        with cert_human.urllib3_patch():
            assert cert_human.using_urllib3_patch()  # nosec
        assert not cert_human.using_urllib3_patch()  # nosec

    def test_check_urllib3_patch(self):
        """Pass."""
        with cert_human.urllib3_patch():
            cert_human.check_urllib3_patch()

    def test_not_check_urllib3_patch(self):
        """Pass."""
        with pytest.raises(cert_human.CertHumanError):
            cert_human.check_urllib3_patch()


class TestGetCerts(object):
    """Pass."""

    def test_test_cert_invalid(self, httpbin_secure):
        """Pass."""
        valid, exc = cert_human.test_cert(host=httpbin_secure())
        assert not valid  # nosec
        assert isinstance(exc, requests.exceptions.SSLError)  # nosec

    def test_test_cert_valid(self, httpbin_secure, httpbin_cert):
        """Pass."""
        valid, exc = cert_human.test_cert(host=httpbin_secure(), verify=httpbin_cert)
        print()
        print(locals())
        assert valid  # nosec
        assert exc is None  # nosec

    def test_get_response(self, httpbin_secure, httpbin_cert):
        """Pass."""
        with pytest.warns(None) as warning_records:
            r = cert_human.get_response(httpbin_secure())
        warning_records = [x for x in warning_records]
        assert not warning_records  # nosec
        assert getattr(r.raw, "peer_cert", None)  # nosec
        assert getattr(r.raw, "peer_cert_chain", None)  # nosec
        assert getattr(r.raw, "peer_cert_dict", None)  # nosec
        cert = r.raw.peer_cert
        subj = cert.get_subject().get_components()
        subj_cn = subj[0]
        assert subj_cn == (b"CN", b"example.com")  # nosec

    def test_get_response_invalid_verify(
        self, httpbin_secure, httpbin_cert, other_cert
    ):
        """Pass."""
        with pytest.raises(requests.exceptions.SSLError):
            cert_human.get_response(httpbin_secure(), verify=format(other_cert))

    def test_get_response_valid_verify(self, httpbin_secure, httpbin_cert):
        """Pass."""
        cert_human.get_response(httpbin_secure(), verify=httpbin_cert)

    def test_ssl_socket(self, httpbin_secure, httpbin_cert):
        """Pass."""
        parts = requests.compat.urlparse(httpbin_secure())
        host = parts.hostname
        port = parts.port
        with cert_human.ssl_socket(host=host, port=port) as sock:
            cert = sock.get_peer_certificate()
            cert_chain = sock.get_peer_cert_chain()
        subj = cert.get_subject().get_components()
        subj_cn = subj[0]
        assert subj_cn == (b"CN", b"example.com")  # nosec
        assert len(cert_chain) == 1  # nosec


class TestUtilities(object):
    """Pass."""

    def test_build_url_only_host(self):
        """Pass."""
        url = cert_human.build_url(host="cyborg")
        assert url == "https://cyborg:443"  # nosec

    def test_build_url_host_port(self):
        """Pass."""
        url = cert_human.build_url(host="cyborg", port=445)
        assert url == "https://cyborg:445"  # nosec

    def test_build_url_port_in_host(self):
        """Pass."""
        url = cert_human.build_url(host="cyborg:445")
        assert url == "https://cyborg:445"  # nosec

    def test_build_url_scheme_in_host(self):
        """Pass."""
        url = cert_human.build_url(host="http://cyborg")
        assert url == "http://cyborg:443"  # nosec

    def test_build_url_port_scheme_in_host(self):
        """Pass."""
        url = cert_human.build_url(host="http://cyborg:445")
        assert url == "http://cyborg:445"  # nosec

    def test_clsname(self):
        """Pass."""
        assert cert_human.clsname(str) == "str"  # nosec
        assert cert_human.clsname(self) == "TestUtilities"  # nosec
        assert cert_human.clsname(cert_human.CertStore) == "CertStore"  # nosec

    def test_hexify_int(self):
        """Pass."""
        # some serial numbers have an odd length hex int
        i = 9833040086282421696121167723365753840
        hstr = "0765C64E74E591D68039CA2A847563F0"
        hnozstr = "765C64E74E591D68039CA2A847563F0"
        hspacestr = "07 65 C6 4E 74 E5 91 D6 80 39 CA 2A 84 75 63 F0"
        assert cert_human.hexify(i) == hstr  # nosec
        assert cert_human.hexify(i, zerofill=False) == hnozstr  # nosec
        assert cert_human.hexify(i, space=True) == hspacestr  # nosec

    def test_hexify_bytes(self):
        """Pass."""
        i = b"\x00\x93\xce\xf7\xff\xed"
        hstr = "0093CEF7FFED"
        hnozstr = "0093CEF7FFED"
        hspacestr = "00 93 CE F7 FF ED"
        assert cert_human.hexify(i) == hstr  # nosec
        assert cert_human.hexify(i, zerofill=False) == hnozstr  # nosec
        assert cert_human.hexify(i, space=True) == hspacestr  # nosec

    def test_indent(self):
        """Pass."""
        txt = "test1\ntest2\n"
        itxt = cert_human.indent(txt=txt)
        assert itxt == "    test1\n    test2"  # nosec

    def test_indent2(self):
        """Pass."""
        txt = "test1\ntest2\n"
        itxt = cert_human.indent(txt=txt)
        assert itxt == "    test1\n    test2"  # nosec

    def test_write_file(self, tmp_path):
        """Pass."""
        sub1 = tmp_path / "sub1"
        sub2 = sub1 / "sub2"
        path = sub2 / "file.txt"
        text = "abc\n123\n"
        ret_path = cert_human.write_file(path=path, text=text)
        assert sub1.is_dir()  # nosec
        assert sub2.is_dir()  # nosec
        assert path.is_file()  # nosec
        assert ret_path.read_text() == text  # nosec
        assert oct(sub2.stat()[stat.ST_MODE])[-4:] == "0700"  # nosec
        assert oct(path.stat()[stat.ST_MODE])[-4:] == "0600"  # nosec

    def test_read_file(self, example_cert):
        """Pass."""
        txt = cert_human.read_file(example_cert)
        assert "----" in txt  # nosec

    def test_read_file_error(self, tmp_path):
        """Pass."""
        with pytest.raises(cert_human.CertHumanError):
            cert_human.read_file(tmp_path / "abc.def.ghi")

    def test_write_file_noprotect(self, tmp_path):
        """Pass."""
        sub1 = tmp_path / "sub1"
        sub2 = sub1 / "sub2"
        path = sub2 / "file.txt"
        text = "abc\n123\n"
        ret_path = cert_human.write_file(path=path, text=text, protect=False)
        assert ret_path.read_text() == text  # nosec

    def test_write_overwrite(self, tmp_path):
        """Pass."""
        sub1 = tmp_path / "sub1"
        sub2 = sub1 / "sub2"
        path = sub2 / "file.txt"
        text1 = "abc\n123\n"
        cert_human.write_file(path=path, text=text1)
        text2 = "def\n\456\n"
        ret_path = cert_human.write_file(path=path, text=text2, overwrite=True)
        assert ret_path.read_text() == text2  # nosec

    def test_write_file_parentfail(self, tmp_path):
        """Pass."""
        sub1 = tmp_path / "sub1"
        sub2 = sub1 / "sub2"
        path = sub2 / "file.txt"
        text = "abc\n123\n"
        with pytest.raises(cert_human.CertHumanError):
            cert_human.write_file(path=path, text=text, mkparent=False)

    def test_write_file_existsfail(self, tmp_path):
        """Pass."""
        sub1 = tmp_path / "sub1"
        sub2 = sub1 / "sub2"
        path = sub2 / "file.txt"
        text = "abc\n123\n"
        cert_human.write_file(path=path, text=text)
        with pytest.raises(cert_human.CertHumanError):
            cert_human.write_file(path=path, text=text)

    def test_write_file_noperm_parent(self):
        """Pass."""
        tmpdir = cert_human.pathlib.Path(tempfile.gettempdir())
        path = tmpdir / "file.txt"
        text = "abc\n123\n"
        ret_path = cert_human.write_file(path=path, text=text, overwrite=True)
        assert ret_path.read_text() == text  # nosec

    def test_find_certs(self, example_cert, other_cert):
        """Pass."""
        example_cert_txt = example_cert.read_text()
        other_cert_txt = other_cert.read_text()
        combo_txt = "\n".join([example_cert_txt, other_cert_txt])
        mixed_txt = "{0}\nother\ngobbledy\ngook\nhere\n{1}\n{0}"
        mixed_txt = mixed_txt.format(example_cert_txt, other_cert_txt)

        example_cert_list = cert_human.find_certs(example_cert_txt)
        other_cert_list = cert_human.find_certs(other_cert_txt)
        combo_list = cert_human.find_certs(combo_txt)
        mixed_list = cert_human.find_certs(mixed_txt)
        assert len(example_cert_list) == 1  # nosec
        assert len(other_cert_list) == 1  # nosec
        assert len(combo_list) == 2  # nosec
        assert len(mixed_list) == 3  # nosec
        for lst in [combo_list, mixed_list, example_cert_list, other_cert_list]:
            for crt in lst:
                assert crt.startswith("-----")  # nosec
                assert crt.endswith("-----")  # nosec

    def test_pem_to_x509(self, example_cert):
        """Pass."""
        example_cert_txt = example_cert.read_text()
        x509 = cert_human.pem_to_x509(example_cert_txt)
        assert isinstance(x509, OpenSSL.crypto.X509)  # nosec
        subj = x509.get_subject().get_components()
        subj_cn = subj[0]
        assert subj_cn == (b"CN", b"example.com")  # nosec

    def test_pems_to_x509(self, example_cert):
        """Pass."""
        example_cert_txt = example_cert.read_text()
        x509s = cert_human.pems_to_x509(example_cert_txt)
        assert len(x509s) == 1  # nosec
        assert isinstance(x509s[0], OpenSSL.crypto.X509)  # nosec
        subj = x509s[0].get_subject().get_components()
        subj_cn = subj[0]
        assert subj_cn == (b"CN", b"example.com")  # nosec

    def test_x509_to_pem(self, example_cert):
        """Pass."""
        example_cert_txt = example_cert.read_text()
        x509 = cert_human.pem_to_x509(example_cert_txt)
        back_again = cert_human.x509_to_pem(x509)
        assert example_cert_txt == back_again  # nosec

    def test_x509_to_der(self, example_cert):
        """Pass."""
        example_cert_txt = example_cert.read_text()
        x509 = cert_human.pem_to_x509(example_cert_txt)
        back_again = cert_human.x509_to_der(x509)
        assert isinstance(back_again, six.binary_type)  # nosec

    def test_x509_to_asn1(self, example_cert):
        """Pass."""
        example_cert_txt = example_cert.read_text()
        x509 = cert_human.pem_to_x509(example_cert_txt)
        back_again = cert_human.x509_to_asn1(x509)
        assert isinstance(back_again, asn1crypto.x509.Certificate)  # nosec
        assert back_again.subject.native == {"common_name": "example.com"}  # nosec

    def test_der_to_asn1(self, example_cert):
        """Pass."""
        example_cert_txt = example_cert.read_text()
        x509 = cert_human.pem_to_x509(example_cert_txt)
        der = cert_human.x509_to_der(x509)
        asn1 = cert_human.der_to_asn1(der)
        assert isinstance(asn1, asn1crypto.x509.Certificate)  # nosec
        assert asn1.subject.native == {"common_name": "example.com"}  # nosec


class TestCertStore(object):
    """Pass."""

    def test_init(self, example_cert):
        """Pass."""
        pem = example_cert.read_text()
        x509 = cert_human.pem_to_x509(pem)
        store = cert_human.CertStore(x509)
        assert "Subject: Common Name: example.com" in format(store)  # nosec
        assert "Subject: Common Name: example.com" in repr(store)  # nosec
        assert pem == store.pem  # nosec
        assert isinstance(store.der, six.binary_type)  # nosec

    def test_from_socket(self, httpbin_secure, httpbin_cert):
        """Pass."""
        parts = requests.compat.urlparse(httpbin_secure())
        host = parts.hostname
        port = parts.port
        store = cert_human.CertStore.from_socket(host=host, port=port)
        assert "Subject: Common Name: example.com" in format(store)  # nosec

    def test_from_request(self, httpbin_secure, httpbin_cert):
        """Pass."""
        parts = requests.compat.urlparse(httpbin_secure())
        host = parts.hostname
        port = parts.port
        store = cert_human.CertStore.from_request(host=host, port=port)
        assert "Subject: Common Name: example.com" in format(store)  # nosec

    def test_from_response(self, httpbin_secure, httpbin_cert):
        """Pass."""
        r = cert_human.get_response(httpbin_secure())
        store = cert_human.CertStore.from_response(r)
        assert "Subject: Common Name: example.com" in format(store)  # nosec

    def test_from_response_no_withcert(self, httpbin_secure, httpbin_cert):
        """Pass."""
        cert_human.disable_urllib3_patch()
        r = requests.get(httpbin_secure(), verify=False)  # nosec
        with pytest.raises(cert_human.CertHumanError):
            cert_human.CertStore.from_response(r)

    def test_from_auto(self, httpbin_secure, httpbin_cert, example_cert):
        """Pass."""
        r = cert_human.get_response(httpbin_secure())
        auto_response = cert_human.CertStore.from_auto(r)
        store = cert_human.CertStore.from_path(example_cert)
        auto_asn1 = cert_human.CertStore.from_auto(store.asn1)
        auto_pem = cert_human.CertStore.from_auto(store.pem)
        auto_x509 = cert_human.CertStore.from_auto(store.x509)
        auto_der = cert_human.CertStore.from_auto(store.der)
        for i in [auto_asn1, auto_pem, auto_x509, auto_der, auto_response]:
            assert "Subject: Common Name: example.com" in format(i)  # nosec

    def test_from_auto_bad(self):
        """Pass."""
        with pytest.raises(cert_human.CertHumanError):
            cert_human.CertStore.from_auto(None)
        with pytest.raises(cert_human.CertHumanError):
            cert_human.CertStore.from_auto("x")

    def test_from_path(self, example_cert):
        """Pass."""
        store = cert_human.CertStore.from_path(format(example_cert))
        assert "Subject: Common Name: example.com" in format(store)  # nosec

    def test_to_path(self, example_cert):
        """Pass."""
        tmpdir = cert_human.pathlib.Path(tempfile.gettempdir())
        path = tmpdir / "sub3" / "sub4" / "cert.pem"
        store = cert_human.CertStore.from_path(example_cert)
        ret_path = store.to_path(path, overwrite=True)
        assert ret_path.read_text() == store.pem  # nosec

    def test_test(self, httpbin_secure, httpbin_cert):
        """Pass."""
        store = cert_human.CertStore.from_request(httpbin_secure())
        valid, exc = store.test(host=httpbin_secure())
        assert exc is None  # nosec
        assert valid  # nosec

    def test_issuer(self, example_cert):
        """Pass."""
        store = cert_human.CertStore.from_path(example_cert)
        assert store.issuer == {"common_name": "example.com"}  # nosec

    def test_subject(self, example_cert):
        """Pass."""
        store = cert_human.CertStore.from_path(example_cert)
        assert store.subject == {"common_name": "example.com"}  # nosec

    def test_subject_alt_names(self, example_cert):
        """Pass."""
        store = cert_human.CertStore.from_path(example_cert)
        assert store.subject_alt_names == [  # nosec
            "example.com",
            "example.net",
            "localhost",
            "127.0.0.1",
        ]

    def test_subject_alt_names_none(self, httpbin_builtin_cert):
        """Pass."""
        store = cert_human.CertStore.from_path(httpbin_builtin_cert)
        assert store.subject_alt_names == []  # nosec

    def test_public_key(self, ec_cert, example_cert):
        """Pass."""
        store = cert_human.CertStore.from_path(example_cert)
        assert len(store.public_key) >= 20  # nosec
        assert store.public_key.isupper()  # nosec
        store = cert_human.CertStore.from_path(ec_cert)
        assert len(store.public_key) >= 20  # nosec
        assert store.public_key.isupper()  # nosec

    def test_public_key_str(self, ec_cert, example_cert):
        """Pass."""
        store = cert_human.CertStore.from_path(example_cert)
        assert " " in store.public_key_str  # nosec
        assert "\n" in store.public_key_str  # nosec
        assert store.public_key_str.isupper()  # nosec
        store = cert_human.CertStore.from_path(ec_cert)
        assert " " in store.public_key_str  # nosec
        assert "\n" in store.public_key_str  # nosec
        assert store.public_key_str.isupper()  # nosec

    def test_public_key_parameters(self, ec_cert, example_cert):
        """Pass."""
        store = cert_human.CertStore.from_path(example_cert)
        assert not store.public_key_parameters  # nosec
        store = cert_human.CertStore.from_path(ec_cert)
        assert store.public_key_parameters  # nosec

    def test_public_key_size(self, ec_cert, example_cert):
        """Pass."""
        store = cert_human.CertStore.from_path(example_cert)
        assert store.public_key_size == 4096  # nosec
        store = cert_human.CertStore.from_path(ec_cert)
        assert store.public_key_size == 256  # nosec

    def test_public_key_exponent(self, ec_cert, example_cert):
        """Pass."""
        store = cert_human.CertStore.from_path(example_cert)
        assert store.public_key_exponent == 65537  # nosec
        store = cert_human.CertStore.from_path(ec_cert)
        assert store.public_key_exponent is None  # nosec

    def test_signature(self, example_cert):
        """Pass."""
        store = cert_human.CertStore.from_path(example_cert)
        assert len(store.signature) >= 20  # nosec
        assert store.signature.isupper()  # nosec

    def test_signature_str(self, example_cert):
        """Pass."""
        store = cert_human.CertStore.from_path(example_cert)
        assert " " in store.signature_str  # nosec
        assert "\n" in store.signature_str  # nosec
        assert store.signature_str.isupper()  # nosec

    def test_signature_algorithm(self, example_cert):
        """Pass."""
        store = cert_human.CertStore.from_path(example_cert)
        assert store.signature_algorithm == "sha256_rsa"  # nosec

    def test_x509_version(self, example_cert):
        """Pass."""
        store = cert_human.CertStore.from_path(example_cert)
        assert store.x509_version == "v3"  # nosec

    def test_serial_number(self, ec_cert, example_cert):
        """Pass."""
        store = cert_human.CertStore.from_path(example_cert)
        assert store.serial_number.isupper()  # nosec
        store = cert_human.CertStore.from_path(ec_cert)
        assert isinstance(store.serial_number, six.integer_types)  # nosec

    def test_serial_number_str(self, ec_cert, example_cert):
        """Pass."""
        store = cert_human.CertStore.from_path(example_cert)
        assert " " in store.serial_number_str  # nosec
        assert store.serial_number_str.isupper()  # nosec
        store = cert_human.CertStore.from_path(ec_cert)
        assert isinstance(store.serial_number_str, (six.integer_types))  # nosec

    def test_is_expired(self, example_cert):
        """Pass."""
        store = cert_human.CertStore.from_path(example_cert)
        assert store.is_expired is False  # nosec

    def test_is_self_issued(self, example_cert):
        """Pass."""
        store = cert_human.CertStore.from_path(example_cert)
        assert store.is_self_issued is True  # nosec

    def test_is_self_signed(self, example_cert):
        """Pass."""
        store = cert_human.CertStore.from_path(example_cert)
        assert store.is_self_signed == "maybe"  # nosec

    def test_not_valid_before(self, example_cert):
        """Pass."""
        store = cert_human.CertStore.from_path(example_cert)
        assert isinstance(store.not_valid_before, datetime.datetime)  # nosec

    def test_not_valid_after(self, example_cert):
        """Pass."""
        store = cert_human.CertStore.from_path(example_cert)
        assert isinstance(store.not_valid_after, datetime.datetime)  # nosec

    def test_not_valid_before_str(self, example_cert):
        """Pass."""
        store = cert_human.CertStore.from_path(example_cert)
        assert isinstance(store.not_valid_before_str, six.string_types)  # nosec

    def test_not_valid_after_str(self, example_cert):
        """Pass."""
        store = cert_human.CertStore.from_path(example_cert)
        assert isinstance(store.not_valid_after_str, six.string_types)  # nosec

    def test_extensions(self, example_cert):
        """Pass."""
        store = cert_human.CertStore.from_path(example_cert)
        assert store.extensions == {  # nosec
            "subjectAltName": (
                "DNS:example.com, DNS:example.net, DNS:localhost, IP Address:127.0.0.1"
            )
        }

    def test_extensions_str(self, example_cert):
        """Pass."""
        store = cert_human.CertStore.from_path(example_cert)
        assert store.extensions_str == (  # nosec
            "Extension 1, name=subjectAltName, value=DNS:example.com, DNS:example.net, "
            "DNS:localhost, IP Address:127.0.0.1"
        )

    def test_dump(self, example_cert):
        """Pass."""
        store = cert_human.CertStore.from_path(example_cert)
        assert store.dump["subject"] == {"common_name": "example.com"}  # nosec

    def test_dump_json_friendly(self, example_cert):
        """Pass."""
        store = cert_human.CertStore.from_path(example_cert)
        assert all(  # nosec
            isinstance(
                v, (dict, six.string_types, six.integer_types, list, bool, type(None))
            )
            for v in store.dump_json_friendly.values()
        )

    def test_dump_json(self, example_cert):
        """Pass."""
        store = cert_human.CertStore.from_path(example_cert)
        dump = json.loads(store.dump_json)
        assert (  # nosec
            '"subject": {\n    "common_name": "example.com"\n' in store.dump_json
        )
        assert isinstance(dump, dict)  # nosec

    def test_dump_str(self, example_cert):
        """Pass."""
        store = cert_human.CertStore.from_path(example_cert)
        assert "Subject: Common Name: example.com\n" in store.dump_str  # nosec

    def test_dump_str_exts(self, example_cert):
        """Pass."""
        store = cert_human.CertStore.from_path(example_cert)
        assert store.dump_str_exts == (  # nosec
            "Extensions:\n    Extension 1, name=subjectAltName, "
            "value=DNS:example.com, DNS:example.net, DNS:localhost, "
            "IP Address:127.0.0.1"
        )


class TestChainCertStore(object):
    """Pass."""

    def test_init(self, example_cert, other_cert, ec_cert):
        """Pass."""
        example_pem = example_cert.read_text()
        other_pem = other_cert.read_text()
        ec_pem = ec_cert.read_text()
        x509s = [
            cert_human.pem_to_x509(example_pem),
            cert_human.pem_to_x509(other_pem),
            cert_human.pem_to_x509(ec_pem),
        ]
        store = cert_human.CertChainStore(x509s)
        assert len(store) == 3  # nosec
        assert store[0].x509 == x509s[0]  # nosec
        assert "Subject: Common Name: example.com" in format(store)  # nosec
        assert "Subject: Common Name: otherexample.com" in format(store)  # nosec
        assert "Subject: Common Name: ecexample.com" in format(store)  # nosec
        assert "Subject: Common Name: example.com" in repr(store)  # nosec

    def test_append(self, example_cert, ec_cert, other_cert):
        """Pass."""
        example_store = cert_human.CertStore.from_path(example_cert)
        other_store = cert_human.CertStore.from_path(other_cert)
        ec_store = cert_human.CertStore.from_path(ec_cert)

        store = cert_human.CertChainStore([])
        store.append(example_store.x509)
        store.append(other_store)
        store.append(ec_store.pem)
        assert len(store) == 3  # nosec

    def test_from_socket(self, httpbin_secure, httpbin_cert):
        """Pass."""
        parts = requests.compat.urlparse(httpbin_secure())
        host = parts.hostname
        port = parts.port
        store = cert_human.CertChainStore.from_socket(host=host, port=port)
        assert len(store) == 1  # nosec
        assert "Subject: Common Name: example.com" in format(store[0])  # nosec

    def test_from_request(self, httpbin_secure, httpbin_cert):
        """Pass."""
        parts = requests.compat.urlparse(httpbin_secure())
        host = parts.hostname
        port = parts.port
        store = cert_human.CertChainStore.from_request(host=host, port=port)
        assert len(store) == 1  # nosec
        assert "Subject: Common Name: example.com" in format(store[0])  # nosec

    def test_from_response(self, httpbin_secure, httpbin_cert):
        """Pass."""
        r = cert_human.get_response(httpbin_secure())
        store = cert_human.CertChainStore.from_response(r)
        assert len(store) == 1  # nosec
        assert "Subject: Common Name: example.com" in format(store[0])  # nosec

    def test_from_response_no_withcert(self, httpbin_secure, httpbin_cert):
        """Pass."""
        r = requests.get(httpbin_secure(), verify=False)  # nosec
        with pytest.raises(cert_human.CertHumanError):
            cert_human.CertChainStore.from_response(r)

    def test_from_pem(self, example_cert, other_cert):
        """Pass."""
        example_pem = example_cert.read_text()
        other_pem = other_cert.read_text()
        pems = "\n".join([example_pem, other_pem])
        store = cert_human.CertChainStore.from_pem(pems)
        assert len(store) == 2  # nosec
        assert "Subject: Common Name: example.com" in format(store[0])  # nosec

    def test_from_path(self, example_cert):
        """Pass."""
        store = cert_human.CertChainStore.from_path(example_cert)
        assert len(store) == 1  # nosec
        assert "Subject: Common Name: example.com" in format(store[0])  # nosec
        assert len(store.certs) == 1  # nosec
        assert len(cert_human.find_certs(store.pem)) == 1  # nosec
        assert len(store.x509) == 1  # nosec
        assert len(store.der) == 1  # nosec
        assert len(store.asn1) == 1  # nosec

    def test_to_path(self, example_cert):
        """Pass."""
        tmpdir = cert_human.pathlib.Path(tempfile.gettempdir())
        path = tmpdir / "sub3" / "sub4" / "cert.pem"
        store = cert_human.CertChainStore.from_path(example_cert)
        ret_path = store.to_path(path, overwrite=True)
        assert ret_path.read_text() == store.pem  # nosec

    def test_dumps(self, example_cert):
        """Pass."""
        store = cert_human.CertChainStore.from_path(example_cert)
        dumps = [store.dump_json_friendly, store.dump]
        for d in dumps:
            assert isinstance(d, list)  # nosec
            assert len(d) == 1  # nosec

    def test_dumps_str(self, example_cert):
        """Pass."""
        store = cert_human.CertChainStore.from_path(example_cert)
        dumps = [
            store.dump_str,
            store.dump_str_info,
            store.dump_str_exts,
            store.dump_str_key,
        ]
        for d in dumps:
            assert isinstance(d, six.string_types)  # nosec
            assert "CertStore #1" in d.splitlines()[1]  # nosec

    def test_dump_json(self, example_cert):
        """Pass."""
        store = cert_human.CertChainStore.from_path(example_cert)
        dump = json.loads(store.dump_json)
        assert isinstance(dump, list)  # nosec
        assert len(dump) == 1  # nosec
