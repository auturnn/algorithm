package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	var A, B string

	fmt.Scan(&A, &B)

	reA, _ := strconv.Atoi(re(A))
	reB, _ := strconv.Atoi(re(B))

	if reA > reB {
		fmt.Println(reA)
	} else {
		fmt.Println(reB)
	}
}

func re(a string) string {
	s := make([]string, len(a))

	for i := len(a) - 1; i >= 0; i-- {
		s = append(s, string(a[i]))
	}
	a = strings.Join(s, "")
	return a
}
