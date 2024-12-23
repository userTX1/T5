

	sslciphercheck

	Copyright (c) 2012 woanware
	Developed by Mark Woan (markwoan[at]gmail.com)

	---------------------------------------------------------------------------

	About
	-----
	A simple console application to check SSL cipher support. Basically it uses 
	the openssl tool a bit of C# code to extract the SSL certificate and 
	get info like Server Gated Cryptography (SGC) support. It performs various 
	checks on the certificate, and certificate chain.
	
	Features
	--------
	- Console
	- Supports SSLv2
	- Supports SSLv3
    - Supports TLSv1
    - Checks all SSL ciphers supported by OpenSSL
	- Retrieves the SSL certificate info including SGC
	- Performs a HTTP request to ensure that the protocol/algorithm connection is
	  valid
	- Parses out the HTTP response header and displays to console e.g. HTTP/1.1 
	  200 OK or HTTP/1.1 301 Moved Permanently etc
	- Can output each successful HTTP response to a file in the format:
	
	  PROTOCOL_ALGORITHM_STRENGTH.html e.g. SSLv3_AES256-SHA_256.html (-t)
	  
	- Can perform a keyword(s) match on the HTML response (-m)
	- Alerts for certificate issues such as expired, invalid cert chain, incorrect
	  subject name etc
	- Colourised output to alert if weak ciphers are in use or SSLv2 supported
	- Colourised output to alert on certificate issues
	- Checks for SSL renegotiation issues

	Disclaimer
	-------------------
	THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
	AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
	IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
	ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE 
	LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
	CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
	SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
	INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
	CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
	ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE 
	POSSIBILITY OF SUCH DAMAGE.

	THIS APPLICATION IS ONLY TO BE USED ON WEBSITES/APPLICATIONS THAT EITHER YOU
	OWN OR HAVE EXPRESS WRITTEN PERMISSION TO TEST.

	BY USING THIS SOFTWARE YOU ARE AGREEING TO THE CONDITIONS AND TERMS EXPRESSED 
	ABOVE.


	System Requirements
	-------------------
	- Microsoft .NET Framework v4

	
	---------------------------------------------------------------------------

	woanware
	http://www.woanware.co.uk/

