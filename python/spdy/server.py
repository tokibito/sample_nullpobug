import socket
import ssl
import struct
import zlib
import pprint

RESPONSE_TEXT = b"""HTTP/1.1 200 OK
Server: Test/0.1
Content-Length: 12
Keep-Alive: timeout=10, max=100
Connection: Keep-Alive
Content-Type: text/plain

Hello, SPDY!
"""

SPDY_DATA_FRAME_BIT = 0
SPDY_CONTROL_FRAME_BIT = 1
SPDY_SYN_STREAM = 1
SPDY_SYN_REPLY = 2
SPDY_RST_STREAM = 3
SPDY_SETTINGS = 4
SPDY_PING = 6

# ZLIB用の辞書
SPDY_DICTIONARY = \
    b"\x00\x00\x00\x07\x6f\x70\x74\x69" + \
    b"\x6f\x6e\x73\x00\x00\x00\x04\x68" + \
    b"\x65\x61\x64\x00\x00\x00\x04\x70" + \
    b"\x6f\x73\x74\x00\x00\x00\x03\x70" + \
    b"\x75\x74\x00\x00\x00\x06\x64\x65" + \
    b"\x6c\x65\x74\x65\x00\x00\x00\x05" + \
    b"\x74\x72\x61\x63\x65\x00\x00\x00" + \
    b"\x06\x61\x63\x63\x65\x70\x74\x00" + \
    b"\x00\x00\x0e\x61\x63\x63\x65\x70" + \
    b"\x74\x2d\x63\x68\x61\x72\x73\x65" + \
    b"\x74\x00\x00\x00\x0f\x61\x63\x63" + \
    b"\x65\x70\x74\x2d\x65\x6e\x63\x6f" + \
    b"\x64\x69\x6e\x67\x00\x00\x00\x0f" + \
    b"\x61\x63\x63\x65\x70\x74\x2d\x6c" + \
    b"\x61\x6e\x67\x75\x61\x67\x65\x00" + \
    b"\x00\x00\x0d\x61\x63\x63\x65\x70" + \
    b"\x74\x2d\x72\x61\x6e\x67\x65\x73" + \
    b"\x00\x00\x00\x03\x61\x67\x65\x00" + \
    b"\x00\x00\x05\x61\x6c\x6c\x6f\x77" + \
    b"\x00\x00\x00\x0d\x61\x75\x74\x68" + \
    b"\x6f\x72\x69\x7a\x61\x74\x69\x6f" + \
    b"\x6e\x00\x00\x00\x0d\x63\x61\x63" + \
    b"\x68\x65\x2d\x63\x6f\x6e\x74\x72" + \
    b"\x6f\x6c\x00\x00\x00\x0a\x63\x6f" + \
    b"\x6e\x6e\x65\x63\x74\x69\x6f\x6e" + \
    b"\x00\x00\x00\x0c\x63\x6f\x6e\x74" + \
    b"\x65\x6e\x74\x2d\x62\x61\x73\x65" + \
    b"\x00\x00\x00\x10\x63\x6f\x6e\x74" + \
    b"\x65\x6e\x74\x2d\x65\x6e\x63\x6f" + \
    b"\x64\x69\x6e\x67\x00\x00\x00\x10" + \
    b"\x63\x6f\x6e\x74\x65\x6e\x74\x2d" + \
    b"\x6c\x61\x6e\x67\x75\x61\x67\x65" + \
    b"\x00\x00\x00\x0e\x63\x6f\x6e\x74" + \
    b"\x65\x6e\x74\x2d\x6c\x65\x6e\x67" + \
    b"\x74\x68\x00\x00\x00\x10\x63\x6f" + \
    b"\x6e\x74\x65\x6e\x74\x2d\x6c\x6f" + \
    b"\x63\x61\x74\x69\x6f\x6e\x00\x00" + \
    b"\x00\x0b\x63\x6f\x6e\x74\x65\x6e" + \
    b"\x74\x2d\x6d\x64\x35\x00\x00\x00" + \
    b"\x0d\x63\x6f\x6e\x74\x65\x6e\x74" + \
    b"\x2d\x72\x61\x6e\x67\x65\x00\x00" + \
    b"\x00\x0c\x63\x6f\x6e\x74\x65\x6e" + \
    b"\x74\x2d\x74\x79\x70\x65\x00\x00" + \
    b"\x00\x04\x64\x61\x74\x65\x00\x00" + \
    b"\x00\x04\x65\x74\x61\x67\x00\x00" + \
    b"\x00\x06\x65\x78\x70\x65\x63\x74" + \
    b"\x00\x00\x00\x07\x65\x78\x70\x69" + \
    b"\x72\x65\x73\x00\x00\x00\x04\x66" + \
    b"\x72\x6f\x6d\x00\x00\x00\x04\x68" + \
    b"\x6f\x73\x74\x00\x00\x00\x08\x69" + \
    b"\x66\x2d\x6d\x61\x74\x63\x68\x00" + \
    b"\x00\x00\x11\x69\x66\x2d\x6d\x6f" + \
    b"\x64\x69\x66\x69\x65\x64\x2d\x73" + \
    b"\x69\x6e\x63\x65\x00\x00\x00\x0d" + \
    b"\x69\x66\x2d\x6e\x6f\x6e\x65\x2d" + \
    b"\x6d\x61\x74\x63\x68\x00\x00\x00" + \
    b"\x08\x69\x66\x2d\x72\x61\x6e\x67" + \
    b"\x65\x00\x00\x00\x13\x69\x66\x2d" + \
    b"\x75\x6e\x6d\x6f\x64\x69\x66\x69" + \
    b"\x65\x64\x2d\x73\x69\x6e\x63\x65" + \
    b"\x00\x00\x00\x0d\x6c\x61\x73\x74" + \
    b"\x2d\x6d\x6f\x64\x69\x66\x69\x65" + \
    b"\x64\x00\x00\x00\x08\x6c\x6f\x63" + \
    b"\x61\x74\x69\x6f\x6e\x00\x00\x00" + \
    b"\x0c\x6d\x61\x78\x2d\x66\x6f\x72" + \
    b"\x77\x61\x72\x64\x73\x00\x00\x00" + \
    b"\x06\x70\x72\x61\x67\x6d\x61\x00" + \
    b"\x00\x00\x12\x70\x72\x6f\x78\x79" + \
    b"\x2d\x61\x75\x74\x68\x65\x6e\x74" + \
    b"\x69\x63\x61\x74\x65\x00\x00\x00" + \
    b"\x13\x70\x72\x6f\x78\x79\x2d\x61" + \
    b"\x75\x74\x68\x6f\x72\x69\x7a\x61" + \
    b"\x74\x69\x6f\x6e\x00\x00\x00\x05" + \
    b"\x72\x61\x6e\x67\x65\x00\x00\x00" + \
    b"\x07\x72\x65\x66\x65\x72\x65\x72" + \
    b"\x00\x00\x00\x0b\x72\x65\x74\x72" + \
    b"\x79\x2d\x61\x66\x74\x65\x72\x00" + \
    b"\x00\x00\x06\x73\x65\x72\x76\x65" + \
    b"\x72\x00\x00\x00\x02\x74\x65\x00" + \
    b"\x00\x00\x07\x74\x72\x61\x69\x6c" + \
    b"\x65\x72\x00\x00\x00\x11\x74\x72" + \
    b"\x61\x6e\x73\x66\x65\x72\x2d\x65" + \
    b"\x6e\x63\x6f\x64\x69\x6e\x67\x00" + \
    b"\x00\x00\x07\x75\x70\x67\x72\x61" + \
    b"\x64\x65\x00\x00\x00\x0a\x75\x73" + \
    b"\x65\x72\x2d\x61\x67\x65\x6e\x74" + \
    b"\x00\x00\x00\x04\x76\x61\x72\x79" + \
    b"\x00\x00\x00\x03\x76\x69\x61\x00" + \
    b"\x00\x00\x07\x77\x61\x72\x6e\x69" + \
    b"\x6e\x67\x00\x00\x00\x10\x77\x77" + \
    b"\x77\x2d\x61\x75\x74\x68\x65\x6e" + \
    b"\x74\x69\x63\x61\x74\x65\x00\x00" + \
    b"\x00\x06\x6d\x65\x74\x68\x6f\x64" + \
    b"\x00\x00\x00\x03\x67\x65\x74\x00" + \
    b"\x00\x00\x06\x73\x74\x61\x74\x75" + \
    b"\x73\x00\x00\x00\x06\x32\x30\x30" + \
    b"\x20\x4f\x4b\x00\x00\x00\x07\x76" + \
    b"\x65\x72\x73\x69\x6f\x6e\x00\x00" + \
    b"\x00\x08\x48\x54\x54\x50\x2f\x31" + \
    b"\x2e\x31\x00\x00\x00\x03\x75\x72" + \
    b"\x6c\x00\x00\x00\x06\x70\x75\x62" + \
    b"\x6c\x69\x63\x00\x00\x00\x0a\x73" + \
    b"\x65\x74\x2d\x63\x6f\x6f\x6b\x69" + \
    b"\x65\x00\x00\x00\x0a\x6b\x65\x65" + \
    b"\x70\x2d\x61\x6c\x69\x76\x65\x00" + \
    b"\x00\x00\x06\x6f\x72\x69\x67\x69" + \
    b"\x6e\x31\x30\x30\x31\x30\x31\x32" + \
    b"\x30\x31\x32\x30\x32\x32\x30\x35" + \
    b"\x32\x30\x36\x33\x30\x30\x33\x30" + \
    b"\x32\x33\x30\x33\x33\x30\x34\x33" + \
    b"\x30\x35\x33\x30\x36\x33\x30\x37" + \
    b"\x34\x30\x32\x34\x30\x35\x34\x30" + \
    b"\x36\x34\x30\x37\x34\x30\x38\x34" + \
    b"\x30\x39\x34\x31\x30\x34\x31\x31" + \
    b"\x34\x31\x32\x34\x31\x33\x34\x31" + \
    b"\x34\x34\x31\x35\x34\x31\x36\x34" + \
    b"\x31\x37\x35\x30\x32\x35\x30\x34" + \
    b"\x35\x30\x35\x32\x30\x33\x20\x4e" + \
    b"\x6f\x6e\x2d\x41\x75\x74\x68\x6f" + \
    b"\x72\x69\x74\x61\x74\x69\x76\x65" + \
    b"\x20\x49\x6e\x66\x6f\x72\x6d\x61" + \
    b"\x74\x69\x6f\x6e\x32\x30\x34\x20" + \
    b"\x4e\x6f\x20\x43\x6f\x6e\x74\x65" + \
    b"\x6e\x74\x33\x30\x31\x20\x4d\x6f" + \
    b"\x76\x65\x64\x20\x50\x65\x72\x6d" + \
    b"\x61\x6e\x65\x6e\x74\x6c\x79\x34" + \
    b"\x30\x30\x20\x42\x61\x64\x20\x52" + \
    b"\x65\x71\x75\x65\x73\x74\x34\x30" + \
    b"\x31\x20\x55\x6e\x61\x75\x74\x68" + \
    b"\x6f\x72\x69\x7a\x65\x64\x34\x30" + \
    b"\x33\x20\x46\x6f\x72\x62\x69\x64" + \
    b"\x64\x65\x6e\x34\x30\x34\x20\x4e" + \
    b"\x6f\x74\x20\x46\x6f\x75\x6e\x64" + \
    b"\x35\x30\x30\x20\x49\x6e\x74\x65" + \
    b"\x72\x6e\x61\x6c\x20\x53\x65\x72" + \
    b"\x76\x65\x72\x20\x45\x72\x72\x6f" + \
    b"\x72\x35\x30\x31\x20\x4e\x6f\x74" + \
    b"\x20\x49\x6d\x70\x6c\x65\x6d\x65" + \
    b"\x6e\x74\x65\x64\x35\x30\x33\x20" + \
    b"\x53\x65\x72\x76\x69\x63\x65\x20" + \
    b"\x55\x6e\x61\x76\x61\x69\x6c\x61" + \
    b"\x62\x6c\x65\x4a\x61\x6e\x20\x46" + \
    b"\x65\x62\x20\x4d\x61\x72\x20\x41" + \
    b"\x70\x72\x20\x4d\x61\x79\x20\x4a" + \
    b"\x75\x6e\x20\x4a\x75\x6c\x20\x41" + \
    b"\x75\x67\x20\x53\x65\x70\x74\x20" + \
    b"\x4f\x63\x74\x20\x4e\x6f\x76\x20" + \
    b"\x44\x65\x63\x20\x30\x30\x3a\x30" + \
    b"\x30\x3a\x30\x30\x20\x4d\x6f\x6e" + \
    b"\x2c\x20\x54\x75\x65\x2c\x20\x57" + \
    b"\x65\x64\x2c\x20\x54\x68\x75\x2c" + \
    b"\x20\x46\x72\x69\x2c\x20\x53\x61" + \
    b"\x74\x2c\x20\x53\x75\x6e\x2c\x20" + \
    b"\x47\x4d\x54\x63\x68\x75\x6e\x6b" + \
    b"\x65\x64\x2c\x74\x65\x78\x74\x2f" + \
    b"\x68\x74\x6d\x6c\x2c\x69\x6d\x61" + \
    b"\x67\x65\x2f\x70\x6e\x67\x2c\x69" + \
    b"\x6d\x61\x67\x65\x2f\x6a\x70\x67" + \
    b"\x2c\x69\x6d\x61\x67\x65\x2f\x67" + \
    b"\x69\x66\x2c\x61\x70\x70\x6c\x69" + \
    b"\x63\x61\x74\x69\x6f\x6e\x2f\x78" + \
    b"\x6d\x6c\x2c\x61\x70\x70\x6c\x69" + \
    b"\x63\x61\x74\x69\x6f\x6e\x2f\x78" + \
    b"\x68\x74\x6d\x6c\x2b\x78\x6d\x6c" + \
    b"\x2c\x74\x65\x78\x74\x2f\x70\x6c" + \
    b"\x61\x69\x6e\x2c\x74\x65\x78\x74" + \
    b"\x2f\x6a\x61\x76\x61\x73\x63\x72" + \
    b"\x69\x70\x74\x2c\x70\x75\x62\x6c" + \
    b"\x69\x63\x70\x72\x69\x76\x61\x74" + \
    b"\x65\x6d\x61\x78\x2d\x61\x67\x65" + \
    b"\x3d\x67\x7a\x69\x70\x2c\x64\x65" + \
    b"\x66\x6c\x61\x74\x65\x2c\x73\x64" + \
    b"\x63\x68\x63\x68\x61\x72\x73\x65" + \
    b"\x74\x3d\x75\x74\x66\x2d\x38\x63" + \
    b"\x68\x61\x72\x73\x65\x74\x3d\x69" + \
    b"\x73\x6f\x2d\x38\x38\x35\x39\x2d" + \
    b"\x31\x2c\x75\x74\x66\x2d\x2c\x2a" + \
    b"\x2c\x65\x6e\x71\x3d\x30\x2e"


