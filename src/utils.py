import random
import string
from pymonad.Maybe import *

def random_char(y):
	return ''.join(random.choice(string.ascii_letters) for x in range(y))

def predefinedMove(protocol, idx):
	moves = {
		'bencode+list': [
			'ld1:v1:x1:xi1e1:yi2eee',
			'ld1:v1:x1:xi1e1:yi2eed1:v1:o1:xi1e1:yi1eee',
			'ld1:v1:x1:xi1e1:yi2eed1:v1:o1:xi1e1:yi1eed1:v1:x1:xi2e1:yi2eee',
			'ld1:v1:x1:xi1e1:yi2eed1:v1:o1:xi1e1:yi1eed1:v1:x1:xi2e1:yi2eed1:v1:o1:xi1e1:yi0eee',
			'ld1:v1:x1:xi1e1:yi2eed1:v1:o1:xi1e1:yi1eed1:v1:x1:xi2e1:yi2eed1:v1:o1:xi1e1:yi0eed1:v1:x1:xi0e1:yi1eee',
			'ld1:v1:x1:xi1e1:yi2eed1:v1:o1:xi1e1:yi1eed1:v1:x1:xi2e1:yi2eed1:v1:o1:xi1e1:yi0eed1:v1:x1:xi0e1:yi1eed1:v1:o1:xi0e1:yi2eee',
			'ld1:v1:x1:xi1e1:yi2eed1:v1:o1:xi1e1:yi1eed1:v1:x1:xi2e1:yi2eed1:v1:o1:xi1e1:yi0eed1:v1:x1:xi0e1:yi1eed1:v1:o1:xi0e1:yi2eed1:v1:x1:xi2e1:yi1eee',
			'ld1:v1:x1:xi1e1:yi2eed1:v1:o1:xi1e1:yi1eed1:v1:x1:xi2e1:yi2eed1:v1:o1:xi1e1:yi0eed1:v1:x1:xi0e1:yi1eed1:v1:o1:xi0e1:yi2eed1:v1:x1:xi2e1:yi1eed1:v1:o1:xi0e1:yi0eee',
			'ld1:v1:x1:xi1e1:yi2eed1:v1:o1:xi1e1:yi1eed1:v1:x1:xi2e1:yi2eed1:v1:o1:xi1e1:yi0eed1:v1:x1:xi0e1:yi1eed1:v1:o1:xi0e1:yi2eed1:v1:x1:xi2e1:yi1eed1:v1:o1:xi0e1:yi0eed1:v1:x1:xi2e1:yi0eee',
		],
		'json+list': [
			'[{"x": 1, "y": 2, "v": "x"}]',
			'[{"x": 1, "y": 2, "v": "x"}, {"x": 1, "y": 1, "v": "o"}]',
			'[{"x": 1, "y": 2, "v": "x"}, {"x": 1, "y": 1, "v": "o"}, {"x": 2, "y": 2, "v": "x"}]',
			'[{"x": 1, "y": 2, "v": "x"}, {"x": 1, "y": 1, "v": "o"}, {"x": 2, "y": 2, "v": "x"}, {"x": 1, "y": 0, "v": "o"}]',
			'[{"x": 1, "y": 2, "v": "x"}, {"x": 1, "y": 1, "v": "o"}, {"x": 2, "y": 2, "v": "x"}, {"x": 1, "y": 0, "v": "o"}, {"x": 0, "y": 1, "v": "x"}]',
			'[{"x": 1, "y": 2, "v": "x"}, {"x": 1, "y": 1, "v": "o"}, {"x": 2, "y": 2, "v": "x"}, {"x": 1, "y": 0, "v": "o"}, {"x": 0, "y": 1, "v": "x"}, {"x": 0, "y": 2, "v": "o"}]',
			'[{"x": 1, "y": 2, "v": "x"}, {"x": 1, "y": 1, "v": "o"}, {"x": 2, "y": 2, "v": "x"}, {"x": 1, "y": 0, "v": "o"}, {"x": 0, "y": 1, "v": "x"}, {"x": 0, "y": 2, "v": "o"}, {"x": 2, "y": 1, "v": "x"}]',
			'[{"x": 1, "y": 2, "v": "x"}, {"x": 1, "y": 1, "v": "o"}, {"x": 2, "y": 2, "v": "x"}, {"x": 1, "y": 0, "v": "o"}, {"x": 0, "y": 1, "v": "x"}, {"x": 0, "y": 2, "v": "o"}, {"x": 2, "y": 1, "v": "x"}, {"x": 0, "y": 0, "v": "o"}]',
			'[{"x": 1, "y": 2, "v": "x"}, {"x": 1, "y": 1, "v": "o"}, {"x": 2, "y": 2, "v": "x"}, {"x": 1, "y": 0, "v": "o"}, {"x": 0, "y": 1, "v": "x"}, {"x": 0, "y": 2, "v": "o"}, {"x": 2, "y": 1, "v": "x"}, {"x": 0, "y": 0, "v": "o"}, {"x": 2, "y": 0, "v": "x"}]'
		],
		's-expr+list': [
			'(l (m "x" 1 "y" 2 "v" "x"))',
			'(l (m "x" 1 "y" 2 "v" "x") (m "x" 1 "y" 1 "v" "o"))',
			'(l (m "x" 1 "y" 2 "v" "x") (m "x" 1 "y" 1 "v" "o") (m "x" 2 "y" 2 "v" "x"))',
			'(l (m "x" 1 "y" 2 "v" "x") (m "x" 1 "y" 1 "v" "o") (m "x" 2 "y" 2 "v" "x") (m "x" 1 "y" 0 "v" "o"))',
			'(l (m "x" 1 "y" 2 "v" "x") (m "x" 1 "y" 1 "v" "o") (m "x" 2 "y" 2 "v" "x") (m "x" 1 "y" 0 "v" "o") (m "x" 0 "y" 1 "v" "x"))',
			'(l (m "x" 1 "y" 2 "v" "x") (m "x" 1 "y" 1 "v" "o") (m "x" 2 "y" 2 "v" "x") (m "x" 1 "y" 0 "v" "o") (m "x" 0 "y" 1 "v" "x") (m "x" 0 "y" 2 "v" "o"))',
			'(l (m "x" 1 "y" 2 "v" "x") (m "x" 1 "y" 1 "v" "o") (m "x" 2 "y" 2 "v" "x") (m "x" 1 "y" 0 "v" "o") (m "x" 0 "y" 1 "v" "x") (m "x" 0 "y" 2 "v" "o") (m "x" 2 "y" 1 "v" "x"))',
			'(l (m "x" 1 "y" 2 "v" "x") (m "x" 1 "y" 1 "v" "o") (m "x" 2 "y" 2 "v" "x") (m "x" 1 "y" 0 "v" "o") (m "x" 0 "y" 1 "v" "x") (m "x" 0 "y" 2 "v" "o") (m "x" 2 "y" 1 "v" "x") (m "x" 0 "y" 0 "v" "o"))',
			'(l (m "x" 1 "y" 2 "v" "x") (m "x" 1 "y" 1 "v" "o") (m "x" 2 "y" 2 "v" "x") (m "x" 1 "y" 0 "v" "o") (m "x" 0 "y" 1 "v" "x") (m "x" 0 "y" 2 "v" "o") (m "x" 2 "y" 1 "v" "x") (m "x" 0 "y" 0 "v" "o") (m "x" 2 "y" 0 "v" "x"))'
		],
		'm-expr+list': [
			'l[m["x"; 1; "y"; 2; "v"; "x"]]',
			'l[m["x"; 1; "y"; 2; "v"; "x"]; m["x"; 1; "y"; 1; "v"; "o"]]',
			'l[m["x"; 1; "y"; 2; "v"; "x"]; m["x"; 1; "y"; 1; "v"; "o"]; m["x"; 2; "y"; 2; "v"; "x"]]',
			'l[m["x"; 1; "y"; 2; "v"; "x"]; m["x"; 1; "y"; 1; "v"; "o"]; m["x"; 2; "y"; 2; "v"; "x"]; m["x"; 1; "y"; 0; "v"; "o"]]',
			'l[m["x"; 1; "y"; 2; "v"; "x"]; m["x"; 1; "y"; 1; "v"; "o"]; m["x"; 2; "y"; 2; "v"; "x"]; m["x"; 1; "y"; 0; "v"; "o"]; m["x"; 0; "y"; 1; "v"; "x"]]',
			'l[m["x"; 1; "y"; 2; "v"; "x"]; m["x"; 1; "y"; 1; "v"; "o"]; m["x"; 2; "y"; 2; "v"; "x"]; m["x"; 1; "y"; 0; "v"; "o"]; m["x"; 0; "y"; 1; "v"; "x"]; m["x"; 0; "y"; 2; "v"; "o"]]',
			'l[m["x"; 1; "y"; 2; "v"; "x"]; m["x"; 1; "y"; 1; "v"; "o"]; m["x"; 2; "y"; 2; "v"; "x"]; m["x"; 1; "y"; 0; "v"; "o"]; m["x"; 0; "y"; 1; "v"; "x"]; m["x"; 0; "y"; 2; "v"; "o"]; m["x"; 2; "y"; 1; "v"; "x"]]',
			'l[m["x"; 1; "y"; 2; "v"; "x"]; m["x"; 1; "y"; 1; "v"; "o"]; m["x"; 2; "y"; 2; "v"; "x"]; m["x"; 1; "y"; 0; "v"; "o"]; m["x"; 0; "y"; 1; "v"; "x"]; m["x"; 0; "y"; 2; "v"; "o"]; m["x"; 2; "y"; 1; "v"; "x"]; m["x"; 0; "y"; 0; "v"; "o"]]',
			'l[m["x"; 1; "y"; 2; "v"; "x"]; m["x"; 1; "y"; 1; "v"; "o"]; m["x"; 2; "y"; 2; "v"; "x"]; m["x"; 1; "y"; 0; "v"; "o"]; m["x"; 0; "y"; 1; "v"; "x"]; m["x"; 0; "y"; 2; "v"; "o"]; m["x"; 2; "y"; 1; "v"; "x"]; m["x"; 0; "y"; 0; "v"; "o"]; m["x"; 2; "y"; 0; "v"; "x"]]'
		],
		'scala+list': [
			'List(Map(x -> 1, y -> 2, v -> x))',
			'List(Map(x -> 1, y -> 2, v -> x), Map(x -> 1, y -> 1, v -> o))',
			'List(Map(x -> 1, y -> 2, v -> x), Map(x -> 1, y -> 1, v -> o), Map(x -> 2, y -> 2, v -> x))',
			'List(Map(x -> 1, y -> 2, v -> x), Map(x -> 1, y -> 1, v -> o), Map(x -> 2, y -> 2, v -> x), Map(x -> 1, y -> 0, v -> o))',
			'List(Map(x -> 1, y -> 2, v -> x), Map(x -> 1, y -> 1, v -> o), Map(x -> 2, y -> 2, v -> x), Map(x -> 1, y -> 0, v -> o), Map(x -> 0, y -> 1, v -> x))',
			'List(Map(x -> 1, y -> 2, v -> x), Map(x -> 1, y -> 1, v -> o), Map(x -> 2, y -> 2, v -> x), Map(x -> 1, y -> 0, v -> o), Map(x -> 0, y -> 1, v -> x), Map(x -> 0, y -> 2, v -> o))',
			'List(Map(x -> 1, y -> 2, v -> x), Map(x -> 1, y -> 1, v -> o), Map(x -> 2, y -> 2, v -> x), Map(x -> 1, y -> 0, v -> o), Map(x -> 0, y -> 1, v -> x), Map(x -> 0, y -> 2, v -> o), Map(x -> 2, y -> 1, v -> x))',
			'List(Map(x -> 1, y -> 2, v -> x), Map(x -> 1, y -> 1, v -> o), Map(x -> 2, y -> 2, v -> x), Map(x -> 1, y -> 0, v -> o), Map(x -> 0, y -> 1, v -> x), Map(x -> 0, y -> 2, v -> o), Map(x -> 2, y -> 1, v -> x), Map(x -> 0, y -> 0, v -> o))',
			'List(Map(x -> 1, y -> 2, v -> x), Map(x -> 1, y -> 1, v -> o), Map(x -> 2, y -> 2, v -> x), Map(x -> 1, y -> 0, v -> o), Map(x -> 0, y -> 1, v -> x), Map(x -> 0, y -> 2, v -> o), Map(x -> 2, y -> 1, v -> x), Map(x -> 0, y -> 0, v -> o), Map(x -> 2, y -> 0, v -> x))'
		]
	}

	if protocol in moves.keys():
		return Just(moves[protocol][idx])
	else:
		return Nothing