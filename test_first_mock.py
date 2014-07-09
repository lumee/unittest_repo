import unittest
import mock
import urllib2
import first
class FirstTest(unittest.TestCase):

    def setUp(self):
        #the method we are testing will be called from this object
        self.obj = first.First()

    @mock.patch('urllib2.Request')
    @mock.patch('urllib2.urlopen')
    def test_get_data(self, mock_urlopen, mock_request):
        path = 'http://example.com'
        text = ' random text'
        handle = mock.MagicMock()
	mock_urlopen.return_value =handle
        handle.read.return_value = text
        #mock_urlopen().read.return_value = text
############## the method we are testing ##########
        response = self.obj.get_data(path)
###################################################
        mock_request.assert_called_with(path)
        urllib2.urlopen._called_with(mock_request())
        handle.read.assert_called_once_with()
        self.assertEqual(response, text)
#def main():
# unittest.main()
#
#if __name__ == "__main__":
# main()assert