def print_binary(binary):
    "ビット列を画面にプリントする"
    bits = ''
    for byte in binary:
        bits_for_byte = bin(byte)[2:]
        if len(bits_for_byte) < 8:
            bits += '0' * (8 - len(bits_for_byte))
        bits += bits_for_byte
    width = 32
    while bits:
        pprint.pprint(bits[:width])
        bits = bits[width:]


class SPDYFrame:
    def __init__(self, frame=None):
        self.frame = frame

    @classmethod
    def decode_frame(cls, frame):
        #pprint.pprint(cls)
        #pprint.pprint(frame)
        spdy_frame = cls(frame)
        spdy_frame.decode()
        return spdy_frame

    def decode(self):
        self.get_control_bit()
        self.get_flags()
        self.get_data_length()
        if self.is_control_frame():
            self.decode_control_frame()
        else:
            self.decode_data_frame()

    def get_control_bit(self):
        "フレームの先頭1ビットを返す"
        if not hasattr(self, '_control_bit'):
            #print(type(self.frame[0]))
            self._control_bit = self.frame[0] >> 7
        return self._control_bit
    control_bit = property(get_control_bit)

    def is_control_frame(self):
        return self.get_control_bit() == SPDY_CONTROL_FRAME_BIT

    def is_data_frame(self):
        return self.get_control_bit() == SPDY_DATA_FRAME_BIT

    def get_spdy_version(self):
        "Versionのデコード(C)"
        if not hasattr(self, '_spdy_version'):
            self._spdy_version = \
                struct.unpack('!H', self.frame[0:2])[0] & 0b0111111111111111
        return self._spdy_version
    spdy_version = property(get_spdy_version)

    def get_type(self):
        "Typeのデコード(C)"
        if not hasattr(self, '_type'):
            self._type = struct.unpack('!H', self.frame[2:4])[0]
        return self._type
    type = property(get_type)

    def get_data_length(self):
        "Lengthのデコード(C/D)"
        if not hasattr(self, '_data_length'):
            self._data_length = \
                struct.unpack('!I', b'\x00' + self.frame[5:8])[0]
        return self._data_length
    data_length = property(get_data_length)

    def get_flags(self):
        "Flagsのデコード(C/D)"
        if not hasattr(self, '_flags'):
            self._flags = self.frame[4]
        return self._flags
    flags = property(get_flags)

    def get_number_of_entries(self):
        "Number of entriesのデコード(C:SETTINGS)"
        if not hasattr(self, '_number_of_entries'):
            self._number_of_entries = struct.unpack('!I', self.frame[8:12])[0]
        return self._number_of_entries
    number_of_entries = property(get_number_of_entries)

    def get_stream_id(self):
        "Stream-IDのデコード(C/D)"
        if not hasattr(self, '_stream_id'):
            if self.type == SPDY_SYN_STREAM:
                self._stream_id = \
                    struct.unpack('!I', self.frame[8:12])[0] & 0x7FFFFFFF
        return self._stream_id
    stream_id = property(get_stream_id)

    def get_associated_to_stream_id(self):
        "Associated-To-Stream-IDのデコード(C:SYN_STREAM)"
        if not hasattr(self, '_associated_to_stream_id'):
            if self.type == SPDY_SYN_STREAM:
                self._associated_to_stream_id = \
                    struct.unpack('!I', self.frame[12:16])[0] & 0x7FFFFFFF
        return self._associated_to_stream_id
    associated_to_stream_id = property(get_associated_to_stream_id)

    def get_priority(self):
        "Priorityのデコード(C:SYN_STREAM)"
        if not hasattr(self, '_priority'):
            # 左から3bitを使う
            self._priority = self.frame[16] >> 5
        return self._priority
    priority = property(get_priority)

    def get_slot(self):
        "Slotのデコード(C:SYN_STREAM)"
        if not hasattr(self, '_slot'):
            self._slot = self.frame[17]
        return self._slot
    slot = property(get_slot)

    def get_compressed_data(self):
        "圧縮された領域のデータ(C:SYN_STREAM)"
        zlibobj = zlib.decompressobj(zdict=SPDY_DICTIONARY)
        if not hasattr(self, '_compressed_data'):
            self._compressed_data = zlibobj.decompress(self.frame[18:])
        return self._compressed_data
    compressed_data = property(get_compressed_data)

    def get_number_of_name_and_value_pairs(self):
        "Number of Name/Value pairsのデコード(C:SYN_STREAM)"
        if not hasattr(self, '_number_of_name_and_value_pairs'):
            self._number_of_name_and_value_pairs = \
                struct.unpack('!I', self.get_compressed_data()[:4])[0]
        return self._number_of_name_and_value_pairs
    number_of_name_and_value_pairs = property(get_number_of_name_and_value_pairs)

    def get_headers(self):
        "Name/Value pairsのデコード(C:SYN_STREAM)"
        if not hasattr(self, '_headers'):
            headers_stream = self.get_compressed_data()[4:]
            headers_lst = []
            while headers_stream:
                # Nameを取得
                name_length = struct.unpack('!I', headers_stream[:4])[0]
                headers_stream = headers_stream[4:]
                name = headers_stream[:name_length]
                headers_stream = headers_stream[name_length:]
                # Valueを取得
                value_length = struct.unpack('!I', headers_stream[:4])[0]
                headers_stream = headers_stream[4:]
                value = headers_stream[:value_length]
                headers_stream = headers_stream[value_length:]
                # リストにペアを追加
                headers_lst.append((name, value))
            self._headers = headers_lst
        return self._headers
    headers = property(get_headers)

    def decode_control_frame(self):
        self.get_spdy_version()
        self.get_type()

    def decode_data_frame(self):
        self.get_spdy_version()

    def as_dict_control_frame(self):
        "コントロールフレームの辞書表現"
        result = {
            'control_bit': self.control_bit,
            'spdy_version': self.spdy_version,
            'data_length': self.data_length,
            'flags': self.flags,
            'type': self.type,
        }
        if self.type == SPDY_SETTINGS:
            result['number_of_entries'] = self.number_of_entries
        elif self.type == SPDY_SYN_STREAM:
            result['stream_id'] = self.stream_id
            result['associated_to_stream_id'] = self.associated_to_stream_id
            result['priority'] = self.priority
            result['slot'] = self.slot
            result['compressed_data'] = self.compressed_data
            result['number_of_name_and_value_pairs'] = self.number_of_name_and_value_pairs
            result['headers'] = self.headers
        return result

    def as_dict_data_frame(self):
        "データフレームの辞書表現"
        return {}

    def as_dict(self):
        "辞書表現を返す"
        if self.is_control_frame():
            return self.as_dict_control_frame()
        else:
            return self.as_dict_data_frame()


