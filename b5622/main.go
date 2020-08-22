package main

import (
	"fmt"
)

//알파벳에 따른 시간 정리 ex) s[0] = 'A' = 3sec = dial(2)

var s = [26]int{
	3, 3, 3, 4, 4, 4, 5, 5, 5, 6,
	6, 6, 7, 7, 7, 8, 8, 8, 8, 9,
	9, 9, 10, 10, 10, 10,
}

func main() {
	var input string
	var sum int
	fmt.Scanln(&input)

	for i := range input {
		//ascii 'A' = 65
		sum += s[int(input[i])-65]
	}

	fmt.Println(sum)
}
