import base64


class Codec:

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        return str(base64.b64encode(longUrl.encode('utf-8')), 'utf-8')


    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return str(base64.b64decode(shortUrl), 'utf-8')


# Your Codec object will be instantiated and called as such:
url = 'https://leetcode.com/problems/design-tinyurl'
codec = Codec()
print(codec.decode(codec.encode(url)))