class StreamHandler:
    def __init__(self, connection):
        self.connection = connection
        self.next_frame = None

    def handle(self):
        while True:
            frame = self.recv_frame()
            # データがない場合は終了
            if frame is None:
                return
            spdy_frame = self.decode_frame(frame)
            pprint.pprint(spdy_frame.as_dict())
            print('----------------')
            print_binary(frame)
            # TODO: SYN_STREAMの場合はSYN_REPLYとデータを返す
            if spdy_frame.type == SPDY_SYN_STREAM:
                break

    def recv_frame(self):
        "1回分の送られたデータを全部読んで返す"
        buffer = b''
        # 先頭の固定長の8バイトまで読み込む
        data = self.connection.recv(1024)
        # 読み込むべきデータがない場合はNone
        if len(data) == 0:
            return
        while True:
            #print(type(data))
            buffer += data
            # 8バイトまで読み込めているなら停止
            if len(buffer) >= 8:
                break
            # 続きを読み込む
            data = self.connection.recv(1024)
        # 可変長部分の長さを取得(24bit)
        #pprint.pprint(buffer[5:8])
        data_length = struct.unpack('!I', b'\x00' + buffer[5:8])[0]
        #print(data_length)
        # 可変長部分までを取得
        while True:
            if len(buffer) >= data_length + 8:
                break
            data = self.connection.recv(data_length + 8 - len(buffer))
            buffer += data
        return buffer[:data_length + 8]

    def decode_frame(self, frame):
        #pprint.pprint(frame)
        spdy_frame = SPDYFrame.decode_frame(frame)
        return spdy_frame


def deal_with_client(connstream):
    handler = StreamHandler(connstream)
    handler.handle()
    #connstream.send(RESPONSE_TEXT)


context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
# spdy/3しか使えないようにする
context.set_npn_protocols(['spdy/3'])
context.load_cert_chain(certfile="server.crt", keyfile="server.key")

bindsocket = socket.socket()
bindsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
bindsocket.bind(('0.0.0.0', 8443))
bindsocket.listen(5)

while True:
    newsocket, fromaddr = bindsocket.accept()
    connstream = context.wrap_socket(newsocket, server_side=True)
    try:
        selected_protocol = connstream.selected_npn_protocol()
        print('connected(protocol: {})'.format(selected_protocol))
        deal_with_client(connstream)
    finally:
        #connstream.shutdown(socket.SHUT_RDWR)
        connstream.close()
