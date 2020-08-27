package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

//bufio 사용
func main() {
	r := bufio.NewReader(os.Stdin)
	input, _ := r.ReadString('\n')
	s := strings.Fields(input)

	fmt.Println(len(s))
}

/*
    // bytes 사용
    func main() {
	b := new(bytes.Buffer)
	b.ReadFrom(os.Stdin)
	fmt.Println(len(bytes.Fields(buf.Bytes())))
}
*/
