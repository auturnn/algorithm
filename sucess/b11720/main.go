package main

import (
	"fmt"
	"strconv"
)

func main() {
	var n, sum int
	var s string
	fmt.Scanln(&n)
	fmt.Scanln(&s)
	for i := 1; i <= len(s); i++ {
		ss, _ := strconv.Atoi(s[i-1 : i])
		sum += ss
	}
	fmt.Println(sum)
}
