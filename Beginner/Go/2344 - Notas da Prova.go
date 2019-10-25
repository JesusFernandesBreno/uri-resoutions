package main

import "fmt"

func main(){
	var num int
	fmt.Scanf("%d", &num)

	if num < 35 {
		fmt.Println("D")
	}else if num < 60 {
		fmt.Println("C")
	}else if num < 85 {
		fmt.Println("B")
	} else if num < 100 {
		fmt.Println("A")
	}else {
		fmt.Println("E")
	}	

}