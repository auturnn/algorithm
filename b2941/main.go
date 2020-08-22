package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

var croa = []string{
	"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z=",
}

func main() {
	var input string

	r := bufio.NewReader(os.Stdin)
	fmt.Fscanln(r, &input)

	for i := range croa {
		input = strings.Replace(input, croa[i], "!", -1)
	}

	fmt.Println(len(input))
}
