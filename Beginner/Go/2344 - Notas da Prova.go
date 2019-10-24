package main

import (
	"fmt"
	"bufio"
	"os"
	"strconv"
	"strings"
)

func main(){
	reader := bufio.NewReader(os.Stdin)
	text, _ := reader.ReadString('\n')
	text = strings.Replace(text, "\n", "", -1)

	num, _ := strconv.Atoi(text)

	if num == 0 {
		fmt.Println("E")
	}else if num < 35 {
		fmt.Println("D")
	}else if num < 60 {
		fmt.Println("C")
	} else if num < 85 {
		fmt.Println("B")
	}else {
		fmt.Println("A")
	}	

}