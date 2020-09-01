package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	var word string

	r := bufio.NewReader(os.Stdin)
	fmt.Fscanln(r, &word)

	w := strings.ToUpper(word)
	m := make(map[byte]int)

	for i := range w {
		m[w[i]]++
	}

	var mV int
	var mS byte
	maxSpell := ""

	for k, v := range m {
		if mV < v {
			mS = k
			mV = v
		} else if mV == v {
			maxSpell = "?"
			break
		}
	}

	if maxSpell != "" {
		fmt.Print(maxSpell)
	} else {
		fmt.Print(string(mS))
	}

}

/*
   // goroutine 사용 메모리 초과.

   func main() {
       var word, mS string
       var count = 0
       var wait sync.WaitGroup
       var h sync.RWMutex

       r := bufio.NewReader(os.Stdin)
       fmt.Fscanln(r, &word)

       word = strings.ToUpper(word)

       m := make(map[string]int)

       wait.Add(len(word))

       for i := range word {
           go func(i int) {
               defer wait.Done()
               h.Lock()
               m[string(word[i])] = strings.Count(word, string(word[i]))
               h.Unlock()
           }(i)
       }

       wait.Wait()
       wait.Add(len(m))

       for k, v := range m {
           go func(k string, v int) {
               defer wait.Done()
               if count < v {
                   mS = k
                   count = v
               } else if count == v {
                   mS = "?"
               }
           }(k, v)
       }
       wait.Wait()

       fmt.Println(mS)
   }

*/
