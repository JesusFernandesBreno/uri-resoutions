package main

import "fmt"

func main(){
	var qtd int
	fmt.Scanf("%d", &qtd)

	var power int

	for i := 0; i < qtd; i++{
		
		fmt.Scanf("%d", &power)

		if(power > 8000){
			fmt.Printf("Mais de 8000!\n")
		}else{
			fmt.Printf("Inseto!\n")
			
		}
	}
	
}