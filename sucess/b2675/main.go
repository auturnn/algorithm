package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	var T, R int
	var S string
	result := make(map[int]string)
	r := bufio.NewReader(os.Stdin)
	fmt.Fscanln(r, &T)

	for i := 0; i < T; i++ {
		fmt.Fscan(r, &R, &S)
		for j := range S {
			result[i] += strings.Repeat(string(S[j]), R)
		}
		fmt.Println(result[i])
	}
}
