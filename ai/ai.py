from mod_python import apache, util
from urlparse import urlparse
from random import randint

def handler(req):
        req.log_error('handler')
        req.content_type = 'text/text'
        req.send_http_header()

	qs = req.parsed_uri[apache.URI_QUERY]
        pr = util.parse_qs(qs)
        board = pr['board'][0].split(",")
        score = pr['score'][0]
        move = ai(board, score)
        req.write(move)
        return apache.OK

def ai(board, score):
	moves = [ 'up', 'right', 'down', 'left' ]
	return moves[randint(0, 3)] + "\nRand [" + ','.join(board) + "]\n"

