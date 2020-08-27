package main

func sum(a []int) int {
	var r int

	for _, i := range a { // _ = 카운터용 변수(사용x), i = a의 원소
		r += i
	}

	return r
}
