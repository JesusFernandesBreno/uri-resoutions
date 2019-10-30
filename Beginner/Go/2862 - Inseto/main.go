package main

import (
	"fmt" 
)

func main(){
	var qtd int
	fmt.Scanf("%d", &qtd)

	powers := make([]int, qtd)

	for i := 0; i < qtd; i++{
		fmt.Scanf("%d", &powers[i])
	}

	for _, v := range powers{
		if(v <= 8000){
			fmt.Println("Inseto!")
		}else{
			fmt.Println("Mais de 8000!")
		}
	}
	
}