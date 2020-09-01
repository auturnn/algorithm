package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var N, cnt int
	var word string
	var result uint8
	var group bool
	r := bufio.NewReader(os.Stdin)
	fmt.Fscanln(r, &N)

	M := make(map[byte]int)

	for i := 0; i < N; i++ {
		fmt.Fscanln(r, &word)

		for j := 0; j < len(word); j++ {
			if result != word[j]{
				result = word[j]
			}
		}
	}

}
