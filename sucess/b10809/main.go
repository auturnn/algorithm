package main

import (
	"fmt"
	"strings"
)

func main() {
	var input string
	fmt.Scanln(&input)

	for i := 'a'; i <= 'z'; i++ {
		a := strings.IndexAny(input, string(i))
		fmt.Print(a, " ")
	}
}
