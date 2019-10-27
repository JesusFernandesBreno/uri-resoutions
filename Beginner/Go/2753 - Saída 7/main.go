package main

import "fmt"

func main(){
	l := 'a'
	n := 97
	for i := 0; i <= 25; i++ {
		fmt.Printf("%d e %c\n", n+i, l + rune(i))
	}
}